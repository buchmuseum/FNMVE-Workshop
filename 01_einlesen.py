# Dateiobjekt öffnen

f = open('Goethe_Sammler.txt')               # Variable zuweisen, Funktionsaufruf

text = f.read()                              # Variable zuweisen und Methode des Dateiobjekts ausführen

f.close()                                    # Dateiobjekt wieder schließen

print(text)                                  # Ausgabe, evtl stimmen die Umlaute nicht: open(file, encoding="utf-8")
