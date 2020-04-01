from PIL import Image, ImageTk
#imports
try:
    import tkinter as tk
except:
    import Tkinter as tk

import argparse
import datetime
import cv2
import os

class Application:
    def __init__(self):
        """ Initialize application which uses OpenCV + Tkinter. It displays
            a video stream in a Tkinter window and stores current snapshot on disk """
        self.vs = cv2.VideoCapture(0) # capture video frames, 0 is your default video camera
        self.vs.set ( 3, 640 )  # set video widht
        self.vs.set ( 4, 480 )
        self.root.configure ( background='black' )
        self.current_image = None  # current image from the camera

        self.root = tk.Tk()  # initialize root window
        self.root.title("main")  # set window title

        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.configure ( background='black' )
        self.panel.pack(padx=10, pady=10)
               # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        self.video_loop()


    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        ok, frame = self.vs.read()  # read frame from video stream
        frame = cv2.flip ( frame, -1 )
        if ok:  # frame captured without any errors
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
            self.current_image = Image.fromarray(cv2image)  # convert image for PIL
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.root.attributes("-fullscreen",True)
            #self.oot.wm_state('zoomed')
            self.panel.config(image=imgtk,  )  # show the image

        self.root.after(1, self.video_loop)  # call the same function after 30 milliseconds


    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.root.destroy()
        self.vs.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application



# start the app
print("[INFO] starting...")
pba = Application()
pba.root.mainloop()