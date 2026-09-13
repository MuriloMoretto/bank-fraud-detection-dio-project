def descriptive_statistics(df):
    print("\nEstatísticas descritivas:")
    print(df.describe())


def class_distribution(df):
    print("\nDistribuição da variável Class:")
    print(df["Class"].value_counts())