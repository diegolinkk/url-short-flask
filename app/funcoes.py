from random import choice
def gerar_url_curta_aleatoria():
    caracteres = 'abcdefghijklmnopqrstuvwxyz'

    url_curta = ""
    for _ in range(5):
        url_curta += choice(caracteres)
    
    return url_curta