from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#Inicializar bootstrap
bootstrap = Bootstrap(app)

#key session
app.config['SECRET_KEY'] = 'SUPER SECRETO'

#Clase formulario
class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a producción']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    #raise(Exception('500 error')) # provocar un error 500
    user_ip = request.remote_addr
    
    #Redireccionar
    response = make_response(redirect('/hello'))
    #agregar cookie al response
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET','POST'])
def hello():
    #tomar cookie del response
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    #diccionario
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username':username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        #flash
        flash('Nombre de usuario registrado con exito')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)

