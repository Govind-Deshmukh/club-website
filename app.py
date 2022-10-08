from flask import Flask, render_template, request, redirect,session,url_for, flash,make_response,jsonify
from flask_session import Session
from flask_cors import CORS
import sqlite3
from flask_admin import Admin
# import jwt
# from datetime import datetime, timedelta
# import mysql.connector
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin


app = Flask(__name__)
# database configuration 
app.secret_key = 'iamfuckingcreazy'
# session configuration 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# cors config    
CORS(app)



conn = sqlite3.connect('database.db',check_same_thread=False)
c = conn.cursor()


@app.route('/', methods=['POST','GET'])
def hello():
    if request.method == 'GET':
        return render_template("videos.html")
    if request.method == 'POST':
        query = request.form['query']
        pt1 = 'https://www.google.com/search?q='
        url = pt1 + query
        return redirect(url, 301)

@app.route('/YTSearch',methods=['POST'])
def YTSearch():
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        pt1 = 'https://www.youtube.com/results?search_query='
        url = pt1 + query
        return redirect(url, 301)
    
        

@app.route('/StackOSearch',methods=['POST'])
def StackOSearch():
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        pt1 = 'https://stackoverflow.com/search?q='
        url = pt1 + query
        return redirect(url, 301)

@app.route('/StackESearch',methods=['POST'])
def StackESearch():
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        pt1 = 'https://stackexchange.com/search?q='
        url = pt1 + query
        return redirect(url, 301)
    
@app.route('/GitSearch',methods=['POST'])
def GitSearch():
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        pt1 = 'https://github.com/search?q='
        url = pt1 + query
        return redirect(url, 301)


# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('entry/login.html')
#         # session["name"] = request.form("name")
#     if request.method == 'POST':
#         flash(f"Record Saved!", "success")
#         return 'login'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('entry/register.html')
    if request.method == 'POST':
        if request.form['password'] != request.form['confpassword']:
            flash('Password and Confirm Password does not match', 'error')
            return redirect(url_for('register'))
        else:
            email = request.form['email']
            verify_query = "select * from club_users where email = '"+str(email)+"';"
            user = conn.execute(verify_query)
            if user:
                flash('User already exists','error')
                return redirect(url_for('register'))
            else:
                name = request.form['name' ]
                email = request.form['email']
                mobile = request.form['mobile']
                domain = request.form['domain']
                year = request.form['year']
                password = request.form['password']
                c.execute(f"INSERT INTO club_users (name,email,mobile,domain,year,password) VALUES ('{name}','{email}','{mobile}','{domain}','{year}','{password}');")
                conn.commit()
                flash('You are now registered and can log in','success')
                return redirect(url_for('login'))


@app.route('/login' , methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('entry/login.html')
        # session["name"] = request.form("name")
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        data = conn.execute("SELECT * FROM club_users WHERE email = '"+email+"' AND password = '"+password+"';")
        if (len(data)==0 or len(data)>1):
            flash('Invalid username or password','error')
            return redirect(url_for('login'))
        else:
            # added username in session
            session["user"] = email
            flash('Login successful','success')
            return redirect(url_for())

# logout route
@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('Dashboard/dashboard.html')

# logout route
@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('hello'))


if __name__ == '__main__':
    app.run(debug=True)