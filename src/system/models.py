class Figurinha:
    def __init__(self, id_fig, nome, pais):
        self.id = int(id_fig)
        self.nome = nome.strip()
        self.pais = pais.strip()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais
        }

    def __str__(self):
        return f"[#{self.id:03d}] {self.nome} ({self.pais})"

class NodoLista:
    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None

class NodoFila:
    def __init__(self, dado):
        self.dado = dado 
        self.proximo = None
