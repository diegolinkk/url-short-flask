#será feito em classe
from funcoes import gerar_url_curta_aleatoria

class Site:
    def __init__(self,url_longa="",url_curta = ""):
        self.url_longa = url_longa
        self.url_curta = url_curta
    
    def cadastrar(self):
        self.url_curta = gerar_url_curta_aleatoria()
        #agora tendo a url curta e a longa, pode cadastrar ambas
        #talvez ja retornar daqui o valor da url curta - validar depois
    
    def recuperar_url_longa(self):
        #faz a busca no banco com a url curta
        #retorna sua respectiva url longa
        pass

    def __str__(self):
        return f"Url curta: {self.url_curta}. Url longa {self.url_longa}"
