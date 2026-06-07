import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\n[Pressione ENTER para continuar...]")