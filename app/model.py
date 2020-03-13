#será feito em classe
from funcoes import gerar_url_curta_aleatoria
import sqlite3

class Site:
    def __init__(self,url_longa="",url_curta = ""):
        self.url_longa = url_longa
        self.url_curta = url_curta
        self.banco_de_dados = './app/banco_de_dados.db'

    def cadastrar(self):
        self.url_curta = gerar_url_curta_aleatoria()
        # agora tendo a url curta e a longa, pode cadastrar ambas
        conn = sqlite3.connect(self.banco_de_dados)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sites (url_longa, url_curta)
        VALUES(?,?)
        """,(self.url_longa,self.url_curta))
        conn.commit()
        conn.close()

    def recuperar_url_longa(self):
            #faz a busca no banco com a url curta
            #retorna sua respectiva url longai
            pass

    def __str__(self):
            return f"Url curta: {self.url_curta}. Url longa {self.url_longa}"

#usado somente se precisar criar a tabela
def criar_tabela():
    s = Site()
    conn = sqlite3.connect(s.banco_de_dados)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE sites (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        url_longa VARCHAR NOT NULL,
        url_curta VARCHAR NOT NULL
    )
    """)
    print("Tabela criada com sucesso")
    conn.close()
