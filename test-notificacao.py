from PyQt5.Qt import *
from sys import argv


class TesteNotificacao:
    def __init__(self):
        self.notificacao = QApplication(argv)
        self.ferramentas = QWidget()

    def janelaPrincipal(self):
        janela1 = QFrame(self.ferramentas)
        janela1.move(0, 30)
        layout = QVBoxLayout()
        layout.setSpacing(10)

        labelIntro = QLabel("<h2>Gerando Notificações</h2>")
        labelIntro.setAlignment(Qt.AlignCenter)
        layout.addWidget(labelIntro)

        layoutBotoes = QHBoxLayout()
