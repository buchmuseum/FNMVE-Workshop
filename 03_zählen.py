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


# Ausgabe

print(counter)