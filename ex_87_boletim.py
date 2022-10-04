ficha = list()
while True:
    nome = str(input('Nome: ').capitalize())
    nota1 = int(input('Nota 1:'))
    nota2 = int(input('Nota 2:'))
    media = (nota1 + nota2)/2

    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Quer continuar[S/N]' ).upper())
    if resp != 'S':
        print(f' O boletim de alunos foi:{ficha}')
        
        break