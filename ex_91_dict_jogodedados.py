from random import randint
from time import sleep
from operator import itemgetter
from pprint import pprint


jogo = dict()
lista = list()

for i in range(1,5):
    jogo['jogador'] = f'jogado{i}'
    jogo['dado'] = randint(0,6)
    lista.append(jogo.copy())
    print(f""" jogador{jogo['jogador']} tirou {jogo['dado']} no dado """)
    sleep(2)

print("-="*30)

lista_sort = sorted(lista, key=itemgetter('dado'), reverse=True)
for l in lista_sort:
    print(f'O {lista_sort.index(l)+1}º Lugar foi o {l["jogador"]} que tirou o número {l["dado"]}')
    










