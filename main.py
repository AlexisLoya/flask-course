from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video a producción']

@app.route('/')
def index():
    user_ip = request.remote_addr
    #Redireccionar
    response = make_response(redirect('/hello'))
    #agregar cookie al response
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    #tomar cookie del response
    user_ip = request.cookies.get('user_ip')
    #diccionario
    context = {
    'user_ip': user_ip,
    'todos': todos,
    }
    return render_template('hello.html', **context)

