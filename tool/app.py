from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Scan(db.Model):
    # primary keys are required by SQLAlchemy
    ID = db.Column(db.Integer, primary_key=True)
    IP = db.Column(db.String(100))
    MAC = db.Column(db.String(100))
    Hostname = db.Column(db.String(100))
    Domain = db.Column(db.String(100))
    OS = db.Column(db.String(100))

db.create_all()

@app.route('/')
def main():
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
    return render_template('table.html', data=data)


if __name__ == '__main__':

    app.run(debug=True)
