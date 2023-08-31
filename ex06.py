nota1 = float(input('Coloque um valor de nota!...'))
nota2 = float(input('Coloque a outra nota!...'))
media = (nota1 +nota2)/2
if media < 5:
    print('Você foi reprovado!...')
elif media >= 5 and media  < 7:
    print('Recuperação!')
elif media >= 7:
    print('Você foi aprovado!...')
