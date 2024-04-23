import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui ## Questão 05:  (Complete o código que realiza a
                 ##               importação da biblioteca QtGui)
from ThreadSchlacht import ThreadSchlacht

##################################################

class Janela( Questão 06 ):  ## (Complete o código que declara a classe Janela)
    __LEd1=None
    __LEd2 = None
    __LEd3 = None
    __Bt_Abertura=None
    __Bt_Fechamento=None
    __Barraca1 = None
    __Barraca2 = None
    __Barraca3 = None

    ## Questão 07:  (Criar o construtor da classe Janela)

    def closeEvent(self, event):
        ## Questão 08:  (Criar o código para encerrar o programa clicando
        ##               no ícone do canto superior direito da janela)

    def action_abertura(self):
        ## Questão 09:  (Criar o código para iniciar a Thread chamando
        ##               o método adequado da classe ThreadSchlacht)

    def action_fechamento(self):
        ## Questão 10:  (Criar o código para encerrar a Thread chamando
        ##               o método adequado da classe ThreadSchlacht)

    def inicialize(self):
        Grid = QGridLayout()

        ## Questão 11:  (Alocar todos os componentes gráficos)

        ## Questão 12:  (Associar o botão Bt_Abertura ao evento
        ##               que inicia a Thread)

        ## Questão 13:  (Associar o botão Bt_Fechamento ao evento
        ##               que encerra a Thread)

        ## Questão 14:  (Acrescentar na tela todos os componentes gráficos)

        self.setLayout(Grid)
        self.show()

##################################################
