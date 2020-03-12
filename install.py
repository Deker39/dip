from core import Information, colors
import os, time, subprocess
from sys import stdout

def Command_exe(msg, cmd):
    i = "\033[1mSTATUS"+colors.W+":[Processing]"
    stdout.write(" "+msg+" %s" % i)
    stdout.flush()
    if subprocess.call(cmd+' >/dev/null 2>&1', shell=True) == 0:
        i = "[\033[1m"+colors.G+"OK"+colors.W+"]"
    else:
        i = "["+colors.R+"\033[1mERROR"+colors.W+"]["+colors.O+"\033[1mWARNING"+colors.W+"]"

    stdout.write("\r "+msg+" STATUS:%s" % i)


print ( "" )
print (
    "                    "+colors.B+",:"+colors.W+"       "+colors.B+":,"+colors.W+"                   				 " )  # ,:       :,
print (
    "                   "+colors.B+",/./"+colors.W+" _8_  "+colors.B+"\.\                  				 " )  # /./  _8_  \.\
print (
    "                   "+colors.B+",\ \\"+colors.W+"/"+colors.P+"("+colors.R+"O"+colors.P+")"+colors.W+"\\"+colors.B+"/ /                  				 " )  # \ \/( O )\/ /
print (
    "                    "+colors.B+",\ \:::/ /                   				 ")#                    \ \:::::/ /
print (
    "                     /"+colors.O+"__"+colors.G+"---"+colors.O+"__"+colors.B+"\                   				 "  )#                     /__---__\
print (
    "                    ("+colors.O+"/__\ /__\\"+colors.B+")"+colors.W+"                   				 ")#                    (/__\ /__\)
print (
    "                    "+colors.B+"/"+colors.W+"\  .V.  /"+colors.B+"\\"+colors.W+"                   				 ")#                    /\  .V.  /\
print (
    "                   "+colors.B+"/"+colors.W+"  \,---,/  "+colors.B+"\\"+colors.W+"                  				 ")#                   /  \,---,/  \
print (
    "                   "+colors.B+"\\"+colors.W+"___TTTTT___"+colors.B+"/"+colors.W+"         CODE: KATANA  ")#                   \___TTTTT___/
print ("                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::      DATE: "+Information.date+"")#                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::
print ("                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)      CORE: "+Information.version+", BUILD: "+Information.build )#                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)
print ("        "+Information.Type+"    "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"KATANA."+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"                               ")#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+".ANATAK"+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"
print ("                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               				 ")#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"
print ("    __________?_____________________________________  				 ")#    __________?_________________________________
print ("   {_"+colors.C+"A|"+colors.W+" "+colors.C+"L|"+colors.W+" "+colors.R+"E|"+colors.W+" "+colors.W+"X|"+colors.W+" |"+colors.GR+"#################################"+colors.W+"/  				 ")#   {_"+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" I#################################/
print ("     ^ ^ ^ ^   ,ww   "+colors.O+"FRAMEWORK"+colors.W+"   ww,                   				 ")#     ^ ^ ^ ^ EHT KROWEMARF, dliuB
print ("                   I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_I                  				 ")#                   I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_I
print ("                   \_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_/                  				 ")#                   \_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_/
print ("")
print ("")