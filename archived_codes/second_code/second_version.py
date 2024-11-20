import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variáveis de entrada (número de veículos em cada via)
carros_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'carros_norte')
motos_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'motos_norte')
caminhoes_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'caminhoes_norte')

carros_sul = ctrl.Antecedent(np.arange(0, 101, 1), 'carros_sul')
motos_sul = ctrl.Antecedent(np.arange(0, 101, 1), 'motos_sul')
caminhoes_sul = ctrl.Antecedent(np.arange(0, 101, 1), 'caminhoes_sul')

carros_leste = ctrl.Antecedent(np.arange(0, 101, 1), 'carros_leste')
motos_leste = ctrl.Antecedent(np.arange(0, 101, 1), 'motos_leste')
caminhoes_leste = ctrl.Antecedent(np.arange(0, 101, 1), 'caminhoes_leste')

carros_oeste = ctrl.Antecedent(np.arange(0, 101, 1), 'carros_oeste')
motos_oeste = ctrl.Antecedent(np.arange(0, 101, 1), 'motos_oeste')
caminhoes_oeste = ctrl.Antecedent(np.arange(0, 101, 1), 'caminhoes_oeste')

# Variável de saída (tempo do semáforo verde)
tempo_semaforo_norte = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_norte')
tempo_semaforo_sul = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_sul')
tempo_semaforo_leste = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_leste')
tempo_semaforo_oeste = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_oeste')

# Funções de pertinência para as variáveis de entrada (número de veículos)
def define_pertinencia_veiculos(veiculo):
    veiculo['baixo'] = fuzz.trimf(veiculo.universe, [0, 0, 50])
    veiculo['medio'] = fuzz.trimf(veiculo.universe, [25, 50, 75])
    veiculo['alto'] = fuzz.trimf(veiculo.universe, [50, 100, 100])

# Definir as funções de pertinência para todos os veículos nas 4 vias
define_pertinencia_veiculos(carros_norte)
define_pertinencia_veiculos(motos_norte)
define_pertinencia_veiculos(caminhoes_norte)

define_pertinencia_veiculos(carros_sul)
define_pertinencia_veiculos(motos_sul)
define_pertinencia_veiculos(caminhoes_sul)

define_pertinencia_veiculos(carros_leste)
define_pertinencia_veiculos(motos_leste)
define_pertinencia_veiculos(caminhoes_leste)

define_pertinencia_veiculos(carros_oeste)
define_pertinencia_veiculos(motos_oeste)
define_pertinencia_veiculos(caminhoes_oeste)

# Funções de pertinência para os tempos de semáforo (variável de saída)
tempo_semaforo_norte['curto'] = fuzz.trimf(tempo_semaforo_norte.universe, [0, 0, 30])
tempo_semaforo_norte['medio'] = fuzz.trimf(tempo_semaforo_norte.universe, [15, 30, 45])
tempo_semaforo_norte['longo'] = fuzz.trimf(tempo_semaforo_norte.universe, [30, 60, 60])

tempo_semaforo_sul['curto'] = fuzz.trimf(tempo_semaforo_sul.universe, [0, 0, 30])
tempo_semaforo_sul['medio'] = fuzz.trimf(tempo_semaforo_sul.universe, [15, 30, 45])
tempo_semaforo_sul['longo'] = fuzz.trimf(tempo_semaforo_sul.universe, [30, 60, 60])

tempo_semaforo_leste['curto'] = fuzz.trimf(tempo_semaforo_leste.universe, [0, 0, 30])
tempo_semaforo_leste['medio'] = fuzz.trimf(tempo_semaforo_leste.universe, [15, 30, 45])
tempo_semaforo_leste['longo'] = fuzz.trimf(tempo_semaforo_leste.universe, [30, 60, 60])

tempo_semaforo_oeste['curto'] = fuzz.trimf(tempo_semaforo_oeste.universe, [0, 0, 30])
tempo_semaforo_oeste['medio'] = fuzz.trimf(tempo_semaforo_oeste.universe, [15, 30, 45])
tempo_semaforo_oeste['longo'] = fuzz.trimf(tempo_semaforo_oeste.universe, [30, 60, 60])

# Regras fuzzy para o tempo de semáforo baseado nos tipos de veículos
regra1_norte = ctrl.Rule((carros_norte['alto'] | motos_norte['alto'] | caminhoes_norte['alto']), tempo_semaforo_norte['longo'])
regra2_sul = ctrl.Rule((carros_sul['alto'] | motos_sul['alto'] | caminhoes_sul['alto']), tempo_semaforo_sul['longo'])
regra3_leste = ctrl.Rule((carros_leste['alto'] | motos_leste['alto'] | caminhoes_leste['alto']), tempo_semaforo_leste['longo'])
regra4_oeste = ctrl.Rule((carros_oeste['alto'] | motos_oeste['alto'] | caminhoes_oeste['alto']), tempo_semaforo_oeste['longo'])

regra5_norte = ctrl.Rule((carros_norte['medio'] | motos_norte['medio'] | caminhoes_norte['medio']), tempo_semaforo_norte['medio'])
regra6_sul = ctrl.Rule((carros_sul['medio'] | motos_sul['medio'] | caminhoes_sul['medio']), tempo_semaforo_sul['medio'])
regra7_leste = ctrl.Rule((carros_leste['medio'] | motos_leste['medio'] | caminhoes_leste['medio']), tempo_semaforo_leste['medio'])
regra8_oeste = ctrl.Rule((carros_oeste['medio'] | motos_oeste['medio'] | caminhoes_oeste['medio']), tempo_semaforo_oeste['medio'])

# Controle do sistema fuzzy
controle_semaforo_norte = ctrl.ControlSystem([regra1_norte, regra5_norte])
controle_semaforo_sul = ctrl.ControlSystem([regra2_sul, regra6_sul])
controle_semaforo_leste = ctrl.ControlSystem([regra3_leste, regra7_leste])
controle_semaforo_oeste = ctrl.ControlSystem([regra4_oeste, regra8_oeste])

# Simuladores
simulador_norte = ctrl.ControlSystemSimulation(controle_semaforo_norte)
simulador_sul = ctrl.ControlSystemSimulation(controle_semaforo_sul)
simulador_leste = ctrl.ControlSystemSimulation(controle_semaforo_leste)
simulador_oeste = ctrl.ControlSystemSimulation(controle_semaforo_oeste)

# Testando o sistema com um cenário
simulador_norte.input['carros_norte'] = 80
simulador_norte.input['motos_norte'] = 50
simulador_norte.input['caminhoes_norte'] = 30
simulador_norte.compute()

simulador_sul.input['carros_sul'] = 40
simulador_sul.input['motos_sul'] = 20
simulador_sul.input['caminhoes_sul'] = 10
simulador_sul.compute()

simulador_leste.input['carros_leste'] = 60
simulador_leste.input['motos_leste'] = 10
simulador_leste.input['caminhoes_leste'] = 5
simulador_leste.compute()

simulador_oeste.input['carros_oeste'] = 20
simulador_oeste.input['motos_oeste'] = 30
simulador_oeste.input['caminhoes_oeste'] = 15
simulador_oeste.compute()

# Exibir os resultados
print("Tempo de semáforo Norte:", simulador_norte.output['tempo_semaforo_norte'])
print("Tempo de semáforo Sul:", simulador_sul.output['tempo_semaforo_sul'])
print("Tempo de semáforo Leste:", simulador_leste.output['tempo_semaforo_leste'])
print("Tempo de semáforo Oeste:", simulador_oeste.output['tempo_semaforo_oeste'])

# Plotando as funções de pertinência
fluxo_vias = [carros_norte, motos_norte, caminhoes_norte,
              carros_sul, motos_sul, caminhoes_sul,
              carros_leste, motos_leste, caminhoes_leste,
              carros_oeste, motos_oeste, caminhoes_oeste]

for via in fluxo_vias:
    via.view()

plt.show()
