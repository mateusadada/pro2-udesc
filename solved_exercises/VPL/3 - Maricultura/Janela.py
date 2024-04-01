import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class Janela( Questão 01 ): ## (Complete o código que declara a classe Janela)
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

    ## Questão 02:  (Criar o construtor da classe)

    def total_producao(self):
        ## Questão 03:  (Criar o evento que calcula o total da
        ##               produção por região)

    def maior_regiao(self):
        ## Questão 04:  (Criar o evento que identifica a região
        ##               onde há maior produção)

    def closeEvent(self, event):
        ## Questão 05:  (Qual o comando que encerra o programa
        ##               no canto da tela?)

    def action_Bt_Calc(self):
        ## Questão 06:  (Chamar os eventos que fazem os cálculos
        ##               citados nas Questões 03 e 04)

    def inicialize(self):
        Grid=QGridLayout()

        ## Questão 07:  (Alocar os componentes gráficos)

        ## Questão 08:  (Pintar os componentes gráficos com Palette)
        
        ## Questão 09:  (Associar o botão Bt_Calc ao evento da questão 06)

        ## Questão 10:  (Acrescentar na tela os componentes gráficos)

        self.setLayout(Grid)
        self.show()

##################################################
