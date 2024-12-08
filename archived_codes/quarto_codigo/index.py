import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variáveis de entrada (número total de veículos na via)
veiculos_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'veiculos_norte')
tempo_semaforo_norte = ctrl.Consequent(
    np.arange(0, 61, 1), 'tempo_semaforo_norte')

# Funções de pertinência para o número de veículos
veiculos_norte['baixo'] = fuzz.trimf(veiculos_norte.universe, [0, 0, 50])
veiculos_norte['medio'] = fuzz.trimf(veiculos_norte.universe, [25, 50, 75])
veiculos_norte['alto'] = fuzz.trimf(veiculos_norte.universe, [50, 100, 100])

# Funções de pertinência para o tempo do semáforo
tempo_semaforo_norte['curto'] = fuzz.trimf(
    tempo_semaforo_norte.universe, [0, 0, 30])
tempo_semaforo_norte['medio'] = fuzz.trimf(
    tempo_semaforo_norte.universe, [15, 30, 45])
tempo_semaforo_norte['longo'] = fuzz.trimf(
    tempo_semaforo_norte.universe, [30, 60, 60])

# Regras fuzzy
regra1 = ctrl.Rule(veiculos_norte['alto'], tempo_semaforo_norte['longo'])
regra2 = ctrl.Rule(veiculos_norte['medio'], tempo_semaforo_norte['medio'])
regra3 = ctrl.Rule(veiculos_norte['baixo'], tempo_semaforo_norte['curto'])

# Sistema de controle fuzzy
controle_semaforo = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(controle_semaforo)

# Simulação de um exemplo
entrada_veiculos = 70  # Número de veículos na via norte
simulador.input['veiculos_norte'] = entrada_veiculos
simulador.compute()

# Saída calculada
saida_tempo_semaforo = simulador.output['tempo_semaforo_norte']

# Exibindo no terminal
print(f"\n===== Simulação de Controle de Tráfego =====")
print(f"Número de veículos na via norte: {entrada_veiculos}")
print(f"Tempo sugerido para o semáforo verde (norte): {
      saida_tempo_semaforo:.2f} segundos")
print(f"===========================================\n")

# Interface Gráfica Explicativa
plt.figure(figsize=(12, 8))

# Subplot para o número de veículos
plt.subplot(2, 1, 1)
plt.title("Funções de Pertinência: Número de Veículos (Norte)", fontsize=14)
plt.plot(veiculos_norte.universe,
         veiculos_norte['baixo'].mf, label='Baixo', color='blue')
plt.plot(veiculos_norte.universe,
         veiculos_norte['medio'].mf, label='Médio', color='green')
plt.plot(veiculos_norte.universe,
         veiculos_norte['alto'].mf, label='Alto', color='red')
plt.axvline(x=entrada_veiculos, color='black', linestyle='--',
            label=f"Entrada: {entrada_veiculos} veículos")
plt.xlabel('Número de Veículos', fontsize=12)
plt.ylabel('Grau de Pertinência', fontsize=12)
plt.legend(loc='upper right')
plt.grid()

# Subplot para o tempo do semáforo
plt.subplot(2, 1, 2)
plt.title("Funções de Pertinência: Tempo de Semáforo (Norte)", fontsize=14)
plt.plot(tempo_semaforo_norte.universe,
         tempo_semaforo_norte['curto'].mf, label='Curto', color='purple')
plt.plot(tempo_semaforo_norte.universe,
         tempo_semaforo_norte['medio'].mf, label='Médio', color='orange')
plt.plot(tempo_semaforo_norte.universe,
         tempo_semaforo_norte['longo'].mf, label='Longo', color='brown')
plt.axvline(x=saida_tempo_semaforo, color='black', linestyle='--',
            label=f"Saída: {saida_tempo_semaforo:.2f} segundos")
plt.xlabel('Tempo de Semáforo (segundos)', fontsize=12)
plt.ylabel('Grau de Pertinência', fontsize=12)
plt.legend(loc='upper right')
plt.grid()

plt.tight_layout()
plt.show()
