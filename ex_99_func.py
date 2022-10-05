def maior(*args):
    lista = []
    for i in args:
        print(f' Você adicionou o item {i}')
        lista.append(i)
    
    print(f'O maior valor é {max(lista)}')

maior(4,3,2,7,9)
