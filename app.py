from flask import Flask, render_template, request, redirect,session, flash,make_response,jsonify
from flask_session import Session
import jwt
from datetime import datetime, timedelta
from flask_cors import CORS
import mysql.connector



app = Flask(__name__)
app.secret_key = 'iamfuckingcreazy'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)

# this is configuration for sql database connection 
mydb = mysql.connector.connect(
	host = "remotemysql.com", # your host address (yourservice.com)
	user = "pvDhFaBOFP", # your yasername for sql database
	password = "AOATIK73jC", # your password 
    database = "pvDhFaBOFP" # your database name
)

cursor = mydb.cursor()




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
        return 'register'

# login api route 
@app.route('/login' , methods=['POST'])
def login():
    if request.method == 'POST':
        dump = request.get_json()
        username = dump['username']
        password =  dump['password']
        cursor.execute("SELECT * FROM users WHERE username = '"+username+"' AND password = '"+password+"';")
        data = cursor.fetchall()
        if (len(data)==0 or len(data)>1):
            resp = jsonify({'message' : 'Invalid username or password'})
            resp.status_code = 400
            return resp
        else:
            # added username in session
            session['username'] = username
            # return jwt token 
            token = jwt.encode({'public_id': username,'exp' : datetime.utcnow() + timedelta(hours= 12)}, app.config['SECRET_KEY'])
            
            return make_response(jsonify({'token' : token.decode('UTF-8'),'username' : username }), 201)

#  register api route 
@app.route('/register' , methods=['POST'])
def register():
    if request.method == 'POST':
        #check confirm passowrd and password
        if request.form['password'] != request.form['confpassword']:
            resp = jsonify({'message':'Password and Confirm Password does not match'})
            resp.status_code = 401
            return make_response(resp)
        #check if username already exists
        else:
            username = request.form['username']
            cursor.execute("SELECT * FROM users WHERE username = %s", [username])
            user = cursor.fetchone()
            if user:
                resp = jsonify({'message':'User already exists'})
                resp.status_code = 401
                return make_response(resp)
            else:
                name = request.form['name']
                email = request.form['email']
                contact = request.form['contact']
                username = request.form['username']
                password = request.form['password']
                cursor.execute("INSERT INTO users (name,email,contact,username,password) VALUES (%s,%s,%s,%s,%s)",(name,email,contact,username,password))
                mydb.commit()
                return make_response(jsonify({'message' : 'You are now registered and can log in'}))


# logout route
@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return make_response(jsonify({'message' : 'You successfully logged out'}))



if __name__ == '__main__':
    app.run(debug=True)