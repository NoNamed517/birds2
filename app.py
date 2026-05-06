from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# --- Simulovaná databáze uživatelů ---
users_db = {
    "test@example.com": generate_password_hash("heslo123")
}

# --- Simulovaná databáze ptáků ---
birds_db = [
    {
        "id": 1,
        "name": "Slavík obecný",
        "location": "Praha",
        "date": "2026-05-01",
        "note": "Zpíval u řeky"
    },
    {
        "id": 2,
        "name": "Vrabec domácí",
        "location": "Brno",
        "date": "2026-05-03",
        "note": "Věděl si rady s pečivem"
    }
]

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

# --- Dashboard / Birds dataset ---
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=session['user'], birds=birds_db)

# --- Add new bird ---
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_bird():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        location = request.form.get('location').strip()
        date = request.form.get('date')
        note = request.form.get('note').strip()

        # Validace povinných polí
        if not name or not date:
            flash("Název druhu a datum jsou povinné.", "danger")
            return redirect(url_for('add_bird'))

        # Generování unikátního ID
        new_id = max([b['id'] for b in birds_db], default=0) + 1
        birds_db.append({
            "id": new_id,
            "name": name,
            "location": location,
            "date": date,
            "note": note
        })
        flash("Nový záznam přidán.", "success")
        return redirect(url_for('dashboard'))

    return render_template('add_bird.html')

# --- Delete bird ---
@app.route('/delete/<int:bird_id>')
@login_required
def delete_bird(bird_id):
    global birds_db
    birds_db = [b for b in birds_db if b['id'] != bird_id]
    flash("Záznam odstraněn.", "info")
    return redirect(url_for('dashboard'))

# --- Edit bird ---
@app.route('/edit/<int:bird_id>', methods=['GET', 'POST'])
@login_required
def edit_bird(bird_id):
    bird = next((b for b in birds_db if b['id'] == bird_id), None)
    if not bird:
        flash("Záznam nenalezen.", "danger")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        bird['name'] = request.form.get('name').strip()
        bird['location'] = request.form.get('location').strip()
        bird['date'] = request.form.get('date')
        bird['note'] = request.form.get('note').strip()
        flash("Záznam aktualizován.", "success")
        return redirect(url_for('dashboard'))

    return render_template('edit_bird.html', bird=bird)

# --- Homepage redirect ---
@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)