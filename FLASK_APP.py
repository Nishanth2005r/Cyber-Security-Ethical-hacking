from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML code for login form (inside Python using render_template_string)
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST" action="/login">
        <label>Username:</label>
        <input type="text" name="username"><br><br>
        <label>Password:</label>
        <input type="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return login_page   # show login form

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    password = request.form['password']

    # simple check (you can change username/password)
    if user == "admin" and password == "1234":
        return f"<h2>Welcome, {user}!</h2>"
    else:
        return "<h2>Invalid username or password. Try again.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
