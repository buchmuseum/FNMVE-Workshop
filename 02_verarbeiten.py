# Verarbeiten

with open('Goethe_Sammler.txt', 'r') as f:   # Kurzschreibweise für open und close, Block
    text = f.read()


# Liste aus der Zeichenkette erstellen

tokens = text.split()


# Liste ausgeben

print(tokens)


# Andere Variante mit Schleife

for token in tokens:

    print(token)


# Token verändern

for token in tokens:

    print(token.lower())

    print(token.upper())

    print(token.strip(",.!?"))
