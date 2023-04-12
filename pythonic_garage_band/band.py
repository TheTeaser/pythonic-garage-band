from abc import ABC, abstractmethod


class Band:
    bands = []
    members = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.bands.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def to_list(cls):
        return cls.bands


class Musician:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod

    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I am the band's Guitarist"
    
    def __repr__(self):
        return f"Guitarist: {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "Purple Rain"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name}, and I am the band's Bassist."
    
    def __repr__(self):
        return f"Bassist: {self.name}"

    def get_instrument(self):
        return "Base"

    def play_solo(self):
        return "Base solo"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name}, and I am the band's Drummer."
    
    def __repr__(self):
        return f"Drummer: {self.name}"

    def get_instrument(self):
        return "Drums"

    def play_solo(self):
        return "Stairway to heaven"


if __name__ == "__main__":
    Prince = Guitarist('Prince')
    Led_zeppelin = Drummer('Led Zeppelin')
    Larry_Grahm = Bassist('Larry Graham')

    print(Band.members)
    print(Band.bands)