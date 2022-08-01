from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


confing = {
  "apiKey": "AIzaSyAm2YY8IT6kGhI8Q0efRv-uD8XiIOZ5iTs",
  "authDomain": "hanna-f652b.firebaseapp.com",
  "projectId": "hanna-f652b",
  "storageBucket": "hanna-f652b.appspot.com",
  "messagingSenderId": "177459869692",
  "appId": "1:177459869692:web:f9d9ef5b1dfd629be62479",
  "measurementId": "G-K6RC53GDLM",
  "databaseURL":"https://hanna-f652b-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase= pyrebase.initialize_app(confing)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

# db.child("Users").child(login_session['user']['localld']).get().val()

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)      
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)