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

    def carregar_catalogo_csv(self, arquivo="src/data/album_copa2026.csv"):
        if not os.path.exists(arquivo):
            return False, f"[AVISO] Arquivo {arquivo} não encontrado. Buscas textuais não funcionarão."
            
        with open(arquivo, mode="r", encoding="utf-8") as f:
            leitor = csv.DictReader(f, delimiter=";")
            for linha in leitor:
                try:
                    id_fig = int(linha["id"])
                    self.catalogo_oficial[id_fig] = Figurinha(id_fig, linha["nome"], linha["pais"])
                except ValueError:
                    continue
        return True, "Catálogo carregado com sucesso."
    
    def buscar_sugestoes(self, termo):
        termo = termo.lower().strip()
        sugestoes = []
        for fig in self.catalogo_oficial.values():
            if termo in fig.nome.lower() or termo in fig.pais.lower():
                sugestoes.append(fig)
                if len(sugestoes) >= 15:
                    break
        return sugestoes
    
    def inserir_pacotinho(self, id_fig):
        try:
            id_fig = int(id_fig)
            if id_fig not in self.catalogo_oficial:
                return False, f"[ERRO] ID #{id_fig} não existe no catálogo oficial da Copa."

            fig_matriz = self.catalogo_oficial[id_fig]
            nova_fig = Figurinha(fig_matriz.id, fig_matriz.nome, fig_matriz.pais)
            
            if self.album.buscar_por_id(id_fig) is not None:
                self.repetidas.adicionar(nova_fig)
                return True, f"✓ REPETIDA: {nova_fig.nome} foi para o seu monte de trocas!"
            else:
                self.album.adicionar(nova_fig)
                return True, f"★ NOVA: {nova_fig.nome} colada no álbum com sucesso!"
                
        except ValueError:
            return False, "[ERRO] ID inválido."
        
    def realizar_troca_manual(self, id_oferecida, id_desejada):
        fig_oferecida = self.repetidas.buscar_por_id(id_oferecida)
        if not fig_oferecida:
            return False, f"✕ Erro: Você não possui a figurinha #{id_oferecida} nas repetidas."
            
        if id_desejada not in self.catalogo_oficial:
            return False, f"✕ Erro: A figurinha #{id_desejada} não existe no catálogo oficial."
            
        self.repetidas.remover(id_oferecida)
        fig_cat = self.catalogo_oficial[id_desejada]
        nova_fig = Figurinha(fig_cat.id, fig_cat.nome, fig_cat.pais)
        
        if self.album.buscar_por_id(id_desejada):
            self.repetidas.adicionar(nova_fig)
            msg_destino = "foi para suas repetidas"
        else:
            self.album.adicionar(nova_fig)
            msg_destino = "foi colada no álbum"
            
        registro = f"MANUAL: Deu #{id_oferecida} ({fig_oferecida.nome}) por #{id_desejada} ({nova_fig.nome})."
        self.historico.enqueue(registro)
        
        return True, f"✓ Sucesso! Você deu {fig_oferecida.nome} e recebeu {nova_fig.nome} ({msg_destino})."
    
    def realizar_troca_automatica(self):
        if self.repetidas.tamanho == 0:
            return False, "✕ Você não possui figurinhas repetidas."

        total_repetidas = 0
        atual = self.repetidas.cabeca
        while atual is not None:
            total_repetidas += atual.figurinha.quantidade
            atual = atual.proximo

        fila_faltantes = Fila()
        for id_cat in range(1, self.total_figurinhas + 1):
            if id_cat in self.catalogo_oficial and not self.album.buscar_por_id(id_cat):
                fila_faltantes.enqueue(id_cat)
                if fila_faltantes.tamanho == total_repetidas:
                    break

        if fila_faltantes.tamanho == 0:
            return False, "★ Seu álbum já está 100% completo!"

        relatorio_removidas = ""
        qtd_trocada = fila_faltantes.tamanho
        
        for _ in range(qtd_trocada):
            if self.repetidas.cabeca is not None:
                id_topo = self.repetidas.cabeca.figurinha.id
                fig_removida = self.repetidas.remover(id_topo)
                
                if relatorio_removidas != "":
                    relatorio_removidas += "\n    "
                relatorio_removidas += f"[-] Saiu: [#{fig_removida.id:03d}] {fig_removida.nome}"

        relatorio_adicionadas = ""
        atual_faltante = fila_faltantes.inicio
        
        while atual_faltante is not None:
            fig_cat = self.catalogo_oficial[atual_faltante.dado]
            nova_fig = Figurinha(fig_cat.id, fig_cat.nome, fig_cat.pais)
            self.album.adicionar(nova_fig)
            
            if relatorio_adicionadas != "":
                relatorio_adicionadas += "\n    "
            relatorio_adicionadas += f"[+] Entrou: [#{nova_fig.id:03d}] {nova_fig.nome}"
            
            atual_faltante = atual_faltante.proximo

        self.historico.enqueue(f"AUTO: Trocou {qtd_trocada} repetidas por inéditas.")
        mensagem_final = (
            f"✓ TROCA AUTOMÁTICA CONCLUÍDA ({qtd_trocada} figurinhas)!\n\n"
            f"  RESUMO DAS SAÍDAS:\n    {relatorio_removidas}\n\n"
            f"  RESUMO DAS ENTRADAS:\n    {relatorio_adicionadas}"
        )
        return True, mensagem_final
