from flask import Flask,render_template,request,url_for #import flask library
from ppadb.client import Client                         # os for communicating to device

adb = Client(host="127.0.0.1",port=5037)
app=Flask(__name__)                                     #name to app obj

devices = adb.devices()
device = devices[0]


@app.route("/" , methods=['POST','GET'])                #first line / represents the route dir 
def home():                                             #definiton of "/" is home its is mandetery in this code 
    if request.method =='POST':
        
        if len(devices) != 0:
            device =  devices[0]
            return render_template ("ModuleList.html")
        else:
            return ('device not connected try again  <a href="/">home</a> ')
    else:
        return render_template ("home.html")            #content of that page...

@app.route("/disconnect" )   
def disconnect():
    device.disconnect()
    return render_template ("home.html") 



@app.route("/listAll" )
def listAll():
    list = (device.shell("pm list packages")).split() #packages are coming like package:name format
    list1=[]  #for saving splited packages 
    for i in range(0,len(list)):
        list[i]=list[i].split(':')
        list1.append(list[i][1])
    return render_template("Listall.html",list1=list1,len=len(list))

# @app.route("/remove",methods=['POST','GET'])
@app.route("/remove")
def remove():
    # rm=request.form.getlist('check')
    # for i in rm:
    #     print('pm uninstall --user 0 '+str(i))
    # return ("these items <table>{%for i in rm%}<tr><td>{{i}}</td></tr>{%endfor%}</table> Uninstalled Go <a href='/listAll'>back</a> Or <a href='/'>Home</a>")
    return('pm uninstall --user 0 ')


if __name__ == "__main__":                              #check wether the ___name__ == __main__ conforming only devoloper can debug the code... if this command is not here anyone can access and debug the code..
    app.run() 