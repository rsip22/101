"""
Escreva uma funçao chamada right_justify, que receba uma string chamada s
como parâmetro e exiba a string com espaços suficientes à frente para que a
última letra da string esteja na coluna 70 da tela.
"""

def right_justify(s):
    space = ' '
    column = len(string)
    for number in range(0,(69 - column)):
        space = space + ' '
    print(space, string)

right_justify('monty')
