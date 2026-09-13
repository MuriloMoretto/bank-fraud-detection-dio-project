from src.data_preparation import load_data
from src.eda import (
    descriptive_statistics,
    class_distribution,
    plot_class_distribution,
    amount_by_class,
    plot_amount_by_class,
    time_by_class,
    duplicate_analysis,
    duplicate_by_class
)


def main():
    df = load_data("data/creditcard.csv")

    descriptive_statistics(df)
    class_distribution(df)
    plot_class_distribution(df)
    amount_by_class(df)
    plot_amount_by_class(df)
    time_by_class(df)
    duplicate_analysis(df)
    duplicate_by_class(df)


if __name__ == "__main__":
    main()