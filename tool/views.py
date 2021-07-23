from flask import Blueprint, render_template
from .models import Scan
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/scan')
def Scan__():
    IP = '192.168.43.246'
    MAC = 'XX:XX:XX:XX'
    Hostname = 'shanmukmichael'
    Domain = 'shanmukmichael'
    OS = 'Windows'

    #-------------------------------------------------------------------
    data = Scan(IP=IP, MAC=MAC, Hostname=Hostname, Domain=Domain, OS=OS)
    db.session.add(data)
    db.session.commit()
    #-------------------------------------------------------------------
    #data from db
    data = Scan.query
    print(data)
    return render_template('table.html', data=data)
