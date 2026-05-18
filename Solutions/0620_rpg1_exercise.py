"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0622_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i 0624_rpg1_solution.py
"""

class Character:
    def __init__(self,name,max_health,_current_health,attack_power):
        self.name = str(name)
        self.max_health = int(max_health)
        self._current_health = int(_current_health)
        self.attack_power = int(attack_power)

    def __repr__(self):
        return f"{self.name} has an HP of {self._current_health}/{self.max_health} and an attacking power of {self.attack_power}."

    def hit(self,target):
        if not isinstance(target,Character):
            return "Target must be of class Character."
        else:
            print(f"{self.name} hits {target.name}!")
            target.hit_receive(self.attack_power)

    def hit_receive(self,hit_amount):
        self._current_health -= hit_amount
        print(f"{self.name} took {hit_amount}DMG, HP is now {self._current_health}/{self.max_health}!")

    def heal_receive(self,heal_amount):
        self._current_health += heal_amount
        print(f"{self.name} healed for {heal_amount}HP, HP is now {self._current_health}/{self.max_health}!")

class Healer(Character):
    def __init__(self,name,max_health,_current_health,attack_power,heal_power):
        super().__init__(name,max_health,_current_health,attack_power)
        self.attack_power = 0
        self.heal_power = heal_power

    def heal(self,target):
        if not isinstance(target,Character):
            return "Target must be of class Character"
        else:
            print(f"{self.name} heals {target.name}!")
            target.heal_receive(self.heal_power)