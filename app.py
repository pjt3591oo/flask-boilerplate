from datetime import datetime
from flask import Flask, request, flash, url_for, redirect,render_template, abort, json,jsonify
from model import Todo, db

app = Flask(__name__)

@app.before_request
def db_connect():
    print 'before'


@app.route('/all', methods=['GET'])
def show_all():
    try:
        #2,"2","3",4,5,"6"

        Todo_list = db.session.query(Todo).first()
        #print conn.execute("SELECT *FROM userinfo")

        return 'test'
    except :
        print('error')
        return 'error'

@app.route('/projects/')
def projects():
    print(request.args.get('a', ''))
    return 'The project page'

@app.route('/at/<name>', methods=['POST'])
def at(name = None):
    v = request.form.main[0]
    print(v)

    return v

@app.route('/login', methods=['POST'])
def login():
    v = request.form['main']
    print(v)
    if request.method == 'POST':
        return 'asd'

if __name__ == '__main__':
    app.run()
