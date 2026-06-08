from system.engine import SistemaFigurinhas
from system.utils import limpar_terminal, pausar
from system.ui import imprimir_cabecalho, exibir_menu, exibir_album, exibir_historico, solicitar_entrada_inteligente

def main():
    sistema = SistemaFigurinhas()
    
    while True:
        limpar_terminal()
        imprimir_cabecalho("ÁLBUM DE FIGURINHAS DA COPA DE 2026")
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            imprimir_cabecalho("Inserção de Figurinha")
            id_fig = solicitar_entrada_inteligente(sistema, "Digite o ID ou parte do NOME da figurinha: ")
            if id_fig is not None:
                sucesso, msg = sistema.inserir_pacotinho(id_fig)
                print(f"\n{msg}")
            pausar()

            
        elif opcao == "0":
            print("\nEncerrando o sistema.")
            break
            
        else:
            print("\nOpção inválida.")
            pausar()

if __name__ == "__main__":
    main()