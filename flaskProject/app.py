from flask import Flask
from flask import render_template
from lunar_python import Solar
from datetime import datetime


app = Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    now = datetime.now()
    Now=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(now)
    solar = Solar(*now.timetuple()[:6])
    lunar = solar.getLunar()
    baZi = lunar.getEightChar()
    print(baZi)
    Time = baZi
    return render_template('website2.html', time=Time,NOW=Now)

@app.route('/gettime')

def gettime():
    now = datetime.now()
    Now=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

    solar = Solar(*now.timetuple()[:6])
    lunar = solar.getLunar()
    baZi = lunar.getEightChar()
    Time = baZi


    return {'english':Now}#'chinese':Time
