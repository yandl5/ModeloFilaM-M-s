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
    print(tUtilizacao)
    tempoMedio=(probabilidadeOcupacao(nGuiches,tUtilizacao)/(1-tUtilizacao))*tUtilizacao
    return tempoMedio
# %% dados base bancos cidade A
numeroGuichesBancos = 8
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
centroMetropoleDia = [0]*40
for i in range(0,40):
    centroMetropoleDia[i] = np.random.randint((centroMetropole*0.00008),(centroMetropole*0.00014))
# %% bancos da metrópole
numeroGuiches = [8]*5
# %% Media Hora na cidade 
MediaDia = [0]*8
# %%
contadorDia = [0]*40
for i in range(0,40):
    contadorDia[i]=tempoMedioFila(numeroGuichesBancos,atendimentoHoraGuiche,centroMetropoleDia[i])
j = 0
for i in range(0,8):
    MediaDia[i]=contadorDia[j]+contadorDia[j+1]+contadorDia[j+2]+contadorDia[j+3]+contadorDia[j+4]
    j=j+5
for i in range(0,8): 
    MediaDia[i]=MediaDia[i]/5*60
# %% Dados referentes ao custo em hora
custoGuicheHora = 0.50
custoClienteHora = 2.00
taxaEsperaCliente = 5.00
vetorCusto = np.zeros(8)
for i in range(0,8):
    if MediaDia[i]<=15 :
        vetorCusto[i] = custoGuicheHora*numeroGuichesBancos + custoClienteHora*(MediaDia[i]/60)
    else:
        vetorCusto[i] = custoGuicheHora*numeroGuichesBancos + custoClienteHora*(MediaDia[i]/60)+taxaEsperaCliente
# %% Gerar gráficos média dia
import matplotlib.pyplot as plt
y_axis = MediaDia
x_axis = range(len(y_axis))
width_n = 0.4
bar_color = 'black'

plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
plt.show()
# %% Gerar gráfico custo
y_axis = vetorCusto
x_axis = range(len(y_axis))
width_n = 0.4
bar_color = 'black'

plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
plt.show() 

