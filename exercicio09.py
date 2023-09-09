'''Verificação de Dia da Semana:
Solicite ao usuário que insira o dia da semana (por exemplo, "segunda", "terça", etc.). Se for um dia útil (de segunda a sexta), imprima "É dia útil." Caso contrário, imprima "É fim de semana."
'''
dias_uteis = ["segunda feira", "terça feira", "quarta feira", "quinta feira", "sexta feira"]
dias_nao_uteis = ["sabado", "domingo"]
todos_os_dias = dias_uteis + dias_nao_uteis


escolha_um_dia = input("Digite um dia da semana:")

if escolha_um_dia in dias_uteis:
    print("É um dia útil!")
else:
    print("Não é um dia útil!")    

#nao consegui vou esperar explicação 

