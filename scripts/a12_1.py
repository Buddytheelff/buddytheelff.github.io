#!/usr/bin/env python

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class jackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class dachshund(Dog):
    def __eq__(self, notself):
        return self.age == notself.age


class bulldog(Dog):
    def __eq__(self, notself):
        return self.name == notself.name


def main():
    names = ["Miles", "Rover", "Jack"]

    miles = jackRussellTerrier("Miles", 3)
    rover = dachshund("Rover", 3)
    jack = bulldog("Jack", 3)
    jim = bulldog("Jim", 3)

    jim.speak("Woof")

    # I thoughht that the different sub classes would trip up the __eq__ it doesn't
    print(rover == miles)
    print(jack == jim)
    print(jack == jack)
    # poor miles has to be deleted for science
    del miles
    try:
        print(miles)
    except:
        print("Miles has been deleted :(")


if __name__ == "__main__":
    main()
