import json
import uuid
import random
import math
from flask import Flask
from flask import request


app = Flask(__name__)

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