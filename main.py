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
        user_error = "Please enter a valid username"
        return render_template('home_form.html', user_error=user_error, email=email)
    else:
        if len(username) < 3:
            user_error = 'Username must contain 3 characters or more'
            return render_template('home_form.html', user_error=user_error, username=username, email=email)

        if len(username) > 20:
            user_error = 'Username must contain less than 20 characters'
            return render_template('home_form.html', user_error=user_error, username=username, email=email)

        else:
            if ' ' in username:
                user_error = "Username cannot contain spaces"
                return render_template('home_form.html', user_error=user_error, username=username, email=email)

    if not is_blank(email): 
        if len(email) < 3:
            email_error = 'E-mail must be longer than 3 characters'
            return render_template('home_form.html', username=username, email_error=email_error, email=email)
        
        if len(email) > 20:
            email_error = "E-mail must be less than 20 character"
            return render_template('home_form.html', username=username, email_error=email_error, email=email)

        else:
            if " " in email:
                email_error = 'E-mail cannot contain spaces'
                return render_template('home_form.html', username=username, email_error=email_error, email=email)
            else:
                if ('@' and '.') not in email:
                    email_error = 'Not a valid email, please re-enter.'
                    return render_template('home_form.html', username=username, email_error=email_error, email=email)

    if is_blank(password):
        password_error = "Please enter a valid password"
        return render_template('home_form.html', username=username, password_error=password_error, email=email)

    if not is_blank(password) and is_blank(ver_password):
        ver_blank_error = "Please verify your password"
        return render_template('home_form.html', username=username, user_error=user_error, 
        password_error=password_error, ver_blank_error=ver_blank_error, email=email)
    
    else:
        if len(password) < 3:
            password_error = "Passwords must contain 3 characters or more"
            return render_template('home_form.html', username=username, password_error=password_error, email=email)

        if len(password) > 20:
            password_error = "Passwords must contain less than 20 characters"
            return render_template('home_form.html', username=username, password_error=password_error, email=email)

        else:
            if ' ' in password:
                password_error = "Passwords cannot contain spaces"
                return render_template('home_form.html', username=username, password_error=password_error, email=email)
            
            else:
                if password != ver_password:
                    password_error = "Passwords do not match, please re-enter."
                    return render_template('home_form.html', username=username, password_error=password_error, email=email)

    
        if not user_error and not password_error and not email_error:
            return render_template('welcome_page.html', username=username)





app.run()