import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ThreadAgua ## Questão 05: (Complete o código que realiza a
                ##              importação da biblioteca QtGui) 

##################################################

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

    def closeEvent(self, event):
        ## Questão 08: (Criar o código para encerrar o programa clicando
        ##              no ícone no canto superior direito da janela)

    def action_iniciar_producao_consumo(self):
        ## Questão 09: (Criar o código para iniciar a produção e consumo
        ##              de água chamando os métodos adequados da classe ThreadAgua) 

    def action_parar_producao_consumo(self):
        ## Questão 10: (Criar o código para terminar a produção e consumo
        ##              de água chamando os métodos adequados da classe ThreadAgua)

    def inicialize(self):
        Grid = QGridLayout()

        ## Questão 11: (Alocar todos os componentes gráficos)

        ## Questão 12: (Acrescentar na tela todos os componentes gráficos)

        ## Questão 13: (Associar ao botão Bt_iniciar um evento para
        ##              chamar o método que inicia a produção e consumo de água)

        ## Questão 14: (Associar ao botão Bt_terminar um evento para
        ##              chamar o método que encerra a produção e consumo de água)

        self.setLayout(Grid)
        self.show()

##################################################
