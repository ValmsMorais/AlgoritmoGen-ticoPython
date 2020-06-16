import random
from operator import attrgetter
from Tabela import Tabela

def funcao_objetivo(x,y):
    f = 2 - ((x-2)**2) - ((y-3)**2)
    return f

def definePond(tabela):
    for i in range(len(tabela)):
        if i<4 :
            tabela[i].setPond(4-i)

def mostrarTabela(tabela):
    if tabela[0].obterPond() != 0:
        print("X       Y      Cromossomo       f(x,y)       Pond")
        for i in range(len(tabela)):
            print(tabela[i].obterX(), "     ", tabela[i].obterY(), "      ", tabela[i].obterCromossomo(),
                "        ", tabela[i].obterFitness(),"          ", tabela[i].obterPond())
    else:
        print("X       Y      Cromossomo       f(x,y)")
        for i in range(len(tabela)):
            print(tabela[i].obterX(), "     ", tabela[i].obterY(), "      ", tabela[i].obterCromossomo(),
                  "        ", tabela[i].obterFitness())

def crossover(table):#tabelaSele
    tabela.clear()
    for i in range(len(table)):
        for j in range(table[i].obterPond()):
            novaLinhaTabela = Tabela()
            randomico = random.randint(0,3)
            #novaLinhaTabela.x(table[i].obterX())
            novaLinhaTabela.cromossomo(table[i].obterCromossomo()[0:4] + table[randomico].obterCromossomo()[4:6])
            #novaLinhaTabela.x(int(novaLinhaTabela.obterCromossomo()[0:3],2))
            #novaLinhaTabela.y(int(novaLinhaTabela.obterCromossomo()[3:7], 2)) 7
            tabela.append(novaLinhaTabela)


def mutacao(table):#tabela
    min = 0
    max = 1
    for i in range(0,5):
        posGene = random.randint(0,5)
        linhaIndividuo = random.randint(min,max+1)
        print("Linha: ",linhaIndividuo)
        print("Gene: ",posGene)
        #table[random.randint(min,max)].obterCromossomo()
        min = min+2
        max = max+2

def mutation(table):
    cromossomos = []
    posMin = 0
    posCromossomo = 0
    crom = ''
    for l in range(len(table)):
        for i in range(0,6):
            cromossomos.append(table[l].obterCromossomo()[i])
    #print("Cromossomos: ",cromossomos)
    print("\nMutação: ")
    for j in range(len(cromossomos)):

        posGene = random.randint(posMin,posMin+12)
        print("Pos min: ",posMin,"Pos min +12: ",posMin+12)
        print("Pos gene: ",posGene)
        if(posGene == 60):
            posGene = 59
        if cromossomos[posGene] == '1':
            #print("Tem um ",cromossomos[posGene])
            cromossomos[posGene] = '0'
        elif cromossomos[posGene] == '0':
            #print("Tem um ", cromossomos[posGene])
            cromossomos[posGene] = '1'
        posMin = posMin+12
        if posMin+12 > 60:
            break

    #print("\nCromossomos:" ,cromossomos)
    for z in range(len(table)):
        crom = ''
        for j in range(posCromossomo,posCromossomo+6):
            crom = crom + cromossomos[j]
        posCromossomo = posCromossomo + 6
        #print(z,crom)
        #print("Sem mutacao: ",table[z].obterCromossomo())
        table[z].cromossomo = crom
        #print(table[z].obterCromossomo())



def decodificar(table):
    for i in range(len(table)):
        table[i].x(int(table[i].obterCromossomo()[0:3], 2))
        table[i].y(int(table[i].obterCromossomo()[3:7], 2))
        table[i].setFitness(funcao_objetivo(table[i].obterX(),table[i].obterY()))

geracao = 50000
x = [];
y = [];
binX = []
binY = []
cromossomo = []
funcao_obj = []
tabela = []#List de Tabela
tabelaSele = []#List de Tabela sem população selecionada

for i in range(0,10):
    x.append(random.randint(0,7))
    y.append(random.randint(0, 7))
#definindo X, Y, cromossomos e f(x,y)
for i in range(len(x)):
    binX.append('{0:03b}'.format(x[i]))
    binY.append('{0:03b}'.format(y[i]))
    cromossomo.append(binX[i]+binY[i])
    funcao_obj.append(funcao_objetivo(x[i],y[i]))
#Colocando os dados na tabela
for z in range(len(x)):
    linhaTabela = Tabela();#x,y,cromossomo,f(x,y),pond
    linhaTabela.x(x[z])
    linhaTabela.y(y[z])
    linhaTabela.cromossomo(cromossomo[z])
    linhaTabela.setFitness(funcao_obj[z])
    tabela.append(linhaTabela)

print("X: ",x)
#print("Bin x: ",binX)
print("Y: ",y)
#("Bin Y: ",binY)
print("Cromossomo: ",cromossomo)
print("fitness: ",funcao_obj)
print("\nTabela Inicial:")
mostrarTabela(tabela)

#Ordenando pelo f(x,y)
for i in range(0,geracao):
    if (tabela[0].obterFitness() == 2):
        break
    print("\n------------------------------------------------------------\n*****  Geração: ", i+1,"  *****")
    tabelaSele.clear()
    for pos2 in range(0,4):
        tabelaSele.append(tabela[pos2])#Faz a seleção dos 4 mais aptos
    print("\nTabela ordenada:")
    tabela.sort(reverse=True, key=attrgetter("fitness"))  # Ordenar tabela pelo f(x,y)
    mostrarTabela(tabela)
    print("\nSelecionados:")
    mostrarTabela(tabelaSele)
    definePond(tabelaSele)
    print("\nTabela Ponderada:")
    mostrarTabela(tabelaSele)
    '''
    print("\nTabela normal:")
    mostrarTabela(tabela)
    '''
    crossover(tabelaSele)

    print("\nTabela crossover:")
    print("X       Y      Cromossomo       f(x,y)")
    for i in range(len(tabela)):
        print("                ",tabela[i].obterCromossomo())

    mutation(tabela)
    decodificar(tabela)
    print("\nTabela decodificada: ")
    mostrarTabela(tabela)
    print("\nTabela Final Geração:")
    tabela.sort(reverse=True, key=attrgetter("fitness"))  # Ordenar tabela pelo f(x,y)
    mostrarTabela(tabela)

