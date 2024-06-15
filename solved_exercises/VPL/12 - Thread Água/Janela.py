import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
## Questão 05: (Complete o código que realiza a importação da biblioteca QtGui)
from ThreadAgua import ThreadAgua

class Janela(QWidget):
    __Lb1 = None
    __Lb2 = None
    __LEd1 = None
    __LEd2 = None
    __Bt_iniciar = None
    __Bt_terminar = None
    __Produzir = None
    __Consumir = None

    ## Questão 07: (Criar o construtor da classe Janela)
    def __init__(self, Str="Janela", cor="orange"):
        super().__init__()
        
        self.setWindowTitle(Str)
        self.setGeometry(400, 200, 380, 180)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        ## Questão 08: (Criar o código para encerrar o programa clicando
        ##              no ícone no canto superior direito da janela)
        self.destroy()
        sys.exit(0)

    def action_iniciar_producao_consumo(self):
        ## Questão 09: (Criar o código para iniciar a produção e consumo
        ##              de água chamando os métodos adequados da classe ThreadAgua) 
        self.__Produzir.iniciar()
        self.__Consumir.iniciar()

    def action_parar_producao_consumo(self):
        ## Questão 10: (Criar o código para terminar a produção e consumo
        ##              de água chamando os métodos adequados da classe ThreadAgua)
        self.__Produzir.iniciar()
        self.__Consumir.iniciar()

    def inicialize(self):
        Grid = QGridLayout()

        ## Questão 11: (Alocar todos os componentes gráficos)
        self.__Lb1 = QLabel('Produção:')
        self.__Lb2 = QLabel('Consumo:')

        self.__LEd1 = QLineEdit()
        self.__LEd2 = QLineEdit()

        self.__Bt_iniciar = QPushButton('Iniciar')
        self.__Bt_terminar = QPushButton('Terminar')

        ## Questão 12: (Acrescentar na tela todos os componentes gráficos)
        Grid.addWidget(self.__Lb1, 0, 0)
        Grid.addWidget(self.__Lb2, 1, 0)
        Grid.addWidget(self.__LEd1, 0, 1, 1, 2)
        Grid.addWidget(self.__LEd2, 1, 1, 1, 2)
        Grid.addWidget(self.__Bt_iniciar, 2, 1, 1, 1)
        Grid.addWidget(self.__Bt_terminar, 2, 2, 1, 1)

        ## Questão 13: (Associar ao botão Bt_iniciar um evento para
        ##              chamar o método que inicia a produção e consumo de água)
        self.__Bt_iniciar.clicked.connect(self.action_iniciar_producao_consumo)

        ## Questão 14: (Associar ao botão Bt_terminar um evento para
        ##              chamar o método que encerra a produção e consumo de água)
        self.__Bt_terminar.clicked.connect(self.action_parar_producao_consumo)

        self.__Produzir = ThreadAgua(self.__LEd1, 2, False)
        self.__Consumir = ThreadAgua(self.__LEd2, 1, True)

        self.setLayout(Grid)
        self.show()
