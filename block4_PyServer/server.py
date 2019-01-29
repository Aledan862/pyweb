from bottle import route, run, view, redirect, static_file
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/api/forecasts")

def forecasts():
	return {"prophecies" : generate_prophecies(6,2)}


@route("/")
@view("index")
def index():   
   now = dt.now()
   return {
    "date": f"{now.year}-{now.month}-{now.day}"
  }
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@route("/api/test")
def api_test():
    return {"test_passed": True}

run(
  host="192.168.99.204",
  port=8080,
  autoreload=True
)