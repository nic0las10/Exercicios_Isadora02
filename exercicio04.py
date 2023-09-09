'''Verificação de Idade para Dirigir:
Solicite a idade do usuário e, se a idade for 18 anos ou mais, imprima "Você pode dirigir!" Caso contrário, imprima "Desculpe, você ainda não pode dirigir."'''

Idade_Usuario = int(input("Digite sua idade:"))

if Idade_Usuario >= 18:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir, apenas depois dos 18 anos de idade. Lamento!")
