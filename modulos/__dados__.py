from datetime import date as dt
class Dados(object):
    def __init__(self, nome, localidade, dono):
        self.nome = nome
        self.localidade = localidade
        self.dono = dono
        self.data = dt.today().year

    def __repr__(self):
        return f'A ostra com o nome de {self.nome} pertence ao {self.dono}'

    def __str__(self):
        return f'A {self.nome} está localizada em {self.localidade} no ano de {self.data}'

if __name__ == '__main__':
    dados = Dados('Ostrinha', 'Florianópolis', 'SOHO')
    print(dados)
else:
    pass