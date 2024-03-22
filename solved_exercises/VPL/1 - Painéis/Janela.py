import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

########################################################

class Janela(QWidget): ## (Complete o código que declara a classe Janela)
    __Lb_Nome = None
    __Lb_Telefone = None    
    __Lb_Email = None
    __Lb_Endereco = None
    __LEd_Nome = None
    __LEd_Telefone = None
    __LEd_Email = None
    __LEd_Endereco = None

    ## Questão 02: (Criar o construtor da classe)
    def __init__(self, Str="Janela", px=0, py=0, dx=640, dy=480, cor="orange"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(px, py, dx, dy)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        ## Questão 03: (Qual o comando que encerra o programa no canto da tela?)
        sys.exit(0)

    def inicialize(self):
        Grid=QGridLayout()
        
        ## Questão 04: (Alocar os componentes gráficos)
        self.__Lb_Nome=QLabel(self, text="Nome:")
        self.__Lb_Telefone=QLabel(self, text="Telefone:")
        self.__Lb_Email=QLabel(self, text="Email:")
        self.__Lb_Endereco=QLabel(self, text="Endereço:")

        ## Questão 05: (Pintar os componentes gráficos com Palette)
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        self.__Lb_Nome.setAutoFillBackground(True)
        self.__Lb_Nome.setPalette(p1)

        self.__Lb_Telefone.setAutoFillBackground(True)
        self.__Lb_Telefone.setPalette(p1)

        self.__Lb_Email.setAutoFillBackground(True)
        self.__Lb_Email.setPalette(p1)

        self.__Lb_Endereco.setAutoFillBackground(True)
        self.__Lb_Endereco.setPalette(p1)

        self.__LEd_Nome=QLineEdit(self, width=52)
        self.__LEd_Telefone=QLineEdit(self, width=52)
        self.__LEd_Email=QLineEdit(self, width=52)
        self.__LEd_Endereco=QLineEdit(self, width=52)

        ## Questão 06: (Acrescentar na tela os componentes gráficos)

        Grid.addWidget(self.__Lb_Nome, 0, 0)
        Grid.addWidget(self.__Lb_Telefone, 1, 0)
        Grid.addWidget(self.__Lb_Email, 2, 0)
        Grid.addWidget(self.__Lb_Endereco, 3, 0)

        Grid.addWidget(self.__LEd_Nome, 0, 1)
        Grid.addWidget(self.__LEd_Telefone, 1, 1)
        Grid.addWidget(self.__LEd_Email, 2, 1)
        Grid.addWidget(self.__LEd_Endereco, 3, 1)

        self.setLayout(Grid)
        self.show()

########################################################
