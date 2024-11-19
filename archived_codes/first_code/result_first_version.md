# A saída são apenas os gráficos?
Não. Além dos gráficos das funções de pertinência, o código também mostra o resultado numérico do tempo de semáforo calculado pelo sistema fuzzy. Este resultado é exibido pelo print, com a linha:

python```

print("Tempo de semáforo:", simulador.output['tempo_semaforo'])
Se você quer destacar mais os resultados, pode adicionar um formato mais estruturado ou gráficos adicionais, como:
```
python```

print(f"O tempo calculado para o semáforo é: {simulador.output['tempo_semaforo']:.2f} segundos.")
```
# Definição dos conjuntos
Cada conjunto fuzzy foi definido usando funções de pertinência triangulares (trimf). Os valores de entrada estão no intervalo:

Fluxo das pistas (principal e secundária): 0 a 100.

- `baixo: [0, 0, 50]`
- `médio: [25, 50, 75]`
- `alto: [50, 100, 100]`
- `Tempo do semáforo: 0 a 60 segundos.`
<br>

- `curto: [0, 0, 30]`
- `médio: [15, 30, 45]`
- `longo: [30, 60, 60]`
Esses valores definem os limites do comportamento fuzzy para cada variável.

# O que define fluxo lento ou rápido?
Os fluxos são classificados em três categorias (baixo, médio, alto) dependendo dos valores:

Fluxo lento: Quando o valor de fluxo está dentro do intervalo baixo ou próximo aos limites inferiores do médio.

Exemplo: fluxo_pista_principal['baixo'] é verdadeiro para valores próximos de 0 a 50.
Fluxo rápido: Quando o valor de fluxo está no intervalo alto ou próximo ao limite superior do médio.

Exemplo: fluxo_pista_principal['alto'] é verdadeiro para valores acima de 75.
Isso é controlado pelas funções de pertinência triangulares. Cada ponto no intervalo de entrada tem um grau de associação (grau de pertinência) que define se o fluxo é lento ou rápido.

Gráficos e Resultados
Para complementar a visualização, o código já desenha os gráficos das funções de pertinência. Além disso, você pode plotar o resultado final para uma entrada específica:

´´´python
Copiar código
tempo_semaforo.view(sim=simulador)
plt.show()
´´´
Este comando visualiza o grau de pertinência do resultado calculado (tempo do semáforo), destacando a faixa em que ele se encaixa.