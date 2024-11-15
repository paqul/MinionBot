class ZeroRequirements(object):

    def __init__(self):
        self.STR = 3
        self.INT = 3
        self.WIS = 3
        self.DEX = 3
        self.CON = 3
        self.CHA = 3


class MinRequirements(ZeroRequirements):

    def __init__(self):
        super().__init__()
        self.str = self.STR
        self.int = self.INT
        self.wis = self.WIS
        self.dex = self.DEX
        self.con = self.CON
        self.cha = self.CHA

    def __str__(self):
        return f"Min Siła {self.str}, Min Inteligencja {self.int}, Min Mądrość {self.wis}," \
               f"Min Zręczność {self.dex}, Min Kondycja {self.con}, Min Charyzma {self.cha}"

    def acrobat(self):
        pass

    def assassin(self):
        pass

    def barbarian(self):
        self.dex = 9

    def bard(self):
        self.int = 9
        self.dex = 9

    def cleric(self):
        super().__init__()

    def drow(self):
        self.int = 9

    def druid(self):
        pass

    def duergar(self):
        self.int = 9
        self.con = 9

    def dwarf(self):
        self.con = 9

    def elf(self):
        self.int = 9

    def fighter(self):
        pass

    def gnome(self):
        self.con = 9

    def halfelf(self):
        self.con = 9
        self.cha = 9

    def halfling(self):
        self.dex = 9
        self.con = 9

    def halforc(self):
        pass

    def illusionist(self):
        self.dex = 9

    def knight(self):
        self.dex = 9
        self.con = 9

    def magicuser(self):
        pass

    def paladin(self):
        self.cha = 9

    def ranger(self):
        self.wis = 9
        self.con = 9

    def svirfneblin(self):
        self.con = 9

    def thief(self):
        pass


z = MinRequirements()
print(z)
z.acrobat()
print("TEST1")
print(z.str)
print(z.int)
print(z.wis)
print(z.dex)
print(z.con)
print(z.cha)
z.bard()
print("TEST2")
print(z.str)
print(z.int)
print(z.wis)
print(z.dex)
print(z.con)
print(z.cha)
z.cleric()
print("TEST3")
print(z.str)
print(z.int)
print(z.wis)
print(z.dex)
print(z.con)
print(z.cha)

