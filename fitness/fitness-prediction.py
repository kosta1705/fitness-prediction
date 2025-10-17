import csv
import os

def benutzerEingabe():
    print("Bitte geben Sie folgende Informationen ein:")
    name = input("Name: ")
    alter = int(input("Alter: "))
    gewicht = float(input("Gewicht (in kg): "))
    groesse = float(input("Größe (in cm): "))
    geschlecht = input("Geschlecht (m oder w): ")
    fitnesslevel = input("Fitnesslevel (niedrig / mittel / hoch): ").lower()
    #interesse = input("Interesse (z.B. Teamsport, Ausdauer, Entspannung): ").lower()

    return {
        "Name": name,
        "Alter": alter,
        "Gewicht": gewicht,
        "Groesse": groesse,
        "Geschlecht": geschlecht,
        "Fitnesslevel": fitnesslevel,
        #"Interesse": interesse
    }


def sport_vorhersage(daten):
    alter = daten["Alter"]
    gewicht = daten["Gewicht"]
    geschlecht = daten["Geschlecht"]
    fitness = daten["Fitnesslevel"]

    #Erweiterung mit Geschlecht?
    if fitness == "niedrig":
        return "Yoga"
    elif fitness == "mittel":
        if gewicht > 90:
            return "Radfahren oder Schwimmen"
        else:
            return "Fitnessstudio oder Joggen"
    elif fitness == "hoch":
        return "Fußball oder Basketball"
    else:
        return "Allgemeine Bewegung wie Walking"

def datenSpeichern(daten, dateiname="fitness/nutzer_daten.csv"):
    datei_existiert = os.path.isfile(dateiname)
    with open(dateiname, mode="a", newline='', encoding="utf-8") as csvfile:
        feldnamen = list(daten.keys())
        writer = csv.DictWriter(csvfile, fieldnames=feldnamen)

        if not datei_existiert:
            writer.writeheader()
        writer.writerow(daten)

    print(f"\nDaten gespeichert in {dateiname}")

nutzer_daten = benutzerEingabe()
empfehlung = sport_vorhersage(nutzer_daten)
nutzer_daten["Empfehlung"] = empfehlung
print(f"\n Basierend auf deinen Angaben empfehlen wir: {empfehlung}")
datenSpeichern(nutzer_daten)