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
   
        elif opcao == "2":
            imprimir_cabecalho("Álbum Completo")
            exibir_album(sistema.album)
            pausar()
            
        elif opcao == "3":
            imprimir_cabecalho("Estatísticas do Álbum")
            pct = sistema.album.porcentagem_concluida()
            print(f"Progresso: {pct:.2f}% concluído")
            print(f"Figurinhas Únicas Coladas: {sistema.album.tamanho}/{sistema.total_figurinhas}")
            print(f"Quantidade de Repetidas Guardadas: {sistema.repetidas.tamanho}")
            pausar()
            
            
        elif opcao == "0":
            print("\nEncerrando o sistema.")
            break
            
        else:
            print("\nOpção inválida.")
            pausar()

if __name__ == "__main__":
    main()