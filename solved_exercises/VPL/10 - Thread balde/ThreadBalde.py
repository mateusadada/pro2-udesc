import threading
import time

##################################################

class ThreadBalde:
    __Total = None
    __LEd = None
    __PBar = None
    __Thr = None

    ## Questão 01:  (Criar o construtor da classe ThreadBalde
    ##               conforme diagrama da Figura 01)
    def __init__(self, LEd_a, PBar_a):
        self.__LEd = LEd_a
        self.__PBar = PBar_a

    def iniciar(self, Total_a):
        ## Questão 02:  (Criar o método que inicia a ThreadBalde)
        try:
            self.__Total = Total_a
            self.__Thr = threading.Thread(target=self.run)
            self.__Thr.start()
        except:
            pass

    def parar(self):
        ## Questão 03:  (Criar o método que encerra a ThreadBalde)
        try:
            self.__Total = 0;
            self.__Thr = None;
        except:
            pass

    def isRunning(self):
        ## Questão 04:  (Criar o método isRunning)
        return True if self.__Thr else False

    def run(self):
        ## Questão 05:  (Criar o método que realize a ThreadBalde)
        self.__LEd.setText("Tchaise")

##################################################
