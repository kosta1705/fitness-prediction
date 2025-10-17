import csv
import os

def benutzerEingabe():
    print("Bitte geben Sie folgende Informationen ein:")
    name = input("Name: ")
    alter = int(input("Alter: "))
    gewicht = float(input("Gewicht (in kg): "))
    groesse = float(input("Größe (in cm): "))
    fitnesslevel = input("Fitnesslevel (niedrig / mittel / hoch): ").lower()
    #interesse = input("Interesse (z.B. Teamsport, Ausdauer, Entspannung): ").lower()

    return {
        "Name": name,
        "Alter": alter,
        "Gewicht": gewicht,
        "Groesse": groesse,
        "Fitnesslevel": fitnesslevel,
        #"Interesse": interesse
    }


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
datenSpeichern(nutzer_daten)