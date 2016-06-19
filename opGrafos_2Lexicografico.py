
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
print "EXERCÍCIO AULA 12 - EXERCÍCIO 02"
#-----------------INÍCIO GRAFO 02 - PRODUTO LEXICOGRÁFICO --------------------------------------
print "------------------------ LEXICOGRÁFICO -------------------------------"
node = {'AE':['BE','CE','CF','BF','CG','BG'],'BE':['AE','AF','AG','BE','CE','CG'],'CE':['AE','BE','AF','AG','BF','BG'],'AF':['BE','CE','CF','BF','CG','AG'],'BF':['AE','AF','AG','BG','CG','CF','CE'],'CF':['BE','AE','BF','AF','AG','BG','CG'],'AG':['AF','BE','CE','BF','CF','CG','BG'],'BG':['AF','AE','BF','CF','CG','CG'],'CG':['AG','BG','AF','AE','BF','BE','CF']}

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
titulo = plt.plot(quantPontos, graus,linestyle="dashed", marker="o", color="red",label="Grau dos vertices") #plotando os graus dos vertices no grafico
titulo = plt.legend(loc='upper center', bbox_to_anchor=(0.45, -0.025, .45,1.17),fancybox=True, shadow=True, ncol=3) #configurando a legenda
titulo = plt.xlabel("Indice") #legenda para o eixo X
titulo = plt.ylabel("Valores") #legenda para o eixo Y
titulo = plt.title("Graus dos vertices e Autovalores (por indice)") #titulo para o grafico
plt.grid(True) #ativando a grade no grafico
pontos = plt.axis([0, (len(quantPontos)+1), 0, aux]) #setando os intervalos para os eixos X e Y
plt.show() #mostrando o grafico
plt.clf()