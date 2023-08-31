from datetime import date
ano = int(input('Qual o ano que você nasceu?...'))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print('Você pode se alistar!')
elif idade < 18:
    print('Você não tem idade para se alistar!...')
elif idade > 18:
    print('Ja passou o seu tempo de se alistar!...')