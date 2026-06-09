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
            print(f"Quantidade de Repetidas Guardadas: {sistema.repetidas.total_figurinhas()}")
            pausar()

        elif opcao == "4":
            imprimir_cabecalho("Remover Figurinha Repetida")
            if sistema.repetidas.tamanho == 0:
                print("Você não possui figurinhas repetidas no momento.")
            else:
                exibir_album(sistema.repetidas)
                print("\n" + "="*45)
                entrada = input("\nDigite o ID da figurinha que deseja remover (ou Enter para cancelar): ")
                
                if entrada.isdigit():
                    id_fig = int(entrada)
                    removido = sistema.repetidas.remover(id_fig)
                    if removido:
                        print(f"\n✓ Sucesso: {removido.nome} foi removida da lista de repetidas.")
                    else:
                        print(f"\n✕ Erro: A figurinha com ID #{id_fig} não foi encontrada nas repetidas.")
                else:
                    print("\nOperação cancelada.")
            pausar()

        elif opcao == "5":
            imprimir_cabecalho("Figurinhas Repetidas")
            exibir_album(sistema.repetidas)
            pausar()

        elif opcao == "6":
            imprimir_cabecalho("Central de Trocas")
            print("1. Troca Manual")
            print("2. Troca Automática\n")
            
            tipo_troca = input("Selecione (1 ou 2): ").strip()
            
            if tipo_troca == "1":
                print("\n-- Troca Manual --")
                exibir_album(sistema.repetidas)
                
                entrada = input("\nDigite o ID da sua REPETIDA que deseja oferecer (ou Enter para cancelar): ").strip()
                if entrada.isdigit():
                    id_oferecida = int(entrada)
                    print("\n-- Escolha a figurinha que quer RECEBER --")
                    id_desejada = solicitar_entrada_inteligente(sistema, "\nBuscar por ID ou Nome: ")
                    
                    if id_desejada is not None:
                        sucesso, msg = sistema.realizar_troca_manual(id_oferecida, id_desejada)
                        print(f"\n{msg}")
                else:
                    print("\nOperação cancelada.")

            elif tipo_troca == "2":
                print("\n-- Troca Automática --")
                print("Analisando suas figurinhas repetidas e buscando inéditas no catálogo...\n")
                sucesso, msg = sistema.realizar_troca_automatica()
                print(msg)
                
            else:
                print("\n✕ Opção de troca inválida.")
            pausar()

        elif opcao == "7":
            imprimir_cabecalho("Histórico de Trocas")
            exibir_historico(sistema.historico)
            pausar()

        elif opcao == "8":
            imprimir_cabecalho("Salvando Progresso...")
            sucesso, msg = sistema.salvar_dados()
            print(f"\n{msg}")
            pausar()

        elif opcao == "9":
            imprimir_cabecalho("Carregando Progresso...")
            sucesso, msg = sistema.carregar_dados()
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