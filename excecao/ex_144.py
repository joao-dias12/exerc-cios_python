
from excecao_modulos_114 import requisicao

msg , site  = requisicao.req('http://www.pudim.com.br')

print(msg)

print(site.read())