# Frexco_Alimentos
Projeto para previsão de demanda.

O código consiste em fazer uma previsão de demanda para os próximos 5 dias com base no arquivo xlsx que recebemos.

Ao analisar esse nosso arquivo através de um data frame gerado pelo python, podemos notar que falta uma coluna com dias da semana especificados.

Tratamos e adicionamos mais uma coluna com os dias da semana especificados e fizemos um agrupamento botando em ordem seguindos a quantidade de vendas com parâmetro.

Ao nos depararmos com esse data frame, podemos ver como as vendas caem bruscamente aos finais de semana.

A projeção para os próximos 5 dias precisaria levar isso em conta uma vez que os próximos dias serão Sábado, Domingo, Segunda, Terça e Quarta.

Diante de tal cenário, decidimos tratar nossa previsão em duas etapas;

Etapa 1 consiste em fazer a separação das vendas dos finais de semana para analisarmos os ultimos 3 para então termos nossa previsão dos próximos 2 dias.

Etapa 2 foi criar um novo data frame só com os dias da semana e analisarmos para termos uma previsão os 3 próximos dias.

Assim chegamos aos nossos 5 dias esperados.

Somamos as nossas duas previsões e temos então uma previsão mais precisa levando em consideração a queda de vendas nos finais de semama.

Falando do código....

Usamos basicamente a biblioteca pandas para tratarmos os dados.

Criamos novos frames inserindo colunas, outros frames agrupando e variáveis para usar na função final que faz o calculo da previsão.

Todos os frames podem ser visualizados usando o comando "display(nome do frame desejado)" após o final do código.

Faça bom proveito.
