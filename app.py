from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # pro sessions, v produkci používej env proměnnou

# --- Simulovaná databáze uživatelů ---
users_db = {
    "test@example.com": generate_password_hash("heslo123")
}

# --- Decorator pro ochranu rout ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash("Nejprve se přihlašte!", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Login route ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_password_hash = users_db.get(email)
        if user_password_hash and check_password_hash(user_password_hash, password):
            session['user'] = email
            flash("Úspěšně přihlášen!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Neplatné přihlašovací údaje.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

# --- Logout route ---
@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    flash("Odhlášeno.", "info")
    return redirect(url_for('login'))

# --- Protected route ---
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=session['user'])

# --- Homepage redirect ---
@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)