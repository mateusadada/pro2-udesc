import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui ## Questão 06:  (Complete o código que realiza a
                 ##               importação da biblioteca QtGui)
from ThreadBalde import ThreadBalde

##################################################

class Janela( Questão 07 ): ## (Complete o código que declara a classe Janela)
    __LEd1 = None
    __PBar=None
    __Bt1 = None
    __MeuBalde=None

    ## Questão 08:  (Criar o construtor da classe Janela)

    def closeEvent(self, event):
        ## Questão 09:  (Criar o código para encerrar o programa clicando
        ##               no ícone do canto superior direito da janela)

    def action_executar(self):
        ## Questão 10:  (Criar o código para iniciar a Thread chamando
        ##               os métodos adequados da classe ThreadBalde)

    def inicialize(self):
        Grid = QGridLayout()

        ## Questão 11:  (Alocar todos os componentes gráficos)

        ## Questão 12:  (Associar o botão Bt1 ao evento que inicia e para a Thread)

        ## Questão 13:  (Acrescentar na tela todos os componentes gráficos)

        self.setLayout(Grid)
        self.show()

##################################################
