from flask import Flask,render_template

app = Flask(__name__)

#renderiza form e permite o cadastro
@app.route('/', methods=['GET','POST'])
def index():
    return render_template("base.html")


#recebe a url,procura na base e encaminha
#tratar os erros caso a url não existir
@app.route('/<url>')
def encaminhar(url):
    return f"A url digitada foi {url}"