import random
print('[1] Pedra')
print('[2] Tesoura')
print('[3] Papel')
escolha = int(input('.....Escolha entre pedra, papel e tesoura!.....'))
jogo = [1,2,3] 
jogada = random.choice(jogo)
if escolha == 1: 
    if jogada == 1: 
        print('EMPATE!!!')
    elif jogada == 2:
        print('VENCEU!!!')
    elif jogada == 3:
        print('PERDEU!!!')
elif escolha == 2:
    if jogada == 1: 
        print('PERDEU!!!')
    elif jogada == 2:
        print('EMPATE!!!')
    elif jogada == 3:
        print('VENCEU!!!')
elif escolha == 3:
    if jogada == 1: 
        print('VENCEU!!!')
    elif jogada == 2:
        print('PERDEU!!!')
    elif jogada == 3:
        print('EMPATE!!!')
print('....Obrigado por jogar!....')

    

    


