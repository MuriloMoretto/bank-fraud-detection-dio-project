from src.data_preparation import load_data
from src.eda import (
    descriptive_statistics,
    class_distribution,
    plot_class_distribution,
    amount_by_class,
    plot_amount_by_class,
    time_by_class,
    duplicate_analysis,
    duplicate_by_class,
    duplicate_frequency,
    most_repeated_transactions,
    duplicate_impact,
    amount_outliers,
    plot_time_distribution,
    features_by_class,
    correlation_with_class,
    data_quality_check
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
    duplicate_frequency(df)
    most_repeated_transactions(df)
    duplicate_impact(df)
    amount_outliers(df)
    plot_time_distribution(df)
    features_by_class(df)
    correlation_with_class(df)
    data_quality_check(df)


if __name__ == "__main__":
    main()