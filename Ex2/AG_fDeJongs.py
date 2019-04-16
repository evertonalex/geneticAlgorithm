from random import *
# Este AG resolve a funciton de Jong's
# f1(x)sum(x(i)^s)
# i = 1:n
# -5.12<=(i)<=5.12
# Function a ser maximizada -> f(x)=x^2
from random import random

TAMANHOCROMOSSOMO = 15
TAMANHOPOPULACAO = 5

class Individuo():
    def __init__(self, cromossomo, geracao = 0):
        self.cromossomo = cromossomo
        self.geracao = geracao




class AG():
    def __init__(self):
        self.populacao = []

    def inicializaPopulacao(self):
        for i in range(TAMANHOPOPULACAO):
            numeroRand = randint(0,99)
            numeroRandBin = bin(numeroRand)[2:].zfill(15)
            self.populacao[i].append(Individuo(numeroRandBin))
            print("numRand -> ", numeroRand)
            # print("cromossomo -> ", self.populacao[i].cromossomo)

    def run(self):
        # self.populacao.append()
        self.inicializaPopulacao()




if __name__ == '__main__':
    ag = AG()
    ag.run()

















