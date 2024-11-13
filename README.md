# árvore do projeto

ControleDeTrafegoUrbano/
├── src/                           # Código principal do projeto<br>
│   ├── main.py                    # Arquivo principal que executa o sistema de controle de tráfego<br>
│   ├── fuzzy_controller.py        # Código para configurar e calcular o controle fuzzy<br>
│   ├── rules/                     # Pasta para definir regras fuzzy complexas<br>
│   │   ├── traffic_rules.py       # Regras específicas para o controle de tráfego<br>
│   └── utils/                     # Funções auxiliares que podem ser reutilizadas<br>
│       └── fuzzy_utils.py         # Funções de apoio ao sistema fuzzy<br>
│<br>
├── data/                          # Dados para simulação (ex. valores históricos ou testes)<br>
│   └── example_inputs.json        # Exemplos de inputs para teste<br>
│<br>
├── tests/                         # Testes automatizados para o projeto<br>
│   └── test_fuzzy_controller.py   # Testes das funções do controlador fuzzy<br>
│<br>
├── docs/                          # Documentação do projeto<br>
│   └── README.md                  # Documentação geral e instruções de uso<br>
│<br>
├── archived_codes/                # Códigos antigos para estudo e referência<br>
│   └── old_controller_version.py  # Versões anteriores ou experimentais do controlador fuzzy<br>
│<br>
├── requirements.txt               # Dependências do projeto<br>
└── .env                           # Arquivo do ambiente virtual (opcional, pode ficar na raiz)<br>


# coisas para resolver
- como definimos a função triângulo
- a saída são apenas os gráficos `precisda mostrar gráficos com resultados`
- definição dos conjuntos
- o que define fluxo lento ou rápido


# Controle de Tráfego Urbano

Desenvolver um sistema de gerenciamento de tráfego que utiliza lógica fuzzy para otimizar os sinais de trânsito com base em variáveis como fluxo de veículos, condições climáticas e horários de pico.

Problematização: Como a lógica nebulosa pode otimizar  o tempo de resposta dos semáforos em cruzamentos movimentados, minimizando o congestionamento e o tempo de espera dos veículos, principalmente em horários de pico?


# instalação das dependências
<hr>

`pip install -r requirements.txt` - esse comando serve para a instalação das dependências

<hr>

`pip show numpy` - mostrar a versão da dependência

<hr>

# Anotações

as dependências do projeto estão armazenadas no ambiente virtual
- nesse projeto usamos o ambiente venv `ambiente virtual` com as dependências
pois isso é necessários rodar o comando
- `python -m venv .env`
- o `.env` é o nome do ambiente virtual
- `.env\Scripts\activate` caminho para ativação do ambiente virtual