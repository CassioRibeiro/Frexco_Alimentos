###            Frexco Alimentos            ###
### Somos a ponte entre o campo e a cidade ###
###     Previsão de demanda para 5 dias    ###
### Estágiario responsável: Cássio Ribeiro ###



#Importanto biblíotecas para o uso no projeto

import pandas as pd


#Importanto os dados fornecidos para trabalharmos com ele

dados = pd.read_excel("Dados.xlsx")


#Adicionando uma coluna de dias da semana para melhorarmos a qualidade da nossa previsão de demanda.
#Nela ainda irá conter as datas numéricas mas iremos tratar disso logo mais.

dados.loc[ : ,"Dia da Semana"] = dados["Data"]

#Definindo uma função para substituir as datas numéricas por nome dos dias.

def diasemana (x):
    return x.strftime("%A")

#Subistituindo as datas numéricas na coluna dia da Semana pelos nomes dos dias em inglês.

dados ["Dia da Semana"] = dados["Dia da Semana"].apply(diasemana)

#Criando um dicionário para tradução dos dias da semana.dados 

Dic_Dias_PTBR = {"Monday": "Segunda-Feira",
                "Tuesday":"Terça-Feira",
                "Wednesday":"Quarta-feira",
                "Thursday":"Quinta-Feira",
                "Friday": "Sexta-Feira",
                "Saturday":"Sábado",
                "Sunday":"Domingo"}


#Realizando a troca dos nomes dos dias de inglês para o português.
dados["Dia da Semana"] = dados["Dia da Semana"].replace(Dic_Dias_PTBR)

#Criando um DataFrame apenas com os dados referentes as vendas nos finais de semana.

sabado = (dados.loc[dados["Dia da Semana"]=="Sábado"])
domingo = (dados.loc[dados["Dia da Semana"]=="Domingo"])
finaldesemana = pd.concat([sabado,domingo])
finaldesemana =  finaldesemana.sort_values("Data")

#Criando variáveis que iremos usar na função final para calcular nossa previsão de demanda para os próximos 5 dias.

final1 = finaldesemana.loc[[39,40]]
final2 = finaldesemana.loc[[32,33]]
final3 = finaldesemana.loc[[25,26]]
final1 = final1["Vendas"].sum()
final2 = final2["Vendas"].sum()
final3 = final3["Vendas"].sum()

#Criando DataFrames apenas com os dados referentes as vendas nos dias de semana.

segunda = (dados.loc[dados["Dia da Semana"]=="Segunda-Feira"])
terça = (dados.loc[dados["Dia da Semana"]=="Terça-Feira"])
quarta = (dados.loc[dados["Dia da Semana"]=="Quarta-Feira"])
quinta = (dados.loc[dados["Dia da Semana"]=="Quinta-Feira"])
sexta = (dados.loc[dados["Dia da Semana"]=="Sexta-Feira"])
semana = pd.concat([segunda,terça,quarta,quinta,sexta]).sort_values("Data")

#Criando variáveis para serem usadas na função final.

sema1 = semana.loc[[42,44,45]]
sema1 = sema1["Vendas"].sum()

sema2 = semana.loc[[37,38,41]]
sema2 = sema2["Vendas"].sum()

sema3 = semana.loc[[31,34,35]]
sema3 = sema3["Vendas"].sum()

#Função final que irá calcular nossa previsão de demanda para os próximos 5 dias.
def previsaodemanda (a,b,c):
    return ((a+b+c)/3)

print ("A previsão de demanda para os próximos 5 dias são {:.0f} produtos."
    .format (previsaodemanda(sema1, sema2, sema3) + previsaodemanda(final1, final2, final3)))






