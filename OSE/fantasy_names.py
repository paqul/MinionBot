from rolls import r

first_names = [
    "Kaelen",
    "Lysander",
    "Aurora",
    "Thorne",
    "Roran",
    "Selene",
    "Dorian",
    "Aria",
    "Talon",
    "Rowan",
    "Livia",
    "Gryphon",
    "Elowen",
    "Thaddeus",
    "Serafina",
    "Drystan",
    "Arwynn",
    "Magnus",
    "Lyanna",
    "Eirian",
    "Oberon",
    "Freya",
    "Tristan",
    "Celestia",
    "Kairos",
    "Serenity",
    "Bastian",
    "Elara",
    "Lucien",
    "Rhiannon",
    "Silas",
    "Thalia",
    "Ashlynne",
    "Ryker",
    "Tavian",
    "Leona",
    "Valen",
    "Lysandra",
    "Arianwen",
    "Ryland",
    "Seraphina",
    "Declan",
    "Alaric",
    "Asher",
    "Lyra",
    "Aerith",
    "Draven",
    "Finnian",
    "Isolde",
    "Orion",
    "Ember",
    "Aurelia",
    "Cassius",
    "Elysia",
    "Finnian",
    "Isolde",
    "Lysandra",
    "Maeve",
    "Nikolai",
    "Ravenna",
    "Thalia",
    "Xander",
    "Zephyr",
    "Aria",
    "Cyrus",
    "Elara",
    "Faelan",
    "Ivy",
    "Lorenzo",
    "Nova",
    "Rune",
    "Talia",
    "Zara",
    "Branwen",
    "Darius",
    "Evangeline",
    "Felix",
    "Isla",
    "Lyra",
    "Orion",
    "Soraya",
    "Theo",
    "Zora",
    "Bastian",
    "Daphne",
    "Ezra",
    "Fiona",
    "Jasper",
    "Mira",
    "Ophelia",
    "Sebastian",
    "Theodora",
    "Zephyra",
    "Caius",
    "Eira",
    "Finley",
    "Juliet",
    "Mae",
    "Orla",
    "Raphael",
    "Seren",
    "Tiberius",
    "Zarael",
    "Aurelian",
    "Cassia",
    "Elysian",
    "Finnick",
    "Isadora",
    "Lyric",
    "Maelle",
    "Naida",
    "Raven",
    "Thaddea",
    "Xanthe",
    "Zephyrine",
    "Artemis",
    "Cyril",
    "Elowyn",
    "Faelwen",
    "Icarus",
    "Lysistrata",
    "Nyx",
    "Rufus",
    "Tamsin",
    "Zephyrus",
    "Bellatrix",
    "Dorian",
    "Evelina",
    "Frost",
    "Ismene",
    "Lysander",
    "Odessa",
    "Soren",
    "Thelonius",
    "Zephyrion",
    "Calista",
    "Evangeline",
    "Freyja",
    "Jaxon",
    "Morrigan",
    "Orpheus",
    "Severin",
    "Theodosia",
    "Zephyrine",
    "Caledon",
    "Elara",
    "Finola",
    "Juniper",
    "Maia",
    "Orson",
    "Sable",
    "Tiberia",
    "Zephyros"
]

last_names = [
    "Sunseeker",
    "Frostwhisper",
    "Shadowflame",
    "Moonlight",
    "Fireforge",
    "Stargazer",
    "Stormrider",
    "Silverwind",
    "Nightshade",
    "Thunderheart",
    "Ravencrest",
    "Swiftblade",
    "Ironfist",
    "Goldenshield",
    "Steelbane",
    "Darkwater",
    "Bloodmoon",
    "Blackthorn",
    "Winterbourne",
    "Dragonbane",
    "Highwind",
    "Starfall",
    "Wildheart",
    "Flamebringer",
    "Blacksteel",
    "Icewind",
    "Lightbringer",
    "Whitewind",
    "Soulforge",
    "Duskwalker",
    "Shadowblade",
    "Thunderstone",
    "Silverleaf",
    "Darkflame",
    "Riversong",
    "Stonehammer",
    "Swiftarrow",
    "Brightwood",
    "Stormbreaker",
    "Blackwater",
    "Skywatcher",
    "Moonshadow",
    "Frostblade",
    "Fireheart",
    "Shadowhunter",
    "Stormborn",
    "Winterheart",
    "Bloodthorn",
    "Stonesong"
]


def randomize_fantasy_name():
    first_name = first_names[r(0, len(first_names)-1)]
    last_name = last_names[r(0, len(last_names)-1)]
    selected_name = f"{first_name} {last_name}"
    return selected_name


if __name__ == "__main__":
    name = randomize_fantasy_name()
    print(name)
