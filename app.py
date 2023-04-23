import json
import uuid
import random
import math
import os
from flask import Flask
from flask import request
from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '123456')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'flask_db')
mysql = MySQL(app)

@app.route("/goods")
def list_goods():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM goods")
    rv = cur.fetchall()
    cur.close()
    return json.dumps({
        'code': 200,
        'msg': rv
    })

@app.route("/echo")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pi")
def pi():
    points_within_circle = 0
    steps = request.args.get('steps', 1000)
    steps = int(steps)
    for i in range(steps):
        x = random.random()
        y = random.random()
        if math.sqrt(math.pow(x,2)+math.pow(y,2))<1:
            points_within_circle += 1
    pi=4*points_within_circle/steps
    return json.dumps({
        'code': 200,
        'msg': pi
    })

@app.route("/uuid")
def gen_uuid():
    return uuid.uuid4().hex