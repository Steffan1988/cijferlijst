# ---------------------------------------------------Requirements----------------------------------------------------- #
import json
import random
import os

# ------------------------------------------Constanten voor opmaak---------------------------------------------------- #
# TEKSTOPMAAK
BD = '\033[1m'   # Bold
UL = '\033[4m'   # Underline

# STANDAARD TEKSTKLEUREN
RD = '\033[31m'  # Rood
GR = '\033[32m'  # Groen
YL = '\033[33m'  # Geel
BL = '\033[34m'  # Blauw
MG = '\033[35m'  # Magenta
CY = '\033[36m'  # Cyan
RS = '\033[0m'   # Reset

# -------------------------------------------Errors als constanten---------------------------------------------------- #

VALUE_ERROR = f"{RD}{BD}Je kunt hier alleen getallen invoeren{RS}"
BESTAND_ERROR = f"{RD}{BD}Er is iets mis met het bestand: de cijferlijst kon niet correct worden ingelezen.{RS}"

# ----------------------------------------------Alle functie's-------------------------------------------------------- #
def add_courses_and_grades():
    data = {}
    course = input(f"{CY}Voor welk vak moeten er cijfers gegenereerd worden? {RS}").title()

    try:
        grade = int(input(f"{CY}Hoeveel cijfers moeten er gegenereerd worden voor {course}? {RS}"))

        # Willekeurige floats genereren en afronden met 1 decimaal
        data[course] = [round(random.uniform(1.0, 10.0), 1) for _ in range(grade)]

        # Toon gegenereerde cijfers van ingevoerde vak
        print(f"\n{GR}{BD}De gegenereerde cijfers voor {course} zijn:{RS} {data[course]}\n")
        write(data)
    except ValueError:
        print(VALUE_ERROR)

def write(data):
    # Bestaande JSON inladen
    path = os.path.join("files", "cijferlijst.json")

    # foutafhandeling voor JSON inladen
    try:
        with open(path, 'r') as file:
            existing_data = json.load(file)
    except json.JSONDecodeError:
        # bij leeg of ongeldig bestand
        existing_data = {}

    # voeg toe of vervang
    existing_data.update(data)

    # alles overschrijven, met indent voor de leesbaarheid in de JSON
    with open(path, 'w') as file:
        json.dump(existing_data, file, indent=4)

def show_courses_and_grades():
    path = os.path.join("files", "cijferlijst.json")
    try:
        with (open(path, 'r') as file):
            existing_data = json.load(file)
            while True:
                vak = get_course()
                if vak is not None:
                    break
            print(f"\n{BL}{UL}{BD}Cijfers voor {vak}:{RS}")
            for nummer, cijfer in enumerate(existing_data[vak], start=1):
                print(f"{GR}{nummer}. {cijfer}{RS}")
    except json.JSONDecodeError:
        print(BESTAND_ERROR)

def get_course():
    path = os.path.join("files", "cijferlijst.json")
    try:
        with (open(path, 'r') as file):
            existing_data = json.load(file)

            # Tijdelijke lijst maken met de keys uit de data (de vakken dus!)
            temp_list = []
            print()
            print(f"{CY}{BD}De aanwezige vakken zijn:{RS}")
            # Laat de vakken genummerd zien
            for nummer, key in enumerate(existing_data.keys(), start=1):
                print(f"{GR}{nummer}. {key}{RS}")
                temp_list.append(key)
            try:
                # kies een vak uit de lijst en laat de behaalde cijfer zien.
                print()
                which_course = int(input(
                    f"{YL}Welk vak wil je selecteren?"
                    f"\nKies een nummer van 1 t/m {len(temp_list)}: {RS}"))
                vak = temp_list[which_course - 1]
                return vak

            # foutafhandeling voor meerdere errors
            except ValueError:
                print(VALUE_ERROR)
                return None
            except IndexError:
                if len(temp_list) == 1:
                    woord = "vak"
                    woord2 = "staat"
                else:
                    woord = "vakken"
                    woord2 = "staan"
                print(f"{RD}{BD}Nummer '{which_course}' staat niet op de lijst. "
                      f"\nEr {woord2} momenteel '{len(temp_list)}' {woord} op je lijst.{RS}")
                return None
    except json.JSONDecodeError:
        print(BESTAND_ERROR)
        return None

def statistics():
    path = os.path.join("files", "cijferlijst.json")
    try:
        with open(path, 'r') as file:
            existing_data = json.load(file)
            one_or_all = input("Wil statistieken filteren per vak? Y/N").lower()
            if one_or_all == "y":
                course = get_course()
                temp_list = []
                for v in existing_data[course]:
                    temp_list.append(v)
                print()
                print(f"{MG}{UL}{BD}Statistieken voor {course}:{RS}")
                print(f"-{CY}Aantal cijfers: {len(temp_list)}{RS}")
                print(f"-{CY}Gemiddelde: {round(sum(temp_list) / len(temp_list), 1)}{RS}")
                print(f"-{GR}Hoogste cijfer: {max(temp_list)}{RS}")
                print(f"-{RD}Laagste cijfer: {min(temp_list)}{RS}")
                print()
            elif one_or_all == "n":
            # toon statistieken voor alle vakken (k)
                for k, v in existing_data.items():
                    print(f"{MG}{UL}{BD}Statistieken voor {k}:{RS}")
                    print(f"-{CY}Aantal cijfers: {len(v)}{RS}")
                    print(f"-{CY}Gemiddelde: {round(sum(v) / len(v), 1)}{RS}")
                    print(f"-{GR}Hoogste cijfer: {max(v)}{RS}")
                    print(f"-{RD}Laagste cijfer: {min(v)}{RS}")
                    print()
            else:
                print(f"{RD}{BD}Ongeldige invoer. Voer 'y' voor ja of 'n' voor nee in.{RS}")
    except json.JSONDecodeError:
        print(BESTAND_ERROR)

# ----------------------------------------------While-loop voor hoofdmenu--------------------------------------------- #
while True:
    print(f"\n{BL}{BD}Welkom bij de Cijferlijst-app!{RS}\n")

    print(f"{YL}1.{RS} Voeg een nieuw vak met cijfers toe")
    print(f"{YL}2.{RS} Bekijk de behaalde cijfers per vak")
    print(f"{YL}3.{RS} Bekijk statistieken")
    print(f"{YL}4.{RS} Afsluiten")

    try:
        print()
        choice = int(input(f"{YL}Wat wil je doen? (Kies een nummer van 1 t/m 4): {RS}"))
    except ValueError:
        print(VALUE_ERROR)
        continue

    if choice == 1:
        print()
        print(f'{BL}{BD}NIEUW VAK MET CIJFERS{RS}')
        add_courses_and_grades()

    elif choice == 2:
        print()
        print(f'{BL}{BD}TOON CIJFERS PER VAK{RS}')
        show_courses_and_grades()

    elif choice == 3:
        print()
        print(f'{BL}{BD}TOON STATISTIEKEN{RS}')
        statistics()

    elif choice == 4:
        print(f"{GR}{BD}Bedankt voor het gebruiken van de cijferlijst-app. Tot ziens!{RS}")
        break

    else:
        print(f"{BD}{RD}Kies een geldig getal 1-4.{RS}")