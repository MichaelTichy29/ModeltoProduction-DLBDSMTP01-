import requests
import time

from sensor_stream import sensor_stream


stream = sensor_stream(seed=42)


while True:

    # nächsten simulierten Messwert holen
    messwert = next(stream)

    # Daten für REST API
    daten = {
        "Temperatur": messwert["Temperatur"],
        "Feuchtigkeit": messwert["Feuchtigkeit"],
        "Laerm": messwert["Laerm"]
    }

    # Messwerte an API schicken
    response = requests.post(
        "http://localhost:5000/predict",
        json=daten
    )

    # Antwort der API
    prediction = response.json()

    # Ausgabe
    print(
        f"Zeit: {messwert['Zeit']:4d} | "
        f"Temp: {messwert['Temperatur']:5.1f} | "
        f"Feucht: {messwert['Feuchtigkeit']:5.1f} | "
        f"Lärm: {messwert['Laerm']:5.1f} | "
        #f"Echt: {messwert['Defekt']} | "
        f"Vorhersage: {prediction['anomalie']} | "
        f"P: {prediction['wahrscheinlichkeit']:.2f}"
    )

    # simuliert zeitlichen Abstand zwischen Messungen
    time.sleep(1)
