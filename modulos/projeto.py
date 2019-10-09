from time import sleep as sp
from modulos import __not__.Notificacao as nt
from modulos import __dados__.Dados as dd
from os import system as st

class Ostra(object):
    st('cls')
    def __init__(self, temperatura):
        self.temperatura = temperatura
        self.contador = 0
        self.minute = 1

    def __not__(self):
        __doc__ = ''' método para receber notificação da ostra '''
        while True:
            print(f'A temperatura de {self.temperatura} graus célsius está em stress')
            sp(self.minute)
            self.contador += 1
            self.temperatura += 1
            # st('cls')
            if self.temperatura >= 31:
                print(f'\033[31mQue pena, a ostra está morta\033[m')
                break
        

if __name__ == '__main__':
    def main():
        notificacao = nt()
        notificacao.__noti__
        ostra = Ostra(20)
        ostra.__not__()
    main()
