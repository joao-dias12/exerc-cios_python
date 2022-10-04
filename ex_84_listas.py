#Pegando o nome e o peso das pessoas mais pesadas registradas
users = list()
data = list()
answer = 'S'
max_weigth = min_weight = 0
heavy_people = list()
light_people = list()

while True:
    data.append(str(input('Nome: ')).capitalize())
    data.append(int(input('Peso: ')))
    users.append(data[:])
    data.clear()
    answer = str(input('Quer continuar? [S/N]')).upper()

    if answer != 'S':
        for position,value in enumerate(users):
            if position == 0:
                max_weigth = min_weight = users[position][1]
                heavy_people.append(users[position][0])

            if max_weigth == users[position][1]:
                heavy_people.append(users[position][0])

            if max_weigth < users[position][1]:
                max_weigth = users[position][1]
                heavy_people.clear()
                heavy_people.append(users[position][0])
            

        print(f'Ao todo você cadastrou {len(users)} Pessoas')
        print(f"O maior peso é de {max_weigth} das pessoas: {heavy_people}")
        break