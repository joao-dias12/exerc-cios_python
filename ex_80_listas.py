#Adicionando novos intens a lista e colocando eles na posição correta em ordem crescentee dizendo a posição
list_of_numb = []
value_reference = 0

for i in range(0,5):
    added_value = int(input('Digite um valor: '))
    if i == 0:
        print('Adicionada ao Final da lista')
        list_of_numb.append(added_value)
    else:
        list_of_numb.append(added_value)
        list_of_numb.sort()
        if list_of_numb.index(added_value) != len(list_of_numb)-1: 
            print(f'Adicionado na posição {list_of_numb.index(added_value)}') 
        else: 
            print('Adicionada ao Final da lista')
        

print('A lista Final é: ')
print(list_of_numb)
