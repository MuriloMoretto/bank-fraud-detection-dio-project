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