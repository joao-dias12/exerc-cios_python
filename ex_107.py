from modulos import numeros
from modulos.funcoes import moeda
from random import randint

valor = float(randint(0,60))

print(f'O valor é {valor}')

print(f""" 
A metade de  R${valor} é  R${round(numeros.metade(valor),3)}
O Dobro de  R${valor} é  R${round(numeros.dobro(valor),3)}
10% de aumento em  R${valor} é  R${numeros.aumentar10(valor): >.2f}

{moeda.moeda(valor)}
 """)
