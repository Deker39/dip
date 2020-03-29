from PIL import Image, ImageTk
import tkinter as tk

import cv2
import subprocess

class Application:
    def __init__(self):
        """ Initialize application which uses OpenCV + Tkinter. It displays
            a video stream in a Tkinter window and stores current snapshot on disk """
        self.cam = cv2.VideoCapture('re.mp4') # capture video frames, 0 is your default video camera
        #self.output_path = output_path  # store output path
        self.cam.set ( 3, 640 )  # set video widht
        self.cam.set ( 4, 480 )  # set video height


        self.current_image = None  # current image from the camera

        self.root = tk.Tk()  # initialize root window
        self.root.title("PyImageSearch PhotoBooth")  # set window title
        self.root.configure ( background='black' )
        # self.destructor function gets fired when the window is closed

        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.pack(padx=10, pady=10)

        # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        #self.video_loop()


    def video_loop(self):
        """ Get frame from the video stream and show it in Tkinter """
        recognizer = cv2.face.LBPHFaceRecognizer_create ( )
        recognizer.read ( 'trainer/trainer.yml' )
        cascadePath = "/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier ( cascadePath )

        font = cv2.FONT_HERSHEY_SIMPLEX
        minW = 0.1 * self.cam.get ( 3 )
        minH = 0.1 * self.cam.get ( 4 )
        ret, img = self.cam.read()  # read frame from video stream
        img = cv2.flip ( img, -1 )  # Flip vertically
        gray = cv2.cvtColor ( img, cv2.COLOR_BGR2GRAY )
        faces = faceCascade.detectMultiScale (
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int ( minW ), int ( minH )),
        )


        #cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
        self.current_image = Image.fromarray(gray)  # convert image for PIL
        imgtk = ImageTk.PhotoImage(image=self.current_image)  # convert image for tkinter
        self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        self.root.attributes("-fullscreen",True)
        #self.oot.wm_state('zoomed')
        self.panel.config(image=imgtk)  # show the image


        self.root.after(1, self.video_loop)  # call the same function after 30 milliseconds



    def destructor(self):
        """ Destroy the root object and release all resources """
        print("[INFO] closing...")
        self.root.destroy()
        self.cam.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application


# start the app
print("[INFO] starting...")

pba = Application()
pba.root.mainloop()
