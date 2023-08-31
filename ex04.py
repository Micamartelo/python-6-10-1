nu1 = int(input('Coloque um valor em numero inteiro:...'))
nu2 = int(input('Coloque um outro valor em numero inteiro:...'))
if nu1 < nu2:
    maior = nu2
elif nu1 > nu2: 
    maior = nu1
elif nu1 < nu2:
    menor = nu1
elif nu1 > nu2: 
    menor = nu2

print('O maior numero é {}...'.format(maior))
print('O menor número é {}...'.format(menor))