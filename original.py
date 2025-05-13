# Desenvolva seu código aqui!
 
candidatos = {
    'Python Silva': {'partido': 'Partido do Código Aberto (PCA)', 'numero': 11},
    'CSS Cardoso': {'partido': 'Desenvolvedores Ágeis (DA)', 'numero': 22},
    'SQL Ferreira': {'partido': 'Orientados a Objetos (POO)', 'numero': 33},
    'HTML Santos': {'partido': 'Marcação para Todos (MT)', 'numero': 44},
    'JavaScript Oliveira': {'partido': 'Assíncronos Independentes (AI)', 'numero': 55}
}
votos = {
    'Python Silva': 0,
    'CSS Cardoso': 0,
    'SQL Ferreira': 0,
    'HTML Santos': 0,
    'JavaScript Oliveira': 0
}


# votos = {
#     'Python Silva': 10,
#     'CSS Cardoso': 50,
#     'SQL Ferreira': 20,
#     'HTML Santos': 70,
#     'JavaScript Oliveira': 0
# }


# ----------------- FUNÇÕES ---------------------- #

def votar():
    cont = 0
    numeros_candidatos = []
    for nome, info in candidatos.items():
        numeros_candidatos.append(info.get("numero"))
        print(f'{info.get("numero")} - Candidato {nome}, partido {info.get("partido")}')
    while cont < 1:
        selec_voto = int(input('Digite o número do candidato que deseja votar'))
        if selec_voto in numeros_candidatos:
            for nome, info in candidatos.items():
                if info.get('numero') == selec_voto:
                    print(f' Candidato: {nome}\n Número: {info.get('numero')}\n Partido: {info.get('partido')}')
                    confirma = input('Deseja confirmar seu voto? Digite Sim ou Não').lower()
                    if confirma == 'sim':
                        votos[nome] += 1
                        cont += 1
                        print('Voto realizado')
                    else: 
                        print('Votação reiniciada.')
        else: 
            print('Número de candidato inexistente')

def encerrar():
    # encerrar vai para a votação, retornar o candidato com maior numero de votos
    eleito = max(votos, key = votos.get)
    print(f'O vendedor da eleição é {eleito}, com {votos.get(eleito)} votos.')
    
            


# ------------------------------------------------ #
menu = """

    URNA ELETRÔNICA
    1 - Votar
    2 - Encerrar Votação
    
"""

while True:
    print(menu)
    opcao = input('Selecione uma opção: ')
    if opcao == '1':
        votar()
        continue
    elif opcao == '2':
        encerrar()
        break
    else:
        print('Opção invalida, selecione uma correta')
        continue