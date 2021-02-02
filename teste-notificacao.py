from PyQt5.Qt import *
from sys import argv


class TesteNotificacao:
    def __init__(self):
        self.notificacao = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowIcon(QIcon("img/news_icon.png"))
        self.ferramentas.setWindowTitle("Notificador-GC")
        self.ferramentas.setPalette(QPalette(QColor("orange")))

        menu = QMenuBar(self.ferramentas)
        instr = menu.addAction("Instrução")
        instr.triggered.connect(self.instrucao)
        sobre = menu.addAction("Sobre")
        sobre.triggered.connect(self.sobre)

        self.labelIntro = None
        self.titulo = None
        self.mensagem = None

        self.janelaPrincipal()

    def instrucao(self):
        QMessageBox.information(self.ferramentas, "Instrução", """
Olá apresento te a versão teste
e introdutória do Notificador-GC

Este script-programa serve para apresentar como se
gera notificações no menu principal..
Usando três ferramentas diferentes
e suas respectivas sintaxes..

© 2019-2021 Nurul-GC
™ ArtesGC
""")

    def sobre(self):
        QMessageBox.information(self.ferramentas, "Sobre o Programa", """
Nome: Notificador-GC
Versão: (teste)
Programador & Designer: Nurul-GC
Empresa: ArtesGC
""")

    def janelaPrincipal(self):
        janela1 = QFrame(self.ferramentas)
        janela1.move(0, 30)
        layout = QVBoxLayout()
        layout.setSpacing(10)

        labelIntro = QLabel("<h2>Gerando Notificações</h2>")
        labelIntro.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelIntro)

        layoutFormulario = QFormLayout()
        self.titulo = QLineEdit()
        self.titulo.setToolTip("OBRIGATÓRIO!")
        layoutFormulario.addRow("Insira um &Título: *", self.titulo)

        self.mensagem = QTextEdit()
        self.mensagem.setToolTip("OBRIGATÓRIO!")
        layoutFormulario.addRow("Insira uma &Mensagem: *", self.mensagem)
        layout.addLayout(layoutFormulario)

        layoutBotoes = QHBoxLayout()
        botao1 = QPushButton("(desktop-notify)")
        botao1.clicked.connect(self.desktopNotify)
        layoutBotoes.addWidget(botao1)

        botao2 = QPushButton("(py-notifier)")
        botao2.clicked.connect(self.pyNotifier)
        layoutBotoes.addWidget(botao2)

        botao3 = QPushButton("(notify2)")
        botao3.clicked.connect(self.notify2)
        layoutBotoes.addWidget(botao3)
        layout.addLayout(layoutBotoes)

        self.labelIntro = QLabel("Pressione um botão..")
        layout.addWidget(self.labelIntro)

        janela1.setLayout(layout)
        janela1.show()

    def desktopNotify(self):
        title = self.titulo.text()
        sms = self.mensagem.toPlainText()
        if (title or sms) is '':
            QMessageBox.critical(self.ferramentas, "Erro", "Defina um titulo e mensagem para a notificão..")
        else:
            self.labelIntro.setText("Botão [desktop-notify] pressionado!")
            import desktop_notify as dn

            nome_programa = dn.Server(app_name="Demo-Notificação")
            notificacao = nome_programa.Notify()

            notificacao.set_summary(f"{title}")
            notificacao.set_body(f"{sms}")
            notificacao.set_icon("notification-message-im")
            notificacao.set_timeout(5000)
            notificacao.show()

    def pyNotifier(self):
        title = self.titulo.text()
        sms = self.mensagem.toPlainText()
        if (title or sms) is '':
            QMessageBox.critical(self.ferramentas, "Erro", "Defina um titulo e mensagem para a notificão..")
        else:
            self.labelIntro.setText("Botão [py-notifier] pressionado!")
            from pynotifier import Notification

            notificacao = Notification(title=f"{title}", description=f"{sms}", duration=5,
                                       urgency=Notification.URGENCY_NORMAL, icon_path="notification-message-im")

            notificacao.send()

    def notify2(self):
        title = self.titulo.text()
        sms = self.mensagem.toPlainText()
        if (title or sms) is '':
            QMessageBox.critical(self.ferramentas, "Erro", "Defina um titulo e mensagem para a notificão..")
        else:
            self.labelIntro.setText("Botão [notify2] pressionado!")
            import notify2
            notify2.init(app_name='Teste-Notificação')

            notificao = notify2.Notification(summary=f"{title}", message=f"{sms}", icon='notification-message-im')

            notificao.set_timeout(5)
            notificao.show()


if __name__ == '__main__':
    app = TesteNotificacao()
    app.ferramentas.show()
    app.notificacao.exec_()
