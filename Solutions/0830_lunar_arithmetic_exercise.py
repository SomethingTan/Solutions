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
    def __add__(self, other_int):
        padded_min = str(min(self, other_int)).zfill(len(str(max(self, other_int))))
        for i in range(len(str(padded_min))):
            if str(max(self, other_int))[i] > str(padded_min)[i]:
                print(str(max(self, other_int))[i], end="")
            else:
                print(str(padded_min)[i], end="")
        return "\n"

    def __mul__(self, other_int):
        padded_min = str(min(self, other_int)).zfill(len(str(max(self, other_int))))
        for i in reversed(str(max(self, other_int))):
            for j in reversed(str(padded_min)):
                if j < i:
                    0
                else:
                    0
        return "\n"

print(Lunar_int(1250722) + Lunar_int(-97615), Lunar_int(83) * Lunar_int(190))