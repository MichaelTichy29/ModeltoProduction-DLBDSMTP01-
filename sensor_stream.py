import numpy as np


def sensor_stream(seed=42):

    rng = np.random.default_rng(seed)

    zeit = 0
    naechster_defekt = rng.integers(100, 300)
    defekt_aktiv = False

    while True:

        # -----------------------------
        # Normalwerte
        # -----------------------------
        temperatur = 22 + rng.normal(0, 0.4)
        feuchtigkeit = 50 + rng.normal(0, 1.5)
        laerm = 40 + rng.normal(0, 2.0)

        defekt = 0

        # -----------------------------
        # Neuen Defekt starten
        # -----------------------------
        if zeit >= naechster_defekt and not defekt_aktiv:

            defekt_aktiv = True
            defekt_start = zeit

            # Dauer des linearen Anstiegs
            anstiegsdauer = rng.integers(30, 100)

            # Dauer auf hohem Niveau
            plateaudauer = rng.integers(20, 80)

            plateau_start = defekt_start + anstiegsdauer
            defekt_ende = plateau_start + plateaudauer

            # Zufällige maximale Anstiege
            anstiege = {
                "Temperatur": rng.uniform(5, 12),
                "Feuchtigkeit": rng.uniform(10, 25),
                "Laerm": rng.uniform(15, 35)
            }

            # Zufällig 2 oder 3 Sensoren auswählen
            anzahl_sensoren = rng.integers(2, 4)

            aktive_sensoren = rng.choice(
                list(anstiege.keys()),
                size=anzahl_sensoren,
                replace=False
            )

        # -----------------------------
        # Defektverlauf
        # -----------------------------
        if defekt_aktiv:

            # Phase 1: linearer Anstieg
            if zeit < plateau_start:

                fortschritt = (
                    zeit - defekt_start
                ) / anstiegsdauer

                rampe = fortschritt

            # Phase 2: hohes Niveau
            else:
                rampe = 1.0
                defekt = 1

            # ausgewählte Sensoren verändern
            if "Temperatur" in aktive_sensoren:
                temperatur += rampe * anstiege["Temperatur"]

            if "Feuchtigkeit" in aktive_sensoren:
                feuchtigkeit += rampe * anstiege["Feuchtigkeit"]

            if "Laerm" in aktive_sensoren:
                laerm += rampe * anstiege["Laerm"]

            # schon während der zweiten Hälfte des Anstiegs
            # als Defekt markieren
            if zeit >= defekt_start + anstiegsdauer / 2:
                defekt = 1

            # -----------------------------
            # Reparatur
            # -----------------------------
            if zeit >= defekt_ende:

                defekt_aktiv = False

                # nächster Defekt erst später
                naechster_defekt = (
                    zeit + rng.integers(100, 300)
                )

        # -----------------------------
        # Messwert ausgeben
        # -----------------------------
        yield {
            "Zeit": zeit,
            "Temperatur": temperatur,
            "Feuchtigkeit": feuchtigkeit,
            "Laerm": laerm,
            "Defekt": defekt
        }

        zeit += 1
"""
# Test:
for eintrag in sensor_stream():
    zeit = eintrag["Zeit"]
    print(eintrag["Zeit"])
    print(eintrag["Temperatur"])
    print(eintrag["Feuchtigkeit"])
    print(eintrag["Laerm"])
    print(eintrag["Defekt"])
    if zeit >= 5000:
        break
    
"""