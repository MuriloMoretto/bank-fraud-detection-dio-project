from src.data_preparation import load_data


def main():
    df = load_data("data/creditcard.csv")

    print("Primeiras linhas:")
    print(df.head())

    print("\nDimensões do dataset:")
    print(df.shape)

    print("\nInformações do dataset:")
    df.info()

    print("\nValores nulos:")
    print(df.isnull().sum())

    print("\nDuplicatas:")
    print(df.duplicated().sum())

    print("\nDistribuição da variável Class:")
    print(df["Class"].value_counts())


if __name__ == "__main__":
    main()