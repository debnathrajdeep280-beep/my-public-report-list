from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Fake database users aur complaints ke liye
users_db = {}
problems = [
    {'title': 'Street Light Kharab Hai', 'category': 'Bijli', 'details': 'Ward No. 3 ki street light band hai.', 'user': 'Rajdeep'}
]

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    
    # User ko database mein save kiya
    users_db[email] = {'username': username, 'phone': phone, 'password': password}
    
    # Register ke baad seedhe login karwa rahe hain
    return render_template('dashboard.html', username=username, phone=phone, email=email, role='user', problems=problems)

@app.route('/guest')
def guest_login():
    return render_template('dashboard.html', username='Guest User', phone='', email='', role='guest', problems=problems)

@app.route('/submit-problem', methods=['POST'])
def submit_problem():
    title = request.form.get('title')
    category = request.form.get('category')
    details = request.form.get('details')
    username = request.form.get('username', 'User')
    phone = request.form.get('phone', '')
    email = request.form.get('email', '')
    
    # Nayi shikayat ko list mein jodh rahe hain
    problems.append({'title': title, 'category': category, 'details': details, 'user': username})
    
    # Wapas dashboard par hi bhej rahe hain bina kisi error ke
    return render_template('dashboard.html', username=username, phone=phone, email=email, role='user', problems=problems)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
