import urllib
import urllib.request

def req(url):
    try:
        site = urllib.request.urlopen(url)
    except:
        print('Deu erro')
    else:
        print('tudo okay')
        return 'Pessoal Tudo certo', site
    