Resumo do Resultado
Tempo de semáforo para a via Norte: 38.64 segundos
Tempo de semáforo para a via Sul: 30.00 segundos
Tempo de semáforo para a via Leste: 34.51 segundos
Tempo de semáforo para a via Oeste: 30.00 segundos
Além disso, você obteve gráficos que representam as funções de pertinência para as variáveis de entrada (número de veículos em cada via) e para as variáveis de saída (tempo do semáforo).

Explicação do Código com Base nos Resultados
1. Configuração das Variáveis de Entrada (Número de Veículos)
Primeiro, temos as variáveis de entrada para os tipos de veículos em cada via:

carros_norte, motos_norte, caminhoes_norte
carros_sul, motos_sul, caminhoes_sul
carros_leste, motos_leste, caminhoes_leste
carros_oeste, motos_oeste, caminhoes_oeste
Essas variáveis representam o número de veículos em cada categoria e são usadas para calcular o tempo de semáforo.

2. Funções de Pertinência das Variáveis de Entrada
Você tem funções de pertinência para essas variáveis de entrada, dividindo o número de veículos em três categorias: baixo, médio e alto. Aqui estão os valores definidos para essas categorias (para qualquer tipo de veículo):

baixo: [0, 0, 50] (até 50 veículos, com uma transição suave entre 0 e 50)
médio: [25, 50, 75] (de 25 a 75 veículos)
alto: [50, 100, 100] (acima de 50 veículos)
Essas funções de pertinência são desenhadas automaticamente pela biblioteca skfuzzy nos gráficos que você viu. Elas ajudam a transformar os valores numéricos (quantidade de veículos) em categorias fuzzy (como "baixo", "médio" e "alto").

3. Funções de Pertinência da Variável de Saída (Tempo de Semáforo)
Você também definiu funções de pertinência para o tempo do semáforo, dividindo-o em três categorias:

curto: [0, 0, 30] (tempo até 30 segundos)
médio: [15, 30, 45] (tempo entre 15 e 45 segundos)
longo: [30, 60, 60] (tempo até 60 segundos)
Essas funções são usadas para determinar quanto tempo cada semáforo ficará verde, com base no número de veículos nas vias.

4. Regras Fuzzy
As regras definem a relação entre a quantidade de veículos e o tempo do semáforo. Aqui estão algumas das regras:

Se a quantidade de veículos é alta em qualquer via, o semáforo deve ser longo.
Se a quantidade de veículos é baixa em uma via, o semáforo deve ser curto.
Se a quantidade de veículos é média, o tempo do semáforo será médio.
Essas regras são aplicadas pelo sistema fuzzy para calcular o tempo de semáforo com base na entrada dos veículos.

5. Simulação do Sistema Fuzzy
Durante a execução do código, o sistema foi simulado com os seguintes valores de entrada para os veículos nas vias:

Via Norte:
Carros: 80
Motos: 50
Caminhões: 30
Via Sul:
Carros: 40
Motos: 20
Caminhões: 10
Via Leste:
Carros: 60
Motos: 10
Caminhões: 5
Via Oeste:
Carros: 20
Motos: 30
Caminhões: 15
Esses valores foram usados para determinar o tempo de semáforo para cada via, conforme as regras fuzzy.

6. Resultado Final
Com base nas regras e nas funções de pertinência, o sistema calculou o seguinte:

Tempo de semáforo para a via Norte: 38.64 segundos
Como o número de veículos na via Norte é relativamente alto, o semáforo ficará verde por mais tempo (38.64 segundos).
Tempo de semáforo para a via Sul: 30.00 segundos
A via Sul tem um número menor de veículos, então o semáforo fica verde por um tempo médio de 30 segundos.
Tempo de semáforo para a via Leste: 34.51 segundos
A via Leste tem uma quantidade média de veículos, então o tempo do semáforo fica em torno de 34.5 segundos.
Tempo de semáforo para a via Oeste: 30.00 segundos
A via Oeste tem uma quantidade média de veículos, semelhante à via Sul, e também recebe um tempo médio de 30 segundos.
Esses tempos de semáforo são o resultado da aplicação das funções de pertinência e das regras fuzzy com os valores de entrada dados.

7. Gráficos das Funções de Pertinência
Os gráficos que você viu representam as funções de pertinência para cada variável (entrada e saída). Cada gráfico mostra como os valores das variáveis são mapeados para suas respectivas categorias (baixo, médio, alto para entrada, e curto, médio, longo para a saída).

Cada gráfico é um triângulo (para funções de pertinência trimf) que representa a distribuição de cada categoria de valor. Por exemplo, no gráfico de carros_norte, você verá como o número 80 se encaixa na categoria "alto" de veículos, o que influencia o tempo do semáforo a ser maior.

Resumo Final do Processo
O sistema fuzzy recebe os valores de entrada (quantidade de veículos nas vias).
As funções de pertinência são usadas para transformar esses valores em categorias fuzzy.
As regras fuzzy são aplicadas para calcular o tempo de semáforo verde para cada via.
O sistema computa o tempo de semáforo e exibe os resultados.
As funções de pertinência para cada variável de entrada e saída são visualizadas graficamente.
Esse processo garante que o semáforo se ajuste automaticamente ao fluxo de veículos, aumentando o tempo de semáforo nas vias mais movimentadas e reduzindo o tempo nas vias com menos veículos.



