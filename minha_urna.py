# # Desenvolva seu código aqui!
 
# candidatos = {
#     'Python Silva': {'partido': 'Partido do Código Aberto (PCA)', 'numero': 11},
#     'CSS Cardoso': {'partido': 'Desenvolvedores Ágeis (DA)', 'numero': 22},
#     'SQL Ferreira': {'partido': 'Orientados a Objetos (POO)', 'numero': 33},
#     'HTML Santos': {'partido': 'Marcação para Todos (MT)', 'numero': 44},
#     'JavaScript Oliveira': {'partido': 'Assíncronos Independentes (AI)', 'numero': 55}
# }
# votos = {
#     'Python Silva': 0,
#     'CSS Cardoso': 0,
#     'SQL Ferreira': 0,
#     'HTML Santos': 0,
#     'JavaScript Oliveira': 0
# }


# # votos = {
# #     'Python Silva': 10,
# #     'CSS Cardoso': 50,
# #     'SQL Ferreira': 20,
# #     'HTML Santos': 70,
# #     'JavaScript Oliveira': 0
# # }


# # ----------------- FUNÇÕES ---------------------- #

# def votar():
#     cont = 0
#     numeros_candidatos = []
#     for nome, info in candidatos.items():
#         numeros_candidatos.append(info.get("numero"))
#         print(f'{info.get("numero")} - Candidato {nome}, partido {info.get("partido")}')
#     while cont < 1:
#         selec_voto = int(input('Digite o número do candidato que deseja votar'))
#         if selec_voto in numeros_candidatos:
#             for nome, info in candidatos.items():
#                 if info.get('numero') == selec_voto:
#                     print(f' Candidato: {nome}\n Número: {info.get('numero')}\n Partido: {info.get('partido')}')
#                     confirma = input('Deseja confirmar seu voto? Digite Sim ou Não').lower()
#                     if confirma == 'sim':
#                         votos[nome] += 1
#                         cont += 1
#                         print('Voto realizado')
#                     else: 
#                         print('Votação reiniciada.')
#         else: 
#             print('Número de candidato inexistente')

# def encerrar():
#     # encerrar vai para a votação, retornar o candidato com maior numero de votos
#     eleito = max(votos, key = votos.get)
#     print(f'O vendedor da eleição é {eleito}, com {votos.get(eleito)} votos.')
    
            


# # ------------------------------------------------ #
# menu = """

#     URNA ELETRÔNICA
#     1 - Votar
#     2 - Encerrar Votação
    
# """

# while True:
#     print(menu)
#     opcao = input('Selecione uma opção: ')
#     if opcao == '1':
#         votar()
#         continue
#     elif opcao == '2':
#         encerrar()
#         break
#     else:
#         print('Opção invalida, selecione uma correta')
#         continue

import tkinter as tk
from tkinter import messagebox

votacao_ativa = False

candidatos = {
    'Python Silva': {'partido': 'Partido do Código Aberto (PCA)', 'numero': 11, 'voto': 0},
    'CSS Cardoso': {'partido': 'Desenvolvedores Ágeis (DA)', 'numero': 22, 'voto': 0},
    # 'SQL Ferreira': {'partido': 'Orientados a Objetos (POO)', 'numero': 33, 'voto': 0},
    # 'HTML Santos': {'partido': 'Marcação para Todos (MT)', 'numero': 44, 'voto': 0},
    # 'JavaScript Oliveira': {'partido': 'Assíncronos Independentes (AI)', 'numero': 55, 'voto': 0}
}
votos = []

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
    botao_encerrar = tk.Button(janela, text="Encerrar Votação", command=votar)
    botao_encerrar.pack(pady=5)

def add_candidato():
    janela_add_candidato = tk.Toplevel(janela)
    janela_add_candidato.title("Cadastro de Candidato")
    janela_add_candidato.geometry("1200x600")
    # BOTÃO DE VOLTAR
    btn_voltar = tk.Button(janela_add_candidato, text="voltar", command=janela_add_candidato.destroy)
    btn_voltar.pack(pady=10)
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
        matricula = entrada_matricula.get()
        voto = int(entrada_voto.get())
        if matricula:
            for nome, dados in candidatos.items():
                if dados['numero'] == voto:
                    confirmacao = messagebox.askyesno('Confirmação', f'Você portador da matricula: {matricula}, confirma seu voto em {nome}, {dados['numero']}, {dados['partido']}')
                

        # if confirma:
        #     print(candidatos)
            
        
        
    btn_votar = tk.Button(janela_votacao, text='Confirmar Voto', command=confirmar_voto)
    btn_votar.pack(pady=30)
    
            


# ------------------------------------------------ #

menu()

janela.mainloop()