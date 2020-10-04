from flask import Flask,render_template,request,url_for #import flask library
import os   # os for communicating to device

app=Flask(__name__)         #name to app obj
@app.route("/" , methods=['POST','GET'])            #first line / represents the route dir 
def home():                #definiton of "/" is home its is mandetery in this code 
    if request.method =='POST':
        print ('works')
        print (request.form.get('method'))
        return  (request.form.get('method'))
        
        
        
    else:
        return render_template ("home.html")    #content of that page...




if __name__ == "__main__":      #check wether the ___name__ == __main__ conforming only devoloper can debug the code... if this command is not here anyone can access and debug the code..
    app.run() 