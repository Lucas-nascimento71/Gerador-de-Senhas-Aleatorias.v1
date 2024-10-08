import random
import string

print('=-=-=-==-=--=-=-==-=GERADOR DE SENHAS ALEATÓRIAS=-=-=-=-=--=-=-=-=-=-=-=-=-=')
print('Características:', '\n', '12 caracteres', '\n', 'Alfanuméricos', '\n', 'Letras Maiúsculos', '\n', 'Letras minúsculas', '\n', 'Caracteres Especiais')
print('=-=-=-==-=--=-=-==-==-=-=-=-=--=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=---==-=-=-==')

def gerar_senhas(tamanho=12):
    caracteres = string.ascii_letters + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print(f'Senha Gerada: {gerar_senhas()}')
print('=-=-=-==-=--=-=-==-==-=-=-=-=--=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=---==-=-=-==')