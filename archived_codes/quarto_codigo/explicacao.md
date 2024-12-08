
# Explicação do Código de Controle de Tráfego Usando Lógica Fuzzy

Este documento explica um código de exemplo que utiliza lógica fuzzy para ajustar dinamicamente o tempo de um semáforo com base no fluxo de veículos. A seguir, cada parte do código será descrita detalhadamente, respondendo às questões propostas.

---

## **1. Objetivo do Código**
O código visa implementar um **sistema de controle de tráfego** para determinar o tempo de permanência do semáforo verde em uma via, utilizando a lógica fuzzy. Ele considera o número de veículos como entrada e ajusta o tempo do semáforo de forma não linear e mais realista.

---

## **2. Como Funciona o Código**
### **2.1 Importação de Bibliotecas**
```python
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
```
- **`numpy`**: Gera os universos de valores contínuos.
- **`skfuzzy`**: Manipula a lógica fuzzy e funções de pertinência.
- **`matplotlib.pyplot`**: Gera gráficos para visualizar as funções de pertinência e resultados.

---

### **2.2 Definição das Variáveis Fuzzy**
#### Variável de Entrada: Número de Veículos
```python
veiculos_norte = ctrl.Antecedent(np.arange(0, 101, 1), 'veiculos_norte')
```
- Representa o número total de veículos na via norte.
- Intervalo de valores: 0 a 100.

#### Variável de Saída: Tempo de Semáforo Verde
```python
tempo_semaforo_norte = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_semaforo_norte')
```
- Define o tempo do semáforo verde em segundos.
- Intervalo de valores: 0 a 60.

---

### **2.3 Funções de Pertinência**
As funções de pertinência são modeladas como **triângulos** para representar níveis "baixo", "médio" e "alto".

#### Para Número de Veículos
```python
veiculos_norte['baixo'] = fuzz.trimf(veiculos_norte.universe, [0, 0, 50])
veiculos_norte['medio'] = fuzz.trimf(veiculos_norte.universe, [25, 50, 75])
veiculos_norte['alto'] = fuzz.trimf(veiculos_norte.universe, [50, 100, 100])
```
- **Função triangular (`fuzz.trimf`)** define os limites de cada conjunto fuzzy.

#### Para Tempo do Semáforo
```python
tempo_semaforo_norte['curto'] = fuzz.trimf(tempo_semaforo_norte.universe, [0, 0, 30])
tempo_semaforo_norte['medio'] = fuzz.trimf(tempo_semaforo_norte.universe, [15, 30, 45])
tempo_semaforo_norte['longo'] = fuzz.trimf(tempo_semaforo_norte.universe, [30, 60, 60])
```

---

### **2.4 Regras Fuzzy**
```python
regra1 = ctrl.Rule(veiculos_norte['alto'], tempo_semaforo_norte['longo'])
regra2 = ctrl.Rule(veiculos_norte['medio'], tempo_semaforo_norte['medio'])
regra3 = ctrl.Rule(veiculos_norte['baixo'], tempo_semaforo_norte['curto'])
```
- Se o número de veículos for **alto**, o tempo será **longo**.
- Se for **médio**, o tempo será **médio**.
- Se for **baixo**, o tempo será **curto**.

---

### **2.5 Simulação**
```python
simulador = ctrl.ControlSystemSimulation(controle_semaforo)
entrada_veiculos = 70
simulador.input['veiculos_norte'] = entrada_veiculos
simulador.compute()
saida_tempo_semaforo = simulador.output['tempo_semaforo_norte']
```
- Simula o sistema fuzzy com **70 veículos** como entrada.
- Calcula o tempo sugerido para o semáforo: **~49 segundos** (variável `saida_tempo_semaforo`).

---

### **2.6 Gráficos Explicativos**
Dois gráficos são gerados:
1. Função de pertinência para número de veículos.
2. Função de pertinência para o tempo do semáforo.

---

## **3. Respostas às Perguntas**
### **3.1 Como definimos a função triângulo?**
A função triangular (`fuzz.trimf`) é definida por três pontos: início, pico, e final. Exemplo:
```python
fuzz.trimf(universe, [a, b, c])
```
- **a**: Início do triângulo.
- **b**: Pico (máxima pertinência = 1).
- **c**: Final do triângulo.

### **3.2 A saída são apenas os gráficos?**
Não. Além dos gráficos, o código exibe no terminal:
```
Número de veículos na via norte: 70
Tempo sugerido para o semáforo verde (norte): 49.25 segundos
```

### **3.3 Definição dos conjuntos**
- **Baixo**: Poucos veículos (0 a 50).
- **Médio**: Fluxo moderado (25 a 75).
- **Alto**: Grande volume de veículos (50 a 100).

### **3.4 O que define fluxo lento ou rápido?**
- **Fluxo lento (baixo número de veículos)**: Semáforo verde mais curto.
- **Fluxo rápido (alto número de veículos)**: Semáforo verde mais longo.

---



## **Conclusão**
Este código demonstra como aplicar a lógica fuzzy para resolver problemas de controle de tráfego, otimizando o tempo de semáforos com base em variáveis imprecisas como o número de veículos.

