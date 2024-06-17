import random

placarj1 = 0
placarj2 = 0

#modo
print("MODOS: Pessoa x Pessoa (0), Pessoa x Computador (1), Computador x Computador (2)")
modo = int(input("Qual modalildade voce gostaria de jogar? "))


while True:
    #escolhas
    if  modo ==0 :
        jogada1 = input('Faça sua jogada (Pedra, papel ou tesoura) ').upper()
        jogada2 = input('Faça sua jogada (Pedra, papel ou tesoura) ').upper()

    elif modo ==1:
        jogada1 = input('Faça sua jogada (Pedra, papel ou tesoura) ').upper()
        jogada2 = (random.choice(['PEDRA', 'PAPEL', 'TESOURA']))
        print('O computador escolheu:', jogada2)

    elif modo == 2:
        jogada1 = (random.choice(['PEDRA', 'PAPEL', 'TESOURA']))
        jogada2 = (random.choice(['PEDRA', 'PAPEL', 'TESOURA']))
        print('O computador 1 escolheu:', jogada1)
        print('O computador 2 escolheu:', jogada2)

    else: print('Jogada invalida')

    #jogo e resultado
    if jogada1 == jogada2:
        resultado = 'Empate'

    elif (jogada1 == 'PEDRA' and jogada2 == 'TESOURA') or \
        (jogada1 == 'TESOURA' and jogada2 == 'PAPEL') or \
        (jogada1 == 'PAPEL' and jogada2 =='PEDRA' ):
        resultado = 'Jogador 1 venceu'

    else: resultado = 'Jogador 2 venceu'

    #contagem resultado
    print('Resultado:', resultado)


    if  resultado == 'Jogador 1 venceu':
        placarj1 = placarj1 + 1
    elif resultado == 'Jogador 2 venceu':
        placarj2 = placarj2 + 1


    print('Placar:')
    print('Jogador 1:', placarj1)
    print('Jogador 2:', placarj2)


    #checar se jogador quer continuar
    continua = input('Deseja continuar jogando? (S/N) ').upper()
    if continua != 'S':
        print('Placar final: ')
        print('Jogador 1:', placarj1)
        print('Jogador 2:', placarj2)
        print('Obrigado por jogar pedra, papel, tesoura.')
        break
