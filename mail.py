import subprocess
import time

from cffi.setuptools_ext import execfile

#execfile("main.py", globals())


program = "main.py"
process = subprocess.Popen(program, shell=True)
code = process.wait ( )

print ( code )  # 0

