#!/usr/bin/env python2.7

"""OOP WTPC2016 dia 2.
 """

__author__      = "Humberto Celleri"

import radar
import medio
import blanco
import generador
import datetime
import detector
import matplotlib.pyplot as plt


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)
    # print tiempo_inicial,"\n"
    # CONSULTA!: Como mide datetime? en segundos?

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi


    # Pedimos a generador que genere una senar
    Un_generador = generador.Generador(amplitud,fase,frecuencia)
    Una_senal = Un_generador.generar(tiempo_inicial,tiempo_final)
    # print Una_senal
    # Plot tthe signal
    fig = plt.figure()
    plt.plot(Una_senal)
    plt.grid(True)
    plt.show()
    
    #TODO construir un detector

    #TODO construir un nuevo radar


    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #TODO contruir un nuevo blanco


    #TODO contruir un medio

    #TODO construir un radar

if __name__ == "__main__":
    main()
