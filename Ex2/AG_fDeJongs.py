from math import *
# Este AG resolve a funciton de Jong's
# f1(x)sum(x(i)^s)
# i = 1:n
# -5.12<=(i)<=5.12
# Function a ser maximizada -> f(x)=x^2
import random
import numpy as np
import struct



TAMANHOCROMOSSOMO = 15
TAMANHOPOPULACAO = 4
NUMEROGERACOES = 4
PONTOCORTE=5
PROBABILIDADEMUTACAO = 0.05

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

    def crossover(self, outroIndividuo):
        filho1 = outroIndividuo.cromossomo[0:PONTOCORTE] + self.cromossomo[PONTOCORTE:PONTOCORTE+5] + outroIndividuo.cromossomo[PONTOCORTE+5::]
        filho2 = self.cromossomo[0:PONTOCORTE] + outroIndividuo.cromossomo[PONTOCORTE:PONTOCORTE+5] + self.cromossomo[PONTOCORTE+5::]

        filhos = [
            Individuo(self.cromossomo, self.geracao + 1),
            Individuo(self.cromossomo, self.geracao + 1)
        ]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        print("CROMOSSOMO ORIGINAL ", self.cromossomo)
        print("CROMOSSOMO CROSS ", filho2)
        return filhos

    def mutacao(self, taxaMutacao):
        print("MUTACAO before %s" % self.cromossomo)
        for i in range(len(self.cromossomo)):
            if random.randint(0,1) < taxaMutacao:
                print("CROMO TESTE ", self.cromossomo[i])
                if self.cromossomo[i] == '1':
                    print("IGUL 1")
                    # self.cromossomo[i] = '0'
                else:
                    print("IGUL 0")
                    # self.cromossomo[i] = '1'
        print("MUTACAO after %s" % self.cromossomo)
        return self


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

    def ordenaPopulacao(self):
        self.populacao = sorted(self.populacao, key=lambda populacao: populacao.notaFitness, reverse=False)

    def somaFtnessIndividuos(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.notaFitness
        return soma

    def roletaSelecionaPai(self, somaFitness):
        pai = -1
        randomSort = random.uniform(0,1)
        # print("RANDOM -> ", randomSort)
        valorSorteado = randomSort * somaFitness
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valorSorteado:
            print("Nota fitt - %s SOMA FITS %s | valorSorteado %s" % (
            self.populacao[i].notaFitness, somaFitness, valorSorteado))

            soma += self.populacao[i].notaFitness
            pai += 1
            i += 1

        # print("paiRoleta --> %s" % (pai))
        return pai

    def run(self, numeroGeracoes):
        # self.populacao.append()
        self.inicializaPopulacao()
        for i in range(len(self.populacao)):
            self.populacao[i].fitness()

        self.ordenaPopulacao()

        print("MELHOR SOLUCAO *** ", self.populacao[0].notaFitness)

        novaPopulacao = []
        for individuosGerados in range(0, TAMANHOPOPULACAO, 2):
            somaAvaliacoes = self.somaFtnessIndividuos()

            pai1 = self.roletaSelecionaPai(somaAvaliacoes)
            pai2 = self.roletaSelecionaPai(somaAvaliacoes)

            print("pai1 %s pai2 %s " % (pai1, pai2))
            # for individuoGeracao in range(0, numeroGeracoes, 2):
            #     pai1 = self.roletaSelecionaPai(somaAvaliacoes)
            #     pai2 = self.roletaSelecionaPai(somaAvaliacoes)
                            # print("pai1 -> ", pa)

            # for geracao in range(tamanhoGeracao):

            #Crosover
            filhos = ag.populacao[pai1].crossover(ag.populacao[pai2])

            #novaPopulacao
            novaPopulacao.append(filhos[0].mutacao(PROBABILIDADEMUTACAO))
            novaPopulacao.append(filhos[1].mutacao(PROBABILIDADEMUTACAO))

        ag.populacao = list(novaPopulacao)
        for individuo in ag.populacao:
            individuo.fitness()
        ag.ordenaPopulacao()

        print("************************ MELHOR INDIVIDUO NOVO --> ", self.populacao[0].notaFitness)



if __name__ == '__main__':
    ag = AG()
    ag.run(NUMEROGERACOES)


















