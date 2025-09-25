from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm
from app.models import User

# ROTA DA PÁGINA INICIAL (FALTANDO)
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Página Inicial')

# ROTA DE LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # Esta linha vai dar erro se a rota 'index' não existir.
        # É por isso que precisamos da função index() acima.
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('Falha no login. Verifique seu e-mail e senha.', 'danger')
    return render_template('login.html', title='Login', form=form)

# ROTA DE LOGOUT
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
