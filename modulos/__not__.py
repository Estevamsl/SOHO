from pyfiglet import Figlet as fg
class Notificacao(object):
    def __init__(self):
        pass
        __doc__ = ''' pip install pyfiglet '''
        
    def __noti__(self):
        # __doc__ = '''
        #             notificação grande
        #                 '''
        art = fg(font='epic')
        print(art.renderText('\033[33mNotificacion de status\033[m'))

if __name__ == '__main__':
    notificacao = Notificacao()
    notificacao.__noti__()