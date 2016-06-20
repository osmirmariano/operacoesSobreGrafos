
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def execute(g,tam):
    print "Grafo:"
    P = g.plot()
    P.show(figsize=tam)

    laplaciana = g.kirchhoff_matrix() #laplaciana
    polinomio = laplaciana.charpoly() #polinomio caracteristico
    autovalores = laplaciana.eigenvalues() #autovalores

    #garantindo o aredondamento dos autovalores
    aut = []
    for i in range(len(autovalores)):
        aut.append(round(autovalores[i],5))
    aut = sorted(aut)
    print "AUTOVALORES"
    print aut

    graus = g.degree_sequence(); #grau
    graus.sort();
    print "Graus:"
    print graus
    print "Grau minimo:"
    print min(graus) #grau min
    print "Grau maximo:"
    print max(graus) #grau max
    if len(aut) > 1: #printando a(G)
        print "Conectividade algebrica"
        print aut[1]

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

    plt.clf()
    titulo = plt.plot(quantPontos, aut,linestyle="dashed", marker="o", color="blue",label="Autovalores") #plotando os autovalores no grafico
    titulo = plt.plot(quantPontos, graus,linestyle="dashed", marker="o", color="red",label="Grau dos vertices") #plotando os graus dos vertices no grafico
    titulo = plt.legend(loc='upper center', bbox_to_anchor=(0.45, -0.025, .45,1.17),fancybox=True, shadow=True, ncol=3) #configurando a legenda
    titulo = plt.xlabel("Indice") #legenda para o eixo X
    titulo = plt.ylabel("Valores") #legenda para o eixo Y
    titulo = plt.title("Graus dos vertices e Autovalores (por indice)") #titulo para o grafico
    plt.grid(True) #ativando a grade no grafico
    plt.show() #mostrando o grafico
    plt.clf()
    print "\n\n\n\n\n\n\n"


#CALCULANDO GRAFO 1 LEXICOGRÁFICO - AULA 12 
#---------------------------------------------------------------------------------------
g = Graph({'AF':['AE','AG','BE','BF','BG'],'AE':['BE','BF','BG'],'AG':['BE','BF','BG'],'BE':['BF','CE','CF','CG'],'BF':['BG','CE','CF','CG'],'BG':['CE','CF','CG'],'CE':['CF','DE','DF','DG'],'CF':['CG','DE','DF','DG'],'CG':['DE','DF','DG'],'DE':['DF'],'DF':['DG']})
execute(g,[3,3])









