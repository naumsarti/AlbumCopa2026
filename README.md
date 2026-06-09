# Projeto Álbum da Copa de 2026

 Este projeto foi desenvolvido como requisito avaliativo para a disciplina de **Estrutura de Dados** da **FATEC Rio Claro**. O objetivo principal é aplicar os conceitos teóricos de estruturas de dados dinâmicas lineares em um cenário prático e divertido: o gerenciamento de um álbum de figurinhas da Copa do Mundo de 2026.

---

## Estrutura do Projeto

```
└── src/
    ├── data/
    │   ├── album_copa2026.csv   # Base de dados oficial imutável com IDs, Nomes e Países
    │   └── dados_copa.json      # Arquivo gerado automaticamente para salvar o progresso
    ├── main.py                  # Ponto de entrada do programa (Loop do Menu Principal)
    └── system/
        ├── __init__.py
        ├── engine.py            # Motor do sistema (Gerencia fluxo de dados e persistência JSON)
        ├── estruturas.py        # Implementação manual das classes Album (Lista Encadeada) e Fila
        ├── models.py            # Modelos das entidades primitivas (Figurinha, NodoLista, NodoFila)
        ├── ui.py                # Camada visual do terminal (Menus, prints e inputs inteligentes)
        └── utils.py             # Funções de suporte
```

---

## Sobre o Projeto

O sistema simula a experiência de colecionar figurinhas, permitindo colar novos cromos, gerenciar itens repetidos, realizar trocas simuladas e acompanhar estatísticas de progresso. 

O grande diferencial técnico deste projeto é que **não foram utilizadas as coleções nativas do Python (como `lists` ou `dicts`)** para gerenciar o armazenamento principal do álbum, das repetidas ou do histórico. Toda a manipulação de dados foi feita por meio de estruturas implementadas manualmente usando ponteiros e nós dinâmicos.

---

## Funcionalidades Principais

* **1. Colar Figurinha:** Adiciona uma nova figurinha ao sistema. Se já estiver no álbum, ela vai automaticamente para a estrutura de repetidas.
* **2. Ver Álbum Completo:** Exibe de forma sequencial e ordenada todas as figurinhas coladas pelo usuário.
* **3. Ver Estatísticas:** Mostra a porcentagem de conclusão do álbum, a quantidade de figurinhas únicas e a contagem física total de repetidas guardadas (somando as quantidades de cada nó).
* **4. Remover das Repetidas:** Permite retirar manualmente uma figurinha do bolo de repetidas.
* **5. Ver Minhas Repetidas:** Lista todas as figurinhas que você possui em duplicidade e as suas respectivas quantidades.
* **6. Propor Troca:** Permite simular a troca de uma figurinha repetida sua por uma nova figurinha que você ainda não possui.
* **7. Histórico de Trocas:** Exibe a fila cronológica de todas as trocas efetuadas com sucesso no sistema.
* **8. Salvar/Carregar Progresso:** Serialização automática de todo o estado do álbum, repetidas e histórico em formato `JSON` para persistência de dados.
* **9. Busca Inteligente (Autocompletar):** O sistema lê um catálogo oficial em `CSV` contendo mais de 900 figurinhas da Copa 2026. Ao digitar o nome de um jogador, o sistema busca e sugere opções correspondentes para facilitar o input.

---

## Como Rodar

### Pré-requisitos:
* **Python 3.x**

### 1. **Clone o Repositório:**
```bash
git clone https://github.com/naumsarti/AlbumCopa2026.git
cd AlbumCopa2026
```
### 2. **Garantir a Estrutura de Dados:**
* Verifique se dentro da pasta do projeto existe o caminho src/data/album_copa2026.csv com a lista oficial de jogadores para que o autocompletar e as buscas por nome funcionem corretamente.
### 3. **Rodar o Sistema**
Execute o arquivo pelo terminal:
```bash
python src/main.py
```

---

## Disciplina e Autor
* **Curso:** Inteligência Artificial
* **Instituição:** FATEC Rio Claro - SP
* **Disciplina:** Estrutura de Dados
* **Autor:** [@naumsarti](https://github.com/naumsarti)