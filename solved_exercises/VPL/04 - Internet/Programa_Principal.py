import sys
from PyQt5.QtWidgets import *
from Janela import Janela

##################################################

App=QApplication(sys.argv)
Jan1=Janela("Preço de internet banda larga em diversas provedoras")
App.exec_()

##################################################
