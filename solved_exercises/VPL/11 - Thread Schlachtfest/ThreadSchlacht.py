import random
import threading
import time

class ThreadSchlacht:
    __Total=None
    __LEd=None
    __Thr=None

    ## Questão 01: (Criar o construtor da classe ThreadSchlacht
    ##               conforme diagrama da Figura 01)
    def __init__(self, LEd_a):
        self.__LEd = LEd_a

    def iniciar(self, Total_a):
        ## Questão 02: (Criar o método que inicia a ThreadSchlacht)
        try:
            if (self.__Thr is None):
                self.__Total = Total_a
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print('Error: unable to start thread')
        
    def parar(self):
        ## Questão 03: (Criar o método que encerra a ThreadSchlacht)
        try:
            self.__Total = 0
            self.__Thr = None
        except Exception as ex:
            print('Error: unable to stop thread')

    def run(self):
        ## Questão 04: (Criar o método que realiza a ThreadSchlacht)
        ii = 0
        while ii < self.__Total:
            ii += 1
            self.__LEd.setText("%d" % ii)
            tempo = random.random()
            time.sleep(tempo)
