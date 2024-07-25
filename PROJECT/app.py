from flask import Flask, render_template, request, url_for, redirect 
from flask import session 
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyATgy3BMiKmrHGkEpVDm_9lXjLDuP6Q58Y",
  "authDomain": "project-40ddc.firebaseapp.com",
  "projectId": "project-40ddc",
  "storageBucket": "project-40ddc.appspot.com",
  'messagingSenderId': "787161856750",
  "appId": "1:787161856750:web:3ee699cbcb0678563051ff",
  "measurementId": "G-SCR2BCM9VR",
   "databaseURL": "https://project-40ddc-default-rtdb.europe-west1.firebasedatabase.app/"
} 

firebase = pyrebase.initialize_app(firebaseConfig)
db =firebase.database()
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def home ():

  if request.method == 'GET':

    return render_template("home.html")
  else :
    return redirect(url_for('signup'))
 
  





@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email=request.form['email']
    password= request.form['password']
    user = {"email": email,"password": password, "name":  request.form['name'],  "favsong":  request.form['favsong'], "score":0 }
    try:
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['points'] = 0
    
      ID = session['user']['localId']
      db.child("Users").child(ID).set(user)
      print(db.child("Users").child(ID).get().val())

      #session['quotes'] = []
      #return redirect(url_for('songs',number=0))
      return redirect(url_for('songs',number=0))

    except Exception as e :
        error = "Authentication failed"
        print(e)
  return render_template("signup.html")





@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    db.child('Users').child(session['user']['localId']).update({'score':0})
    if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      try:
        session['user'] = auth.sign_in_with_email_and_password(email, password)
        session['points'] = 0
        # db.child('Users').child(ID).update({'score':0})
        # return redirect(url_for('song1'))
      #   session['quotes'] = []
      #   print(session['user'])
        number=0
        #return redirect(url_for('songs'))
        return redirect(url_for('songs',number=0))

      except Exception as e :
        error = "Authentication failed"
        print(e)

    return render_template("signin.html")


@app.route('/songs/<int:number>', methods=['GET', 'POST'])
def songs(number):
  if request.method == 'POST':
    ID = session['user']['localId']
    user_info = db.child('Users').child(ID).get().val()
    score = user_info['score']
    print(score)
    rating = int(request.form['rating'])
    score += rating
    db.child('Users').child(ID).update({'score':score})

  info= {
  "song1": {"name":"STRANGERS IN THE NIGHT","link":"https://youtu.be/Fd_3EkGr0-4?si=ywGabbPnxE1kzDRf","image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy0SICj43GnrYhV4nOyVxTpYY8g1Adwuc-kg&s.jpg"},
  
  "song2": {"name":"MARINERS APARTMENT COMPLEX","link":"https://youtu.be/1uFv9Ts7Sdw?si=Syia096k3XWwI3NW","image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSV86vt_O1LuJkOnE3dd9xW7-Rde8E7pMI0RQ&s.jpg"},
 
  "song3": {"name":"IN A GOOD WAY","link":"https://youtu.be/IdaD4TPLuXQ?si=qIJEzbCEs5wD5itx","image":"https://images.genius.com/5934fb116eb0f254cb06c8563e61ab2d.1000x1000x1.jpg"},

  "song4": {"name":"BACK TO THE OLD HOUSE","link":"https://youtu.be/jPKgaKHII-Y?si=81L3YqNbUctjbBOn","image":"https://i1.sndcdn.com/artworks-lkXcRg2c4eH3-0-t500x500.jpg"},

  "song5": {"name":"LOUISE","link":"https://youtu.be/qMwRRV_mFQE?si=CVIxHd2bbYht53Ln","image":"https://i.pinimg.com/736x/99/a5/9a/99a59a834f77fa093b6448e094ee7fa6.jpg"},

  "song6": {"name":"PAIN","link":"https://youtu.be/9-QsLBtiLss?si=15672HUhtJdQIPb0","image":"https://imgix.bustle.com/uploads/image/2022/1/6/596235f1-1f5e-4778-b3bd-e55e7610eaa2-pinkpantheress_245226757_6907958595888266_7347954318923902896_n.jpg?w=1200&h=900&fit=crop&crop=faces&fm=.jpg"},

  "song7": {"name":"THINKIN BOUT YOU","link":"https://youtu.be/6JHu3b-pbh8?si=PveLgN0qjP2vEzZ4","image":"https://lastfm.freetls.fastly.net/i/u/ar0/c0097390e321f20873a2d0e22d32d84e.jpg"},

  "song8": {"name":"MY LOVE MINE ALL MINE","link":"https://youtu.be/Qy9LTRu89FA?si=VosXaQbJ4OfrRMP0","image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShuMDxz8Az_NQW5IBFhRZoB1w5I54qE1d6lA&s.jpg"},

  "song9": {"name":"KEEP ON LOVING YOU","link":"https://youtu.be/PDJPpG8e4n4?si=ev0Qy5WMZgQAsplm","image":"https://f4.bcbits.com/img/a1219317813_65.jpg"},

  "song10": {"name":"FADE INTO YOU","link":"https://youtu.be/avv2IIdDnnk?si=UhaWThZKH54NbEER","image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRX-iIh9hCm4LFq0Pql2gsEbPuZEECbp3vJbQ&s.jpg"}

  }
  return render_template("songs.html", number=number, info= list(info.values()))


@app.route('/score', methods=['GET', 'POST'])
def score ():
  ID = session['user']['localId']
  user_info = db.child('Users').child(ID).get().val()
  score = user_info['score'] 
  name = user_info['name']
  if request.method == 'GET':
    return render_template("score.html",score= score, name=name)
  else:
    return redirect(url_for('score'))
    






if __name__ == '__main__':
 
    app.run( debug=True)