import threading
import time

class ThreadAgua:
    __Prod_Seg=None
    __LEd=None
    __Sair=None
    __Thr = None

    ## Questão 01: (Criar o construtor da classe ThreadAgua)
    def __init__(self, LEd_a, prod, sair):
        self.__LEd = LEd_a
        self.__Prod_Seg = prod
        self.__Sair = sair

    def iniciar(self):
        ## Questão 02: (Criar o método que inicia a ThreadAgua)
        self.__Thr = threading.Thread(target=self.run)
        self.__Thr.start()

    def parar(self):
        ## Questão 03: (Criar o método que encerra a ThreadAgua)
        self.__Thr = None

    def run(self):
        ## Questão 04: (Criar o método que realize a ThreadAgua)
        i = 0
        while True:
            i += 1
            if self.__Sair:
                valor = i
            else:
                valor = 2 * i
            self.__LEd.setText("%d" % valor)
            time.sleep(1)
