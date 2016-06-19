
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
print "EXERCÍCIO AULA 12 - EXERCÍCIO 01"
#-----------------INÍCIO GRAFO 01 - SOMA --------------------------------------
print "------------------------ SOMA -------------------------------"
node = {'A':['B','F','G','E'],'B':['A','C','D','E','F','G'],'C':['B','F','G','E'],'D':['B','F','G','E'],'E':['A','B','C','D','F'],'F':['A','B','C','D','E','G'],'G':['A','B','C','D','F']}

g = Graph(node)
P = g.plot()
P.show(figsize=[2,2])
 
L = g.kirchhoff_matrix() #laplaciana

P = L.charpoly();P #polinomio caracteristico
autovalores = L.eigenvalues() #autovalores
autovalores.sort() #ordenando autovalores
print "Autovalores:"
print autovalores

print "Graus dos Vértices:"
graus = g.degree_sequence(); #grau
graus.sort();graus

print "Grau Máximo:"
max(graus) #grau max
print "Grau Mínimo:"
min(graus) #grau min


if len(autovalores) > 1: #printando a(G)
    print "Conectividade Algebria:"
    print autovalores[1]
 
#calculando o tamanho do eixo X
quantPontos =[]
for i in range(len(graus)): 
    quantPontos.append(i)
#calculando o tamanho do eixo Y
aux = []
if graus[len(graus)-1] > autovalores[len(graus)-1]:
    aux = graus[len(graus)-1] +2
else:
    aux = autovalores[len(graus)-1] +2
 
#garantindo o aredondamento dos autovalores
aut = []
autovalores = L.eigenvalues()
for i in range(len(autovalores)):
    aut.append(round(autovalores[i]))
aut = sorted(aut)
 
plt.clf()
titulo = plt.plot(quantPontos, aut,linestyle="dashed", marker="o", color="green",label="Autovalores") #plotando os autovalores no grafico
titulo = plt.plot(quantPontos, graus,linestyle="dashed", marker="o", color="black",label="Grau dos vertices") #plotando os graus dos vertices no grafico
titulo = plt.legend(loc='upper center', bbox_to_anchor=(0.45, -0.025, .45,1.17),fancybox=True, shadow=True, ncol=3) #configurando a legenda
titulo = plt.xlabel("Indice") #legenda para o eixo X
titulo = plt.ylabel("Valores") #legenda para o eixo Y
titulo = plt.title("Graus dos vertices e Autovalores (por indice)") #titulo para o grafico
plt.grid(True) #ativando a grade no grafico
pontos = plt.axis([0, (len(quantPontos)+1), 0, aux]) #setando os intervalos para os eixos X e Y
plt.show() #mostrando o grafico
plt.clf()

