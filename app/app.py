from flask import Flask,render_template,request
from model import Site
app = Flask(__name__)

#renderiza form e permite o cadastro
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return f"Você digitou {request.form['url-longa']} no formulário "
    return render_template("base.html")


#recebe a url,procura na base e encaminha
#tratar os erros caso a url não existir
@app.route('/<url>')
def encaminhar(url):
    return f"A url digitada foi {url}"


site1 = Site()
print(site1)