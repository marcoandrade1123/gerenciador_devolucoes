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


