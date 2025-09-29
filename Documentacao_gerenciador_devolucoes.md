# Projeto gerenciador_devolucoes
Este projeto foi desenvolvido utilizando as seguintes linguagens e tecnologias:
* ### Backend (Linguagem): Python
* ### Framework Web: Flask
*Flask é um microframework web em Python, o que significa que é um conjunto de ferramentas e bibliotecas focado em ser leve, flexível e minimalista para construir aplicações web e APIs de forma rápida.*
* ### Banco de Dados: SQLite. 
*É um banco de dados que não requer um servidor separado, armazenando tudo em um único arquivo no projeto.*<br>
*Ele já vem incluído com o Python, é gratuito e perfeito para aplicações de pequeno a médio porte.*<br>
*Quando ou projeto crescer, será fácil migrar para um banco de dados mais potente como o PostgreSQL.*
* ### Frontend (Interface do Usuário): HTML, CSS e JavaScript. 
*São as tecnologias padrão para criar as páginas que o usuário verá no navegador.*
## Estrutura de Pastas do Projeto
![Estrutura das pastas](/app/static/img/Estrutura_pastas.png)
### Explicação de Cada Parte
* **run.py**: É o ponto de entrada do aplicativo.<br>Você executará este arquivo para iniciar o servidor web e poder acessar o sistema no seu navegador.<br>Exemplo:<br>(venv) PS C:\projetos_python\gerenciador_devolucoes>python run.py
* **app/**: Este é o "coração" do projeto.
* **__init__.py**: Configura a aplicação Flask, conecta com o banco de dados e carrega outras partes do sistema.
* **models.py**: Aqui será definida a estrutura dos dados.<br>Por exemplo, uma classe Usuario (com campos como username e password) e uma classe Devolucao (com campos como produto, data_devolucao, motivo, status).
* **routes.py**: Controla o que acontece quando um usuário acessa uma URL.<br>Por exemplo, quando o usuário for para /login, este arquivo terá a função que renderiza a página login.html e processa os dados do formulário de login.
* **forms.py**: Facilita a criação e validação de formulários HTML, como o de login e o de cadastro de devoluções.
* **templates/**: Contém os arquivos HTML que formam a interface visual do aplicativo.
* **static/**: Guarda arquivos que não mudam, como CSS para estilização e JavaScript para comportamento dinâmico no navegador.
* **venv/**: É o ambiente virtual do Python.<br>
Ele isola as bibliotecas que o projeto usa (como o Flask, etc.) das outras instaladas no seu computador, evitando conflitos.<br>
---
## <span style="color: yellow;">Iniciando o projeto (criar/ativar ambiente virtual, iniciar repositório Git, instalar o Flask e bibliotecas...)
### Criando o ambiente virtual:
```
C:\projetos_python\gerenciador_devolucoes>python -m venv venv
```
Após a criação do ambiente virtual, é necessário sua ativação com o seguinte comando:
```
C:\projetos_python\gerenciador_devolucoes>venv\Scripts\activate
```
### Iniciar o Repositório Git e Criar o .gitignore
O ***.gitignore*** é um arquivo essencial que diz ao Git para ignorar certos arquivos e pastas, como o ambiente venv e outros arquivos temporários.<br>
Primeiro, crie o arquivo .gitignore com o conteúdo recomendado, no diretório do projeto **C:\projetos_python\gerenciador_devolucoes>**, digitando o seguinte comamndo:
```
echo venv/ > .gitignore<br>
echo __pycache__/ >> .gitignore<br>
echo *.pyc >> .gitignore<br>
echo instance/ >> .gitignore<br>
```
Agora, inicie o repositório Git localmente:
```
git init<br>
git add .<br>
git commit -m "Estrutura inicial do projeto"
```
### Próximos Passos (GitHub)
O projeto agora está com a estrutura criada e versionado localmente com o Git.<br> O próximo passo é conectá-lo ao GitHub.<br>
Vá até o site do GitHub e crie um novo repositório (clique em "New").<br>
Dê a ele o nome gerenciador_devolucoes.<br>Importante: Não marque as opções para adicionar README, .gitignore ou licença, pois já criamos tudo localmente.<br>
Após criar o repositório, o GitHub lhe dará uma URL (ex: https://github.com/seu-usuario/gerenciador_devolucoes.git ) e alguns comandos.<br>Agora, executar os seguintes comandos no seu terminal para que o código seja versionado no GitHub.<br><br>**C:\projetos_python\gerenciador_devolucoes>**
```
git remote add origin https://github.com/seu-usuario/gerenciador_devolucoes.git
git branch -M main<br>
git push -u origin main
```
### Instalando o Framework Flask e algumas bibliotecas
Lembre-se de que o ambiente virtual deve estar ativo para que as bibliotecas sejam instaladas no lugar certo.<br>Você saberá que ele está ativo se vir (venv) no início da linha do seu terminal.<br>Se não estiver ativo, basta executar novamente em **C:\projetos_python\gerenciador_devolucoes>**
```
venv\Scripts\activate
```
Com o ambiente ativo, execute o seguinte comando para instalar o Flask e as extensões que nos ajudarão a trabalhar com o banco de dados, login de usuários e formulários:
```
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Login Flask-WTF python-dotenv Flask-Bcrypt
```
Vamos entender o que cada uma faz:<br>
* **Flask**: O framework web principal.
* **Flask-SQLAlchemy**: Facilita a comunicação com o banco de dados (nosso SQLite) usando Python em vez de SQL puro.
* **Flask-Migrate**: Ajuda a gerenciar alterações na estrutura do banco de dados (como adicionar uma nova coluna) de forma organizada.
* **Flask-Login**: Gerencia todo o processo de autenticação de usuários (login, logout, sessões).
* **Flask-WTF**: Simplifica a criação e validação de formulários web, como os de login e de devolução.
* **python-dotenv**: Permite carregar configurações de um arquivo .env, o que é ótimo para guardar informações sensíveis.
* **Flask-Bcrypt**: Usaremos para criar o "hash" seguro das senhas dos usuários.
### Criando o Arquivo de Requisitos
Após a instalação, é uma boa prática salvar a lista de bibliotecas e suas versões em um arquivo chamado requirements.txt.<br>Isso facilita a instalação do projeto em outro computador ou no servidor (como na AWS).<br>
Execute este comando:
```
pip freeze > requirements.txt
```
Agora, se eu (ou outra pessoa) precisar configurar o projeto em uma nova máquina, bastará executar pip install -r requirements.txt para instalar todas as dependências de uma só vez.<br>
Não se esqueça de adicionar essa mudança ao Git:<br> **C:\projetos_python\gerenciador_devolucoes>**
```
git add requirements.txt
git commit -m "Adiciona dependências do projeto"
git push origin main
```
---
## <span style="color: yellow;">1. Primeira parte (Banco de Dados -> Dados Iniciais -> Interface de Login -> Lógica de Login) 
Seguir essa sequência lógica ***(Banco de Dados -> Dados Iniciais -> Interface de Login -> Lógica de Login)***, <br>
é muito mais didático, onde cada passo se baseia no anterior, tornando o processo de construção claro e coeso.
### Código para app/__init__.py<br>
Este arquivo é o coração do pacote app.<br>Ele vai inicializar o Flask, carregar as configurações e registrar as extensões que instalamos.<br>
```
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
```
O que este código faz?<br>
* Importa o Flask e todas as extensões que foram instaladas.<br>
* Cria a variável app, que é a aplicação Flask.<br>
* SECRET_KEY: É uma chave de segurança usada pelo Flask para proteger as sessões dos usuários. *(Vamos torná-la mais segura depois.)*<br>
* SQLALCHEMY_DATABASE_URI: Informa ao SQLAlchemy onde o banco de dados está.<br>sqlite:///site.db significa que ele criará um arquivo chamado site.db dentro da pasta principal do projeto.<br>
* Inicializa db, migrate, bcrypt e login_manager associando-os à nossa app.<br>
* Importa routes e models no final.<br>Isso é crucial para que as rotas e os modelos de banco de dados que será criado a seguir, sejam "enxergados" pela aplicação.

---
### Código para run.py
Este arquivo é muito mais simples.<br>Sua única função é importar a variável **app** que acabamos de criar e iniciar o servidor de desenvolvimento.
```
from app import app

if __name__ == '__main__':
    app.run(debug=True)
```
* if __name__ == '__main__': é uma construção padrão em Python que garante que o código dentro dela só será executado quando o arquivo run.py for o arquivo principal.
* app.run(debug=True) inicia o servidor.<br>O modo debug=True é extremamente útil durante o desenvolvimento, pois ele reinicia o servidor automaticamente a cada alteração no código e mostra mensagens de erro detalhadas no navegador.

---
### Código para **app/models.py**<br>
Ele define a classe User que será mapeada para a tabela no banco de dados.<br>
Vamos transformar a estrutura da tabela **User** (que eu defini como seria), em código Python usando o SQLAlchemy.

```
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
```
### Entendendo o Código
* **from app import db, login_manager, bcrypt**: Importamos as instâncias do SQLAlchemy (db), do LoginManager e do Bcrypt que criamos no __init__.py.
* **from flask_login import UserMixin**: UserMixin é uma classe especial do Flask-Login que já inclui as implementações padrão para os métodos que o Flask-Login espera que um modelo de usuário tenha (como is_authenticated, is_active, etc.).
* **@login_manager.user_loader**: Este é um "decorator" que registra a função load_user com o Flask-Login.<br>Toda vez que o Flask-Login precisar obter as informações do usuário logado, ele chamará esta função com o ID do usuário.
* **class User(db.Model, UserMixin)**: Nossa classe User herda de db.Model (para que o SQLAlchemy saiba que ela é um modelo de banco de dados) e de UserMixin (para obter as funcionalidades de login).
* **__tablename__ = 'user'**: Embora o SQLAlchemy geralmente adivinhe o nome da tabela, é uma boa prática defini-lo explicitamente.
* **db.Column(...)**: Cada atributo da classe que é uma db.Column se tornará uma coluna na nossa tabela do banco de dados, com os tipos e restrições que definimos.
* **password, @password.setter, verify_password**: Este é o trio que lida com a segurança da senha.<br>
A propriedade **password** impede que alguém acidentalmente leia a senha.<br>
O método **password.setter** é chamado quando fazemos **usuario.password = 'nova_senha'**.<br>Ele não armazena 'nova_senha', mas sim o **hash** gerado pelo bcrypt.<br>
O método **verify_password** será usado na nossa rota de login para comparar a senha que o usuário digitou com o hash que está no banco.<br>
* **__repr__**: É um método opcional que define como o objeto User será exibido se você o imprimir no terminal.<br>É muito útil para depuração.<br>
Com este código, temos um modelo de usuário completo, seguro e pronto para ser usado.
---
## Criando o Banco de Dados e a Tabela User
Abra o seu terminal na pasta do projeto **C:\projetos_python\gerenciador_devolucoes** e certifique-se de que o ambiente virtual **(venv)** está ativo.<br>
* Passo 1: Inicializar o Flask-Migrate<br>
Este comando criará uma nova pasta chamada ***migrations*** no seu projeto.<br>É nela que os scripts de migração ficarão guardados.<br><br>
Execute no terminal:
```
flask db init
```
***Observação: Você só precisa fazer isso uma única vez.***
* Passo 2: Gerar o Script de Migração<br>
Agora, vamos pedir ao Flask-Migrate para ler nosso **models.py** e criar o primeiro script de migração, que conterá as instruções para criar a tabela user.<br><br>
Execute no terminal:
```
flask db migrate -m "Cria a tabela User"
```
* O -m "Cria a tabela User" é uma mensagem descritiva que nos ajuda a lembrar o que essa migração faz.<br>
Você verá uma mensagem como INFO [alembic.runtime.migration] Generating ...\migrations\versions\xxxxxxxxxxxx_cria_a_tabela_user.py ... done.<br>Isso confirma que o script foi criado.
## Passo 3: Aplicar a Migração (Criar a Tabela)
Este é o comando que efetivamente executa o script e cria a tabela no banco de dados.<br><br>
Execute no terminal:
```
flask db upgrade
```
***Você verá algumas linhas de log do Alembic (a biblioteca por trás do Flask-Migrate) e, ao final, a tabela user estará criada.***

**Observações:**<br>
* O nome ***site.db*** não é um padrão obrigatório, mas sim o nome que nós escolhemos no arquivo de configuração ***--init--.py***.
* ***app.config['SQLALCHEMY_DATABASE_URI']***: Esta é a chave de configuração que o Flask-SQLAlchemy usa para saber como e onde se conectar ao banco de dados.
* ***sqlite:///***: Esta parte informa que estamos usando o driver do SQLite.
* ***site.db***: Esta é a parte onde o nome do arquivo é definido.<br>Poderia ter sido escolhido qualquer outro nome, como devolucoes.db, meu_banco.sqlite, ou qualquer outra coisa.

**Importante:** A configuração ***sqlite:///site.db*** (com três barras) diz ao ***SQLAlchemy*** para criar o arquivo ***site.db*** em uma pasta padrão de instância do Flask, que é a pasta ***instance***.<br>É por isso que o arquivo ***site.db*** apareceu lá dentro.

***Verificando o Resultado***<br>
Agora, na pasta raiz do projeto (gerenciador_devolucoes), verá um novo arquivo: ***site.db*** (Este é o banco de dados SQLite!)<br>
A tabela ***user*** e as demais que serão criadas, estarão dentro deste arquivo ***site.db***<br>Podemos usar um programa como o ***DB Browser for SQLite*** (que é gratuito) para abrir o arquivo ***site.db*** e visualizar a estrutura da tabela ***user*** que acabamos de criar.

***Atualizando as alteraçõs do projeto: C:\projetos_python\gerenciador_devolucoes - no GitHub***
```
git add .
git commit -m "Configura o Flask-Migrate e cria a tabela User"
git push origin main
```
---
## Criando o Comando para Adicionar Usuários na tabela user
Abra o arquivo ***app/models.py*** e adicione o seguinte código ao final do arquivo:
```
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
```
### O que esse código faz?
* ***import click***: Click é uma biblioteca que o Flask usa para criar comandos de linha de comando.
* ***@app.cli.command('create-user')***: Registra uma nova função como um comando flask.<br>Agora poderemos executar ***flask create-user*** ... no terminal.
* ***@click.argument(...)***: Define os argumentos que o comando espera receber: name, email, password e role.<br>
* A função ***create_user_command*** recebe esses argumentos, faz validações (para garantir que o e-mail não exista e que o papel é válido), cria o objeto User, define a senha (o que aciona nosso @password.setter para criar o hash) e salva tudo no banco de dados.
### Executando o Comando para Criar o Usuário admin (exemplo)
Vá para o seu terminal, ***com o ambiente (venv) ativo***, e execute o comando abaixo.<br>
***Importante:*** Escolha um nome, e-mail e senha para o seu administrador.
```
flask create-user "Administrador do Sistema" "admin@devolucoes.com" "senha123" "admin"
```
###  salvar as alterações no Git:
```
git add app/models.py
git commit -m "Adiciona comando para criar usuários via CLI"
git push origin main
```
---
### Próximos passos:
* ***Criar o Formulário de Login (app/forms.py)***: Definiremos os campos do formulário (e-mail e senha) usando a biblioteca ***Flask-WTF***.
* ***Criar a Página de Login (app/templates/login.html)***: Criaremos o HTML básico para exibir o formulário que o usuário irá preencher.
* ***Implementar a Rota de Login (app/routes.py)***: Escreveremos a lógica em Python que:<br>
1. Exibe a página de login.
2. Recebe os dados do formulário quando o usuário clica em "Entrar".
3. Verifica se o usuário existe e se a senha está correta (usando o método ***verify_password*** que criamos).
4. "Loga" o usuário no sistema usando o ***Flask-Login***.
5. Redireciona o usuário para a página principal após o login bem-sucedido.<br>
Essa abordagem nos dará um ciclo completo e funcional:<br> 
um usuário que existe no banco de dados conseguirá, de fato, entrar no sistema.
> * ***app/templates/login.html*** (O Desenho / A Aparência): Este arquivo é o "O QUÊ".<br>
Ele define o que o usuário vê na tela. É a estrutura visual, o esqueleto da página.<br> 
Ele contém as tags HTML que dizem: "aqui vai um campo para o e-mail", "aqui vai um campo para a senha", "aqui vai um botão de enviar".<br> 
Ele cuida da aparência, das cores, da disposição dos elementos. É a parte visual e estática.
> * ***app/forms.py*** (A Lógica / O Cérebro): Este arquivo é o "COMO".<br> 
Ele define como aquele formulário deve se comportar e quais são as suas regras.<br>
Ele não tem aparência. É puro código Python que diz:<br>
"O campo 'e-mail' é obrigatório."<br>
"O campo 'e-mail' deve ser um endereço de e-mail válido."<br>
"O campo 'senha' também é obrigatório."<br>
"O campo 'Lembre-se de mim' é uma caixa de seleção (checkbox)."<br>
"Quando o formulário for enviado, valide se todas essas regras foram cumpridas."<br>
"Proteja o formulário contra ataques do tipo CSRF (Cross-Site Request Forgery)."<br>

>> ***Como Eles Trabalham Juntos?***<br>
Na sua rota em ***routes.py***, você cria uma instância do formulário definido em ***forms.py***.<br>
Você "envia" essa instância para o seu template ***login.html***.<br>
No ***login.html***, em vez de escrever ***input type="text"*** manualmente, você usa um código especial (do Flask) que diz:<br>
 {{ form.email.label }} {{ form.email() }}. <br>
 O Flask, então, olha para a definição do campo email em ***forms.py*** e gera o HTML correto, já com todas as validações e atributos de segurança embutidos.<br>
Quando o usuário preenche e envia, os dados voltam para a rota em ***routes.py***.<br>
Lá, você usa o mesmo objeto do formulário para validar os dados recebidos com um simples ***form.validate_on_submit()***.
### Criar o Formulário de Login (app/forms.py)<br>
Neste arquivo, vamos definir, em ***Python***, quais campos nosso formulário de login terá e quais as regras de validação para cada um deles.<br>
Usaremos a biblioteca ***Flask-WTF*** que já instalamos.
```
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    """
    Formulário de login para os usuários.
    """
    email = StringField('E-mail', 
                        validators=[DataRequired(message="Este campo é obrigatório."), 
                                    Email(message="Por favor, insira um e-mail válido.")])
    
    password = PasswordField('Senha', 
                             validators=[DataRequired(message="Este campo é obrigatório.")])
    
    remember_me = BooleanField('Lembrar de mim')
    
    submit = SubmitField('Entrar')
```
#### Entendendo o Código<br>
* ***from flask_wtf import FlaskForm***: Importa a classe base para todos os nossos formulários.<br> 
Ela já vem com a proteção CSRF embutida.<br>
* ***from wtforms import ...***: Importamos os tipos de campos que nosso formulário usará:<br>
* ***StringField***: Um campo de texto normal (para o e-mail).<br>
* ***PasswordField***: Um campo de texto que esconde o que está sendo digitado (para a senha).<br>
* ***BooleanField***: Uma caixa de seleção (checkbox).<br>
* ***SubmitField***: O botão de envio do formulário.<br>
* ***from wtforms.validators import ...***: Importamos as "regras" que vamos aplicar aos campos:<br>
* ***DataRequired***: Garante que o campo não pode ser enviado em branco.<br>
* ***Email***: Verifica se o texto inserido tem o formato de um e-mail válido.<br>
* ***class LoginForm(FlaskForm):***: Criamos nossa classe de formulário, que herda de ***FlaskForm***.<br>
* ***email = StringField(...)***: Criamos o campo email.<br>
* ***'E-mail'***: É o "label" ou rótulo do campo, o texto que aparecerá para o usuário.<br>
* ***validators=[...]***: É a lista de regras que se aplicam a este campo.<br> 
Personalizamos as mensagens de erro para ficarem em português.<br>
* ***password = PasswordField(...)***: O campo de senha, também obrigatório.<br>
* ***remember_me = BooleanField(...)***: O campo "Lembrar de mim", que é opcional.<br>
* ***submit = SubmitField('Entrar')***: O botão que o usuário clicará para fazer o login.<br>
Com isso, a "inteligência" do nosso formulário está pronta.<br> 
O sistema já sabe quais campos existem, quais são obrigatórios e como validá-los.
### Criar a Página de Login (app/templates/login.html)<br>
Este arquivo usará a estrutura do formulário que criamos em Python para renderizar os campos de E-mail, Senha e o botão de Entrar.

---
## <span style="color: yellow;">2. Segunda parte (Criação de: routes.py, layout.html, base.html) 
### Análise da Estratégia<br>
A abordagem adotada foi criar uma hierarquia de templates de três níveis:<br>
1. ***layout.html***: Um template "avô", super básico.<br>
Ele contém apenas a estrutura HTML fundamental (***html***, ***head***, ***body***) e os links para os arquivos CSS e JavaScript (como o Bootstrap), que são comuns a todas as páginas do site, incluindo a de login.<br>
2. ***base.html***: Um template "pai" que herda de layout.html.<br> 
Ele adiciona os elementos visuais que são compartilhados apenas pela área interna/logada da aplicação, como a barra de navegação principal (Navbar) e a estrutura de container do conteúdo.<br>
3. Templates de Página (***login.html***, ***index.html***): Os templates "filhos" que representam as páginas finais.<br> 
A página ***login.html*** herda diretamente do ***layout.html*** para ter um visual limpo e sem menus.<br> 
A página ***index.html*** (e futuras páginas internas) herda do ***base.html*** para incluir a Navbar e o layout padrão da aplicação.<br>
Este modelo nos dá total controle sobre a aparência de diferentes seções do nosso site.
## Passo 1: Simplificar o Fluxo de Login (Backend)<br>
Primeiro, criamos o ***routes.py*** para que, após um login bem-sucedido, o usuário seja redirecionado diretamente para a página inicial, sem a exibição de uma mensagem "flash".<br> 
A mensagem de erro em caso de falha no login, foi mantida apenas para a página de ***login.html***.
```
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    # A variável 'current_user' é fornecida pelo Flask-Login e já está disponível
    # em todas as rotas e templates. Não precisamos passá-la explicitamente,
    # mas vamos deixar o código mais claro para o aprendizado.
    # O template pode acessar 'current_user' diretamente.
    #Uma das belezas do Flask-Login é que ele automaticamente disponibiliza a variável current_user para todos os templates Jinja2. 
    # Portanto, não precisamos passá-la explicitamente no render_template. 
    # O código acima já está correto. Apenas sabendo que current_user existe, já podemos usá-la no HTML.
    return render_template('index.html', title='Página Inicial')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            # A mensagem flash de sucesso foi REMOVIDA daqui.
            return redirect(url_for('index'))
        else:
            # A mensagem de erro permanece, pois ela é exibida na própria página de login.
            flash('Falha no login. Verifique seu e-mail e senha.', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    # A mensagem flash de logout foi REMOVIDA daqui.
    return redirect(url_for('login'))
```
## Passo 2: Implementar a Hierarquia de Layouts (Frontend)
A) O Layout "Avô"
Criamos o arquivo ***layout.html*** para ser a base de tudo, contendo as definições de head e body e os links para os assets.<br>
app/templates/layout.html
```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Gerenciador de Devoluções{% endblock %}</title>
    
    <!-- CSS do Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <!-- Nosso CSS customizado (vem depois para poder sobrescrever estilos ) -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

</head>
<body>
    {% block body_content %}{% endblock %}

    <!-- JavaScript do Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
```
B ) O Layout "Pai" da Área Logada
O arquivo ***base.html*** foi modificado para herdar de ***layout.html*** e para conter a barra de navegação (Navbar) e a estrutura principal da área interna.<br>
app/templates/base.html
```
{% extends "layout.html" %}

{% block body_content %}
    <!-- Barra de Navegação Principal -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('index') }}">Gerenciador de Devoluções</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavDropdown">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('index') }}">Home</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Devolução</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Adicionar</a></li>
                            <li><a class="dropdown-item" href="#">Editar</a></li>
                        </ul>
                    </li>
                    {% if current_user.role == 'admin' %}
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Gerenciamento</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Usuários</a></li>
                        </ul>
                    </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('logout') }}">Sair</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Conteúdo Principal da Página -->
    <main class="container mt-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        {% block main_content %}{% endblock %}
    </main>
{% endblock %}
```
C) O Template da Página de Login
O login.html agora herda diretamente de layout.html, garantindo que ele não tenha a Navbar, e possui sua própria estrutura de container para centralizar o formulário.<br>
app/templates/login.html
```
{% extends "layout.html" %}

{% block title %}Login - Gerenciador de Devoluções{% endblock %}

{% block body_content %}
    <div class="login-container">
        <h2>Login de Acesso</h2>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" action="">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.email.label }}
                {{ form.email(class="form-control") }}
                {% for error in form.email.errors %}
                    <span class="error-message">[{{ error }}]</span>
                {% endfor %}
            </div>
            <div class="form-group">
                {{ form.password.label }}
                {{ form.password(class="form-control") }}
                {% for error in form.password.errors %}
                    <span class="error-message">[{{ error }}]</span>
                {% endfor %}
            </div>
            <div class="form-group remember-me">
                {{ form.remember_me() }}
                {{ form.remember_me.label }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary w-100") }}
            </div>
        </form>
    </div>
{% endblock %}
```

D) Estilos CSS Adicionais

Para dar suporte ao novo layout da página de login, adicionamos estilos específicos ao nosso arquivo CSS.<br>
app/static/css/style.css
```
body { 
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    margin: 0;
    background-color: #f8f9fa;
}

header {
    background-color: #343a40;
    color: white;
    padding: 1rem 2rem;
}

header h1 {
    margin: 0;
}

main {
    padding: 2rem;
}

/* Estilos para as mensagens flash */
.alert { 
    padding: 1em; 
    margin-bottom: 1em; 
    border: 1px solid transparent; 
    border-radius: .25rem; 
}
.alert-danger { 
    color: #721c24; 
    background-color: #f8d7da; 
    border-color: #f5c6cb; 
}
.alert-success { 
    color: #155724; 
    background-color: #d4edda; 
    border-color: #c3e6cb; 
}
.alert-info { 
    color: #0c5460; 
    background-color: #d1ecf1; 
    border-color: #bee5eb; 
}

/* Estilos para os formulários */
.form-group { 
    margin-bottom: 1rem; 
}

.form-group label {
    display: block;
    margin-bottom: .5rem;
}

.form-control { 
    display: block; 
    width: 100%;
    max-width: 400px; /* Limita a largura para melhor leitura */
    padding: .375rem .75rem; 
    font-size: 1rem; 
    line-height: 1.5; 
    border: 1px solid #ced4da; 
    border-radius: .25rem; 
}

.btn { 
    display: inline-block; 
    font-weight: 400; 
    text-align: center; 
    padding: .5rem 1rem; 
    font-size: 1rem; 
    line-height: 1.5; 
    border-radius: .25rem; 
    cursor: pointer;
    border: 1px solid transparent;
    text-decoration: none;
}

.btn-primary { 
    color: #fff; 
    background-color: #007bff; 
    border-color: #007bff; 
}

/* Estilos para o container de login */
.login-container {
    width: 100%;
    max-width: 400px;
    margin: 5rem auto; /* Centraliza vertical e horizontalmente */
    padding: 2rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #fff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.login-container h2 {
    text-align: center;
    margin-bottom: 1.5rem;
}

.error-message {
    color: #dc3545; /* Um vermelho mais padrão */
    font-size: 0.875em;
}

.remember-me {
    display: flex;
    align-items: center;
}

.remember-me label {
    margin-bottom: 0;
    margin-left: 0.5rem;
}
```
---
## <span style="color: yellow;">3. Terceira parte (routes.py, base.html, admin_users.html)
Alteração em ***routes.py*** adicionando nova rota para, ao clicar no menu "Configurações > Usuários",<br>
carregue a página "admin_users.html"<br>
### Passo 1: Criar a Rota e a Lógica de Acesso
Primeiro, criamos a rota em ***routes.py***.<br>
Esta rota precisa ser protegida para que apenas administradores possam acessá-la e deve buscar todos os usuários no banco de dados para passá-los a um template: ***admin_users.html***<br>
***app/routes.py***
```
# ... (outras importações no topo)
from functools import wraps

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

```
### Passo 2: Criar o Link no Menu de Navegação
Tornamos o link "Usuários" no menu funcional, apontando para a nova rota.<br>
***app/templates/base.html*** (Linha alterada)
```
<!-- O código original era: -->
<!-- <li><a class="dropdown-item" href="#">Usuários</a></li> -->

<!-- O código foi alterado para: -->
<li><a class="dropdown-item" href="{{ url_for('admin_users') }}">Usuários</a></li>
```
### Passo 3: Criar o Template da Página de Listagem
Criamos a página HTML que exibe a tabela de usuários.<br>
***app/templates/admin_users.html*** (Novo Arquivo)
```
{% extends "base.html" %}

{% block main_content %}
    <h1>{{ title }}</h1>
    <p>Aqui você pode visualizar todos os usuários cadastrados no sistema.</p>

    <table class="table table-hover mt-4">
        <thead class="table-dark">
            <tr>
                <th scope="col">ID</th>
                <th scope="col">Nome</th>
                <th scope="col">E-mail</th>
                <th scope="col">Permissão (Role)</th>
                <th scope="col">Status</th>
                <th scope="col">Ações</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <th scope="row">{{ user.id }}</th>
                <td>{{ user.name }}</td>
                <td>{{ user.email }}</td>
                <td>
                    <span class="badge 
                        {% if user.role == 'admin' %}bg-danger
                        {% elif 'add' in user.role %}bg-success
                        {% elif 'edit' in user.role %}bg-warning text-dark
                        {% else %}bg-secondary
                        {% endif %}">
                        {{ user.role }}
                    </span>
                </td>
                <td>
                    {% if user.is_active %}
                        <span class="badge bg-success">Ativo</span>
                    {% else %}
                        <span class="badge bg-secondary">Inativo</span>
                    {% endif %}
                </td>
                <td>
                    <a href="#" class="btn btn-sm btn-primary">Editar</a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```
###Resumo:###
Arquivos que criamos/modificamos:<br>
* ***app/routes.py*** (adicionamos o decorator admin_required e a rota admin_users)
* ***app/templates/base.html*** (atualizamos o link do menu)
* ***app/templates/admin_users.html*** (criamos o novo template da página)
### Atualizar GitHub ###
Comandos via terminal:<br>
```
git add .
git commit -m "Feat: Adiciona pagina de listagem de usuarios para admin"
git push origin main
```
---
## <span style="color: yellow;">4. Quarta parte (edit_users.html)
Criar página para Edição de usuários.<br>
Para criar a página de edição de usuário, vamos seguir um padrão muito parecido com o que fizemos para a página de login.<br>
O fluxo será:<br>
* O admin clica no botão "Editar" de um usuário específico (ex: usuário com ID 5).
* O navegador o leva para uma URL como /admin/user/5/edit.
* O Flask carrega os dados do usuário 5 do banco.
* O Flask renderiza um formulário pré-preenchido com os dados desse usuário.
* O admin altera os dados e clica em "Salvar".
* O Flask valida os dados, atualiza o usuário no banco e redireciona o admin de volta para a lista de usuários com uma mensagem de sucesso.<br>
Para fazer tudo isso acontecer, vamos precisar mexer nos seguintes arquivos:<br>

| Arquivo | Ação | Popósito |
|---|:---:|---:|
| app/forms.py | Criar (nova classe) | Definiremos uma nova classe, EditUserForm, <br> que conterá os campos do formulário de edição (Nome, E-mail, Role, Status). |
| app/routes.py | Criar (nova rota) | Criaremos a rota /admin/user/<int:user_id>/edit <br> que vai lidar com a lógica de carregar, exibir e salvar o usuário. |
| app/templates/edit_user.html | Criar (novo arquivo) | Este será o novo arquivo HTML que conterá o formulário de edição, herdando do nosso base.html. |
| app/templates/admin_users.html | Alterar | Vamos modificar o link do botão "Editar" para que ele aponte para a URL correta, passando o ID do usuário. |

### Passo 1: Criar o Formulário de Edição (EditUserForm)
Este formulário definirá os campos que o administrador poderá editar.<br> 
Será um pouco diferente do LoginForm, pois teremos mais campos e um campo de "seleção" (dropdown) para o role.<br>
Abra o arquivo app/forms.py e adicione a nova classe no final do arquivo.<br>
***app/forms.py*** (Adicionar no final)
```
# ... (importações no topo, como StringField, PasswordField, etc.)
# Adicione a importação do SelectField
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models import User # Precisamos do modelo User para validar o e-mail

# ... (classe LoginForm existente) ...


# --- NOVO FORMULÁRIO DE EDIÇÃO DE USUÁRIO ---
class EditUserForm(object):
    """
    Formulário para um administrador editar os dados de um usuário.
    """
    name = StringField('Nome Completo', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    role = SelectField('Permissão (Role)', choices=[
        ('admin', 'Administrador'),
        ('sac1_sac2_add_edit', 'SAC 1 & 2 (Add/Edit)'),
        ('sac1_edit', 'SAC 1 (Edit)'),
        ('sac2_edit', 'SAC 2 (Edit)'),
        ('fat_edit', 'Faturamento (Edit)'),
        ('viewer', 'Visualizador')
    ], validators=[DataRequired()])
    is_active = SelectField('Status', choices=[
        (True, 'Ativo'),
        (False, 'Inativo')
    ], coerce=bool, validators=[DataRequired()]) # coerce=bool é importante para converter o valor
    
    submit = SubmitField('Salvar Alterações')

    def __init__(self, original_email, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.original_email = original_email

    def validate_email(self, email):
        """
        Valida se o novo e-mail já não está em uso por OUTRO usuário.
        """
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Este e-mail já está em uso por outro usuário.')
```
Agora que temos o ***EditUserForm*** (***forms.py***) definido e salvo no Git, vamos usá-lo para construir a rota que vai orquestrar toda a lógica de edição.<br>
Este é o passo mais complexo, pois a mesma função/rota terá duas responsabilidades:<br>
Quando acessada via ***GET***: Carregar o usuário do banco, preencher o formulário com seus dados atuais e exibir a página.<br>
Quando acessada via ***POST*** (após o admin clicar em "Salvar"): Validar os dados enviados, atualizar o usuário no banco e redirecionar.<br>
### Passo 2: Criar a Rota edit_user
Abra o arquivo ***app/routes.py*** e adicione o seguinte bloco de código no final.<br>
***app/routes.py*** (Adicionar no final)
```
# ... (importações no topo)
# Adicione a importação do novo formulário
from app.forms import LoginForm, EditUserForm

# ... (outras rotas como login, logout, admin_users, etc.) ...


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
```
### Passo 3: Criar o Template edit_user.html
Crie um novo arquivo chamado ***edit_user.html*** dentro da pasta app/templates/.<br>
***app/templates/edit_users.html*** (Novo Arquivo)
#### Passo 4: Ajustar o Link do Botão "Editar"
Precisamos ir à nossa página de listagem de usuários e fazer com que o botão "Editar" de cada linha aponte para a URL correta, passando o ID daquele usuário específico.<br>
Abra o arquivo ***app/templates/admin_users.html*** e encontre a linha do botão ***"Editar"***.<br>
***app/templates/admin_users.html*** (Linha para alterar)
```
<!-- Encontre esta linha -->
<a href="#" class="btn btn-sm btn-primary">Editar</a>

<!-- E altere para esta -->
<a href="{{ url_for('edit_user', user_id=user.id) }}" class="btn btn-sm btn-primary">Editar</a>

```
## <span style="color: yellow;">5. Quinta parte (add_user.html - Adicionar Usuário)
O fluxo para ***"Adicionar Usuário"*** será muito, muito parecido com o de "Editar Usuário". <br>
A principal diferença é que começaremos com um formulário em branco em vez de um pré-preenchido.

| Arquivo | Ação | Popósito |
|---|:---:|---:|
| app/forms.py | Criar (nova classe) | Criaremos um AddUserForm, que será quase idêntico ao EditUserForm, <br> mas com uma validação de e-mail mais simples (apenas verifica se já existe) e um campo de senha. |
| app/routes.py | Criar (nova rota) | Criaremos a rota /admin/user/add <br> que exibirá o formulário em branco e processará a criação do novo usuário. |
| app/templates/add_user.html | Criar (novo arquivo) | Este será o template HTML para a página de adição. <br> Ele será praticamente uma cópia do edit_user.html. |
| app/templates/base.html | Alterar | Modificaremos o menu "Gerenciamento" para refletir sua sugestão: <br> um link para "Editar Usuário" e um novo link para "Adicionar Usuário". |

### Passo 1: Criar o Formulário de Adição (AddUserForm)
Este formulário precisa de todos os campos do EditUserForm, mais um campo para a senha.<br>
Abra o arquivo ***app/forms.py*** e adicione esta nova classe no final.<br>
***app/forms.py*** (Adicionar no final)
```
# --- NOVO FORMULÁRIO DE ADIÇÃO DE USUÁRIO ---
class AddUserForm(FlaskForm):
    """
    Formulário para um administrador adicionar um novo usuário ao sistema.
    """
    name = StringField('Nome Completo', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=8)])
    role = SelectField('Permissão (Role)', choices=[
        ('admin', 'Administrador'),
        ('sac1_sac2_add_edit', 'SAC 1 & 2 (Add/Edit)'),
        ('sac1_edit', 'SAC 1 (Edit)'),
        ('sac2_edit', 'SAC 2 (Edit)'),
        ('fat_edit', 'Faturamento (Edit)'),
        ('viewer', 'Visualizador')
    ], validators=[DataRequired()])
    is_active = SelectField('Status', choices=[
        (True, 'Ativo'),
        (False, 'Inativo')
    ], coerce=bool, validators=[DataRequired()])
    
    submit = SubmitField('Adicionar Usuário')

    def validate_email(self, email):
        """
        Valida se o e-mail fornecido já não está em uso.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este e-mail já está cadastrado. Por favor, utilize outro.')
```
### Passo 2: Criar nova rota add_user
Abra o arquivo ***app/routes.py*** e adicione o seguinte bloco de código no final.<br>
***app/routes.py*** (Adicionar no final do arquivo)
```
# --- NOVA ROTA DE ADIÇÃO DE USUÁRIO ---
@app.route('/admin/user/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_user():
    # Instancia o formulário de adição
    form = AddUserForm()

    # --- LÓGICA PARA QUANDO O FORMULÁRIO É ENVIADO (MÉTODO POST) ---
    if form.validate_on_submit():
        # Cria uma nova instância do objeto User com os dados do formulário
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            role=form.role.data,
            is_active=form.is_active.data
        )
        # Usa o nosso método set_password para gerar o hash da senha
        new_user.set_password(form.password.data)
        
        # Adiciona o novo usuário à sessão do banco de dados
        db.session.add(new_user)
        # "Comita" a sessão para salvar o novo usuário permanentemente
        db.session.commit()
        
        # Exibe uma mensagem de sucesso
        flash(f'Usuário "{form.name.data}" criado com sucesso!', 'success')
        
        # Redireciona para a página de listagem de usuários
        return redirect(url_for('admin_users'))

    # --- LÓGICA PARA QUANDO A PÁGINA É CARREGADA (MÉTODO GET) ---
    # Apenas renderiza o template com o formulário em branco
    return render_template('add_user.html', title='Adicionar Novo Usuário', form=form)
```
### Passo 3: Criar o Template add_user.html
Crie um novo arquivo chamado ***add_user.html*** dentro da sua pasta ***app/templates/***.
***app/templates/add_user.html*** (Novo Arquivo)
```
{% extends "base.html" %}

{% block main_content %}
    <h1>{{ title }}</h1>
    <hr>

    <!-- O 'novalidate' desativa a validação padrão do navegador, 
         permitindo que nossas validações do Flask (WTForms) funcionem. -->
    <form method="POST" action="" novalidate>
        
        <!-- Campo oculto de proteção CSRF. Essencial para segurança. -->
        {{ form.hidden_tag() }}

        <div class="mb-3">
            {{ form.name.label(class="form-label") }}
            {{ form.name(class="form-control") }}
            {% for error in form.name.errors %}
                <div class="invalid-feedback d-block">{{ error }}</div>
            {% endfor %}
        </div>

        <div class="mb-3">
            {{ form.email.label(class="form-label") }}
            {{ form.email(class="form-control") }}
            {% for error in form.email.errors %}
                <div class="invalid-feedback d-block">{{ error }}</div>
            {% endfor %}
        </div>

        <!-- CAMPO DE SENHA (A principal diferença em relação à edição) -->
        <div class="mb-3">
            {{ form.password.label(class="form-label") }}
            {{ form.password(class="form-control") }}
            {% for error in form.password.errors %}
                <div class="invalid-feedback d-block">{{ error }}</div>
            {% endfor %}
        </div>

        <div class="mb-3">
            {{ form.role.label(class="form-label") }}
            {{ form.role(class="form-select") }}
            {% for error in form.role.errors %}
                <div class="invalid-feedback d-block">{{ error }}</div>
            {% endfor %}
        </div>

        <div class="mb-3">
            {{ form.is_active.label(class="form-label") }}
            {{ form.is_active(class="form-select") }}
            {% for error in form.is_active.errors %}
                <div class="invalid-feedback d-block">{{ error }}</div>
            {% endfor %}
        </div>

        <hr>

        <div class="mb-3">
            {{ form.submit(class="btn btn-success") }} <!-- Botão verde para 'Adicionar' -->
            <a href="{{ url_for('admin_users') }}" class="btn btn-secondary">Cancelar</a>
        </div>

    </form>
{% endblock %}
```
#### Análise das Diferenças (em relação ao edit_user.html):
***Campo de Senha***: A mudança mais óbvia e importante é a adição do bloco para renderizar o campo ***form.password***.<br>
***Botão de Envio***: Mudei a classe do botão de btn-primary para btn-success ({{ form.submit(class="btn btn-success") }}).<br>
É uma convenção de UX (User Experience) comum usar a cor verde para ações de "criação" ou "sucesso".<br>
***Título e Texto***: O título \<h1>\{{ title }}\</h1> será "Adicionar Novo Usuário", conforme definimos na rota.
### Passo 4: Ajustar o menu de navegação no arquivo: ***base.html***<br>
Vamos modificar o nosso template principal, ***base.html***, para que o menu "Gerenciamento" tenha os links corretos para as páginas de "Editar" (que é a nossa lista de usuários) e "Adicionar".<br>
Abra o arquivo ***app/templates/base.html***.<br>
Encontre o trecho de código do menu dropdown "Gerenciamento".<br>
Ele deve estar parecido com isto:
***app/templates/base.html*** (Trecho para encontrar)
```
<li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        Gerenciamento
    </a>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="{{ url_for('admin_users') }}">Usuários</a></li>
    </ul>
</li>
```
***Agora, vamos substituir o trecho de código acima, pelo novo código (menu):***
```
<li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        Gerenciamento
    </a>
    <ul class="dropdown-menu">
        <!-- Link para a página de ADICIONAR um novo usuário -->
        <li><a class="dropdown-item" href="{{ url_for('add_user') }}">Adicionar Usuário</a></li>
        
        <!-- Link para a página de LISTAR/EDITAR usuários existentes -->
        <li><a class="dropdown-item" href="{{ url_for('admin_users') }}">Editar Usuários</a></li>
    </ul>
</li>
```
***Análise da Mudança:***
* **href="{{ url_for('add_user') }}": ** O primeiro item do menu agora aponta para a nossa nova rota add_user, que exibe o formulário em branco.<br>
* **href="{{ url_for('admin_users') }}": ** O segundo item aponta para a rota admin_users, que é a nossa página de listagem, de onde podemos iniciar a edição.<br>
* Texto dos Links: Alteramos o texto para "Adicionar Usuário" e "Editar Usuários", que são ações muito mais explícitas e claras para o administrador.