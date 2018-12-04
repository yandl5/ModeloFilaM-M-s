# -*- coding: utf-8 -*-
"""
Spyder Editor
Este é um arquivo de script temporário.
"""
import numpy as np
# %% Função fatorial python
def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1) 
# %% taxa Utilização
def taxaUtilizacaoSistema(nGuiches,nClientesHora,tAtendimentoHora):
    return (nClientesHora/(nGuiches*tAtendimentoHora))
# %% pi zero
def piZero(nGuiches,tUtilizacao):
    primeiroTermo = 0
    segundoTermo = (((nGuiches*tUtilizacao)**nGuiches)/(fatorial(nGuiches)*(1-tUtilizacao)))
    for i in range(0,nGuiches):
        primeiroTermo = primeiroTermo+(((nGuiches*tUtilizacao)**i)/fatorial(i))
    return (1/(primeiroTermo+segundoTermo))
# %% probabilidade de ocupação de um guichê
def probabilidadeOcupacao(nGuiches,tUtilizacao):
    return ((((nGuiches*tUtilizacao)**nGuiches)/(fatorial(nGuiches)*(1-tUtilizacao)))*piZero(nGuiches,tUtilizacao))
# %% tempo médio de fila
def tempoMedioFila(nGuiches,aHoraGuiche,tClientesHora):
    tUtilizacao=taxaUtilizacaoSistema(nGuiches,tClientesHora,aHoraGuiche)
    tempoMedio=(probabilidadeOcupacao(nGuiches,tUtilizacao)/(1-tUtilizacao))*tUtilizacao
    return tempoMedio
# %% dados base bancos cidade A
numeroGuichesBancos = 4
atendimentoHoraGuiche = 20
taxaClientesHora = 70

# %% Cidades
cidadeA = 803739
cidadeB = 202456
cidadeC = 76801
cidadeD = 23704
cidadeE = 43191
#estipular o fenômeno da migração pendular de 10% dos munícipios para A
#durante o periodo de 8:00 até 16:00, somando 8 horas, logo teremos o centro da
#metrópole com o total de habitantes nesse dado período de:
# %% centro da metrópole
centroMetropole=(cidadeA*0.9)+(cidadeB*0.1)+(cidadeC*0.1)+(cidadeD*0.1)+(cidadeE*0.1)
centroMetropoleHora = [0]*8
for i in range(0,8):
    centroMetropoleHora[i] = np.random.randint(centroMetropole*0.0004,centroMetropole*0.0007)
#print (centroMetropoleHora)
# %% bancos da metrópole
numeroGuiches = [8]*5
# %% Media Hora na cidade 
MediaHora = [0]*8
# %%

for i in range(0,8):
    for j in range(0,5):
        MediaHora[i]=MediaHora[i]+tempoMedioFila(numeroGuiches[j],atendimentoHoraGuiche,(centroMetropoleHora[i]/5))
       # print(MediaHora[i])
for i in range(0,8): 
    MediaHora[i]=MediaHora[i]/5*60
# %% Criar matriz horas por dia
matrizA = np.zeros((8,2),int)
for i in range(0,8):
    matrizA[i][0]=MediaHora[i]
    matrizA[i][1]=i+1
# %% Gerar gráficos
import matplotlib.pyplot as plt
y_axis = MediaHora
x_axis = range(len(y_axis))
width_n = 0.4
bar_color = 'black'

plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
plt.show()
    

