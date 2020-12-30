from flask import request, make_response, redirect, render_template, session, url_for, flash

import unittest
from app import create_app
from app.forms import LoginForm
app = create_app()

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a producción']



@app.cli.command()
def test():
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(test)


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

