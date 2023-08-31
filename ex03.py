nu = int(input('Digite um número inteiro:...'))
binario = nu/2
print('Escolha uma das bases conversão:')
print('[1] Converte para binario')
print('[2] Converte para octal')
print('[3] Converte para hexadecimal')
opção = int(input('Sua opção...'))
if opção == 1:
    print('Seu resultado será:...{}'.format(bin(nu))) 
elif opção == 2:
    print('Seu resultado será:...{}'.format(oct(nu))) 
elif opção == 3:
    print('Seu resultado será:...{}'.format(hex(nu))) 
else: 
    print('INVALIDO...')




