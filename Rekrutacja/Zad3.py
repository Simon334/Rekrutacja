print("Wpisz 0 jezeli chcesz zakonczyc petle\n")

a=True
b=True

while (a!=0 and b!=0):
  a=float(input("Wpisz 1 liczbe"))
  b=float(input("Wpisz 2 liczbe\n"))
  if (a!=0 and b!=0):
    wynik=float(a+b)
    print("Wynik to\n", wynik)
  else:
    print("Wpisales liczbe 0")
    break


"""
a=True
b=True
pętla dopóki True:
a = pobierz liczbę od użytkownika
b = pobierz liczbę od użytkownika
jeśli a!=0 i b!=0:
wynik=a+b
wyswietl wynik
w przeciwnym wypadku:
wyświetl("Wpisales liczbe 0")
zakończ pętle
"""