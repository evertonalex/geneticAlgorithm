from random import *
import matplotlib.pyplot as plt
import numpy as np
import math

CORTE = 1
TAXAMUTACAO = 0.05
QTDGENESES = 3
TAMANHOCROMOSSOMO = 3
TAMANHOPOPULACAO = 4
# PROBALIDIDADEMUTACAO = 0.01

NUMEROGERACOES = 100

class Genese():
    def __init__(self, nunGeneses, valorGenese):
        self.nunGeneses = nunGeneses
        self.valorGenese = valorGenese

class Individuo():
    def __init__(self, listaGeneses = [],
                 # valores,
                 geracao=0):
        # self.nunGeneses = nunGeneses
        # self.valores = valores
        self.geracao = geracao
        self.notaAvaliacao = 0
        self.cromossomo = []

        # for i in range(0,TAMANHOCROMOSSOMO):
        #     if random() < 0.5:
        #         self.cromossomo.append(0)
        #     else:
        #         self.cromossomo.append(1)

        print("listaGeneses", listaGeneses)

        for i in range(len(listaGeneses)):
            self.cromossomo.append(listaGeneses[i])
        print("cromossomo = %s" % (self.cromossomo))

    def avaliacao(self): #FITNESS
        nota = 0

        for i in range(len(self.cromossomo)):

            # print("avaliacao valor = %s" % (self.valores[i]))

            nota = abs(((2 * self.cromossomo[i]) + (self.cromossomo[i] ** 2) + self.cromossomo[i]) - 52)
        self.notaAvaliacao = nota

    def crossover(self, outroIndividuo):
        corte = CORTE

        filho1 = outroIndividuo.cromossomo[0:corte]+self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outroIndividuo.cromossomo[corte::]

        filhos = [
            Individuo([],self.geracao + 1),
            Individuo([],self.geracao + 1)
        ]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        print("filho1 - %s \n filho2 -%s " %(filhos[0].cromossomo, filhos[1].cromossomo))
        return filhos

    def mutacao(self, taxaMutacao): #mutaOsFilhos
        print("before mutacao - %s" % (self.cromossomo))
        for i in range(len(self.cromossomo)):
            if randint(0,1) > taxaMutacao:
                self.cromossomo[i] = randint(0,9)
                # if self.cromossomo == 1:
                #     self.cromossomo[i] = 0
                # else:
                #     self.cromossomo[i] = 1
        print("after mutacao - %s " % (self.cromossomo))
        return self

class AlgoritimoGenerito(): #populacao
    def __init__(self, tamanhoPopulacao):
        self.tamanhoPopulacao = tamanhoPopulacao
        self.populacao = [] #objetosTipoIndividuos
        self.geracao = 0
        self.melhorSolucao = 0
        self.listaSolucoes = [] #grafico

    def inicializaPopulacao(self):

        for i in range(TAMANHOPOPULACAO):
            listaGeneses = []
            for y in range(0, QTDGENESES):
                listaGeneses.append(randint(0, 9))
            self.populacao.append(Individuo(listaGeneses))
        self.melhorSolucao = self.populacao[0]

    def ordenaPopulacao(self):
        self.populacao = sorted(self.populacao, key=lambda populacao: populacao.notaAvaliacao, reverse=False)

    def melhorIndiviuo(self, individuo):
        if individuo.notaAvaliacao < self.melhorSolucao.notaAvaliacao:
            self.melhorSolucao = individuo

    def somaAvaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.notaAvaliacao
        return soma

    def selecionaPai(self, somaAvaliacao): #ROLETA
        pai = -1
        # valorSorteado = random() * somaAvaliacao
        valorSorteado = randint(1,3)
        soma = 0
        i = 0
        while i < len(self.populacao) and soma < valorSorteado:
            soma += 1
            pai += 1
            i += 1
        return pai

    def visualizaGeracao(self):
        melhor = self.populacao[0]

        print("GERACAO -> %s" % self.populacao[0].geracao)
        print("FITNESS -> %s" % melhor.notaAvaliacao )
        print("Cromossomo -> %s" % melhor.cromossomo )


    def resolver(self, taxaMutacao, numeroGeracao):
        self.inicializaPopulacao()

        for individuo in self.populacao:
            individuo.avaliacao()

        self.ordenaPopulacao()

        self.melhorSolucao = self.populacao[0] #grafico
        self.listaSolucoes.append(self.melhorSolucao.notaAvaliacao) #grafico

        self.visualizaGeracao()

        for geracao in range(numeroGeracao):
            somaAvaliacao = self.somaAvaliacoes()
            novaPopulacao = []

            for individuoGerados in range(0, self.tamanhoPopulacao, 2):
                pai1 = self.selecionaPai(somaAvaliacao)
                pai2 = self.selecionaPai(somaAvaliacao)

                print("pai1 %s | pai2 %s " % (pai1, pai2))

                filhos = self.populacao[pai1].crossover(self.populacao[pai2])

                print("populacaoPai1 ", self.populacao[pai1])

                novaPopulacao.append(filhos[0].mutacao(taxaMutacao))
                novaPopulacao.append(filhos[1].mutacao(taxaMutacao))

            self.populacao = list(novaPopulacao) #sobrescrevePopulacaoAntiva

            for individuo in self.populacao:
                individuo.avaliacao()

            self.ordenaPopulacao()
            self.visualizaGeracao()
            melhor = self.populacao[0]

            self.listaSolucoes.append(melhor.notaAvaliacao)  # grafico

            self.melhorIndiviuo(melhor)

            print("MELHOR SOLUCAO *******")
            print("** GERACAO -> %s" % self.melhorSolucao.geracao)
            print("** FITNESS -> %s" % self.melhorSolucao.notaAvaliacao)
            print("** Cromossomo -> %s" % self.melhorSolucao.cromossomo)
        return self.melhorSolucao.cromossomo


if __name__ == '__main__':

    algotimoGenetico = AlgoritimoGenerito(TAMANHOPOPULACAO)

    resultado = algotimoGenetico.resolver(TAXAMUTACAO, NUMEROGERACOES)


    plt.plot(algotimoGenetico.listaSolucoes)
    plt.title("Valor AG")
    plt.show()
