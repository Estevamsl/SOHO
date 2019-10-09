from projeto import *
from os import system as st
st('cls')

def main():
    while True:
        while True:
            try:
                temp = int(input('Digite uma temperatura em graus célsius: '))
                st('cls')
                if temp:
                    break
            except (ValueError, NameError, TypeError) as err:
                return f'ERRO do tipo: {err}, tente novamente!'
            else:
                return 'Continuando...'
        
        ostra = Ostra(temp)
        ostra.__not__()

        while True:
            resp = ' '
            resp = str(input('Deseja continuar [S/N]: ')).strip().title()
            st('cls')
            while resp not in 'SsNn':
                resp = str(input('\033[31mERRO digite novamente, para continuar [S/N]: ')).strip().title()
                st('cls')
            if resp in 'Nn':
                break

if __name__ == '__main__':
    main()
else:
    pass