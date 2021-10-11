# -*- coding: utf-8 -*-
"""
@author: lucas
"""

"Least Square"

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import statistics as sta

kar = []   
var = []
with open('monet.txt','r') as myfile:
    for myline in myfile:
        kar = kar + [myline]
# print(kar[3])
for i in range(236):
    exec('var = var + ['+kar[i]+']')
    


# selic = 1
# ipca = 2
# poupança = 3
# m1 = 4
# títulos = 5
# fundos = 6
# fun = 7
# IPCA Acumulado = 8
# POUPANÇA / IPCA ACUMULADO = 9
# M1 / IPCA ACUMULADO = 10
# TÍTULOS / IPCA ACUMULADO = 11
# FUNDOS / IPCA ACUMULADO = 12
# PIB / IPCA ACUMULADO = 13


selic = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
poup = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
m_1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
tit = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
fun = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
pib = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

'--------------------------------Obtendo os dados reais'

for i in range(19):
    for j in range(12):
        selic[i] = selic[i] + [var[i*12 + j + 1][1]]
        poup[i] = poup[i] + [var[i*12 + j + 1][9]]
        m_1[i] = m_1[i] + [var[i*12 + j + 1][10]]
        tit[i] = tit[i] + [var[i*12 + j + 1][11]]
        fun[i] = fun[i] + [var[i*12 + j + 1][12]]
        pib[i] = pib[i] + [var[i*12 + j + 1][13]]

# def dados_ano(x,y):
#     if x == 20:
#         for i in range(7):
#             t = y+'_ano = []'
#             exec(str(t))
#             s = y + ' = ' + y + '_ano' + y + '[228+i]'
#             exec(str(s))


# my_rho = np.corrcoef(selic, poup)
# print(my_rho)

resselic = []
respoup = []
resm_1 = []
restit = []
resfun = []
respib = []

for i in range(7):
    resselic = resselic + [var[228 + i+1][1]]
    respoup = respoup + [var[228 + i + 1][9]]
    resm_1 = resm_1 + [var[228 + i + 1][10]]
    restit = restit + [var[228 + i + 1][11]]
    resfun = resfun + [var[228 + i + 1][12]]
    respib = respib + [var[228 + i + 1][13]]
for i in range(5):
    resselic = resselic + [0]
    respoup = respoup + [0]
    resm_1 = resm_1 + [0]
    restit = restit + [0]
    resfun = resfun + [0]
    respib = respib + [0]
 
def mean(x,y):
    soma = 0
    for i in range(len(x)):
        soma = soma + x[i][y]
    return soma/len(x)

def stdmi(x,y):
    soma = []
    for i in range(len(x)):
        soma = soma + [x[i][y]]
    return sta.stdev(soma)

x_1 = 190
x_2 = 2660
def mean_n(x,y):
    return mean(x,y)*len(x)
def f_n(x,y):
    soma = 0
    for i in range(len(x)):
        soma = soma + (i+1)*x[i][y]
    return soma

def reg(x,y):    
    a = 19*f_n(x,y)-x_1*mean_n(x,y)
    a = a/(19*x_2 - x_1**2)
    b = mean_n(x,y)-a*x_1
    b = b/19
    # print(a)
    # print(b)
    return a*20+b

for i in range(7):
    print(str(i+1) +' selic: ' + str((reg(selic,i)-resselic[i])/resselic[i]))
    print(str(i+1) +' poup: ' + str((reg(poup,i)-respoup[i])/respoup[i]))
    print(str(i+1) +' m_1: ' + str((reg(m_1,i)-resm_1[i])/resm_1[i]))
    print(str(i+1) +' tit: ' + str((reg(tit,i)-restit[i])/restit[i]))
    print(str(i+1) +' fun: ' + str((reg(fun,i)-resfun[i])/resfun[i]))
    print(str(i+1) +' pib: ' + str((reg(pib,i)-respib[i])/respib[i]))
    print('--------------------------------------------------------------------')

for i in range(5):
    print('--------------------------------------------------------------------')
    print(str(i+8) +' selic: ' + str(reg(selic,i)))
    print(str(i+8) +' poup: ' + str(reg(poup,i)))
    print(str(i+8) +' m_1: ' + str(reg(m_1,i)))
    print(str(i+8) +' tit: ' + str(reg(tit,i)))
    print(str(i+8) +' fun: ' + str(reg(fun,i)))
    print(str(i+8) +' pib: ' + str(reg(pib,i)))
    print('--------------------------------------------------------------------')

input('Digite algum comando no terminal para encerrar o programa. ')
