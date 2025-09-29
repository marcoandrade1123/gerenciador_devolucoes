from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models import User # Importa o modelo User para validação de e-mail

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

# --- NOVO FORMULÁRIO DE EDIÇÃO DE USUÁRIO ---
class EditUserForm(FlaskForm):
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



