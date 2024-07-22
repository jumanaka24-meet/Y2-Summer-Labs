from flask import Flask, render_template, request, url_for, redirect 
from flask import session 
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyBV4AlvXHKIhhX_v8FpuBOnkb5sZjG1BT4",
  "authDomain": "auth-lab-20f56.firebaseapp.com",
  "projectId": "auth-lab-20f56",
  "storageBucket": "auth-lab-20f56.appspot.com",
  "messagingSenderId": "630974933261",
  "appId": "1:630974933261:web:396b740e8a23f298d4e844",
  "measurementId": "G-22NCPQB3FR", "databaseURL": ""
} 

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
  try:
    print(email,password)
    session['user'] = auth.create_user_with_email_and_password(email, password)
    session['quotes'] = []
    return redirect(url_for('home'))
  except :
    error = "Authentication failed"
    print(error)
  return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      try:
        session['user'] = auth.sign_in_with_email_and_password(email, password)
        session['quotes'] = []
        print(session['user'])
        return redirect(url_for('home'))
      except Exception as e :
        error = "Authentication failed"
        print(e)
    return render_template("signin.html")



@app.route('/signout')
def signout():
    # session.pop('user')
    session['user']=None
    auth.current_user = None
    print("signed out user")
    return redirect(url_for('signin'))




@app.route('/home', methods=['GET', 'POST'])
def home():
    error = ""
    if request.method == 'GET':
       return render_template("home.html")
    else:
      session['quotes'].append(request.form["quotes"])
      session.modified = True
      return redirect(url_for('thanks'))









@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template("thanks.html")




@app.route('/display', methods=['GET', 'POST'])
def display():
    error = ""
    if request.method == 'GET':
      return render_template('display.html',quotes = session['quotes'])






if __name__ == '__main__':
 
    app.run( debug=True)