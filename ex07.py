from datetime import date
data = int(input('Qual é o ano do seu nascimento?...'))
atual = date.today().year
idade = atual - data
if idade <= 9:
    print('Sua classe é MIRIM...')
elif idade <= 14:
    print('Sua classe é INFANTIL...')
elif idade <= 19:
    print('Sua classe é JUNIOR...')
elif idade <= 20:
    print('Sua classe é SENIOR')
else:
    print('Sua classe é MASTER...')
print('.........................')
print('Tenha um bom dia!')