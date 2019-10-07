# Einlesen

with open('Goethe_Sammler.txt', 'r') as f:

    text = f.read()


# Verarbeiten:

# 1. Liste mit einzelnen Tokens erstellen

tokens = text.split()


# 2. Dictionary zum Zählen der Tokens erstellen

counter = {}

for token in tokens:

    if token in counter.keys():

        counter[token] += 1

    else:

        counter[token] = 1


# Ausgabe

print("Der Text besteht aus {} Token.".format(len(tokens)))

print("Es wurden unterschiedliche {} Token identifiziert.".format(len(counter.keys())))