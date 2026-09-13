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