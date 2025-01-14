import math
import sys


# A-Levels
def startProgram():
    print("Hello, this is the Admission Calculator! Version for admission year 2024/25")
    while True:
        print("From here you can choose between different grading Systems")
        print("0 for system, where 1 is the best and 6 the worst.")
        print("1 for the german Abitur system")
        print("2 for any different system, there will be further instructions.")
        print("If you want to exit the programm write exit")
        gradingSystem = input("What is your grading system?: ")
        match(gradingSystem):
            case "0":
                AdmissionCalculatorCase0()
            case "1":
                AdmissionCalculatorCase1()
            case "2":
                AdmissionCalculatorCase2()
            case "exit":
                sys.exit()
            case _:
                continue


def AdmissionCalculatorCase0():
    pass
# Fächerspezifisch
def AdmissionCalculatorCase1():
    SingeGradesDict = {}
    SingeGradesDict["Abiturnote Umgerechnet"] = []
    Abiturnote = float(input("Gebe die Abiturnote an: "))
    Umgerechneter_Abiturnote = 120 - 20 * Abiturnote
    SingeGradesDict["Abiturnote Umgerechnet"].append(Umgerechneter_Abiturnote)
    SingeGradesDict["Fächer"] = []
    for x in range(4):
        Halbjahresleistung = 0
        match x:
            case 0:
                Fach = f"Mathe"
                mult = 3
            case 1:
                Fach = f"Deutsch"
                mult = 1
            case 2:
                Fach = f"Englisch"
                mult = 1
            case 3:
                Fach = f"Naturwissenschaft"
                mult = 2
        SingeGradesDict[Fach] = []
        for i in range(1, 6):
            if i == 5:
                i = f"Abitur"
            Halbjahresleistung = float(input(f"Halbjahresleistung_{i}_{Fach}: "))
            SingeGradesDict[Fach].append(Halbjahresleistung)
        SingeGradesDict["Einzelnotensumme_" + Fach] = []
        SingeGradesDict["Einzelnotensumme_" + Fach].append(mult * sum(SingeGradesDict[Fach]))
        SingeGradesDict["Fächer"].append(Fach)
    Fächer = list(SingeGradesDict["Fächer"])
    Einzelnoten_gesamt = 0
    for fach in Fächer:
        Einzelnoten_gesamt += sum(SingeGradesDict["Einzelnotensumme_" + fach])

    Einzelnotendurchschnitt = Einzelnoten_gesamt / 35
    Umrechnung_Einzelnotendurchschnitt_raw = 10 + 6 * (Einzelnotendurchschnitt)
    Umrechnung_Einzelnotendurchschnitt = math.ceil(Umrechnung_Einzelnotendurchschnitt_raw)
    print(Umrechnung_Einzelnotendurchschnitt_raw)
    print(Umrechnung_Einzelnotendurchschnitt)
    Gesamtbewertung_raw = 0.65 * Umgerechneter_Abiturnote + 0.35 * Umrechnung_Einzelnotendurchschnitt
    Gesamtbewertung = math.ceil(Gesamtbewertung_raw)
    print(Gesamtbewertung_raw)
    print(Gesamtbewertung)
    if input("Jungendforscht? : Ja für Ja, sonst nein: ") == "Ja":
        Gesamtbewertung = Gesamtbewertung + 2
        print("JF" + str(Gesamtbewertung))
    else:
        print(Gesamtbewertung)

def AdmissionCalculatorCase2():
    pass

startProgram()