"""
Opgave "chessboard":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv en funktion chessboard, der accepterer 2 parametre.
Kald funktionen med argumenterne rows og cols.
I denne eksempel skal funktionen udskrive "A1 A2 A3 A4 A5 B1 B2 .... D4 D5".

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

rows = ["A", "B", "C", "D"]
cols = ["1", "2", "3", "4", "5"]

def chessboard(rows,cols):
    for i in range(0,len(rows)):
        row_value = rows[i]
        for j in range(0,len(cols)):
            col_value = cols[j]
            print(f"{row_value}{col_value} ", end="")
        print("\n")

chessboard(rows, cols)