class Tabela:
    ponderacao = 0
    fitness = 0

    def x(self,x):
        self.x = x

    def y(self,y):
        self.y = y

    def cromossomo(self,cromossomo):
        self.cromossomo = cromossomo

    def setFitness(self,fitness):
        self.fitness = fitness

    def setPond(self,ponderacao):
        self.ponderacao = ponderacao

    def obterX(self):
        return self.x

    def obterY(self):
        return self.y

    def obterCromossomo(self):
        return self.cromossomo

    def obterFitness(self):
        return self.fitness

    def obterPond(self):
        return self.ponderacao
