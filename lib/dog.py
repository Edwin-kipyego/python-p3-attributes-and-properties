class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Doggo", breed="Pug"):  # default valid breed
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
