'''Decisão entre Três Números:
Peça ao usuário para inserir três números inteiros e determine o maior deles. Imprima o número maior.

'''
num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))
num3 = int(input("Digite outro numero inteiro:"))

lista = [num1,num2, num3]
maior_numero = max(lista)

print(f"O maior número é:{maior_numero}")    







