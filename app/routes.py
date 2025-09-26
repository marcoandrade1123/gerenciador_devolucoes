from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm, EditUserForm
from app.models import User
from functools import wraps

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

# --- DECORATOR DE PERMISSÃO DE ADMIN ---
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Acesso negado. Esta área é restrita a administradores.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


# --- NOVA ROTA DE GERENCIAMENTO DE USUÁRIOS ---
@app.route('/admin/users')
@login_required
@admin_required
def admin_users():
    # Busca todos os usuários no banco de dados, ordenados pelo nome
    users = User.query.order_by(User.name).all()
    return render_template('admin_users.html', title='Gerenciamento de Usuários', users=users)

# --- NOVA ROTA DE EDIÇÃO DE USUÁRIO ---
@app.route('/admin/user/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    # Busca o usuário no banco de dados pelo ID fornecido na URL.
    # O .first_or_404() é um atalho útil: se não encontrar o usuário, ele
    # automaticamente retorna uma página de erro 404 (Not Found).
    user = User.query.get_or_404(user_id)
    
    # Instancia o formulário, passando o e-mail original do usuário
    # para a lógica de validação personalizada que criamos.
    form = EditUserForm(original_email=user.email)

    # --- LÓGICA PARA QUANDO O FORMULÁRIO É ENVIADO (MÉTODO POST) ---
    if form.validate_on_submit():
        # Atualiza os dados do objeto 'user' com os dados que vieram do formulário
        user.name = form.name.data
        user.email = form.email.data
        user.role = form.role.data
        user.is_active = form.is_active.data
        
        # "Comita" a sessão para salvar as alterações no banco de dados
        db.session.commit()
        
        # Exibe uma mensagem de sucesso para o administrador
        flash('Usuário atualizado com sucesso!', 'success')
        
        # Redireciona de volta para a página de listagem de usuários
        return redirect(url_for('admin_users'))

    # --- LÓGICA PARA QUANDO A PÁGINA É CARREGADA PELA PRIMEIRA VEZ (MÉTODO GET) ---
    # Preenche o formulário com os dados atuais do usuário que veio do banco
    form.name.data = user.name
    form.email.data = user.email
    form.role.data = user.role
    form.is_active.data = user.is_active
    
    # Renderiza o template de edição, passando o formulário preenchido
    return render_template('edit_user.html', title=f'Editar Usuário: {user.name}', form=form, user=user)
