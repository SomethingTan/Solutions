""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""

def calc():
    print("Please select an operator\n-------\n+, -, *, /\nType \"End\" to exit program\n-------")
    operator = input().lower()
    match operator:
        case "+":
            print("Please give 2 numbers, seperated by a space.")
            numbers = input().split()
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            print(f"{num1+num2}\n-------")
            calc()
            return
        case "-":
            print("Please give 2 numbers, seperated by a space.")
            numbers = input().split()
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            print(f"{num1 - num2}\n-------")
            calc()
            return
        case "*":
            print("Please give 2 numbers, seperated by a space.")
            numbers = input().split()
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            print(f"{num1 * num2}\n-------")
            calc()
            return
        case "/":
            print("Please give 2 numbers, seperated by a space.")
            numbers = input().split()
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            print(f"{num1 / num2}\n-------")
            calc()
            return
        case "end":
            print("Exiting")
            return
        case _:
            print("Please select a valid operator.")
            calc()
            return

calc()