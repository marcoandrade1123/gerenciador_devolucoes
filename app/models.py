from app import db, login_manager, bcrypt
from flask_login import UserMixin

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DO FLASK-LOGIN
# -----------------------------------------------------------------------------

# Esta função é necessária para o Flask-Login.
# Ela é usada para recarregar o objeto do usuário a partir do ID de usuário 
# armazenado na sessão, sempre que uma página protegida é acessada.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -----------------------------------------------------------------------------
# MODELO DE DADOS DO USUÁRIO
# -----------------------------------------------------------------------------

class User(db.Model, UserMixin):
    """
    Modelo da tabela de Usuários.
    Armazena informações de login, dados pessoais e o papel de acesso do usuário.
    """
    # Nome da tabela no banco de dados
    __tablename__ = 'user'

    # --- Colunas da Tabela ---
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(30), nullable=False, default='viewer')
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    # --- Métodos de Gerenciamento de Senha ---

    def set_password(self, password):
        """
        Gera o hash da senha fornecida e o armazena no campo password_hash.
        Este método é chamado ao criar um novo usuário ou ao resetar uma senha.
        """
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Verifica se a senha fornecida no formulário de login corresponde ao 
        hash armazenado no banco de dados.
        Retorna True se a senha for válida, False caso contrário.
        """
        return bcrypt.check_password_hash(self.password_hash, password)

    # --- Representação do Objeto ---

    def __repr__(self):
        """
        Define como o objeto User será exibido quando for printado.
        Útil para depuração.
        """
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', role='{self.role}')"

