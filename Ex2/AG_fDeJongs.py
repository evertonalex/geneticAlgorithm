from math import *
# Este AG resolve a funciton de Jong's
# f1(x)sum(x(i)^s)
# i = 1:n
# -5.12<=(i)<=5.12
# Function a ser maximizada -> f(x)=x^2
import random
import numpy as np
import struct

from numba.cuda.tests.cudapy.test_blackscholes import randfloat

TAMANHOCROMOSSOMO = 15
TAMANHOPOPULACAO = 1
PONTOCORTE=5

class Individuo():
    def __init__(self, cromossomo, geracao = 0):
        self.cromossomo = cromossomo
        self.geracao = geracao
        self.notaFitness = 0

    def fitness(self):
        # cromossomoInt = int(self.cromossomo,2)

        cromossoPicado = []
        cromossoPicado.append(self.cromossomo[0:PONTOCORTE])
        cromossoPicado.append(self.cromossomo[PONTOCORTE:PONTOCORTE+5])
        cromossoPicado.append(self.cromossomo[PONTOCORTE+PONTOCORTE::])

        for i in range(len(cromossoPicado)):
            print("parte %s -> %s " % (i, cromossoPicado[i]))

        x1 = 1+(int(cromossoPicado[0],2))*(2-(-2))/(2**6-1)
        x2 = 1+(int(cromossoPicado[1],2))*(2-(-2))/(2**6-1)
        x3 = 1+(int(cromossoPicado[2],2))*(2-(-2))/(2**6-1)
        print(x1)
        print(x2)
        print(x3)

        self.notaFitness = x1 **2 + x2 **2 + x3 **2
        print("Nota fitness ", self.notaFitness)


class AG():
    def __init__(self):
        self.populacao = []

    def inicializaPopulacao(self):
        for i in range(TAMANHOPOPULACAO):
            cromossomo = ""
            for k in range(TAMANHOCROMOSSOMO):
                cromossomo += str(random.randint(0,1))
            self.populacao.append(Individuo(cromossomo))
            print("cromossomo gerado ", self.populacao[i].cromossomo)








            # # numeroRand = randint(0, 99)
            # # print(random.randrange(1, 5))
            # numeroRand = round(random.uniform(-5.12, 5.12),14)
            # print(numeroRand)
            # # numeroRandBin = bin(struct.unpack('!i',struct.pack('!f',numeroRand))[0])
            # numeroRandBin = format(struct.unpack('!I', struct.pack('!f', numeroRand))[0], '015b')
            # print("NUM GERADO --> ", numeroRand)
            # print("NUM gerado to BIN --> ", numeroRandBin)
            # print("NUM BIN TO FLOAT --> ", struct.unpack('!f',struct.pack('!I', int(numeroRandBin, 2)))[0])
            # # numeroRandBin = bin(numeroRand)[2:].zfill(15)
            # # print("iiii -> ", i)
            # # print("numRand -> ", numeroRand)
            # # print("numRand -> ", numeroRandBin)
            # self.populacao.append(Individuo(numeroRandBin))
            # print("cromossomo -> ", self.populacao[i].cromossomo)

    def run(self):
        # self.populacao.append()
        self.inicializaPopulacao()
        for i in range(len(self.populacao)):
            self.populacao[i].fitness()




if __name__ == '__main__':
    ag = AG()
    ag.run()

















