from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Configurações simples por enquanto (depois moveremos para um arquivo de configuração)
app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-dificil-de-adivinhar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # Define o banco de dados SQLite

# Inicializa as extensões
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Informa ao Flask-Login qual é a rota de login
login_manager.login_message_category = 'info' # Categoria da mensagem de flash para o login

# Importa as rotas e os modelos para que sejam registrados na aplicação
# A importação é feita no final para evitar importações circulares
from app import routes, models

