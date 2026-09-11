
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from Testdaten import testdata_rampe, testdata_simple
import joblib


def train_model(test=2):

    if test ==1:
        df = testdata_simple(1000)
    elif test ==2: 
        df = testdata_rampe(1000)
    
    
    # -------------------------
    # 1. Merkmale und Zielwert
    # -------------------------

    X = df[[
        "Temperatur",
        "Feuchtigkeit",
        "Laerm"
    ]]

    y = df["Defekt"]


    # -------------------------
    # 2. Train-Test-Split
    # -------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    
    # -------------------------
    # 3. Logistische Regression
    # -------------------------

    modell = LogisticRegression()

    modell.fit(
        X_train,
        y_train
    )


    # -------------------------
    # 4. Vorhersage
    # -------------------------

    y_pred = modell.predict(X_test)


    # -------------------------
    # 5. Confusion Matrix
    # -------------------------

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print("Confusion Matrix:")
    print(cm)

    ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["OK", "Defekt"]
    ).plot()

    plt.show()


    return modell

modell = train_model(1)

joblib.dump(modell, "modell.joblib")
