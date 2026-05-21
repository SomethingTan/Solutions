""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

number = str(random.randint(1000,9999))
print("A 4-digit number has been randomly generated. Type a 4-digit guess,\nif digit is present and in correct position, you gain a \U000025CF\nif digit is present and in incorrect position, you gain a \U000025CB\n----------------")
def guess():
    global black_coin_amt
    black_coin_amt = 0
    white_coin_amt = 0
    guess = str(input())
    for i in range(len(guess)):
        if guess[i-1] == number[i-1]:
            black_coin_amt += 1
        else:
            for j in range(len(number)):
                if number[j-1] == guess[i-1]:
                    white_coin_amt += 1
                    break
    print(f"----------------\n\U000025CF : {black_coin_amt}\n\U000025CB : {white_coin_amt}\n----------------")
    return

guess()
while black_coin_amt < 4:
    guess()
