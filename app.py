from flask import Flask, render_template, request, redirect,session,url_for, flash,make_response,jsonify
from flask_session import Session
import jwt
from datetime import datetime, timedelta
from flask_cors import CORS
import mysql.connector
import sqlite3


app = Flask(__name__)
app.secret_key = 'iamfuckingcreazy'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)



conn = sqlite3.connect('database.db')



@app.route('/', methods=['POST','GET'])
def hello():
    if request.method == 'GET':
        return render_template("videos.html")
    if request.method == 'POST':
        query = request.form.get()['query']
        pt1 = 'https://www.google.com/search?q='
        url = pt1 + query
        return redirect(url, 301)

@app.route('/YTSearch',methods=['POST'])
def YTSearch():
    if request.method == 'POST':
        query = request.form.get()['query']
        print(query)
        pt1 = 'https://www.youtube.com/results?search_query='
        url = pt1 + query
        return redirect(url, 301)
    
        

@app.route('/StackOSearch',methods=['POST'])
def StackOSearch():
    if request.method == 'POST':
        query = request.form.get()['query']
        print(query)
        pt1 = 'https://stackoverflow.com/search?q='
        url = pt1 + query
        return redirect(url, 301)

@app.route('/StackESearch',methods=['POST'])
def StackESearch():
    if request.method == 'POST':
        query = request.form.get()['query']
        print(query)
        pt1 = 'https://stackexchange.com/search?q='
        url = pt1 + query
        return redirect(url, 301)
    
@app.route('/GitSearch',methods=['POST'])
def GitSearch():
    if request.method == 'POST':
        query = request.form.get()['query']
        print(query)
        pt1 = 'https://github.com/search?q='
        url = pt1 + query
        return redirect(url, 301)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('entry/login.html')
        # session["name"] = request.form.get("name")
    if request.method == 'POST':
        flash(f"Record Saved!", "success")
        return 'login'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('entry/register.html')

    if request.method == 'POST':
        if request.form.get('password') != request.form.get('confpassword'):
            flash("Password and Confirm Password does not match") 
            return redirect(url_for('register'))
        else:
            email = request.form.get('email')
            sql_query = "select * from user where email="+email
            conn.execute(sql_query)
            conn.commit()
            user = conn.fetchall()
            print("email verified")
            if user:
                flash('User already exists')
                return redirect(url_for('register'))
            else:
                name = request.form.get('name' )
                email = request.form.get('email')
                domain = request.form.get('domain')
                year = request.form.get('year')
                password = request.form.get('password')
                conn.execute("INSERT INTO user (name,email,doamin,year,password) VALUES (%s,%s,%s,%s,%s)",(name,email,domain,year,password))
                conn.commit()
                flash('You are now registered and can log in')
                print("data inserted")
                return redirect(url_for('register'))


# @app.route('/login' , methods=['POST'])
# def login():
#     if request.method == 'POST':
#         dump = request.get_json()
#         username = dump['username']
#         password =  dump['password']
#         conn.execute("SELECT * FROM users WHERE username = '"+username+"' AND password = '"+password+"';")
#         data = conn.fetchall()
#         if (len(data)==0 or len(data)>1):
#             resp = jsonify({'message' : 'Invalid username or password'})
#             resp.status_code = 400
#             return resp
#         else:
#             # added username in session
#             session['username'] = username
#             # return jwt token 
#             token = jwt.encode({'public_id': username,'exp' : datetime.utcnow() + timedelta(hours= 12)}, app.config['SECRET_KEY'])
#             return make_response(jsonify({'token' : token.decode('UTF-8'),'username' : username }), 201)


# logout route
@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return make_response(jsonify({'message' : 'You successfully logged out'}))



if __name__ == '__main__':
    app.run(debug=True)