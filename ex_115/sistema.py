from lib.interface import *
from time import sleep

cabecalho('SISTEMA ARQUIVO v1.0')

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        cabecalho('\033[32mOpção 1 Escolhida\033[m')
    elif resposta == 2:
        cabecalho('\033[32mOpção 2\033[m')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Volte Sempre')
        break
    else:
        cabecalho('\033[31mErro: Digite um valor válido\033[m')
    sleep(2)