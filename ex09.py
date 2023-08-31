pagar = float(input('Qual o valor do produto!...'))
print('[1] A vista')
print('[2] Cheque')
print('[3] Cartão a vista')
print('[4] 2x no cartão')
print('[5] 3x ou mais no cartão')
qual = int(input('Qual é a forma de pagamento?...'))
dich = pagar*0.90
cart = pagar*0.95
normal = pagar
juros = (pagar*0.20) + pagar
if qual == 1 or qual == 2:
    print('Seu valor do produto será {}'.format(dich))
elif qual == 3:
    print('Seu valor do prouduto será de {}'.format(cart))
elif qual == 4:
    print('Seu valor do produto será de {}'.format(normal))
elif qual == 5:
    print('Seu valor do produto será de {}'.format(juros))


