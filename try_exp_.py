from typing import final



try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a/b
# #except Exception as erro:
#     print(f'Tivemos um Problema ! {erro.__class__}') esse é um tipo de tratamento

except (ValueError, TypeError):
    print(f'Tivemos um Problema com os tipos de dados inseridos')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero')

except KeyboardInterrupt:
    print('O usuário prefiriu não informar os dados')

else:
    print(r)
finally:
    print('')
