from flask import Flask, request, make_response, redirect


app = Flask(__name__)

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
    return f'Hello flask tu ip es  {user_ip}'