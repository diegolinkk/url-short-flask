## ENCURTADOR DE URL

encurtador de URL feito em flask para fins didáticos

## Gerenciador de pacotes
O sistema está usando o gerenciador de pacotes [poetry](https://python-poetry.org/)

## Para executar esse programa em computador local

### 1 Instale o poetry
Para instalar o poetry, siga as instruções de instalação no site.

### 2 Instale as dependências do projeto
Já com o Poetry instalado, na raiz do projeto, digite:
```
poetry check #verifica se está tudo ok
poetry install #instala as dependências
poetry shell #inicia a virtual env do projeto
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