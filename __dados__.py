from datetime import date as dt
from os import system as st

class Dados(object):
    st('cls')
    def __init__(self, nome, localidade, dono):
        
        self.nome = nome
        self.localidade = localidade
        self.dono = dono
        self.data = dt.today()

    def __str__(self):
        return f'A {self.nome} está localizada em {self.localidade} em {self.data}'

if __name__ == '__main__':
    dados = Dados('Ostrinha', 'Florianópolis', 'SOHO')
    print(dados)
else:
    pass