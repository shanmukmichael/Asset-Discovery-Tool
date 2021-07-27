from tool import remote_info
from flask import Blueprint, render_template
from .models import Scan
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/scan')
def Scan__():
    data = remote_info.remote_data_2_()
    print(data)
    for (Hostname,IP,MAC,Lastseen,Status) in zip(data['Hostname'], data['IP'], data['MAC'], data['Lastseen'], data['Status']):
       data = Scan(Hostname=Hostname, IP=IP, MAC=MAC, Lastseen=Lastseen, Status=Status)    
        # add the cols to the database
       db.session.add(data)
    db.session.commit()
        #data from db
    data = Scan.query
    return render_template('table.html', data=data)
