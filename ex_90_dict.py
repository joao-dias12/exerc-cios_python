boletim = {'Nome':str(input('Nome: ')), 'Média':int(input('Média: '))}

if boletim['Média'] < 7:
    message = f"""- Nome é igual a {boletim['Nome']}
- média é igual a {boletim['Média']}
- Situação é de RECUPERAÇÃO"""
else:
    message = f"""- Nome é igual a {boletim['Nome']}
- média é igual a {boletim['Média']}
- Situação é de Aprovação""" 

print(message)
    


