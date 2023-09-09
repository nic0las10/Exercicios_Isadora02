'''Verificação de Número Positivo/Negativo:
Escreva um programa que recebe um número inteiro e verifica se é positivo, negativo ou zero. Imprima a mensagem correspondente.'''

num1 = int(input("Digite um numero inteiro:" ))

if num1 < 0:
    print("O número é negativo!")
elif num1 > 0: 
    print("O número é positivo!")
else:
    print("O número é igual a zero!")       