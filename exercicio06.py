'''Verificação de Divisibilidade:
Receba um número inteiro do usuário. Verifique se ele é divisível por 5. Se for, imprima "É divisível por 5." Caso contrário, imprima "Não é divisível por 5."'''


num = int(input("Digite um número inteiro:"))
divisao = 5

if num % divisao == 0:
    print("O número é divisível por 5!")
else:
    print("O número não é divisível por 5!")    


#Documentação :Divisão (/) sempre retorna ponto flutuante (float).
#Para fazer uma divisão pelo piso e receber um inteiro como resultado você pode usar o operador //; para calcular o resto você pode usar o %:"
