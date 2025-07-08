# Welke api request waren er nog maar weer?
# - post
# - put / patch
# - delete
# - get

# welke 4 argumenten kun je meegeven aan een API-request
# - Parameters
# - URL
# - json (data)
# - Headers

# Bestanden openen
# Met of zonder with

# Met 'with':
# Open het bestand in de leesmodus ('r' staat voor 'read').
# Het voordeel van 'with' is dat het bestand automatisch wordt gesloten, zelfs als er fouten optreden.
# Dit is de aanbevolen manier om bestanden te openen.

# with open('path\\to\\file1.txt', 'r') as file:
#     # code om je bestand te lezen
#     pass

# Zonder 'with':
# Open het bestand in de leesmodus ('r' staat voor 'read').
# Vergeet niet het bestand handmatig te sluiten met file.close().

# file = open('path\\to\\file2.txt', 'r')
# # code om je bestand te lezen
# file.close()

# Bestand modi
# Lezen, Schrijven of Bewerken van Bestanden:

# Lezen:
# Gebruik open() met modus 'r'.
# Dit opent het bestand in leesmodus.
# Voorbeeld:
# with open('bestand.txt', 'r') as bestand:
#     inhoud = bestand.read()

# Schrijven:
# Gebruik open() met modus 'w'.
# Dit opent het bestand in schrijfmodus en overschrijft bestaande inhoud.
# Voorbeeld:
# with open('bestand.txt', 'w') as bestand:
#     bestand.write('Nieuwe inhoud')

# Toevoegen:
# Gebruik open() met modus 'a' voor het toevoegen van records.
# Dit opent het bestand in append-modus en voegt inhoud toe aan het einde.
# Voorbeeld:
# with open('bestand.txt', 'a') as bestand:
#     bestand.write('\nToegevoegde regel')

# Lezen en schrijven:
# Gebruik open() met modus 'r+'.
# Hiermee kun je zowel lezen als schrijven in een bestaand bestand.
# Voorbeeld:
# with open('bestand.txt', 'r+') as bestand:
#     inhoud = bestand.read()
#     bestand.write('\nExtra regel')

# Lezen van Bestanden:

# Lezen:
# Gebruik de read() of readline() methode van file.
# Voorbeeld:
# with open('bestand.txt', 'r') as bestand:
#     inhoud = bestand.read()
#     print(inhoud)

# Alles lezen:
# Gebruik readlines().
# Let op: niet geschikt voor grote bestanden, want het leest alles in één keer in het geheugen.
# Voorbeeld:
# with open('bestand.txt', 'r') as bestand:
#     regels = bestand.readlines()
#     print(regels)

# Regel voor regel:
# Gebruik een for-loop om het bestand regel voor regel te lezen.
# Dit is efficiënt en geschikt voor grote bestanden.
# Voorbeeld:
# with open('bestand.txt', 'r') as bestand:
#     for regel in bestand:
#         print(regel.strip())

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
