from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import click # Importa a biblioteca click para os comandos de CLI

# -----------------------------------------------------------------------------
# INICIALIZAÇÃO DA APLICAÇÃO E EXTENSÕES
# -----------------------------------------------------------------------------

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Configurações da aplicação
app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-dificil-de-adivinhar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Inicializa as extensões com a aplicação
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Configurações do Flask-Login
login_manager.login_view = 'login' # Informa ao Flask-Login qual é a rota de login
login_manager.login_message_category = 'info' # Categoria da mensagem de flash

# -----------------------------------------------------------------------------
# COMANDOS PERSONALIZADOS DA LINHA DE COMANDO (CLI)
# -----------------------------------------------------------------------------

# É preciso importar o modelo User aqui para usá-lo no comando
from app.models import User

@app.cli.command('create-user')
@click.option('--name', required=True, help='Nome completo do usuário.')
@click.option('--email', required=True, help='E-mail de login do usuário.')
@click.option('--password', required=True, help='Senha do usuário.')
@click.option('--role', default='viewer', help='Role de acesso (ex: admin, viewer).')
def create_user_command(name, email, password, role):
    """Cria um novo usuário na linha de comando."""
    # Verifica se o usuário já existe
    if User.query.filter_by(email=email).first():
        click.echo(f'Erro: O e-mail "{email}" já está em uso.')
        return

    # Cria a instância do usuário
    user = User(name=name, email=email, role=role)
    user.set_password(password) # Define a senha com hash

    # Adiciona à sessão e SALVA permanentemente no banco de dados
    db.session.add(user)
    db.session.commit() # <<< --- ESTA ERA A LINHA CRUCIAL QUE FALTAVA

    click.echo(f'Sucesso! Usuário "{name}" criado com o role "{role}".')

# -----------------------------------------------------------------------------
# IMPORTAÇÃO FINAL DE ROTAS E MODELOS (EVITA IMPORTAÇÃO CIRCULAR)
# -----------------------------------------------------------------------------
# Esta importação deve permanecer no final do arquivo.
# Ela garante que as rotas e modelos sejam "vistos" pela aplicação,
# mas só depois que a variável 'app' e as extensões já foram criadas.
from app import routes, models
