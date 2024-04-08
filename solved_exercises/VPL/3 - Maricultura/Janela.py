import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class Janela(QWidget): # (Complete o código que declara a classe Janela)
    __Lb_TituloRegiao=None
    __Lb_TituloPeixe=None
    __Lb_TituloCamarao=None
    __Lb_TotalProd=None

    __Lb_Regiao=[]
    __LEd_Peixe=[]
    __LEd_Camarao=[]
    __LEd_TotalProd=[]

    __LEd_MaiorRegiao=None
    __Bt_Calc=None

    # Questão 02: (Criar o construtor da classe)
    def __init__(self, Str="Janela", px=0, py=0, dx=640, dy=480, cor="orange"):
        super().__init__()
        super().setWindowTitle(Str)
        self.setGeometry(px, py, dx, dy)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def total_producao(self):
        # Questão 03: (Criar o evento que calcula o total da produção por região)
        pass
    
    def maior_regiao(self):
        # Questão 04: (Criar o evento que identifica a região onde há maior produção)
        pass
    
    def closeEvent(self, event):
        # Questão 05: (Qual o comando que encerra o programa no canto da tela?)
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    def action_Bt_Calc(self):
        # Questão 06: (Chamar os eventos que fazem os cálculos citados nas Questões 03 e 04)
        pass

    def inicialize(self):
        Grid=QGridLayout()

        regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
        peixes = [''] * 5
        camarao = [''] * 5
        total_prod = [''] * 5

        # Alocar os componentes gráficos
        self.__Lb_TituloRegiao=QLabel(self, text="Região")
        self.__Lb_TituloPeixe=QLabel(self, text="Peixe")
        self.__Lb_TituloCamarao=QLabel(self, text="Camarão")
        self.__Lb_TotalProd=QLabel(self, text="Total da Prod.")
        
        self.__LEd_MaiorRegiao=QLineEdit(self)
        
        # Pintar os componentes gráficos com Palette
        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)        
        
        # Adicionar os LEd
        for i, peixes in enumerate(peixes):
            led_peixes = QLineEdit(self, width=18)
            led_peixes.setAutoFillBackground(True)
            led_peixes.setPalette(p1)
            Grid.addWidget(led_peixes, i + 1, 1)
            
        for i, camarao in enumerate(camarao):
            led_camarao = QLineEdit(self, width=18)
            led_camarao.setAutoFillBackground(True)
            led_camarao.setPalette(p1)
            Grid.addWidget(led_camarao, i + 1, 2)
            
        for i, total_prod in enumerate(total_prod):
            led_total_prod = QLineEdit(self, width=18)
            led_total_prod.setAutoFillBackground(True)
            led_total_prod.setPalette(p1)
            Grid.addWidget(led_total_prod, i + 1, 3)
        
        # Adicionar o nome das regiões
        for i, regiao in enumerate(regioes):
            label_regiao = QLabel(self, text=regiao)
            label_regiao.setAutoFillBackground(True)
            label_regiao.setPalette(p1)
            Grid.addWidget(label_regiao, i + 1, 0)
        
        self.__Lb_TituloRegiao.setAutoFillBackground(True)
        self.__Lb_TituloRegiao.setPalette(p1)
        
        self.__Lb_TituloPeixe.setAutoFillBackground(True)
        self.__Lb_TituloPeixe.setPalette(p1)
        
        self.__Lb_TituloCamarao.setAutoFillBackground(True)
        self.__Lb_TituloCamarao.setPalette(p1)
        
        self.__Lb_TotalProd.setAutoFillBackground(True)
        self.__Lb_TotalProd.setPalette(p1)


        # Associar o botão Bt_Calc ao evento da questão 06
        self.__Bt_Calc = QPushButton('Calcular', self)
        self.__Bt_Calc.clicked.connect(self.action_Bt_Calc)

        # Acrescentar na tela os componentes gráficos
        Grid.addWidget(self.__Lb_TituloRegiao, 0, 0)
        Grid.addWidget(self.__Lb_TituloPeixe, 0, 1)
        Grid.addWidget(self.__Lb_TituloCamarao, 0, 2)
        Grid.addWidget(self.__Lb_TotalProd, 0, 3)

        Grid.addWidget(self.__Bt_Calc, len(regioes) + 1, 1)
        Grid.addWidget(self.__LEd_MaiorRegiao, len(regioes) + 1, 2)

        self.setLayout(Grid)
        self.show()

##################################################
