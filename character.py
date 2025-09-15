from attributes import Attributes

class PlayerCharacter:
    def __init__(self, name, hp, attributes):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attributes = attributes  #instance of Attributes class

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"HP: {self.current_hp}/{self.max_hp}\n"
            f"Attributes:\n"
            f"  Strength: {self.attributes.strength}\n"
            f"  Dexterity: {self.attributes.dexterity}\n"
            f"  Intelligence: {self.attributes.intelligence}\n"
            f"  Constitution: {self.attributes.constitution}\n"
            f"  Wisdom: {self.attributes.wisdom}\n"
            f"  Charisma: {self.attributes.charisma}\n"     
        )
    def is_alive(self):
        """Returns True if the character is alive (hp>0), else False."""
        return self.current_hp > 0