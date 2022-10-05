from  lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(f'{nome}', 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(':')
            dado[1]= dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>4} anos')
    finally:
        a.close()

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO: Erro ao abrir o arquivo.\033[m')
    else:
        try:
            a.write(f'{nome}:{idade}\n')
        except:
            print('\033[31mERRO: ERRO ao TENTAR ESCREVER NO ARQUIVO\033[m')
        else:
            print(f'\033[32mNovo registro de {nome} realizado.\033[m')