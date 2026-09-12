from src.data_preparation import load_data, prepare_data
from src.feature_engineering import create_features
from src.models import train_models
from src.evaluation import evaluate_model


def main():
    print("Iniciando projeto de detecção de fraudes...")

    df = load_data()

    df = create_features(df)

    X_train, X_test, y_train, y_test = prepare_data(df)

    models = train_models(X_train, y_train)

    for name, model in models.items():
        evaluate_model(
            model,
            X_test,
            y_test,
            name
        )

if __name__ == "__main__":
    main()