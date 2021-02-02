# importando o módulo
import desktop_notify as dn

# definindo um servidor (base) para o programa
nome_programa = dn.Server(app_name="Demo-Notificação")

# definindo a instancia para a notificacao
notificacao = nome_programa.Notify()

if __name__ == '__main__':
    # definindo o titulo para a notificação
    notificacao.set_summary("Titulo da Notificação")

    # definindo o corpo da memsagem
    notificacao.set_body("Mensagem da Notificação - Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    # definindo o icone para a notificaçao
    notificacao.set_icon("notification-message-im")

    # definindo o tempo de duração para o balão da notificação
    notificacao.set_timeout(5000)

    # apresentando a notificação no ecrã
    notificacao.show()
