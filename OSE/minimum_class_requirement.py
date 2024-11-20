class ZeroRequirements:
    STR = 3
    INT = 3
    WIS = 3
    DEX = 3
    CON = 3
    CHA = 3

    @classmethod
    def _get_requirements(cls):
        return cls.STR, cls.INT, cls.WIS, cls.DEX, cls.CON, cls.CHA


class MinRequirements(ZeroRequirements):

    cha = None
    con = None
    dex = None
    wis = None
    int = None
    str = None
    prime_req1 = None
    prime_req2 = None

    @classmethod
    def __get_requirements(cls):
        requirements = super()._get_requirements()
        cls.prime_req1 = None
        cls.prime_req2 = None
        return requirements

    @classmethod
    def acrobat(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Zręczność"

    @classmethod
    def assassin(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Zręczność"
    
    @classmethod
    def barbarian(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9
        cls.prime_req1 = "Kondycja"
        cls.prime_req2 = "Siła"

    @classmethod
    def bard(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9
        cls.dex = 9
        cls.prime_req1 = "Charyzma"

    @classmethod
    def cleric(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Mądrość"
    
    @classmethod
    def drow(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9
        cls.prime_req1 = "Siła"
        cls.prime_req2 = "Mądrość"

    @classmethod
    def druid(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Mądrość"

    @classmethod
    def duergar(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9
        cls.con = 9
        cls.prime_req1 = "Siła"

    @classmethod
    def dwarf(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9
        cls.prime_req1 = "Siła"
    
    @classmethod
    def elf(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9
        cls.prime_req1 = "Inteligencja"
        cls.prime_req2 = "Siła"

    @classmethod
    def fighter(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Siła"

    @classmethod
    def gnome(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9
        cls.prime_req1 = "Zręczność"
        cls.prime_req2 = "Inteligencja"

    @classmethod
    def halfelf(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9
        cls.cha = 9
        cls.prime_req1 = "Inteligencja"
        cls.prime_req2 = "Siła"

    @classmethod
    def halfling(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9
        cls.con = 9
        cls.prime_req1 = "Zręczność"
        cls.prime_req2 = "Siła"

    @classmethod
    def halforc(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Zręczność"
        cls.prime_req2 = "Siła"

    @classmethod
    def illusionist(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9
        cls.prime_req1 = "Inteligencja"

    @classmethod
    def knight(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9
        cls.con = 9
        cls.prime_req1 = "Siła"

    @classmethod
    def magicuser(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Inteligencja"

    @classmethod
    def paladin(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.cha = 9
        cls.prime_req1 = "Siła"
        cls.prime_req2 = "Mądrość"

    @classmethod
    def ranger(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.wis = 9
        cls.con = 9
        cls.prime_req1 = "Siła"

    @classmethod
    def svirfneblin(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9
        cls.prime_req1 = "Siła"

    @classmethod
    def thief(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.prime_req1 = "Zręczność"

    @classmethod
    def __str__(cls):
        return (f"Min Siła {cls.str}, Min Inteligencja {cls.int}, Min Mądrość {cls.wis}, "
                f"Min Zręczność {cls.dex}, Min Kondycja {cls.con}, Min Charyzma {cls.cha}")

# print("TEST1")
# MinRequirements.acrobat()
# print(MinRequirements.str)
# print(MinRequirements.int)
# print(MinRequirements.wis)
# print(MinRequirements.dex)
# print(MinRequirements.con)
# print(MinRequirements.cha)