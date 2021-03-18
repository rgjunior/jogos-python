import random


def jogar():
    print("********************************")
    print("Bem-vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = round(random.randrange(0, 101))
    total_tentativas = 0
    pontos = 1000

    print("Selecione o nível de dificuldade: ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5    

    for rodada in range(1, total_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)
       
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior   = numero_secreto < chute
        menor   = numero_secreto > chute

        if (acertou):
            print("Resposta certa")
            print("Sua pontuação: {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Errado! Seu chute é MAIOR que o número secreto!")
            elif(menor):
                print("Errado! Seu chute é MENOR que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Resposta correta: ", numero_secreto)
    print("********Fim do jogo*************")

if(__name__ == "__main__"):
    jogar()