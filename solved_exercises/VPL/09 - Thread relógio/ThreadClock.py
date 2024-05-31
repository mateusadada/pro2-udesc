import datetime
import threading
import time

class ThreadClock:
    __Total = None
    __LEd = None
    __Thr = None

    ## Questão 01:  (Criar o construtor da classe ThreadClock
    ##               conforme diagrama da Figura 01)
    def __init__(self, LEd):
        self.__LEd = LEd

    def iniciar(self, Total_a):
        ## Questão 02:  (Criar o método que inicia a ThreadClock)
        try:
            self.__Total = Total_a
            self.__Thr = threading.Thread(target=self.run)
            self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s\n" % (ex))

    def parar(self):
        ## Questão 03:  (Criar o método que encerra a ThreadClock)
        try:
            
            self.__Total = 0;
            self.__Thr = None
        except:
            print("Error: unable to start thread: %s\n" % (ex))

    def isRunning(self):
        ## Questão 04:  (Criar o método isRunning)
        return self.__Thr.is_alive() if self.__Thr else False

    def run(self):
        ## Questão 05:  (Criar o método que realiza a ThreadClock)
        count = 0
        while count < self.__Total:
            count += 1
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S")
            self.__LEd.setText(time_str)
            time.sleep(1)
        self.__Thr = None
