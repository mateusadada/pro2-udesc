import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class Janela(QWidget): # Questão 01: (Complete o código que declara a classe)
    __Lb_valor1=None
    __Lb_valor2=None
    __Lb_result=None
    __LEd_valor1=None
    __LEd_valor2=None
    __LEd_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None

    # Questão 02: (Criar o construtor da classe Janela)
    def __init__(self, Str="Janela", px=0, py=0, dx=640, dy=480, cor="orange"):
        super().__init__()
        super().setWindowTitle(Str)
        self.setGeometry(px, py, dx, dy)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        # Questão 03: (Qual o código necessário para encerrar o programa no canto superior direito da janela)
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    def action_Bt_adic(self):
        # Questão 04: (Criar o evento que calcula a adição dos valores numéricos)
        try:
            n1=float(self.__LEd_valor1.text().replace(',', '.'))
            n2=float(self.__LEd_valor2.text().replace(',', '.'))
            total= n1 + n2
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numéricos")

    def action_Bt_sub(self):
        # Questão 05: (Criar o evento que calcula a subtração dos valores numéricos)
        try:
            n1=float(self.__LEd_valor1.text().replace(',', '.'))
            n2=float(self.__LEd_valor2.text().replace(',', '.'))
            total= n1 - n2
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numéricos")
        
    def action_Bt_mult(self):
        # Questão 06: (Criar o evento que calcula a multiplicação dos valores numéricos)
        try:
            n1=float(self.__LEd_valor1.text().replace(',', '.'))
            n2=float(self.__LEd_valor2.text().replace(',', '.'))
            total= n1 * n2
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numéricos")

    def action_Bt_div(self):
        # Questão 07: (Criar o evento que calcula a divisão dos valores numéricos)
        try:
            n1=float(self.__LEd_valor1.text().replace(',', '.'))
            n2=float(self.__LEd_valor2.text().replace(',', '.'))
            total= n1 / n2
            self.__LEd_result.setText("%04.2f" % total)
        except ValueError as ve:
            QMessageBox.critical(None, "Janela de Erro #1", "Voce deve digitar valores numéricos")

    def inicialize(self):
        Grid=QGridLayout()
        
        # Questão 08: Realize a alocação dos componentes gráficos)
        self.__Lb_valor1=QLabel(self, text="Valor1:")
        self.__Lb_valor2=QLabel(self, text="Valor2:")
        self.__Lb_result=QLabel(self, text="Resultado:")
        
        self.__LEd_valor1=QLineEdit(self, width=52)
        self.__LEd_valor2=QLineEdit(self, width=52)
        self.__LEd_result=QLineEdit(self, width=52)
        
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)
        
        self.__Lb_valor1.setAutoFillBackground(True)
        self.__Lb_valor1.setPalette(p1)

        self.__Lb_valor2.setAutoFillBackground(True)
        self.__Lb_valor2.setPalette(p1)

        self.__Lb_result.setAutoFillBackground(True)
        self.__Lb_result.setPalette(p1)
        
        self.__Bt_adic=QPushButton(self, text='Adic')
        # Questão 09: (Conectar o botão Bt_adic ao evento que realiza a adição dos valores numéricos)
        self.__Bt_adic.clicked.connect(self.action_Bt_adic)
        
        self.__Bt_sub = QPushButton(self, text='Sub')
        # Questão 10: (Conectar o botão Bt_sub ao evento que realiza a subtração dos valores numéricos)
        self.__Bt_sub.clicked.connect(self.action_Bt_sub)
        
        self.__Bt_mult = QPushButton(self, text='Mult')
        # Questão 11: (Conectar o botão Bt_mult ao evento que realiza a multiplicação dos valores numéricos)
        self.__Bt_mult.clicked.connect(self.action_Bt_mult)
        
        self.__Bt_div = QPushButton(self, text='Div')
        # Questão 12: (Conectar o botão Bt_div ao evento que realiza a divisão dos valores numéricos)
        self.__Bt_div.clicked.connect(self.action_Bt_div)
        
        ############# Grid #############
        # Questão 13: (Acrescentar os componentes gráficos na Tela)
        Grid.addWidget(self.__Lb_valor1, 0, 0)
        Grid.addWidget(self.__Lb_valor2, 1, 0)
        Grid.addWidget(self.__Lb_result, 3, 0)

        Grid.addWidget(self.__LEd_valor1, 0, 1, 1, 4)
        Grid.addWidget(self.__LEd_valor2, 1, 1, 1, 4)
        Grid.addWidget(self.__LEd_result, 3, 1, 1, 4)
        
        Grid.addWidget(self.__Bt_adic, 2, 1)
        Grid.addWidget(self.__Bt_sub, 2, 2)
        Grid.addWidget(self.__Bt_mult, 2, 3)
        Grid.addWidget(self.__Bt_div, 2, 4)
        
        self.setLayout(Grid)
        self.show()

##################################################
