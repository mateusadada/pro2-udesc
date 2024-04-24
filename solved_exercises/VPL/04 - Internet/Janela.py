import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Janela(QWidget):
    __Lb_cabNome=None
    __Lb_cabPreco=None
    __Lb_cabMens=None
    __Lb_cabTotal=None

    __Lb_nome=[]
    __LEd_preco=[]
    __LEd_mens=[]
    __LEd_total=[]

    __LEd_prov=None
    __Bt_calc=None

    def __init__(self, Str="Janela"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(400, 200, 456, 200)

        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(), QColor("orange"))
        self.setPalette(p)

        self.inicialize()

    def calcula_total(self):
        for i, tot in enumerate(self.__LEd_total):
            try:
                tot.setText("%7.2f" % (float(self.__LEd_preco[i].text()) + (float(self.__LEd_mens[i].text()) * 12)))
            except:
                pass
    
    def acha_menor(self):
        try:
            sm_index = 9999999
            sm_tot = 9999999
            for i, tot in enumerate(self.__LEd_total):
                try:
                    if float(self.__LEd_total[i].text()) < sm_tot:
                        sm_tot = float(self.__LEd_total[i].text());
                        sm_index = i
                except:
                    pass
            self.__LEd_prov.setText(self.__Lb_nome[sm_index].text())
        except:
            pass

    def closeEvent(self, event):
        print("Destruindo janela...")
        self.destroy()
        sys.exit(0)

    def action_Bt_Calc(self):
        self.calcula_total()
        self.acha_menor()
        pass

    def inicialize(self):
        Grid=QGridLayout()

        self.__Lb_cabNome= QLabel(self, text="Provedora")
        self.__Lb_cabPreco= QLabel(self, text="Instalação")
        self.__Lb_cabMens= QLabel(self, text="Mensalidade")
        self.__Lb_cabTotal= QLabel(self, text="Total/Ano")

        self.__Lb_nome = [
            QLabel(self, text="Claro"),
            QLabel(self, text="Vivo"),
            QLabel(self, text="Oi"),
            QLabel(self, text="Net"),
            QLabel(self, text="Gvt"),
            QLabel(self, text="Tim")
            ]

        self.__LEd_preco = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self)
            ]

        self.__LEd_mens = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self)
            ]

        self.__LEd_total = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self)
            ]

        self.__Bt_calc=QPushButton(self, text='Calcular')
        self.__Bt_calc.clicked.connect(self.action_Bt_Calc)

        self.__LEd_prov=QLineEdit(self)

        p1 = self.palette()
        p1.setColor(self.backgroundRole(), Qt.yellow)

        self.__Lb_cabNome.setAutoFillBackground(True)
        self.__Lb_cabNome.setPalette(p1)

        self.__Lb_cabPreco.setAutoFillBackground(True)
        self.__Lb_cabPreco.setPalette(p1)

        self.__Lb_cabMens.setAutoFillBackground(True)
        self.__Lb_cabMens.setPalette(p1)

        self.__Lb_cabTotal.setAutoFillBackground(True)
        self.__Lb_cabTotal.setPalette(p1)

        try:
            for i in range(len(self.__Lb_nome)):
                self.__Lb_nome[i].setAutoFillBackground(True)
                self.__Lb_nome[i].setPalette(p1)
        except:
            pass

        Grid.addWidget(self.__Lb_cabNome, 0, 0, 1, 1)
        Grid.addWidget(self.__Lb_cabPreco, 0, 1, 1, 1)
        Grid.addWidget(self.__Lb_cabMens, 0, 2, 1, 1)
        Grid.addWidget(self.__Lb_cabTotal, 0, 3, 1, 1)

        try:

            for i, reg in enumerate(self.__Lb_nome):
                Grid.addWidget(self.__Lb_nome[i], i + 1, 0, 1, 1)
                
            for i, reg in enumerate(self.__LEd_preco):
                Grid.addWidget(self.__LEd_preco[i], i + 1, 1, 1, 1)
                
            for i, reg in enumerate(self.__LEd_mens):
                Grid.addWidget(self.__LEd_mens[i], i + 1, 2, 1, 1)
                
            for i, reg in enumerate(self.__LEd_total):
                Grid.addWidget(self.__LEd_total[i], i + 1, 3, 1, 1)

        except IndexError:
            pass

        Grid.addWidget(self.__Bt_calc, 7,1 ,1 ,1)
        Grid.addWidget(self.__LEd_prov, 7,2 ,1 ,1)

        self.setLayout(Grid)
        self.show()
