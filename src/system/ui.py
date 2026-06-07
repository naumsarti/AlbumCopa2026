def imprimir_cabecalho(titulo):
    print("\n" + "="*45)
    print(f" {titulo.upper()} ")
    print("="*45 + "\n")

def exibir_menu():
    print("="*45)
    print("1. Colar Figurinha")
    print("2. Ver Álbum Completo")
    print("3. Ver Estatísticas")
    print("4. Remover Figurinha das Repetidas")
    print("5. Ver Minhas Repetidas")
    print("6. Propor Troca")
    print("7. Histórico de Trocas")
    print("8. Salvar Progresso (JSON)")
    print("9. Carregar Progresso (JSON)")
    print("0. Sair")
    print("="*45)

def exibir_album(album):
        atual = album.cabeca
        if not atual:
            print("Álbum vazio.")
            return
        while atual is not None:
            print(atual.figurinha)
            atual = atual.proximo

def exibir_historico(fila):
        atual = fila.inicio
        if not atual:
            print("Nenhuma troca registrada.")
            return
        while atual is not None:
            print(f"- {atual.dado}")
            atual = atual.proximo