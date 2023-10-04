from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secret key of your choice

# Your user database (this is a simple example, you would typically use a database)
users = {
    'username': 'password',
    'shak' : 'shak'
}

@app.route('/')
def home():
    if 'username' in session:
        # return redirect(url_for('dashboard'))
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if users.get(username) == password:
        session['username'] = username
        return render_template('home.html')
    else:
        return 'Invalid credentials. Please try again.'

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Welcome to the Dashboard, {session["username"]}!'
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')
