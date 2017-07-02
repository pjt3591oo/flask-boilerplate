from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from model import user, password, db, host
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(user, password, host, db)
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column('id', db.Integer, primary_key=True)
    nick = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    age = db.Column(db.Integer)
    count = db.Column(db.Integer)
    token = db.Column(db.String(80))

    def __init__(self, id, nick,gender,age,count,token ):
        self.id = id
        self.nick = nick
        self.gender = gender
        self.age = age
        self.count = count
        self.token = token
    def __repr__(self):
        return '<User (id="%r", nick="%s", gender="%s") >' % (self.id, self.nick, self.gender)

db.create_all()

print 'db_model_success'
