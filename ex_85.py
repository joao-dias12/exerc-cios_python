# Colocando lista de pares e lista de impares dentro de uma lista só
princ = list()
temp_par = list()
temp_impar = list()

for i in range (1,8):
    added_value = int(input(f'Digite o {i}º valor: '))
    if added_value % 2 == 0:
        temp_par.append(added_value)
    else:
        temp_impar.append(added_value)

princ.append(temp_par[:])
princ.append(temp_impar[:])


print(f" O valores pares são: {princ[0]}")
print(f" O valores impares são: {princ[1]}")