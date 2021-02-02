# importando o modulo
import notify2

# iniciando a instancia
notify2.init(app_name='script-Notificação')

# definindo a variavel que sera usada para definiçao
# dos parametros e detalhes da notificaçao
notificao = notify2.Notification(  # definindo o titulo da notificação
                                 summary='Titulo da Notificação',
                                 # definindo a mensagem da notificação
                                 message='Mensagem da Notificação - Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                                 # definindo o icone da notificação
                                 icon='notification-message-im')

if __name__ == '__main__':
    # definindo a duração da notificação
    notificao.set_timeout(5)

    # apresentando a notificaçao no ecra
    notificao.show()
