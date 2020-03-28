#execfile("main.py", globals())
import subprocess

program = "main.py"
process = subprocess.Popen(program, shell= True)
code = process.wait( )
print ( process.stdout )  # 0
#sys.exit(0)
print('В сраку гіляку')


#start_time = datetime.now()

#Тут выполняются действия
#time.sleep(5)

#print(start_time )
#localtime = time.localtime(time.time())
#print (time.gmtime().tm_hour)





