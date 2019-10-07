# Einlesen
with open('Goethe_Sammler.txt', 'r') as f:
    text = f.read()
 
 
# Verarbeiten:
# 1. Liste erstellen
tokens = text.split()
 
# 2. Dictionary zum Zählen der Tokens erstellen
counter = {}
for token in tokens:                    # Schleife
 
    if token in counter.keys():         # Bedingung prüfen mit if
 
        counter[token] += 1             # Kurzschreibweise für counter[token] = counter[token] + 1
 
    else:
        counter[token] = 1
 
 
# Ausgabe, ausführliche Variante
for key, value in counter.items():                             # Schleife
    print("Das Wort {} taucht {} mal auf.".format(key, value)) # Interpolieren
 
 
print("Der Text besteht aus {} Token.".format(len(tokens)))                             # Alle Wörter
print("Es wurden unterschiedliche {} Token identifiziert.".format(len(counter.keys()))) # Schlüssel des Dicts