from flask import Flask 
from flask import Flask,request,make_response
import os ,json
from flask_cors import CORS,cross_origin



app=Flask(__name__)
@app.route('/')
def index():
    return "Web app with flask"









if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)
