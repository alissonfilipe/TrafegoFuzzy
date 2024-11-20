import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variáveis de entrada (número total de veículos na via)
veiculos_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'veiculos_norte')
veiculos_sul = ctrl.Antecedent(np.arange(0, 101, 1), 'veiculos_sul')
veiculos_leste = ctrl.Antecedent(np.arange(0, 101, 1), 'veiculos_leste')
veiculos_oeste = ctrl.Antecedent(np.arange(0, 101, 1), 'veiculos_oeste')

# Variáveis de saída (tempo do semáforo verde)
tempo_semaforo_norte = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_norte')
tempo_semaforo_sul = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_sul')
tempo_semaforo_leste = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_leste')
tempo_semaforo_oeste = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_oeste')

# Funções de pertinência para o número de veículos
def define_pertinencia_veiculos(veiculo):
    veiculo['baixo'] = fuzz.trimf(veiculo.universe, [0, 0, 50])
    veiculo['medio'] = fuzz.trimf(veiculo.universe, [25, 50, 75])
    veiculo['alto'] = fuzz.trimf(veiculo.universe, [50, 100, 100])

# Aplicando as funções de pertinência para as variáveis de entrada
define_pertinencia_veiculos(veiculos_norte)
define_pertinencia_veiculos(veiculos_sul)
define_pertinencia_veiculos(veiculos_leste)
define_pertinencia_veiculos(veiculos_oeste)

# Funções de pertinência para o tempo do semáforo
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

# Definindo as regras fuzzy
regra1_norte = ctrl.Rule(veiculos_norte['alto'], tempo_semaforo_norte['longo'])
regra2_norte = ctrl.Rule(veiculos_norte['medio'], tempo_semaforo_norte['medio'])
regra3_norte = ctrl.Rule(veiculos_norte['baixo'], tempo_semaforo_norte['curto'])

regra1_sul = ctrl.Rule(veiculos_sul['alto'], tempo_semaforo_sul['longo'])
regra2_sul = ctrl.Rule(veiculos_sul['medio'], tempo_semaforo_sul['medio'])
regra3_sul = ctrl.Rule(veiculos_sul['baixo'], tempo_semaforo_sul['curto'])

regra1_leste = ctrl.Rule(veiculos_leste['alto'], tempo_semaforo_leste['longo'])
regra2_leste = ctrl.Rule(veiculos_leste['medio'], tempo_semaforo_leste['medio'])
regra3_leste = ctrl.Rule(veiculos_leste['baixo'], tempo_semaforo_leste['curto'])

regra1_oeste = ctrl.Rule(veiculos_oeste['alto'], tempo_semaforo_oeste['longo'])
regra2_oeste = ctrl.Rule(veiculos_oeste['medio'], tempo_semaforo_oeste['medio'])
regra3_oeste = ctrl.Rule(veiculos_oeste['baixo'], tempo_semaforo_oeste['curto'])

# Sistema de controle fuzzy para cada via
controle_semaforo_norte = ctrl.ControlSystem([regra1_norte, regra2_norte, regra3_norte])
controle_semaforo_sul = ctrl.ControlSystem([regra1_sul, regra2_sul, regra3_sul])
controle_semaforo_leste = ctrl.ControlSystem([regra1_leste, regra2_leste, regra3_leste])
controle_semaforo_oeste = ctrl.ControlSystem([regra1_oeste, regra2_oeste, regra3_oeste])

# Simuladores para cada via
simulador_norte = ctrl.ControlSystemSimulation(controle_semaforo_norte)
simulador_sul = ctrl.ControlSystemSimulation(controle_semaforo_sul)
simulador_leste = ctrl.ControlSystemSimulation(controle_semaforo_leste)
simulador_oeste = ctrl.ControlSystemSimulation(controle_semaforo_oeste)

# Testando o sistema com um exemplo de fluxo de veículos
simulador_norte.input['veiculos_norte'] = 70
simulador_sul.input['veiculos_sul'] = 40
simulador_leste.input['veiculos_leste'] = 30
simulador_oeste.input['veiculos_oeste'] = 20

# Calculando o tempo de semáforo
simulador_norte.compute()
simulador_sul.compute()
simulador_leste.compute()
simulador_oeste.compute()

# Exibindo os tempos de semáforo
print("Tempo de semáforo Norte:", simulador_norte.output['tempo_semaforo_norte'])
print("Tempo de semáforo Sul:", simulador_sul.output['tempo_semaforo_sul'])
print("Tempo de semáforo Leste:", simulador_leste.output['tempo_semaforo_leste'])
print("Tempo de semáforo Oeste:", simulador_oeste.output['tempo_semaforo_oeste'])

# Plotando as funções de pertinência
veiculos_norte.view()
veiculos_sul.view()
veiculos_leste.view()
veiculos_oeste.view()
tempo_semaforo_norte.view()
tempo_semaforo_sul.view()
tempo_semaforo_leste.view()
tempo_semaforo_oeste.view()

plt.show()
