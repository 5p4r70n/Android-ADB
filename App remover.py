from flask import Flask,render_template,request,url_for #import flask library
from ppadb.client import Client                         # os for communicating to device

adb = Client(host="127.0.0.1",port=5037)
app=Flask(__name__)                                     #name to app obj
@app.route("/" , methods=['POST','GET'])                #first line / represents the route dir 
def home():                                             #definiton of "/" is home its is mandetery in this code 
    if request.method =='POST':
        
        if len(list_devices()) != 0:
           return ('device connected')
        else:
            return ('device not connected try again  <a href="/">home</a> ')
    else:
        return render_template ("home.html")            #content of that page...
def list_devices():
    devices = adb.devices()
    return devices
    
        


if __name__ == "__main__":                              #check wether the ___name__ == __main__ conforming only devoloper can debug the code... if this command is not here anyone can access and debug the code..
    app.run() 