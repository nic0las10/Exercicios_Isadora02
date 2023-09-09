'''Verificação de Número Múltiplo de 3 e 5:
Receba um número do usuário e verifique se ele é um múltiplo de 3 e 5 ao mesmo tempo. Se for, imprima "É um múltiplo de 3 e 5." Caso contrário, imprima "Não é um múltiplo de 3 e 5.'''

num = int(input("Digite um número:"))
mult1 = 3
mult2 = 5 

if num % mult1 == 0 and num % mult2 == 0: 
    print("E divisível por 3 e 5!")
elif num % mult2 == 0:
    print("E divisivel por 5 !")
elif num % mult1 == 0:
    print("E divisivel por 3!")
else:
    print("Não divisível")

        
