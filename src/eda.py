import matplotlib.pyplot as plt
import seaborn as sns


def descriptive_statistics(df):
    print("\nEstatísticas descritivas:")
    print(df.describe())


def class_distribution(df):
    print("\nDistribuição da variável Class:")
    print(df["Class"].value_counts())


def plot_class_distribution(df):
    sns.countplot(data=df, x="Class")

    plt.title("Distribuição das Transações")
    plt.xlabel("Classe")
    plt.ylabel("Quantidade")

    plt.show()

def amount_by_class(df):
    print("\nEstatísticas do Amount por classe:")
    print(df.groupby("Class")["Amount"].describe())

def plot_amount_by_class(df):
    sns.boxplot(data=df, x="Class", y="Amount")

    plt.title("Distribuição do valor das transações por classe")
    plt.xlabel("Classe")
    plt.ylabel("Valor da transação")

    plt.show()

def time_by_class(df):
    print("\nEstatísticas do Time por classe:")
    print(df.groupby("Class")["Time"].describe())

def duplicate_analysis(df):
    duplicates = df.duplicated().sum()

    print("\nAnálise de duplicatas:")
    print(f"Quantidade de registros duplicados: {duplicates}")

def duplicate_by_class(df):
    duplicated_rows = df[df.duplicated(keep=False)]

    print("\nDuplicatas por classe:")
    print(duplicated_rows["Class"].value_counts())

def duplicate_frequency(df):
    duplicated_rows = df[df.duplicated(keep=False)]

    frequencies = duplicated_rows.value_counts()

    print("\nFrequência das duplicatas:")
    print(frequencies.value_counts().sort_index())

def most_repeated_transactions(df):
    frequencies = df.value_counts()

    print("\nTransações mais repetidas:")
    print(frequencies[frequencies >= 9])

def duplicate_impact(df):
    df_without_duplicates = df.drop_duplicates()

    removed = len(df) - len(df_without_duplicates)

    fraud_original = df["Class"].sum()
    fraud_without_duplicates = df_without_duplicates["Class"].sum()

    print("\nImpacto das duplicatas:")
    print(f"Registros originais: {len(df)}")
    print(f"Registros após remoção: {len(df_without_duplicates)}")
    print(f"Registros removidos: {removed}")
    print(f"Fraudes originais: {fraud_original}")
    print(f"Fraudes após remoção: {fraud_without_duplicates}")
    print(f"Fraudes removidas: {fraud_original - fraud_without_duplicates}")

def amount_outliers(df):
    q1 = df["Amount"].quantile(0.25)
    q3 = df["Amount"].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = df[
        (df["Amount"] < lower_limit) |
        (df["Amount"] > upper_limit)
    ]

    print("\nAnálise de outliers do Amount:")
    print(f"Q1: {q1:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"IQR: {iqr:.2f}")
    print(f"Limite inferior: {lower_limit:.2f}")
    print(f"Limite superior: {upper_limit:.2f}")
    print(f"Quantidade de outliers: {len(outliers)}")

def plot_time_distribution(df):
    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="Time",
        hue="Class",
        bins=50,
        element="step",
        stat="count"
    )

    plt.title("Distribuição das transações ao longo do tempo")
    plt.xlabel("Tempo (segundos)")
    plt.ylabel("Quantidade")

    plt.show()

def features_by_class(df):
    features = [f"V{i}" for i in range(1, 29)]

    print("\nMédia das variáveis V1-V28 por classe:")
    print(df.groupby("Class")[features].mean().T)

def correlation_with_class(df):
    correlations = df.corr()["Class"].sort_values(ascending=False)

    print("\nCorrelação das variáveis com Class:")
    print(correlations)

def data_quality_check(df):
    print("\nVerificação final da qualidade dos dados:")

    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")

    print("\nValores ausentes:")
    print(df.isnull().sum().sum())

    print("\nDuplicatas:")
    print(df.duplicated().sum())

    print("\nTipos de dados:")
    print(df.dtypes.value_counts())