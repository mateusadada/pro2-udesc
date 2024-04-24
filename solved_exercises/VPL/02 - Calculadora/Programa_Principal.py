import sys
from PyQt5.QtWidgets import *
from Janela import Janela

# Questão 14: (Crie o programa principal)
App=QApplication(sys.argv)
Jan1=Janela("Minha Calculadora")
App.exec_()
