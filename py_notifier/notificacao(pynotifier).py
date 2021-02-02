# importando a classe Notification dentro do módulo
from pynotifier import Notification

# definindo a variavel que sera usada para definição
# dos parametros e detalhes da notificação
notificacao = Notification(  # definindo o titulo da notificação
                           title="Titulo da Notificação",
                           # definindo a mensgem da notificação
                           description="Mensagem da Notificação - Lorem ipsum dolor sit amet, consectetur adipiscing elit",
                           # definindo o temp de duração da notificação em segundos
                           duration=5,
                           # definir a prioridade da notificação (.URGENCY_LOW, .URGENCY_NORMAL, .URGENCY_CRITICAL)
                           urgency=Notification.URGENCY_NORMAL,
                           # definindo o icone da notificação (pode ser uma imagem do tipo .png ou .ico no windows)
                           icon_path="notification-message-im")

if __name__ == '__main__':
    # apresentando a notificação no ecrã
    notificacao.send()
