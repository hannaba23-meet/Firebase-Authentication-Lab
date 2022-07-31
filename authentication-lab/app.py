from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyAm2YY8IT6kGhI8Q0efRv-uD8XiIOZ5iTs",
  "authDomain": "hanna-f652b.firebaseapp.com",
  "projectId": "hanna-f652b",
  "storageBucket": "hanna-f652b.appspot.com",
  "messagingSenderId": "177459869692",
  "appId": "1:177459869692:web:f9d9ef5b1dfd629be62479",
  "measurementId": "G-K6RC53GDLM"
  "firebaseURL" : ""
}

firebase= pyrebase.initialize_app(confing)
auth = firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)