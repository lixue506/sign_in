#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash,redirect
import base64
import random
import datetime
import os
from flask import jsonify
import importlib,sys
from operator import Operator_mysql
importlib.reload(sys)

# request 获得form：一般post参数， values：get，post参数， args:get参数

app = Flask(__name__)
app.secret_key = b'#$ds2FG<3d3G6[F#&T_5#y2L"F4Q8z\n\xec]/'
session = {}

def user_login(func):
    def Login_Judge(name):
        if name in session.keys:
            return True
        return False
    return Login_Judge  

# 首页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# 查询
@app.route('/Query', methods=['POST','GET'])
def Query():
    start_time = request.values['start']
    end_time = request.values['end']
    result = Operator_mysql.Query_data(start_time,end_time)
    return jsonify(result)

@app.route('/Login', methods=['POST','GET'])
def Login():
    if request.method == 'GET':
        name = request.values['name']
        pwd = request.values['pwd']
        result = Operator_mysql.Login_Judge(name, pwd)
        return jsonify({"status":str(result)})
    return render_template('Admin/Login.html')

@app.route("/admin/lodout")
def logout():
    pass

@user_login
@app.route('/Admin/index', methods=['GET', 'POST'])
def Admin_index():
    return render_template("admin/index.html")

@user_login
@app.route('/admin/upload',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)
        son_path = "static\\file\\"
        upload_path = os.path.join(basepath, son_path)
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)
        # 文件上传
        f = request.files['data_file']
        f.save(os.path.join(upload_path, f.filename))

        return jsonify({"status":str(1)})


if __name__ == '__main__':
    app.run(port=8000)





