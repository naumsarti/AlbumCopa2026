from .models import NodoLista, NodoFila

class Album:
    def __init__(self, total_album=994):
        self.cabeca = None     
        self.tamanho = 0       
        self.total_album = total_album 

    def adicionar(self, figurinha):
        novo_nodo = NodoLista(figurinha)
        
        if self.cabeca is None or self.cabeca.figurinha.id > figurinha.id:
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
            self.tamanho += 1
            return True
            
        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.figurinha.id < figurinha.id:
            atual = atual.proximo
            
        if atual.figurinha.id == figurinha.id:
            atual.figurinha.quantidade += 1
            return True
        if atual.proximo and atual.proximo.figurinha.id == figurinha.id:
            atual.proximo.figurinha.quantidade += 1
            return True
            
        novo_nodo.proximo = atual.proximo
        atual.proximo = novo_nodo
        self.tamanho += 1
        return True

    def remover(self, id_fig):
        if self.cabeca is None:
            return None
            
        if self.cabeca.figurinha.id == id_fig:
            if self.cabeca.figurinha.quantidade > 1:
                self.cabeca.figurinha.quantidade -= 1
                return self.cabeca.figurinha
            else:
                removida = self.cabeca.figurinha
                self.cabeca = self.cabeca.proximo
                self.tamanho -= 1
                return removida
        
        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.figurinha.id != id_fig:
            atual = atual.proximo
            
        if atual.proximo is not None:
            if atual.proximo.figurinha.quantidade > 1:
                atual.proximo.figurinha.quantidade -= 1
                return atual.proximo.figurinha
            else:
                removida = atual.proximo.figurinha
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return removida
        return None

    def buscar_por_id(self, id_fig):
        atual = self.cabeca
        while atual is not None:
            if atual.figurinha.id == id_fig:
                return atual.figurinha
            atual = atual.proximo
        return None

    def exibir_album(self):
        atual = self.cabeca
        if not atual:
            print("Álbum vazio.")
            return
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

    def porcentagem_concluida(self):
        return (self.tamanho / self.total_album) * 100

class Fila:
    def __init__(self):
        self.inicio = None 
        self.fim = None    
        self.tamanho = 0

    def enqueue(self, dado):
        novo_nodo = NodoFila(dado)
        if self.fim is None:
            self.inicio = novo_nodo
            self.fim = novo_nodo
        else:
            self.fim.proximo = novo_nodo
            self.fim = novo_nodo
        self.tamanho += 1

    def dequeue(self):
        if self.inicio is None:
            return None
        dado_removido = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return dado_removido

    def exibir_historico(self):
        atual = self.inicio
        if not atual:
            print("Nenhuma troca registrada.")
            return
        while atual is not None:
            print(f"- {atual.dado}")
            atual = atual.proximo