import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib import colors
import shutil
import os

votacao_ativa = False

candidatos = {
    'Python Silva': {'partido': 'Partido do Código Aberto (PCA)', 'numero': 11, 'voto': 0},
    'CSS Cardoso': {'partido': 'Desenvolvedores Ágeis (DA)', 'numero': 22, 'voto': 0},
    'SQL Ferreira': {'partido': 'Orientados a Objetos (POO)', 'numero': 33, 'voto': 0},
    'HTML Santos': {'partido': 'Marcação para Todos (MT)', 'numero': 44, 'voto': 4},
    'JavaScript Oliveira': {'partido': 'Assíncronos Independentes (AI)', 'numero': 55, 'voto': 0}
}

janela = tk.Tk()
janela.title("Dizer Olá")

# DESING

COR_FUNDO = "#f5f7fa"
COR_BOTAO = "#007ACC"
COR_TEXTO_BOTAO = "#222222"
COR_BOTAO_VOLTAR = "#007ACC"

# fg = fonte color
# bg = background color
# activebackground = cor quando é clicado

estilo_botao_menu = {
    "bg": "#007ACC",
    "fg": "white",
    "activebackground": "#005F99",
    "font": ("Arial", 12, "bold"),
    "width": 36
}
estilo_botao_add = {
    "bg": "#007ACC",
    "fg": "white",
    "activebackground": "#005F99",
    "font": ("Arial", 12, "bold"),
    "width": 36
}
estilo_botao_voto = {
    "bg": "#007ACC",
    "fg": "white",
    "activebackground": "#005F99",
    "font": ("Arial", 12, "bold"),
    "width": 36
}
estilo_botao_encerrar = {
    "bg": "#007ACC",
    "fg": "white",
    "activebackground": "#005F99",
    "font": ("Arial", 12, "bold"),
    "width": 36
}
estilo_label = {
    "bg": COR_FUNDO,
    "fg": "black",
    "font": ("Arial", 18),
    "width": 50
}
estilo_entry = {
    "bg": COR_FUNDO,
    "fg": "black",
    "font": ("Arial", 12),
    "width": 36
}


# FUNÇÕES E CODIGO

def menu():
    janela.geometry("580x360") 
    janela.configure(padx=20, pady=20, bg=COR_FUNDO)
    
    label_menu = tk.Label(janela, text="Escolha uma opção:", **estilo_label)
    label_menu.pack(pady=10) # Espaçamento entre o rótulo e os botões
    
    botao_cadastro = tk.Button(janela, text="Cadastro de Candidato", command=add_candidato, **estilo_botao_menu) 
    botao_cadastro.pack(pady=5) # Espaçamento entre os botões
    
    botao_votacao = tk.Button(janela, text="Iniciar Votação", command=votar, **estilo_botao_menu)
    botao_votacao.pack(pady=5)
    
    botao_encerrar = tk.Button(janela, text="Encerrar Votação", command=imprimir_relatorio, **estilo_botao_menu)
    botao_encerrar.pack(pady=5)

def add_candidato():
    janela_add_candidato = tk.Toplevel(janela)
    janela_add_candidato.title("Cadastro de Candidato")
    janela_add_candidato.geometry("580x360")  
    janela_add_candidato.configure(padx=20, pady=20, bg=COR_FUNDO)
    # NOME CANDIDATO
    tk.Label(janela_add_candidato, text="Nome do Candidato: ", **estilo_label).pack(pady=5)
    entrada_nome = tk.Entry(janela_add_candidato, **estilo_entry)
    entrada_nome.pack(pady=5)
    # NÚMERO DO CANDIDATO
    tk.Label(janela_add_candidato, text="Número do Candidato: ", **estilo_label).pack(pady=5)
    entrada_numero = tk.Entry(janela_add_candidato, **estilo_entry)
    entrada_numero.pack(pady=5)
    # PARTIDO DO CANDIDATO
    tk.Label(janela_add_candidato, text="Partido do Candidato: ", **estilo_label).pack(pady=5)
    entrada_partido = tk.Entry(janela_add_candidato, **estilo_entry)
    entrada_partido.pack(pady=5)
    def confirmar_add_candidato():
        num = int(entrada_numero.get())
        nome = entrada_nome.get()
        partido = entrada_partido.get()
        candidatos.update({nome: {'partido': partido, 'numero': num, 'voto': 0}})
        aviso = messagebox.showinfo('Candidato Adicionado', f'Candidato {nome} de número {num}, do partido {partido}, foi adicionado com sucesso')


    btn_add_candidato = tk.Button(janela_add_candidato, text="Salvar", command=confirmar_add_candidato, **estilo_botao_add)
    btn_add_candidato.pack(pady=5)
    # BOTÃO DE VOLTAR
    btn_voltar = tk.Button(janela_add_candidato, text="voltar", command=janela_add_candidato.destroy, **estilo_botao_add)
    btn_voltar.pack(pady=10)

def votar():
    janela_votacao = tk.Toplevel(janela)
    janela_votacao.title("Votação")
    janela_votacao.geometry("580x360") 
    janela_votacao.configure(padx=20, pady=20, bg=COR_FUNDO)
    tk.Label(janela_votacao, text="Digite sua matrícula:", **estilo_label).pack(pady=5)
    entrada_matricula = tk.Entry(janela_votacao, **estilo_entry)
    entrada_matricula.pack(pady=5)
    tk.Label(janela_votacao, text="Digite o número do candidato:", **estilo_label).pack(pady=5)
    entrada_voto = tk.Entry(janela_votacao, **estilo_entry)
    entrada_voto.pack(pady=5)
    def confirmar_voto():
        candidato_encontrado = False
        matricula = entrada_matricula.get()
        voto = int(entrada_voto.get())
        if matricula:
            for nome, dados in candidatos.items():
                if dados['numero'] == voto:
                    confirmacao = messagebox.askyesno('Confirmação', f'Você portador da matricula: {matricula}, confirma seu voto em {nome}, Número: {dados['numero']}, {dados['partido']}')
                    dados['voto'] += 1
                    if confirmacao: 
                        voto_feito = messagebox.showinfo('Confirmação', 'Voto feito')
                    candidato_encontrado = True
                    break
        if not candidato_encontrado:
            nao_encontrado_candidato = messagebox.showinfo('Erro', 'Candidato não encontrado')
                
    btn_votar = tk.Button(janela_votacao, text='Confirmar Voto', command=confirmar_voto, **estilo_botao_voto)
    btn_votar.pack(pady=30)
    # BOTÃO DE VOLTAR
    btn_voltar = tk.Button(janela_votacao, text="voltar", command=janela_votacao.destroy, **estilo_botao_voto)
    btn_voltar.pack(pady=10)
    
def imprimir_relatorio():

    relatorio_da_eleicao = "relatorio_da_eleicao.pdf"

    janela_relatorio = tk.Toplevel(janela)
    janela_relatorio.title("Votação")
    janela_relatorio.geometry("580x360")
    janela_relatorio.configure(padx=20, pady=20, bg=COR_FUNDO)
    eleito = max(candidatos, key=lambda nome: candidatos[nome]['voto'])
    msg_relatorio = f'O vendedor da eleição é {eleito}, com {candidatos[eleito]['voto']} votos.'
    label_menu = tk.Label(janela_relatorio, text=msg_relatorio, **estilo_label)
    label_menu.pack(pady=10) # Espaçamento entre o rótulo e os botões

    # FUNÇÕES DE PDF
    def baixar_relatorio():
        relatorio_da_eleicao = "relatorio_da_eleicao.pdf"
        c = canvas.Canvas(relatorio_da_eleicao, pagesize=A4)
        largura, altura = A4

        # TITULO
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(largura / 2, altura - 80, "Relatório Final da Eleição")
        # LINHA 
        c.setStrokeColor(colors.grey)
        c.setLineWidth(1)
        c.line(50, altura - 90, largura - 50, altura - 90)
        # INFOS VOTOS
        c.setFont("Helvetica", 14)
        c.drawString(100, altura - 140, f"Vencedor: {eleito}")
        c.drawString(100, altura - 170, f"Total de Votos: {candidatos[eleito]['voto']}")
        c.drawString(100, altura - 200, f"Partido: {candidatos[eleito]['partido']}")
        # RODAPÉ
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        c.setFont("Helvetica-Oblique", 10)
        c.setFillColor(colors.grey)
        c.drawRightString(largura - 50, 40, f"Gerado em: {data_atual}")

        c.save()
        messagebox.showinfo("Sucesso", f"PDF salvo em:\n{os.path.abspath(relatorio_da_eleicao)}")
        
    # ACABOU

    btn_baixar = tk.Button(janela_relatorio, text="baixar relatorio", command=baixar_relatorio, **estilo_botao_encerrar)
    btn_baixar.pack(pady=10)

    btn_voltar = tk.Button(janela_relatorio, text="voltar", command=janela_relatorio.destroy, **estilo_botao_encerrar)
    btn_voltar.pack(pady=10)

        
            


# ------------------------------------------------ #

menu()

janela.mainloop()