# Detecção de Fraudes em Transações

Projeto de análise de dados desenvolvido em Python com foco na exploração e compreensão de um conjunto de dados de transações bancárias, buscando identificar características associadas às transações fraudulentas.

## Objetivo

O objetivo inicial do projeto é realizar uma Análise Exploratória de Dados (EDA) sobre um conjunto de transações bancárias, investigando:

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
- Jupyter Notebook

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

### 1. Estrutura dos dados

O dataset possui:

```text
Linhas: 284.807
Colunas: 31