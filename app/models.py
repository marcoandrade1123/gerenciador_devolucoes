from app import db, login_manager, bcrypt
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


