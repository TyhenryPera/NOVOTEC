import time

def introducao():
    print("Bem-vindo(a) à aventura interativa!")
    time.sleep(2)
    nome = input("Qual é o seu nome? ")
    print("Você está em uma antiga floresta misteriosa...")
    time.sleep(2)
    print("Você se depara com 2 caminhos em sua frente.")
    time.sleep(2)
    return nome
   
def caminho_esquerda(nome):
    print(f"\nVocê escolheu o caminho da esquerda...")
    time.sleep(2)
    print("Você se depara com uma caverna escura.")
    time.sleep(2)
    decisao = input("Você entra na caverna? (Sim/Não): ").lower()
    if decisao == "sim":
        print("\nDentro da caverna, você encontra um tesouro brilhante!")
        time.sleep(2)
        print("Parabéns! Você se tornou rico e vive feliz para sempre.")
        return 1
    else:
        print("\nVocê decide não entrar na caverna.")
        time.sleep(2)
        print("Você continua sua jornada pela floresta.")
        return 2

def caminho_direita(nome):
    print("\nVocê escolheu o caminho da direita...")
    time.sleep(2)
    print("Você se depara com uma ponte sobre um rio agitado.")
    time.sleep(2)
    decisao = input("Você atravessa a ponte? (Sim/Não): ").lower()
    if decisao == "sim":
        print("\nVocê atravessa a ponte com sucesso.")
        time.sleep(2)
        print("Do outro lado, encontra uma aldeia pacífica.")
        time.sleep(2)
        print("Você observa a aldeia de longe, mas decide não entrar.")
        return 3
    else:
        print("\nVocê decide não arriscar e volta pelo caminho que veio.")
        time.sleep(2)
        print("Você continua sua jornada pela floresta.")
        return 4

def caminho_extra(nome):
    print("\nVocê encontra um atalho estranho.")
    time.sleep(2)
    decisao = input("Você decide seguir o atalho? (Sim/Não): ").lower()
    if decisao == "sim":
        print("\nVocê se perde no atalho desconhecido...")
        time.sleep(2)
        print("Horas se passam e você não encontra o caminho de volta.")
        return 5
    else:
        print("\nVocê decide não arriscar e continua pela trilha principal.")
        time.sleep(2)
        print("Você continua sua jornada pela floresta.")
        return 4

def final_1(nome):
    print(f"\n*** Final Muito Bom ***")
    time.sleep(2)
    print("Você encontrou um tesouro e viveu uma vida próspera.")
    time.sleep(2)

def final_2(nome):
    print(f"\n*** Final Neutro ***")
    time.sleep(2)
    print("Você segue adiante na floresta, em busca de novas aventuras.")

def final_3(nome):
    print(f"\n*** Final Bom ***")
    time.sleep(2)
    print("Você encontrou um lar na aldeia e viveu em paz.")

def final_4(nome):
    print(f"\n*** Final Ruim ***")
    time.sleep(2)
    print("Você continua sua jornada pela floresta, sem saber o que o aguarda.")

def final_5(nome):
    print(f"\n*** Final Muito Ruim ***")
    time.sleep(2)
    print("Você acabou perdido na floresta e não encontrou um caminho seguro.")

def como_chegar_aos_finais():
    print("\n--- Como Chegar aos Finais ---")
    print("1. Final Muito Bom: Escolha o caminho da esquerda e entre na caverna.")
    print("2. Final Neutro: Escolha o caminho da esquerda, mas não entre na caverna.")
    print("3. Final Bom: Escolha o caminho da direita e atravesse a ponte para entrar na aldeia.")
    print("4. Final Ruim: Escolha o caminho da direita e não atravesse a ponte.")
    print("5. Final Muito Ruim: Escolha o caminho extra e siga o atalho.")

nome_jogador = introducao()

escolha_caminho = input("Qual caminho você escolhe? (Direita/Extra/Esquerda): ").lower()

if escolha_caminho == "direita":
    resultado_direita = caminho_direita(nome_jogador)
    if resultado_direita == 3:
        final_3(nome_jogador)
    elif resultado_direita == 4:
        final_4(nome_jogador)
    elif resultado_direita == 5:
        final_5(nome_jogador)

elif escolha_caminho == "extra":
    resultado_extra = caminho_extra(nome_jogador)
    if resultado_extra == 5:
        final_5(nome_jogador)

elif escolha_caminho == "esquerda":
    resultado_esquerda = caminho_esquerda(nome_jogador)
    if resultado_esquerda == 1:
        final_1(nome_jogador)
    elif resultado_esquerda == 2:
        final_2(nome_jogador)