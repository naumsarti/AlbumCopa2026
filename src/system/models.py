class Figurinha:
    def __init__(self, id_fig, nome, pais, quantidade=1):
        self.id = int(id_fig)
        self.nome = nome.strip()
        self.pais = pais.strip()
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "quantidade": self.quantidade
        }

    def __str__(self):
        prefixo = f"{self.quantidade}x " if self.quantidade > 1 else ""
        return f"{prefixo}[#{self.id:03d}] {self.nome} ({self.pais})"

class NodoLista:
    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None

class NodoFila:
    def __init__(self, dado):
        self.dado = dado 
        self.proximo = None
