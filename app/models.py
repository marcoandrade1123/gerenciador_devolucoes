from app import db, login_manager, bcrypt, app
from flask_login import UserMixin

# Esta função é necessária para o Flask-Login.
# Ela é usada para recarregar o objeto do usuário a partir do ID de usuário armazenado na sessão.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    Modelo da tabela de Usuários.
    Armazena informações de login, dados pessoais e o papel de acesso do usuário.
    """
    # Nome da tabela no banco de dados
    __tablename__ = 'user'

    # Colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(30), nullable=False, default='viewer')

    # Propriedade 'password' que não pode ser lida diretamente
    @property
    def password(self):
        raise AttributeError('A senha não é um atributo legível.')

    # Método para definir a senha, gerando o hash
    @password.setter
    def password(self, password_text):
        self.password_hash = bcrypt.generate_password_hash(password_text).decode('utf-8')

    # Método para verificar a senha fornecida no login
    def verify_password(self, password_text):
        return bcrypt.check_password_hash(self.password_hash, password_text)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.role}')"
    

# --- Criando o Comando para Adicionar Usuários ---

import click

@app.cli.command('create-user')
@click.argument('name')
@click.argument('email')
@click.argument('password')
@click.argument('role')
def create_user_command(name, email, password, role):
    """Cria um novo usuário com os dados fornecidos."""
    
    # Verifica se o e-mail já existe
    if User.query.filter_by(email=email).first():
        print(f"Erro: O e-mail '{email}' já está em uso.")
        return

    # Verifica se o papel (role) é válido
    valid_roles = ['admin', 'sac1_sac2_add_edit', 'sac1_edit', 'sac2_edit', 'fat_edit', 'viewer']
    if role not in valid_roles:
        print(f"Erro: O papel '{role}' é inválido. Use um dos seguintes: {', '.join(valid_roles)}")
        return

    # Cria a instância do novo usuário
    user = User(name=name, email=email, role=role)
    # Define a senha (isso vai gerar o hash automaticamente)
    user.password = password
    
    # Adiciona ao banco de dados
    db.session.add(user)
    db.session.commit()
    
    print(f"Usuário '{name}' criado com sucesso com o papel '{role}'.")




