"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

class Character:
    def __init__(self,name,max_health,_current_health,impatience,state,attack_power):
        self.name = str(name)
        self.max_health = int(max_health)
        self._current_health = int(_current_health)
        self.impatience = impatience
        self.state = str(state)
        self.attack_power = int(attack_power)

    def __repr__(self):
        return f"{self.name} has an HP of {self._current_health}/{self.max_health} and an attacking power of {self.attack_power}."

    def hit(self,target):
        if not isinstance(target,Character):
            return "Target must be of class Character."
        else:
            self.state = "Attacking"
            self.impatience = 1
            print(f"{self.name} hits {target.name}!")
            target.hit_receive("Hit",self.attack_power)

    def hit_receive(self,type,hit_amount):
        match type:
            case "Hit":
                if self.state == "Blocking" or "Charging_Special":
                    hit_amount *= 0.5
                self._current_health -= hit_amount
                print(f"{self.name} took {hit_amount*0.5 if self.state == "Blocking" or "Charging_Special" else hit_amount}DMG, HP is now {self._current_health}/{self.max_health}!")
            case "Dagger_Storm":
                if self.state == "Blocking" or "Charging_Special":
                    hit_amount *= 0.5
                self._current_health -= hit_amount
                print(f"{self.name} was hit by Dagger Storm! {round(hit_amount/5)}/7 daggers hit, dealing {hit_amount*0.5 if self.state == "Blocking" or "Charging_Special" else hit_amount}DMG! HP is now {self._current_health}/{self.max_health}.")
            case "Meteor":
                if hit_amount == 0:
                    print(f"Meteor missed, dealing 0DMG! HP is still {self._current_health}/{self.max_health}.")
                else:
                    if self.state == "Blocking" or "Charging_Special":
                        hit_amount *= 0.5
                    self._current_health -= hit_amount
                    print(f"{self.name} was hit by Meteor, dealing {hit_amount*0.5 if self.state == "Blocking" or "Charging_Special" else hit_amount}DMG! HP is now {self._current_health}/{self.max_health}.")
        if self.state == "Blocking":
            print(f"{self.name} blocked the attack!")
        self.state = "Damaged"

    def block(self):
        self.state = "Blocking"
        self.impatience *= 1.5
        print(f"{self.name} blocks!")

class Hunter(Character):
    def __init__(self,name,max_health,_current_health,impatience,state,attack_power):
        super().__init__(name,max_health,_current_health,impatience,state,attack_power)
        self.special_attack_charged = False

    def special_attack(self,target):
        if not isinstance(target,Character):
            return "Target must be of class Character."
        else:
            self.impatience = 1
            if self.special_attack_charged == False:
                self.state = "Charging_Special"
                self.special_attack_charged = True
                print(f"{self.name} charges an attack...")
            else:
                target.hit_receive("Dagger_Storm",random.randint(10,35))
                self.special_attack_charged = False
                self.state = "Idle"

class Magician(Character):
    def __init__(self,name,max_health,_current_health,impatience,state,attack_power):
        super().__init__(name,max_health,_current_health,impatience,state,attack_power)
        self.special_attack_charged = False

    def special_attack(self,target):
        if not isinstance(target,Character):
            return "Target must be of class Character."
        else:
            self.impatience = 1
            if not self.special_attack_charged:
                self.state = "Charging_Special"
                self.special_attack_charged = True
                print(f"{self.name} charges an attack...")
            else:
                target.hit_receive("Meteor",65 if random.random()*100 > 50 else 0)
                self.special_attack_charged = False
                self.state = "Idle"

hunter = Hunter("Hunter",115,115,1,"Idle",10,)
magician = Magician("Magician",100,100,1,"Idle",8)

print("---------- ROUND START ----------")
hunter_wins = 0
magician_wins = 0
for i in range(100):
    while hunter._current_health > 0 and magician._current_health > 0:
        print("Hunter's turn.")
        choice = random.randint(1,3)
        if choice == 2:
            choice += random.randint(-1,1)
        if choice == 3:
            choice -= 1 if random.random()*hunter.impatience>0.5 else 0
        if hunter.special_attack_charged == True:
            hunter.special_attack(magician)
        else:
            match choice:
                case 1:
                    hunter.hit(magician)
                case 2:
                    hunter.special_attack(magician)
                case 3:
                    hunter.block()
        if magician._current_health <= 0:
            break
        print("Magician's turn.")
        choice = random.randint(1, 3)
        if choice == 2:
            choice += random.randint(-1,1)
        if choice == 3:
            choice -= 1 if random.random()*magician.impatience>0.5 else 0
        if magician.special_attack_charged == True:
            magician.special_attack(hunter)
        else:
            match choice:
                case 1:
                    magician.hit(hunter)
                case 2:
                    magician.special_attack(hunter)
                case 3:
                    magician.block()
    if magician._current_health <= 0:
        hunter_wins += 1
        print("Hunter wins!")
    else:
        magician_wins += 1
        print("Magician wins!")
    hunter._current_health = hunter.max_health
    magician._current_health = magician.max_health
print(f"Hunter won {hunter_wins} times, Magician won {magician_wins} times.")