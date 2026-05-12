from tornado.process import task_id


class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = str(name)
        self.sound = str(sound)
        self.height = float(height)
        self.weight = float(weight)
        self.legs = int(legs)
        self.female = bool(female)

    def __repr__(self):

        return f"This animal makes the sound \"{self.sound}\", is {self.height}m tall, weighs {self.weight}kg, has {self.legs} legs and {self.is_a_female()}."

    def is_a_female(self):
        if self.female == True:
            return "is a female"
        else:
            return "is not a female"

    def make_noise(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = float(tail_length)
        self.hunts_sheep = bool(hunts_sheep)

    def __repr__(self):
        return f"This animal makes the sound \"{self.sound}\", is {self.height}m tall, weighs {self.weight}kg, has {self.legs} legs, has a {self.tail_length}cm long tail, {self.is_a_female()} and {self.does_hunts_sheep()}"

    def does_hunts_sheep(self):
        if self.hunts_sheep:
            return "hunts sheep"
        else:
            return "does not hunt sheep"

    def wag_tail(self):
        print(f"{self.name} The Dog wags their {self.tail_length}cm long tail.")

def mate(mother,father):
    if mother.__class__.__name__ and father.__class__.__name__ == "Dog":
        if mother.female == True and father.female == False:
            child_dog = Dog()
        else:
            print("Mother must be Female and Father must be Male.")
    else:
        print("Both parties must be Dogs.")

cow = Animal("cow","moo","42","3521","4",True)
big_dog = Dog("dog","ruff","531","45100","6",False,54,True)

print(f"{cow}\n{big_dog}")