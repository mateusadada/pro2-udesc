import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class Janela( Questão 01 ): ## Questão 01: (Complete o código que declara a classe)
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

    ## Questão 02: (Criar o construtor da classe Janela)

    def closeEvent(self, event):
        ## Questão 03: (Qual o código necessário para encerrar o programa no canto
        ##             superior direito da janela)

    def action_Bt_adic(self):
        ## Questão 04: (Criar o evento que calcula a adição dos valores numéricos)

    def action_Bt_sub(self):
        ## Questão 05: (Criar o evento que calcula a subtração dos valores numéricos)

    def action_Bt_mult(self):
        ## Questão 06: (Criar o evento que calcula a multiplicação dos valores numéricos)

    def action_Bt_div(self):
        ## Questão 07: (Criar o evento que calcula a divisão dos valores numéricos)

    def inicialize(self):
        Grid=QGridLayout()
        
        ## Questão 08: Realize a alocação dos componentes gráficos)
        
        self.__Bt_adic=QPushButton(self, text='Adicionar')
        ## Questão 09: (Conectar o botão Bt_adic ao evento que realiza
        ##              a adição dos valores numéricos)
        
        self.__Bt_sub = QPushButton(self, text='Subtrair')
        ## Questão 10: (Conectar o botão Bt_sub ao evento que realiza
        ##              a subtração dos valores numéricos)
        
        self.__Bt_mult = QPushButton(self, text='Multiplicar')
        ## Questão 11: (Conectar o botão Bt_mult ao evento que realiza
        ##              a multiplicação dos valores numéricos)
        
        self.__Bt_div = QPushButton(self, text='Dividir')
        ## Questão 12: (Conectar o botão Bt_div ao evento que realiza
        ##              a divisão dos valores numéricos)
        
        ############# Grid #############
        ## Questão 13: (Acrescentar os componentes gráficos na Tela) 
        
        self.setLayout(Grid)
        self.show()

##################################################
