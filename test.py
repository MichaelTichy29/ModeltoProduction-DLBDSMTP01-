import requests

daten = {
    "Temperatur": 25.0,
    "Feuchtigkeit": 60.0,
    "Laerm": 50.0
}

response = requests.post(
    "http://127.0.0.1:5000/predict",
    json=daten
)

print(response.status_code)
print(response.json())

