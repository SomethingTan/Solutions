"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.


Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0
."""



class Miner():
    def __init__(self, sleepiness, thirst, hunger, whiskey, gold):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whiskey = whiskey
        self.gold = gold
        self._turn = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        if self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100:
            self._dead()

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 1

    def buy_whiskey(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whiskey += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whiskey -= 1

    def _dead(self):
        self._turn += 1000
        print("Morris has died.")
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100


morris = Miner(0,0,0,0,0)

while morris._turn < 1000:
    morris._turn += 1
    if morris.sleepiness <= 40 and morris.thirst <= 80 and morris.hunger <= 70:
        morris.mine()
    elif morris.sleepiness> 40:
        for i in range(4):
            morris.sleep()
    elif morris.thirst > 80:
        if morris.whiskey > 0:
            morris.drink()
        else:
            morris.buy_whiskey()
            morris.drink()
    elif morris.hunger > 70:
        morris.eat()
    print(f"Turn {morris._turn} | Sleep : {morris.sleepiness}, Thirst : {morris.thirst}, Hunger : {morris.hunger}, Whiskey : {morris.whiskey}, Gold : {morris.gold}")
