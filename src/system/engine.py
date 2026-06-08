import json, os, csv
from .models import Figurinha
from .estruturas import Album, Fila

class SistemaFigurinhas:
    def __init__(self):
        self.total_figurinhas = 994
        self.album = Album(total_album=self.total_figurinhas)       
        self.repetidas = Album(total_album=self.total_figurinhas)   
        self.historico = Fila()                   
        self.banca_trocas = Album(total_album=self.total_figurinhas) 
        
        self.catalogo_oficial = {} 
        self.carregar_catalogo_csv()

    def carregar_catalogo_csv(self, arquivo="src/data/album_copa2026.csv"):
        if not os.path.exists(arquivo):
            return False, f"[AVISO] Arquivo {arquivo} não encontrado. Buscas textuais não funcionarão."
            
        with open(arquivo, mode="r", encoding="utf-8") as f:
            leitor = csv.DictReader(f, delimiter=";")
            for linha in leitor:
                try:
                    id_fig = int(linha["id"])
                    self.catalogo_oficial[id_fig] = Figurinha(id_fig, linha["nome"], linha["pais"])
                except ValueError:
                    continue
        return True, "Catálogo carregado com sucesso."