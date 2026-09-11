import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd


def testdata_simple(n=1000):
    
    # Reproduzierbare Zufallszahlen
    rng = np.random.default_rng(42)
    
    # Anzahl Messpunkte
    #n = 1000
    t = np.arange(n)
    
    # 1. Normalbetrieb simulieren
    temperatur = 22 + rng.normal(0, 0.5, n)   # ca. 22 °C
    feuchtigkeit = 50 + rng.normal(0, 2.0, n) # ca. 50 %
    laerm = 40 + rng.normal(0, 3.0, n)        # ca. 40 dB
    
    # 2. Systemzustand
    # 0 = in Ordnung
    # 1 = Defekt
    defekt = np.zeros(n, dtype=int)
    
    # 3. Zeiträume mit Defekten definieren, zwei der drei werte gehen jeweils hoch
    
    defekt_bereiche = [
        (200, 260),
        #(500, 570),
        #(800, 850)
    ]
    
    for start, ende in defekt_bereiche:
        defekt[start:ende] = 1
    
        # Während eines Defekts steigen die Sensorwerte
        #temperatur[start:ende] += rng.normal(8, 1, ende-start)
        feuchtigkeit[start:ende] += rng.normal(20, 3, ende-start)
        laerm[start:ende] += rng.normal(25, 5, ende-start)
    ##
    
    defekt_bereiche = [
        #(200, 260),
        (500, 570),
        #(800, 850)
    ]
    
    for start, ende in defekt_bereiche:
        defekt[start:ende] = 1
    
        # Während eines Defekts steigen die Sensorwerte
        temperatur[start:ende] += rng.normal(8, 1, ende-start)
        #feuchtigkeit[start:ende] += rng.normal(20, 3, ende-start)
        laerm[start:ende] += rng.normal(25, 5, ende-start)
    
    
    ##
    
    defekt_bereiche = [
        #(200, 260),
        #(500, 570),
        (800, 850)
    ]
    
    for start, ende in defekt_bereiche:
        defekt[start:ende] = 1
    
        # Während eines Defekts steigen die Sensorwerte
        temperatur[start:ende] += rng.normal(8, 1, ende-start)
        feuchtigkeit[start:ende] += rng.normal(20, 3, ende-start)
        #laerm[start:ende] += rng.normal(25, 5, ende-start)
    
    
    
    df = pd.DataFrame({
        "Zeit": t,
        "Temperatur": temperatur,
        "Feuchtigkeit": feuchtigkeit,
        "Laerm": laerm,
        "Defekt": defekt
    })
    
    return df
    
#########################################################################
##### Testdaten mit Rampe.
#########################################################################


def testdata_rampe(n=1000):
    
    # Reproduzierbare Zufallszahlen
    rng = np.random.default_rng(42)
    
    # Anzahl Messpunkte
    #n = 1000
    t = np.arange(n)
    
    # 1. Normalbetrieb simulieren
    temperatur = 22 + rng.normal(0, 0.5, n)   # ca. 22 °C
    feuchtigkeit = 50 + rng.normal(0, 2.0, n) # ca. 50 %
    laerm = 40 + rng.normal(0, 3.0, n)        # ca. 40 dB
    
    # 2. Systemzustand
    # 0 = in Ordnung
    # 1 = Defekt
    defekt = np.zeros(n, dtype=int)
    
    
    #### Defekt 1:
    # -------------------------
    # Langsamer Anstieg
    # -------------------------
    
    start_anstieg = 200
    start_defekt = 240
    ende_defekt = 270
    
    # Länge der Anstiegsphase
    laenge = start_defekt - start_anstieg
    
    # Rampe von 0 bis 1
    rampe = np.linspace(0, 1, laenge)
    
    # Temperatur steigt langsam um insgesamt 8 °C
    temperatur[start_anstieg:start_defekt] += rampe * 8
    
    # Feuchtigkeit steigt um insgesamt 15 %
    feuchtigkeit[start_anstieg:start_defekt] += rampe * 15
    
    ## Lärm steigt um insgesamt 20 dB
    #laerm[start_anstieg:start_defekt] += rampe * 20
    
    
    # -------------------------
    # Defekt
    # -------------------------
    
    defekt[start_defekt:ende_defekt] = 1
    
    temperatur[start_defekt:ende_defekt] += 8
    feuchtigkeit[start_defekt:ende_defekt] += 15
    #laerm[start_defekt:ende_defekt] += 20
    
    #### Defekt 2:
    # -------------------------
    # Langsamer Anstieg
    # -------------------------
    
    start_anstieg = 400
    start_defekt = 420
    ende_defekt = 450
    
    # Länge der Anstiegsphase
    laenge = start_defekt - start_anstieg
    
    # Rampe von 0 bis 1
    rampe = np.linspace(0, 1, laenge)
    
    # Temperatur steigt langsam um insgesamt 10 °C
    temperatur[start_anstieg:start_defekt] += rampe * 10
    
    ## Feuchtigkeit steigt um insgesamt 15 %
    #feuchtigkeit[start_anstieg:start_defekt] += rampe * 15
    
    # Lärm steigt um insgesamt 25 dB
    laerm[start_anstieg:start_defekt] += rampe * 25
    
    
    # -------------------------
    # Defekt
    # -------------------------
    
    defekt[start_defekt:ende_defekt] = 1
    
    temperatur[start_defekt:ende_defekt] += 10
    #feuchtigkeit[start_defekt:ende_defekt] += 15
    laerm[start_defekt:ende_defekt] += 25
    
    #### Defekt 3:
    # -------------------------
    # Langsamer Anstieg
    # -------------------------
    
    start_anstieg = 700
    start_defekt = 710
    ende_defekt = 750
    
    # Länge der Anstiegsphase
    laenge = start_defekt - start_anstieg
    
    # Rampe von 0 bis 1
    rampe = np.linspace(0, 1, laenge)
    
    ## Temperatur steigt langsam um insgesamt 8 °C
    #temperatur[start_anstieg:start_defekt] += rampe * 8
    
    # Feuchtigkeit steigt um insgesamt 18 %
    feuchtigkeit[start_anstieg:start_defekt] += rampe * 18
    
    # Lärm steigt um insgesamt 30 dB
    laerm[start_anstieg:start_defekt] += rampe * 30
    
    
    # -------------------------
    # Defekt
    # -------------------------
    
    defekt[start_defekt:ende_defekt] = 1
    
    #temperatur[start_defekt:ende_defekt] += 8
    feuchtigkeit[start_defekt:ende_defekt] += 18
    laerm[start_defekt:ende_defekt] += 30
    
    
    df = pd.DataFrame({
        "Zeit": t,
        "Temperatur": temperatur,
        "Feuchtigkeit": feuchtigkeit,
        "Laerm": laerm,
        "Defekt": defekt
    })
    
    return df