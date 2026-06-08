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