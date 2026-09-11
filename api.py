from flask import Flask, request, jsonify
import joblib
import pandas as pd


app = Flask(__name__)

# Trainiertes Modell laden
modell = joblib.load("modell.joblib")


@app.route("/predict", methods=["POST"])
def predict():

    # JSON-Daten empfangen
    daten = request.get_json()

    # DataFrame mit genau den Features erzeugen,
    # mit denen das Modell trainiert wurde
    X = pd.DataFrame([{
        "Temperatur": daten["Temperatur"],
        "Feuchtigkeit": daten["Feuchtigkeit"],
        "Laerm": daten["Laerm"]
    }])

    # Vorhersage
    prediction = modell.predict(X)[0]

    # Wahrscheinlichkeit für Defekt = 1
    wahrscheinlichkeit = modell.predict_proba(X)[0, 1]

    # Antwort der REST-API
    return jsonify({
        "anomalie": int(prediction),
        "wahrscheinlichkeit": float(wahrscheinlichkeit)
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

