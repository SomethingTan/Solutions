"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
def inventory(rows):
    numbers_memory = {}
    numbers_current = {}
    for i in range(rows):
        iteration = 0
        while True:
            numbers_current[iteration] = sum(1 for _value in numbers_current.values() if _value == iteration) + int(numbers_memory[iteration] if iteration in numbers_memory else 0)
            if numbers_current[iteration] == 0:
                break
            iteration += 1
        for j in range(len(numbers_current)):
            numbers_memory[j] = sum(1 for _value in numbers_current.values() if _value == j) + int(numbers_memory[j] if j in numbers_memory else 0)
        print(*numbers_current.values())
        print(numbers_memory)
        print()
        numbers_current = {}


inventory(20)