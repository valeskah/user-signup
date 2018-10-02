from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask (__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('home_form.html')

def is_blank(input):
    if input == '':
        return True
    else:
        return False

@app.route('/', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    ver_password= request.form['ver_password']
    email = request.form['email']

    user_error = ''
    password_error = ''
    ver_blank_error = ''
    email_error = ''
    
    if is_blank(username):
        user_error = 'Please enter a valid username'

    elif len(username) < 3:
        user_error = 'Username must contain 3 or more characters'

    elif len(username) > 20:
        user_error = 'Username must be less than 20 characters'

    elif ' ' in username:
        user_error = "Username cannot contain spaces"

    else:
        user_error = ''

    if is_blank(password):
        password_error = 'Please enter a valid password'

    elif len(password) < 3:
        password_error = 'Password must contain 3 characters or more'

    elif len(password) > 20:
        password_error = 'Password must be less than 20 characters'

    elif ' ' in password:
        password_error = 'Password cannot contain spaces'

    elif is_blank(ver_password):
        ver_blank_error = 'Please verify your password'
        
    elif password != ver_password:
        password_error = 'Passwords do not match please re-enter'

    else:
        password_error = ''
        ver_blank_error = ''
    
    if not is_blank(email):
        if len(email) < 3:
            email_error = 'E-mail must contain 3 characters or more'

        elif len(email) > 20:
            email_error = 'E-mail must be less than 20 characters'

        elif ' ' in email:
            email_error = 'E-mail cannot contain spaces'

        elif '@' not in email or '.' not in email:
            email_error = 'Not a valid e-mail'

        else: email_error = ''

    if not user_error and not password_error and not ver_blank_error and not email_error:
        return render_template('welcome_page.html', username=username)

    else:
        return render_template('home_form.html', user_error=user_error, password_error=password_error, email_error=email_error, 
        ver_blank_error = ver_blank_error, username=username, email=email)



app.run()