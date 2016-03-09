"""
Un generador de senal es el responsable de generar una senal portadora.

"""
from numpy import random

class Generador(object):
    """
    Class that generates a noisy signal

    """

    def __init__(self, amplitud, fase, frecuencia, amplitud_ruido = 1):
        """
        Constructor comment
        """
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia
        self.amplitud_ruido = amplitud_ruido

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(int(cantidad_muestras))

        Un_ruido = self.__ruido(muestras)

        #functional for:
        ret = [Un_ruido[i] + self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]

        return ret

    def __ruido(self,muestras):
        # The noise is a factor of the signal
        #
        ret = [random.random()*self.amplitud_ruido for i in muestras]
        # ATENTION: For sentence in Python moves in LISTS!! NOT NUMBER! You have to use range()
        return ret
