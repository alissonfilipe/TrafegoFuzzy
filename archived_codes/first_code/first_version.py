import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variáveis de entrada
fluxo_pista_principal = ctrl.Antecedent(np.arange(0, 101, 1), 'fluxo_pista_principal')
fluxo_pista_secundaria = ctrl.Antecedent(np.arange(0, 101, 1), 'fluxo_pista_secundaria')

# Variável de saída (tempo de semáforo)
tempo_semaforo = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo')

# Funções de pertinência
fluxo_pista_principal['baixo'] = fuzz.trimf(fluxo_pista_principal.universe, [0, 0, 50])
fluxo_pista_principal['medio'] = fuzz.trimf(fluxo_pista_principal.universe, [25, 50, 75])
fluxo_pista_principal['alto'] = fuzz.trimf(fluxo_pista_principal.universe, [50, 100, 100])

fluxo_pista_secundaria['baixo'] = fuzz.trimf(fluxo_pista_secundaria.universe, [0, 0, 50])
fluxo_pista_secundaria['medio'] = fuzz.trimf(fluxo_pista_secundaria.universe, [25, 50, 75])
fluxo_pista_secundaria['alto'] = fuzz.trimf(fluxo_pista_secundaria.universe, [50, 100, 100])

tempo_semaforo['curto'] = fuzz.trimf(tempo_semaforo.universe, [0, 0, 30])
tempo_semaforo['medio'] = fuzz.trimf(tempo_semaforo.universe, [15, 30, 45])
tempo_semaforo['longo'] = fuzz.trimf(tempo_semaforo.universe, [30, 60, 60])

# Definindo algumas regras fuzzy
regra1 = ctrl.Rule(fluxo_pista_principal['alto'] & fluxo_pista_secundaria['baixo'], tempo_semaforo['longo'])
regra2 = ctrl.Rule(fluxo_pista_principal['baixo'] & fluxo_pista_secundaria['alto'], tempo_semaforo['curto'])
regra3 = ctrl.Rule(fluxo_pista_principal['medio'] | fluxo_pista_secundaria['medio'], tempo_semaforo['medio'])

# Controle do sistema fuzzy
controle_semaforo = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(controle_semaforo)

# Testando o sistema
simulador.input['fluxo_pista_principal'] = 70
simulador.input['fluxo_pista_secundaria'] = 20
simulador.compute()

print("Tempo de semáforo:", simulador.output['tempo_semaforo'])

# Plotando as funções de pertinência
fluxo_pista_principal.view()
fluxo_pista_secundaria.view()
tempo_semaforo.view()

plt.show()
