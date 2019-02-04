from flask import Flask, request, redirect, render_template
import os
import jinja2



template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__) 
app.config['DEBUG'] = True 

@app.route("/")
def index():
    template = jinja_env.get_template('signup-one.html')
    return template.render()
    



@app.route("/val", methods=['POST'])
def val():
    username = request.form['username']
    password = request.form['password']
    confirm_pw = request.form['confirm_pw']
    email = request.form['email']
    un_error = ''
    pw_error = ''
    cpw_error = ''
    em_error = ''
    if len(username) < 3 or len(username) > 19:
        un_error = 'Make sure your username is between 3 and 20 characters!'
    if len(password) < 3 or len(username) > 19:
        pw_error = 'Make sure your password is between 3 and 20 characters!'
    if password != confirm_pw:
        cpw_error = "Oops! Looks like your passwords didn't match."
    
    if email.count('@') > 1:
        em_error = 'Invalid e-mail. Make sure you include one "@" and one "."'
    if email.count('.') > 1:
        em_error = 'Invalid e-mail. Make sure you include one "@" and one "."'
    if username == '':
        un_error = 'Please enter a username.'
    if password == '':
        pw_error = 'Please enter a password.'
    if confirm_pw == '':
        cpw_error = 'Please confirm your password.'
    if len(email) > 0:
        if len(email) < 3 or len(email) > 19:
            em_error = 'Make sure your e-mail is between 3 and 20 characters!'
        else:
            em_error = ''

    
    if not un_error and not pw_error and not cpw_error and not em_error:
        return redirect('/success?username={0}'.format(username))
    else:
        template = jinja_env.get_template('signup-one.html')
        return template.render(username=username,
        email=email,
        un_error=un_error,
        pw_error=pw_error,
        cpw_error=cpw_error,
        em_error=em_error)

@app.route('/success')
def success():
    username = request.args.get('username')
    template = jinja_env.get_template('success.html')
    return template.render(username=username)

    


    
    
  
app.run()
