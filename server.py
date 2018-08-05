from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z._-]+\.[a-zA-Z]+$')
name_check= re.compile(r'^[a-zA-Z]+$')
password_check= re.compile(r'\d.+[A-Z]|[A-Z].+\d')
app = Flask(__name__)
app.secret_key="DANKMEMESARENEVERDANKENOUGH"
@app.route('/', methods=['GET'])
def index():
    return render_template("shitter.html")

@app.route('/process', methods=['POST'])
def submit():
    valid = True
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        valid = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        valid = False
    
    if len(request.form['first']) < 1:
        flash("First name cannot be blank!")
        valid = False
    elif not name_check.match(request.form['first']):
        flash("First name can not contain numbers")
        valid = False
    
    if len(request.form['last']) < 1:
        flash("Last name cannot be blank!")
        valid = False
    elif not name_check.match(request.form['last']):
        flash("Last name can not contain numbers")
        valid = False
    
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")
        valid = False
    elif len(request.form['password'])<=8:
        flash("Password has to be at least 8 characters long")
    elif not request.form['password']==request.form['confirmpassword']:
        flash("Password does not match with the confirmation")
        valid=False
    elif not password_check.match(request.form['password']):
        flash("Password needs at least 1 uppercase and one 1numeric value")
        valid = False

    if valid ==False:
        return redirect('/')

    email=request.form['email']
    first=request.form['first']
    last=request.form['last']
    password=request.form['password']
    date=request.form['date']

    return render_template('regire.html')

if __name__=="__main__":
    app.run(debug=True)