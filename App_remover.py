from flask import Flask,render_template,request,url_for #import flask library
from ppadb.client import Client                         # os for communicating to device
import os
import time

adb = Client(host="127.0.0.1",port=5037)
app=Flask(__name__)                                     #name to app obj
devices = adb.devices()
device=devices[0]
dir = os.getcwd()                                       # get present working Directry                                        # get current time

@app.route("/" , methods=['POST','GET'])                #first line / represents the route dir 
def home():                                             #definiton of "/" is home its is mandetery in this code 
    if request.method =='POST':
        devices = adb.devices() 
        if len(devices) != 0:
            return render_template ("ModuleList.html",screen= screen_size() )
        else:
            return ('device not connected try again  <a href="/">home</a> ')
    else:
        return render_template ("home.html")            #content of that page...

@app.route("/listAll" ,methods=['POST','GET'] )
def listAll():

    if request.method=='POST':
        return render_template("Listall.html",list1= appList()[0],len=len(list1),head=appList()[1]) 

    else:
        return render_template ("ModuleList.html")



@app.route("/remove",methods=['POST','GET'])
def remove():
    rm=request.form.getlist('check') #checked apps will come here
    for i in rm:
        device.shell('pm uninstall --user 0 '+str(i))  #this will uninstall apps
    return ("these items Uninstalled GO <a href='/listAll'>back</a> Or GO <a href='/'>Home</a>")



@app.route("/screenCap",methods=['POST','GET'])
def screenCap():
    ts = time.strftime("%Y%m%d%H%M%S")
    device.shell("screencap /sdcard/screenshot.png")
    device.pull("/sdcard/screenshot.png", str(dir)+"/static/"+str(ts)+".png")
    return render_template ("Image.html",ts=ts)    




def appList():
    x=request.form['appType'] # app filter comes here
    cmd={"all" : "pm list packages","user" : "pm list packages -3","system":"pm list packages -s","disabled":"pm list packages -d","enabled":"pm list packages -e"} #hard coded commands each one selected via appType coming from request
    list = (device.shell(cmd[x])).split() #packages are coming mixed with each other 
    list1=[]  #for saving splited packages 
    for i in range(0,len(list)):
        list[i]=list[i].split(':')      #this will split with : for removing "package:" from name
        list1.append(list[i][1])        # added to list array
    return list1,x   



def screen_size():   #function for get screen size of the device
    size=device.shell('wm size')
    density =device.shell('wm density')
    return size,density


if __name__ == "__main__":#check wether the ___name__ == __main__ conforming only devoloper can debug the code... if this command is not here anyone can access and debug the code..
    app.run() 