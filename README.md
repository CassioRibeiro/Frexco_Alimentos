# Frexco_Alimentos
Projeto para previsão de demanda.

O código consiste em fazer uma previsão de demanda para os próximos 5 dias com base no arquivo xlsx que recebemos.

ao analisar esse nosso arquivo através de um data frame gerado pelo python, podemos notar que falta uma coluna com dias da semana especificados.

tratamos e adicionamos mais uma coluna com os dias da semana especificados e fizemos um agrupamento botando a quanridade de vendas em ordem.

ao nos depararmos com esse data frame, podemos ver como as vendas caem bruscamente aos finais de semana.

a projeção para os próximos 5 dias precisaria levar isso em conta uma vez que os próximos dias serão Sábado, Domingo, Segunda, Terça e Quarta.

diante de tal cenário, decidimos tratar nossa previsão em duas etapas

etapa 1 consiste em fazer a separação das vendas dos finais de semana para analisarmos os ultimos 3 para então termos nossa previsão dos próximos 2 dias

etapa 2 foi criar um novo data frame só com os dias da semana e analisarmos para termos uma previsão os 3 próximos dias

assim chegamos aos nosso 5 dias esperados.

somamos as nossas duas previsões e temos então uma previsão mais precisa levando em consideração a queda de vendas nos finais de semama.

falando do código....

usamos basicamente a bibliotecas pandas para tratarmos os dados.

criamos novos frames inserindo colunas, outros agrupando e variáveis para usar na função final que faz o calculo da previsão.

todos os frames podem ser vizualizados usando o comando "display(nome do frame desejado)" após o final do código.

faça com proveito.
