def fatorial(n=0, show=False):
    f=1
    lista = []
    for c in range(n, 1, -1):
        if show:
            print(f'{c} X ', end='')

        f*=c
        
            

    
    print(f)

fatorial(5, show=True)