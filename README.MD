## ENCURTADOR DE URL

encurtador de URL feito em flask para fins didáticos

## Virtualenv
O sistema está usando o virtualenv para gerenciar pacotes e isolar ambientes [virtualenv](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)

## Para executar esse programa em computador local

### 1 Inicialize uma virtualenv
Na raiz do projeto, devemos instalar e executar a virtualenv

Inicializando a virtualenv em Linux
```
python3 -m venv venv #instala uma virtualenv
source /venv/bin/activate #inicializa a virtualenv
```
Inicializando em Windows - Powershell
```
python -m venv venv
\venv\Scripts\Activate.ps1
```

### 2 Instale as dependências do projeto
Dentro do ambiente da virtualenv, devemos instalar as dependências:
```
pip install -r requirements.txt #instala as dependências
```

### 3 Configure as variáveis de ambiente
windows - powershell
```powershell
$env:FLASK_APP = "./app/app.py"
$env:FLASK_ENV = "development"
```
linux - bash (não testado)
```bash
export FLASK_APP=.\app\app.py
export FLASK_ENV=development
```

### 4 execute o flask
```
flask run
```

### 5 acesse o sistema
Pelo navegador:
[http://127.0.0.1:5000](http://127.0.0.1:5000)