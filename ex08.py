com1 = float(input('Coloque um comprimento de um triangulo...'))
com2 = float(input('Coloque o segundo comprimento...'))
com3 = float(input('Coloque o terceiro comprimento...'))
if com1 < com2 + com3 and com2< com1 +com3 and com3< com1 + com2:
    print('Os segmentos formam um triangulo!...')
    if com1 == com2 == com3:
        print('É equilatero!')
    elif com1 != com2 != com3 != com1: 
        print('É escaleno!')
    else:
        print('É isoceles!')
else:
    print('Os segmentos acima não pode formar um triangulo!...')