
1. Importação das Bibliotecas
python
Copiar código
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
numpy: Usado para manipulação de arrays e criação de intervalos de valores (ex.: valores de entrada e saída).
skfuzzy: Biblioteca para controle fuzzy, que fornece funcionalidades para criar variáveis fuzzy, funções de pertinência e regras.
matplotlib.pyplot: Usado para plotar as funções de pertinência, permitindo a visualização gráfica.
2. Definindo as Variáveis de Entrada
O código começa criando as variáveis de entrada para cada tipo de veículo nas 4 vias (Norte, Sul, Leste e Oeste). Cada via possui 3 tipos de veículos (carros, motos e caminhões).

python
Copiar código
carros_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'carros_norte')
motos_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'motos_norte')
caminhoes_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'caminhoes_norte')
# Repete para outras vias: Sul, Leste, Oeste
Antecedent: São as variáveis de entrada do sistema fuzzy. Elas representam as condições que o sistema precisa considerar, ou seja, a quantidade de veículos (carros, motos, caminhões) em cada via.
np.arange(0, 101, 1): Cria um intervalo de valores de 0 a 100 (representando a quantidade de veículos), com um passo de 1.
3. Definindo as Variáveis de Saída (Tempo do Semáforo)
Agora, o código cria variáveis de saída que representam o tempo que o semáforo deve ficar verde para cada via:

python
Copiar código
tempo_semaforo_norte = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_norte')
# Repete para outras vias: Sul, Leste, Oeste
Consequent: São as variáveis de saída do sistema fuzzy, que representam o resultado do controle. No caso, o tempo do semáforo verde.
4. Funções de Pertinência para as Variáveis de Entrada
A função de pertinência descreve como os valores das variáveis de entrada são divididos em categorias ("baixo", "médio", "alto").

python
Copiar código
def define_pertinencia_veiculos(veiculo):
    veiculo['baixo'] = fuzz.trimf(veiculo.universe, [0, 0, 50])
    veiculo['medio'] = fuzz.trimf(veiculo.universe, [25, 50, 75])
    veiculo['alto'] = fuzz.trimf(veiculo.universe, [50, 100, 100])
fuzz.trimf: Cria uma função de pertinência triangular. O parâmetro [0, 0, 50] define o formato da função de pertinência "baixo", onde o valor 0 é o ponto inicial e 50 é o ponto de transição.
Para "médio" e "alto", as funções de pertinência são definidas de maneira semelhante, com intervalos diferentes.
Essas funções de pertinência são aplicadas a todos os tipos de veículos nas 4 vias.

5. Funções de Pertinência para as Variáveis de Saída (Tempo do Semáforo)
As funções de pertinência para o tempo do semáforo também são triangulares, dividindo o tempo em três categorias: "curto", "médio" e "longo".

python
Copiar código
tempo_semaforo_norte['curto'] = fuzz.trimf(tempo_semaforo_norte.universe, [0, 0, 30])
tempo_semaforo_norte['medio'] = fuzz.trimf(tempo_semaforo_norte.universe, [15, 30, 45])
tempo_semaforo_norte['longo'] = fuzz.trimf(tempo_semaforo_norte.universe, [30, 60, 60])
# Repete para outras vias: Sul, Leste, Oeste
[0, 0, 30] define a categoria "curto", indicando um semáforo verde de até 30 segundos.
[15, 30, 45] define a categoria "médio", e assim por diante.
6. Definindo as Regras Fuzzy
As regras fuzzy são onde a lógica de controle é definida. Elas descrevem como o sistema deve calcular o tempo de semáforo com base na quantidade de veículos.

python
Copiar código
regra1_norte = ctrl.Rule((carros_norte['alto'] | motos_norte['alto'] | caminhoes_norte['alto']), tempo_semaforo_norte['longo'])
regra2_sul = ctrl.Rule((carros_sul['alto'] | motos_sul['alto'] | caminhoes_sul['alto']), tempo_semaforo_sul['longo'])
# Repete para outras vias: Leste, Oeste
ctrl.Rule: Define uma regra fuzzy. Cada regra é composta por uma condição (baseada nos tipos de veículos nas vias) e uma ação (tempo de semáforo).
(carros_norte['alto'] | motos_norte['alto'] | caminhoes_norte['alto']): A condição indica que se a quantidade de qualquer tipo de veículo for alta, a ação será definir um tempo de semáforo longo para a via Norte.
Regras adicionais são criadas para as outras vias (Sul, Leste e Oeste), com base nas mesmas condições (veículos altos, médios ou baixos) e ações correspondentes.

7. Configurando o Sistema de Controle Fuzzy
Depois de definir as variáveis de entrada, saída e as regras, o próximo passo é configurar o sistema de controle fuzzy.

python
Copiar código
controle_semaforo_norte = ctrl.ControlSystem([regra1_norte, regra5_norte])
controle_semaforo_sul = ctrl.ControlSystem([regra2_sul, regra6_sul])
# Repete para outras vias: Leste, Oeste
ctrl.ControlSystem: Cria o sistema de controle fuzzy, onde as regras são aplicadas.
8. Simulação do Sistema
Agora que o sistema de controle está configurado, o código simula o comportamento do semáforo com valores de entrada específicos (quantidade de veículos).

python
Copiar código
simulador_norte.input['carros_norte'] = 80
simulador_norte.input['motos_norte'] = 50
simulador_norte.input['caminhoes_norte'] = 30
simulador_norte.compute()
simulador_norte.input[...]: Atribui valores para o número de veículos em cada categoria (carros, motos e caminhões) na via Norte.
simulador_norte.compute(): Executa o cálculo do sistema fuzzy com base nas regras definidas.
O mesmo processo é repetido para as outras vias (Sul, Leste e Oeste).

9. Exibindo os Resultados
Os resultados do tempo de semáforo verde para cada via são impressos.

python
Copiar código
print("Tempo de semáforo Norte:", simulador_norte.output['tempo_semaforo_norte'])
# Repete para as outras vias
simulador_norte.output[...]: Exibe o resultado do tempo do semáforo verde para a via Norte.
10. Visualizando as Funções de Pertinência
Por fim, as funções de pertinência de todas as variáveis (entrada e saída) são visualizadas para facilitar a compreensão gráfica.

python
Copiar código
fluxo_vias = [carros_norte, motos_norte, caminhoes_norte, carros_sul, motos_sul, caminhoes_sul, carros_leste, motos_leste, caminhoes_leste, carros_oeste, motos_oeste, caminhoes_oeste]
for via in fluxo_vias:
    via.view()

plt.show()
via.view(): Exibe as funções de pertinência das variáveis de entrada e saída.
plt.show(): Mostra os gráficos das funções de pertinência.
Resumo
Este código implementa um sistema de controle fuzzy para semáforos com 4 vias, considerando diferentes tipos de veículos (carros, motos, caminhões). Ele usa regras fuzzy para calcular o tempo de semáforo verde com base na quantidade de veículos em cada via, utilizando funções de pertinência para categorizar os valores de entrada e saída. O sistema é configurado, simulado e os resultados (tempos de semáforo) são exibidos. Além disso, as funções de pertinência são visualizadas graficamente para entender melhor como o sistema toma decisões.



