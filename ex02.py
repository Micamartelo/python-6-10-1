em = float(input('Qual o valor do imovel?...'))
sa = float(input('Qual o valor do seu salario?...'))
anos = int(input('Quantos anos você vai pagar?...'))
J = em * (anos/12)
print('Para pagar a casa de R${:.2f} em {} anos...'.format(em,anos))
print('a prestação será de R${:.2f}'.format(J))
minimo = sa * 30 / 100
if J <= minimo:
    print('Emprestimos concedido!....')
else:
    print('Recusado!...')