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