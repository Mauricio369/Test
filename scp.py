# PROGRAMINHA PARA SOLUCIONAR SISTEMA DE EQUAÇÕES LINEARES COM NÚMEROS COMPLEXOS E COEFICIENTES INTEIROS OU DE PONTO FLUTUANTE

import numpy as np
n=int(input("Digite quantas linhas e colunas na matriz: ")) #recebendo dimensão matriz NxN

A=np.zeros((n,n),np.complex128) #tornando uma matriz quadrada de N linhas e colunas, inseridas pelo usuário, e complexa;
b=np.zeros((n,1),np.complex128) #definindo a matriz da entrada do sistema
i=0 #iterador
j=0 #iterador
o=0 #iterador

print("\n\nAgora você irá definir a matriz dos coeficientes do sistema!!!\n") ##iteração para definir os coeficientes de A
for i in range(n):
    for j in range(n):
        print("Defina os coeficientes para A[{}][{}]:".format(i,j)) 
        a=float(input("Parte real de A[{}][{}]: ".format(i,j)))
        c=(float(input("Parte imaginária de A[{}][{}]: ".format(i,j))))*1j
        A[i][j]=a+c
        j=j+1
        print('\n')
    i=i+1 

print("\n\nAgora você irá definir a matriz das entradas do sistema!!!\n") #iteração para definir os coeficientes de b
for o in range (n):
    print("Defina os coeficientes para b[{}][{}]:".format(o,0))
    a=float(input("Parte real de b[{}][{}]: ".format(o,0)))
    c=(float(input("Parte imaginária de b[{}][{}]: ".format(o,0))))*1j
    b[o][0]=a+c
    o=o+1
    print("\n")
    
print("\nVocê definiu as matrizes como sendo:\nA={}\nb={}".format(A,b))
X=np.linalg.solve(A,b)
x=print('\nX é a matriz solução do sistema e é dada por:\nX={}'.format(X))