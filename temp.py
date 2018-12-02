# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
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
    print(tempoMedio)
    return tempoMedio
# %% dados base
numeroGuiches = 4
atendimentoHoraGuiche = 20
taxaClientesHora = 70
tempoFila=tempoMedioFila(numeroGuiches,atendimentoHoraGuiche,taxaClientesHora) 