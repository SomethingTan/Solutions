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
                print(str(max(self, other))[i], end="")
            else:
                print(str(padded_min)[i], end="")
        return "\n"

    def __mul__(self, other):
        print(f"{self} * {other}\n---")
        other_reversed = "".join(reversed(str(other)))
        i_iteration = 0
        for i in str(self):
            for j in range(len(other_reversed)):
                if int(i) < int(other_reversed[j]):
                    # print(f"----- {i}, {other_reversed[j]}")
                    print(i, end="")
                else:
                    # print(f"----- {i}, {other_reversed[j]}")
                    print(other_reversed[j], end="")
            i_iteration += 1
            print()

print(Lunar_int(3276) * Lunar_int(7621))