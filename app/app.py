## coding: utf-8
from flask import Flask,render_template,request,redirect,url_for
from model import Site
app = Flask(__name__)

#renderiza form e permite o cadastro
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        s = Site(url_longa = request.form['url-longa'])
        s.cadastrar()
        return f"""Sua url curta é:
        <a href = {request.url + s.url_curta}>{request.url + s.url_curta} </a>"""

    return render_template("base.html")


#recebe a url,procura na base e encaminha
#tratar os erros caso a url não existir
@app.route('/<url>')
def encaminhar(url):
    s = Site(url_curta=url)
    s.recuperar_url_longa()
    # se não houver url, volta pra raiz
    if s.url_longa == "":
        return redirect(url_for('index'))
    return redirect(f'{s.url_longa}')
