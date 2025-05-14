import tkinter as tk
from tkinter import messagebox

votacao_ativa = False

candidatos = {
    'Python Silva': {'partido': 'Partido do Código Aberto (PCA)', 'numero': 11, 'voto': 0},
    'CSS Cardoso': {'partido': 'Desenvolvedores Ágeis (DA)', 'numero': 22, 'voto': 0},
    'SQL Ferreira': {'partido': 'Orientados a Objetos (POO)', 'numero': 33, 'voto': 0},
    'HTML Santos': {'partido': 'Marcação para Todos (MT)', 'numero': 44, 'voto': 0},
    'JavaScript Oliveira': {'partido': 'Assíncronos Independentes (AI)', 'numero': 55, 'voto': 0}
}

janela = tk.Tk()
janela.title("Dizer Olá")

# 

def menu():
    janela.geometry("1200x600") # Define o tamanho da janela principal
    janela.configure(padx=20, pady=20) # Adiciona margem grande
    label_menu = tk.Label(janela, text="Escolha uma opção:")
    label_menu.pack(pady=10) # Espaçamento entre o rótulo e os botões
    botao_cadastro = tk.Button(janela, text="Cadastro de Candidato", command=add_candidato) # FUNÇÃO QUE É CHAMADA
    botao_cadastro.pack(pady=5) # Espaçamento entre os botões
    botao_votacao = tk.Button(janela, text="Iniciar Votação", command=votar)
    botao_votacao.pack(pady=5)
    botao_encerrar = tk.Button(janela, text="Encerrar Votação", command=imprimir_relatorio)
    botao_encerrar.pack(pady=5)

def add_candidato():
    janela_add_candidato = tk.Toplevel(janela)
    janela_add_candidato.title("Cadastro de Candidato")
    janela_add_candidato.geometry("1200x600")
    # NOME CANDIDATO
    tk.Label(janela_add_candidato, text="Nome do Candidato: ").pack(pady=5)
    entrada_nome = tk.Entry(janela_add_candidato)
    entrada_nome.pack(pady=5)
    # NÚMERO DO CANDIDATO
    tk.Label(janela_add_candidato, text="Número do Candidato: ").pack(pady=5)
    entrada_numero = tk.Entry(janela_add_candidato)
    entrada_numero.pack(pady=5)
    # PARTIDO DO CANDIDATO
    tk.Label(janela_add_candidato, text="Partido do Candidato: ").pack(pady=5)
    entrada_partido = tk.Entry(janela_add_candidato)
    entrada_partido.pack(pady=5)
    def confirmar_add_candidato():
        num = int(entrada_numero.get())
        nome = entrada_nome.get()
        partido = entrada_partido.get()
        candidatos.update({nome: {'partido': partido, 'numero': num, 'voto': 0}})
        print(candidatos)
    btn_add_candidato = tk.Button(janela_add_candidato, text="Salvar", command=confirmar_add_candidato)
    btn_add_candidato.pack(pady=5)
    # BOTÃO DE VOLTAR
    btn_voltar = tk.Button(janela_add_candidato, text="voltar", command=janela_add_candidato.destroy)
    btn_voltar.pack(pady=10)

def votar():
    janela_votacao = tk.Toplevel(janela)
    janela_votacao.title("Votação")
    janela_votacao.geometry("400x300")
    tk.Label(janela_votacao, text="Digite sua matrícula:").pack(pady=5)
    entrada_matricula = tk.Entry(janela_votacao)
    entrada_matricula.pack(pady=5)
    tk.Label(janela_votacao, text="Digite o número do candidato:").pack(pady=5)
    entrada_voto = tk.Entry(janela_votacao)
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
                        # print(candidatos)
                    candidato_encontrado = True
                    break
            
                
                
        if not candidato_encontrado:
            nao_encontrado_candidato = messagebox.showinfo('Erro', 'Candidato não encontrado')
                
    btn_votar = tk.Button(janela_votacao, text='Confirmar Voto', command=confirmar_voto)
    btn_votar.pack(pady=30)
    # BOTÃO DE VOLTAR
    btn_voltar = tk.Button(janela_votacao, text="voltar", command=janela_votacao.destroy)
    btn_voltar.pack(pady=10)
    
def imprimir_relatorio():
    eleito = max(candidatos, key=lambda nome: candidatos[nome]['voto'])
    print(f'O vendedor da eleição é {eleito}, com {candidatos[eleito]['voto']} votos.')
        
            


# ------------------------------------------------ #

menu()

janela.mainloop()