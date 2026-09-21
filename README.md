# Detecção de Fraudes em Transações

Projeto de análise de dados desenvolvido em Python com foco na exploração e compreensão de um conjunto de dados de transações bancárias, buscando identificar características associadas às transações fraudulentas.

## Objetivo

O objetivo do projeto é realizar uma Análise Exploratória de Dados (EDA) sobre um conjunto de transações bancárias, investigando:

- Estrutura e qualidade dos dados;
- Distribuição das classes;
- Desbalanceamento entre transações normais e fraudulentas;
- Distribuição dos valores das transações;
- Distribuição temporal das transações;
- Registros duplicados;
- Possíveis outliers;
- Comportamento das variáveis anonimizadas `V1` a `V28`;
- Correlação das variáveis com a classe de fraude.

A análise serve como etapa inicial para compreender o conjunto de dados e identificar pontos que deverão ser considerados em uma futura etapa de modelagem de Machine Learning.

## Tecnologias e Bibliotecas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset

Foi utilizado o dataset **Credit Card Fraud Detection**, disponibilizado no Kaggle.

O conjunto de dados contém:

- **284.807 transações**
- **31 colunas**
- **492 transações fraudulentas**
- **284.315 transações normais**

A variável `Class` representa a classificação da transação:

- `0` → transação normal
- `1` → transação fraudulenta

As variáveis `V1` a `V28` são variáveis anonimizadas resultantes de uma transformação por PCA. Por esse motivo, não é possível atribuir diretamente um significado de negócio individual a cada uma delas.

A variável `Amount` representa o valor da transação e `Time` representa o tempo decorrido desde a primeira transação registrada no conjunto de dados.

> **Fonte:** Kaggle — Credit Card Fraud Detection  
> https://www.kaggle.com/mlg-ulb/creditcardfraud

## Análise Exploratória de Dados

A EDA foi realizada utilizando Pandas, Matplotlib e Seaborn.

A análise foi dividida em testes individuais, permitindo investigar diferentes características do conjunto de dados.

### 1. Estrutura dos dados

O dataset possui:

```text
Linhas: 284.807
Colunas: 31
```

Todas as colunas possuem 284.807 registros preenchidos.

Não foram encontrados valores ausentes.

### 2. Distribuição das classes

A distribuição encontrada foi:

| Classe | Quantidade |
|---|---:|
| Normal (`0`) | 284.315 |
| Fraude (`1`) | 492 |

As transações fraudulentas representam aproximadamente **0,17%** do conjunto de dados.

Isso demonstra um forte desbalanceamento entre as classes, sendo um ponto importante para uma futura etapa de modelagem.

### 3. Estatísticas descritivas

Foram analisadas as estatísticas descritivas das variáveis numéricas utilizando `DataFrame.describe()`.

Entre os resultados observados, a variável `Amount` apresentou:

- Mediana: aproximadamente 22;
- Média: aproximadamente 88,35;
- Valor máximo: aproximadamente 25.691,16.

A diferença entre média e mediana indica uma distribuição assimétrica dos valores das transações.

### 4. Distribuição do `Amount`

Foi analisada a distribuição dos valores das transações e também realizada uma análise de possíveis outliers utilizando o método do Intervalo Interquartil (IQR).

Os valores encontrados foram:

```text
Q1: 5,60
Q3: 77,16
IQR: 71,56
Limite inferior: -101,75
Limite superior: 184,51
```

Foram identificados **31.904 registros** acima ou abaixo dos limites definidos pelo método IQR.

Esses registros não foram removidos automaticamente, pois um valor considerado outlier estatisticamente não necessariamente representa um erro nos dados. Em um problema de detecção de fraude, valores extremos também podem possuir relevância para a análise.

### 5. Distribuição temporal

A variável `Time` foi analisada para observar a distribuição das transações ao longo do período registrado.

Também foi realizada uma comparação visual da distribuição temporal entre as classes normal e fraudulenta.

O gráfico correspondente foi salvo na pasta `reports/figures/`.

### 6. Análise de duplicatas

Foram encontrados:

```text
1.081 registros duplicados
```

Uma análise adicional mostrou que existem grupos de transações que aparecem múltiplas vezes no dataset.

A frequência encontrada entre os registros duplicados foi:

| Frequência | Quantidade de grupos |
|---:|---:|
| 2 | 611 |
| 3 | 66 |
| 4 | 81 |
| 5 | 10 |
| 6 | 1 |
| 9 | 2 |
| 18 | 2 |

As duplicatas foram identificadas e analisadas, mas não foram removidas automaticamente nesta etapa do projeto.

### 7. Análise das variáveis `V1` a `V28`

Foram comparadas as médias das variáveis anonimizadas entre as classes.

Algumas variáveis apresentaram diferenças consideráveis entre transações normais e fraudulentas, principalmente:

- `V3`
- `V7`
- `V10`
- `V12`
- `V14`
- `V17`

Como essas variáveis são anonimizadas, não foram atribuídos significados específicos a elas.

### 8. Correlação com a variável `Class`

Foi calculada a correlação de Pearson entre as variáveis numéricas e a variável `Class`.

As maiores correlações em valor absoluto foram:

| Variável | Correlação |
|---|---:|
| `V17` | -0,326481 |
| `V14` | -0,302544 |
| `V12` | -0,260593 |
| `V10` | -0,216883 |
| `V16` | -0,196539 |
| `V3` | -0,192961 |
| `V7` | -0,187257 |
| `V11` | +0,154876 |
| `V4` | +0,133447 |

A variável `Amount`, por outro lado, apresentou correlação linear próxima de zero com `Class`:

```text
Amount: 0,005632
```

A análise de correlação foi utilizada como ferramenta exploratória e não como critério isolado para determinar a importância das variáveis.

## Qualidade dos Dados

A verificação final apresentou:

```text
Linhas: 284807
Colunas: 31

Valores ausentes: 0

Duplicatas: 1081

Tipos de dados:
float64: 30
int64: 1
```

Dessa forma, não foram identificados valores ausentes no conjunto de dados.

O principal ponto de atenção identificado durante a EDA foram os registros duplicados, que deverão ser considerados em uma eventual etapa de preparação dos dados.

## Visualizações

Durante a EDA foram geradas e armazenadas algumas visualizações para auxiliar na interpretação dos dados.

Os gráficos produzidos estão organizados em:

```text
reports/
└── figures/
```

Atualmente, a pasta contém:

- `Test 3 graph.png`
- `Test 5 graph.png`
- `Test 13 graph.png`

Essas visualizações correspondem a análises realizadas durante a exploração do conjunto de dados.

## Organização dos Testes

Para manter o processo de desenvolvimento organizado e registrar a evolução da análise, os testes realizados durante a EDA foram separados em diretórios.

A estrutura utilizada é:

```text
tests performed/
├── test1/
├── test2/
├── test3/
├── test4/
├── test5/
├── test6/
├── test7/
├── test8/
├── test9/
├── test10/
├── test11/
├── test12/
├── test13/
├── test14/
├── test15/
├── test16/
└── test17 - summary/
```

Essa organização permite acompanhar individualmente cada etapa da análise exploratória e registrar os resultados obtidos.

## Estrutura do Projeto

```text
bank-fraud-detection-dio-project/
│
├── reports/
│   └── figures/
│       ├── Test 3 graph.png
│       ├── Test 5 graph.png
│       └── Test 13 graph.png
│
├── src/
│   ├── __init__.py
│   ├── data_preparation.py
│   └── eda.py
│
├── tests performed/
│   ├── test1/
│   ├── test2/
│   ├── test3/
│   ├── test4/
│   ├── test5/
│   ├── test6/
│   ├── test7/
│   ├── test8/
│   ├── test9/
│   ├── test10/
│   ├── test11/
│   ├── test12/
│   ├── test13/
│   ├── test14/
│   ├── test15/
│   ├── test16/
│   └── test17 - summary/
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

> O arquivo `creditcard.csv` não é versionado no GitHub devido ao seu tamanho e está incluído no `.gitignore`. Para executar o projeto localmente, o dataset deve ser baixado da fonte indicada na seção **Dataset** e colocado na pasta `data/`.

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/MuriloMoretto/bank-fraud-detection-dio-project.git
```

### 2. Entrar na pasta do projeto

```bash
cd bank-fraud-detection-dio-project
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 6. Adicionar o dataset

Baixe o arquivo `creditcard.csv` a partir da fonte indicada na seção **Dataset**.

Depois, coloque o arquivo na seguinte localização:

```text
data/creditcard.csv
```

### 7. Executar a análise

```bash
python main.py
```

## Resultados da EDA

A análise exploratória permitiu identificar os principais aspectos do conjunto de dados:

- Forte desbalanceamento entre transações normais e fraudulentas;
- Ausência de valores nulos;
- Presença de 1.081 registros duplicados;
- Presença de uma quantidade significativa de possíveis outliers na variável `Amount`;
- Diferenças nas médias de algumas variáveis anonimizadas entre as classes;
- Algumas variáveis apresentam maior correlação linear com `Class`;
- `Amount` apresenta correlação linear muito baixa com a classe de fraude.

Esses resultados fornecem uma visão inicial do dataset e ajudam a definir os cuidados necessários para uma futura etapa de Machine Learning.

## Limitações da Versão Atual

A versão atual do projeto está concentrada na **Análise Exploratória de Dados (EDA)**.

Não foram implementados, nesta versão:

- Modelos de Machine Learning;
- `Train/Test Split`;
- `StandardScaler`;
- SMOTE;
- Logistic Regression;
- Random Forest;
- XGBoost;
- GridSearchCV;
- SHAP;
- Métricas de avaliação de modelos;
- Matriz de confusão de modelos.

Esses recursos fazem parte de possíveis evoluções futuras do projeto.

## Próximos Passos

Como evolução futura, o projeto poderá incluir:

- Tratamento das duplicatas;
- Preparação das variáveis;
- Separação entre treino e teste;
- Normalização dos dados;
- Técnicas para lidar com o desbalanceamento das classes;
- Treinamento de modelos de classificação;
- Avaliação utilizando métricas apropriadas para detecção de fraudes;
- Comparação entre diferentes algoritmos;
- Otimização de hiperparâmetros;
- Técnicas de explicabilidade dos modelos.

## Sobre o Projeto

Projeto desenvolvido como parte do **Bootcamp Bradesco - GenAI, Dados & Cyber**, da DIO.

**Unidade:**  
Análise de Dados com Python: Da Preparação à Aplicação com Segurança

**Desafio de Projeto:**  
Detecção de Anomalias em Transações em Python

O projeto foi desenvolvido com foco no aprendizado prático de análise de dados utilizando Python, desde o carregamento e inspeção do dataset até a realização de uma análise exploratória completa.

---

**Produzido e arquitetado por Murilo Moretto.**