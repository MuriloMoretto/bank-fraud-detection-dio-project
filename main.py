from src.data_preparation import load_data
from src.eda import descriptive_statistics, class_distribution


def main():
    df = load_data("data/creditcard.csv")

    descriptive_statistics(df)
    class_distribution(df)


if __name__ == "__main__":
    main()