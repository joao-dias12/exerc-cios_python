from lib.interface import *
from lib.arquivo import *
from time import sleep

#começo de sistema e configuração
arq = 'ex_115\cursoemvideo.txt'
if not arquivoexiste(arq):
    criarArquivo(arq)


cabecalho('SISTEMA ARQUIVO v1.0')


#Navegação de Usuário
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo!
        cabecalho('\033[32mOpção 1 Escolhida\033[m')
        lerArquivo(arq)

    elif resposta == 2:
        #Opção de cadastrar uma pessoa nova
        cabecalho('\033[32NOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Volte Sempre')
        break
    else:
        cabecalho('\033[31mErro: Digite um valor válido\033[m')
    sleep(2)