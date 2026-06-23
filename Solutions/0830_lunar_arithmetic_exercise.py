"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se denne video fra 0:00 til 2:41:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""



class Lunar_int(int):
    def __add__(self, other):
        padded_min = str(min(self, other)).zfill(len(str(max(self, other))))
        for i in range(len(padded_min)):
            if int(str(max(self, other))[i]) > int(padded_min[i]):
                return int(str(max(self, other))[i])
            else:
                return int(str(padded_min)[i])

    def __mul__(self, other):
        digits = []
        self_reversed = "".join(reversed(str(self)))
        for i in self_reversed:
            for j in range(len(str(other))):
                if int(i) < int(str(other)[j]):
                    if j < len(digits):
                        digits[j] = Lunar_int(int(i)) + digits[j]
                    else:
                        digits.append(int(i))
                else:
                    if j < len(digits):
                        digits[j] = Lunar_int(int(str(other)[j])) + digits[j]
                    else:
                        digits.append(int(str(other)[j]))
            digits.insert(0, 0)
        digits.pop(0)
        digits_str = ""
        for n in digits:
            digits_str += str(n)
        return int(digits_str)

def calc_lunar_primes(n):
    prime_amount = 0
    current_number = 19
    while prime_amount < n:
        nine_check = False
        prime = False
        for _i in str(current_number):
            if int(_i) == 9:
                nine_check = True
                break
        if nine_check:
            for _i in range(10, current_number):
                if Lunar_int(current_number) * Lunar_int(_i) == current_number:
                    print(f"not prime! {Lunar_int(current_number) * Lunar_int(_i)}")
                    break
                prime = True
                print(f"prime! {Lunar_int(current_number) * Lunar_int(_i)}")
            if prime:
                print(current_number)
                prime_amount += 1
                print("prime!")
        current_number += 1



calc_lunar_primes(20)