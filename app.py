from flask import redirect, session, render_template, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask import Flask, jsonify
from flask import url_for

# https://fontawesome.com/icons
from flask_fontawesome import FontAwesome

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

boostrap = Bootstrap(app)
fa = FontAwesome(app)

nav = Nav()
nav.init_app(app)

@app.route('/')
def inicio():
    return render_template('index.html', title='Inicial')

@app.route("/logout")
def logout():
    '''
    Para encerrar a sessão autenticada de um usuário
    :return: redireciona para a página inicial
    '''
    session.clear()
    return redirect(url_for('inicio'))

@app.errorhandler(404)
def page_not_found(e):
    '''
    Para tratar erros de páginas não encontradas - HTTP 404
    :param e:
    :return:
    '''
    return render_template('404.html'), 404

## Rota para definir qual imagem será exibida

## Rotas que pega a imagem a ser exibidas

@app.route('/route1', methods=['GET', 'POST'])
def imgRoute1():
    imgSrc = ((request.values.get('path')))
    return render_template('page1.html', title='Page 1',form=imgSrc), 200

@app.route('/route2', methods=['GET', 'POST'])
def imgRoute2():
    imgSrc = ((request.values.get('path')))
    return render_template('page2.html', title='Page 2', form=imgSrc), 200

@app.route('/route3', methods=['GET', 'POST'])
def imgRoute3():
    imgSrc = ((request.values.get('path')))
    return render_template('page3.html', title='Page 3', form=imgSrc), 200



if __name__ == '__main__':
    port = 5000
    app.run(debug=True, host="127.0.0.1", port=port)

