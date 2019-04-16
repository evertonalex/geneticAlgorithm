# Este AG resolve a funciton de Jong's
# f1(x)sum(x(i)^s)
# i = 1:n
# -5.12<=(i)<=5.12
# Function a ser maximizada -> f(x)=x^2
from random import random

POPULACAO = []
POPULACAO.append("001100")
POPULACAO.append("010101")
POPULACAO.append("111000")
POPULACAO.append("000111")
POPULACAO.append("101011")
POPULACAO.append("101000")


taxaMutacao = 5

class Individuo():
    def __init__(self, cromossomo, geracao = 0):
        self.cromossomo = cromossomo
        self.notaFitness = 0
        self.geracao = geracao

    def fitness(self):
        self.notaFitness = int(self.cromossomo, 2)  # converteBinarioToINT

    def crossover(self, individuoCrusamento):
        # corte = len(self.cromossomo)/2
        corte = 3

        print("CORTE %s" % (corte))

        filho1 = individuoCrusamento.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + individuoCrusamento.cromossomo[corte::]

        filhos = [
            Individuo(self.cromossomo, self.geracao + 1),
            Individuo(self.cromossomo, self.geracao + 1)
        ]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        print("filho 1 %s -> filho 2 %s " % (filhos[0].cromossomo, filhos[1].cromossomo))

        return filhos

    def mutacao(self, taxaMutacao):
        print("before mutacao - %s" % (self.cromossomo))
        for i in range(len(self.cromossomo)):
            if random() < taxaMutacao:
                # print("cromossomo %s -> %s " % (i, self.cromossomo[i]))
                if self.cromossomo == 1:
                    self.cromossomo[i] = 0
                # else:
                    # self.cromossomo[i] = 1
        print("after mutacao - %s " % (self.cromossomo))
        return self


class AG():
    def __init__(self):
        self.populacao = []

    def inicializaPopulacao(self, POPULACAO):
        for i in range(len(POPULACAO)):
            self.populacao.append(Individuo(POPULACAO[i]))
        # return self.populacao


    def printPopulacao(self):
        print("**** POPULACAO INICIAL ****")
        for k in range(len(self.populacao)):
            print("Individuo %s -> %s -> fitness %s" % (k, self.populacao[k].cromossomo, self.populacao[k].notaFitness))
        print("**** POPULACAO INICIAL ****")

    def ordenaPopulacao(self):
        self.populacao = sorted(self.populacao, key=lambda populacao: populacao.notaFitness, reverse=True)

    def selecionaPai(self): #selecionaPorTorneio
        return [0,1] #maioresValhores

    def resolver(self):
        self.inicializaPopulacao(POPULACAO)
        for i in range(len(self.populacao)):
            self.populacao[i].fitness()
        self.printPopulacao()
        self.ordenaPopulacao()
        self.printPopulacao()

        novaPopulacao = []

        #SELECIONA PAI POR TORNEIO 2 melhores valores

        pai1 = self.populacao[0]
        pai2 = self.populacao[1]

        print("************************ p1", pai1.cromossomo)
        print("************************ p2", pai2.cromossomo)


        filhos = pai1.crossover(pai2)

        novaPopulacao.append(filhos[0].mutacao(taxaMutacao))
        novaPopulacao.append(filhos[1].mutacao(taxaMutacao))

        print("nova populacao - ")
        for i in range(len(novaPopulacao)):
            novaPopulacao[i].fitness()
            print("populacao %s -> fitnesss %s " % (novaPopulacao[i].cromossomo, novaPopulacao[i].notaFitness))



if __name__ == '__main__':
    ag = AG()
    # ag.inicializaPopulacao(POPULACAO)
    ag.resolver()

    # for i in range(ag.populacao):
    #     print(i.populacao)

    # integet = int('000111',2)
    # bin = bin(integet)[2:].zfill(6)
    # int = 1

    # print("int %s" % (integet))
    # print("bin %s" % (bin))