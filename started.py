from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    valid = True
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        valid = False

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        valid = False

    else:
        flash("Success!")


    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
        valid = False

    
    elif len(request.form['comment']) > 100:
        flash("Comment must be less than 100 characters", 'comment')
        valid = False

    if valid==False:
        return redirect('/')

    email=request.form['email']
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']

    return render_template('resultpage.html')
if __name__=="__main__":
    app.run(debug=True)