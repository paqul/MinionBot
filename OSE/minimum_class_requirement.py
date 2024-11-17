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

    @classmethod
    def __get_requirements(cls):
        requirements = super()._get_requirements()
        return requirements

    @classmethod
    def acrobat(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()

    @classmethod
    def assassin(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
    
    @classmethod
    def barbarian(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9

    @classmethod
    def bard(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9
        cls.dex = 9

    @classmethod
    def cleric(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        pass
    
    @classmethod
    def drow(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9

    @classmethod
    def druid(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        pass

    @classmethod
    def duergar(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9
        cls.con = 9

    @classmethod
    def dwarf(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9
    
    @classmethod
    def elf(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.int = 9

    @classmethod
    def fighter(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        pass

    @classmethod
    def gnome(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9

    @classmethod
    def halfelf(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9
        cls.cha = 9

    @classmethod
    def halfling(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9
        cls.con = 9

    @classmethod
    def halforc(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        pass

    @classmethod
    def illusionist(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9

    @classmethod
    def knight(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.dex = 9
        cls.con = 9

    @classmethod
    def magicuser(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        pass

    @classmethod
    def paladin(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.cha = 9

    @classmethod
    def ranger(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.wis = 9
        cls.con = 9

    @classmethod
    def svirfneblin(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        cls.con = 9

    @classmethod
    def thief(cls):
        cls.str, cls.int, cls.wis, cls.dex, cls.con, cls.cha = cls.__get_requirements()
        pass

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
#
# print("TEST2")
# MinRequirements.bard()
# print(MinRequirements)
# print(MinRequirements.str)
# print(MinRequirements.int)
# print(MinRequirements.wis)
# print(MinRequirements.dex)
# print(MinRequirements.con)
# print(MinRequirements.cha)
#
# print("TEST3")
# MinRequirements.cleric()
# print(MinRequirements)
# print(MinRequirements.str)
# print(MinRequirements.int)
# print(MinRequirements.wis)
# print(MinRequirements.dex)
# print(MinRequirements.con)
# print(MinRequirements.cha)
print("#####################")
