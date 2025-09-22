 
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Olá, Mundo! O aplicativo está no ar!</h1>"
