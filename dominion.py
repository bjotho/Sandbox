import numpy as np
import warnings


# Card names

# Base game cards
cellar = "Kjeller"
chapel = "Kapell"
moat = "Vollgrav"
chancellor = "Rikskanseller"
village = "Landsby"
woodcutter = "Tømmerhogger"
workshop = "Verksted"
bureaucrat = "Byråkrat"
feast = "Gilde"
gardens = "Park"
militia = "Hird"
moneylender = "Pengeutlåner"
remodel = "Ombygging"
smithy = "Smie"
spy = "Spion"
thief = "Tyv"
throne_room = "Tronsal"
council_room = "Rådssal"
festival = "Festival"
laboratory = "Laboratorium"
library = "Bibliiotek"
market = "Marked"
mine = "Gruve"
witch = "Heks"
adventurer = "Eventyrer"

# Seaside cards
ambassador = "Ambassador"
bazaar = "Bazaar"
caravan = "Caravan"
cutpurse = "Cutpurse"
embargo = "Embargo"
explorer = "Explorer"
fishing_village = "Fishing Village"
ghost_ship = "Ghost Ship"
haven = "Haven"
island = "Island"
lighthouse = "Lighthouse"
lookout = "Lookout"
merchant_ship = "Merchant Ship"
native_village = "Native Village"
navigator = "Navigator"
outpost = "Outpost"
pearl_diver = "Pearl Diver"
pirate_ship = "Pirate Ship"
salvager = "Salvager"
sea_hag = "Sea Hag"
smugglers = "Smugglers"
tactician = "Tactician"
treasure_map = "Treasure Map"
treasury = "Treasury"
warehouse = "Warehouse"
wharf = "Wharf"


# Prosperity cards
workers_village = "Arbeiderlandsby"
bank = "Bank"
bishop = "Biskop"
counting_house = "Bokholderi"
venture = "Forretninger"
peddler = "Gateselger"
trade_route = "Handelsrute"
city = "Kjøpstad"
royal_seal = "Kongelig Segl"
kings_court = "Kongens Hoff"
contraband = "Kontrabande"
goons = "Ludendreiere"
loan = "Lån"
rabble = "Mobb"
monument = "Monument"
mint = "Myntmakeri"
expand = "Påbygning"
mountebank = "Sjarlatan"
hoard = "Skattkammer"
quarry = "Steinbrudd"
grand_market = "Stormarked"
forge = "Sverdmakeri"
talisman = "Talisman"
watchtower = "Vakttårn"
vault = "Velv"


# Alchemy cards
transmute = "Transmute"
vineyard = "Vineyard"
herbalist = "Herbalist"
apothecary = "Apothecary"
scrying_pool = "Scrying Pool"
university = "University"
alchemist = "Alchemist"
familiar = "Familiar"
philosophers_stone = "Philosopher\'s Stone"
golem = "Golem"
apprentice = "Apprentice"
possession = "Possession"


# Dark Ages cards
altar = "Altar"
armory = "Armory"
band_of_misfits = "Band of Misfits"
bandit_camp = "Bandit Camp"
beggar = "Beggar"
catacombs = "Catacombs"
count = "Count"
counterfeit = "Counterfeit"
cultist = "Cultist"
death_cart = "Death Cart"
forager = "Forager"
fortress = "Fortress"
graverobber = "Graverobber"
hunting_grounds = "Hunting Grounds"
ironmonger = "Ironmonger"
junk_dealer = "Junk Dealer"
marauder = "Marauder"
market_square = "Market Square"
mystic = "Mystic"
pillage = "Pillage"
poor_house = "Poor House"
procession = "Procession"
rebuild = "Rebuild"
rogue = "Rogue"
sage = "Sage"
scavenger = "Scavenger"
squire = "Squire"
hermit = "Hermit + Madman"
urchin = "Urchin + Mercenary"
rats = "Rats"
storeroom = "Storeroom"
vagrant = "Vagrant"
wandering_minstrel = "Wandering Minstrel"
feodum = "Feodum"
knights = "Knights"


# Empires cards
archive = "Archive"
capital = "Capital"
catapult_rocks = "Catapult + Rocks"
chariot_race = "Chariot Race"
charm = "Charm"
city_quarter = "City Quarter"
crown = "Crown"
encampment_plunder = "Encampment + Plunder"
enchantress = "Enchantress"
engineer = "Engineer"
farmers_market = "Farmers\' Market"
forum = "Forum"
gladiator_fortune = "Gladiator + Fortune"
groundskeeper = "Groundskeeper"
legionary = "Legionary"
overlord = "Overlord"
patrician_emporium = "Patrician + Emporium"
royal_blacksmith = "Royal Blacksmith"
sacrifice = "Sacrifice"
settlers_bustling_village = "Settlers + Bustling Village"
temple = "Temple"
villa = "Villa"
wild_hunt = "Wild Hunt"
castles = "Castles"


# Renaissance cards
border_guard = "Border Guard"
ducat = "Ducat"
lackeys = "Lackeys"
acting_troupe = "Acting Troupe"
cargo_ship = "Cargo Ship"
experiment = "Experiment"
improve = "Improve"
flag_bearer = "Flag Bearer"
hideout = "Hideout"
inventor = "Inventor"
mountain_village = "Mountain Village"
patron = "Patron"
priest = "Priest"
research = "Research"
silk_merchant = "Silk Merchant"
old_witch = "Old Witch"
recruiter = "Recruiter"
scepter = "Scepter"
scholar = "Scholar"
sculptor = "Sculptor"
seer = "Seer"
spices = "Spices"
swashbuckler = "Swashbuckler"
treasurer = "Treasurer"
villain = "Villain"


# Allies cards
augurs = "Augurs"
barbarian = "Barbarian"
bauble = "Bauble"
broker = "Broker"
capital_city = "Capital City"
carpenter = "Carpenter"
clashes = "Clashes"
contract = "Contract"
courier = "Courier"
emissary = "Emissary"
forts = "Forts"
galleria = "Galleria"
guildmaster = "Guildmaster"
highwayman = "Highwayman"
hunter = "Hunter"
importer = "Importer"
innkeeper = "Innkeeper"
marquis = "Marquis"
merchant_camp = "Merchant Camp"
modify = "Modify"
odysseys = "Odysseys"
royal_gallery = "Royal Gallery"
sentinel = "Sentinel"
skirmisher = "Skirmisher"
specialist = "Specialist"
swap = "Swap"
sycophant = "Sycophant"
town = "Town"
townsfolk = "Townsfolk"
underling = "Underling"
wizards = "Wizards"


# Projects
cathedral = "Cathedral"
city_gate = "City Gate"
pageant = "Pageant"
sewers = "Sewers"
star_chart = "Star Chart"
exploration = "Exploration"
fair = "Fair"
silos = "Silos"
sinister_plot = "Sinister Plot"
academy = "Academy"
capitalism = "Capitalism"
fleet = "Fleet"
guildhall = "Guildhall"
piazza = "Piazza"
road_network = "Road Network"
barracks = "Barracks"
crop_rotation = "Crop Rotation"
innovation = "Innovation"
canal = "Canal"
citadel = "Citadel"


# Events
triumph = "Triumph"
annex = "Annex"
donate = "Donate"
advance = "Advance"
delve = "Delve"
tax = "Tax"
banquet = "Banquet"
ritual = "Ritual"
salt_the_earth = "Salt the Earth"
wedding = "Wedding"
windfall = "Windfall"
conquest = "Conquest"
dominate = "Dominate"


# Landmarks
aqueduct = "Aqueduct"
arena = "Arena"
bandit_fort = "Bandit Fort"
basilica = "Basilica"
baths = "Baths"
battlefield = "Battlefield"
colonnade = "Colonnade"
defiled_shrine = "Defiled Shrine"
fountain = "Fountain"
keep = "Keep"
labirynth = "Labirynth"
mountain_pass = "Mountain Pass"
museum = "Museum"
obelisk = "Obelisk"
orchard = "Orchard"
palace = "Palace"
tomb = "Tomb"
tower = "Tower"
triumphal_arch = "Triumphal Arch"
wall = "Wall"
wolf_den = "Wolf Den"


# Allies
architects_guild = "Architects\' Guild"
band_of_nomads = "Band of Nomads"
cave_dwellers = "Cave Dwellers"
circle_of_witches = "Circle of Witches"
city_state = "City-state"
coastal_haven = "Coastal Haven"
crafters_guild = "Crafters\' Guild"
desert_guides = "Desert Guides"
family_of_inventors = "Family of Inventors"
fellowship_of_scribes = "Fellowship of Scribes"
forest_dwellers = "Forest Dwellers"
gang_of_pickpockets = "Gang of Pickpockets"
island_folk = "Island Folk"
league_of_bankers = "League of Bankers"
league_of_shopkeepers = "League of Shopkeepers"
market_towns = "Market Towns"
mountain_folk = "Mountain Folk"
order_of_astrologers = "Order of Astrologers"
order_of_masons = "Order of Masons"
peaceful_cult = "Peaceful Cult"
plateau_shepherds = "Plateau Shepherds"
trappers_lodge = "Trappers\' Lodge"
woodworkers_guild = "Woodworkers\' Guild"

liasion_cards = [bauble,
                 sycophant,
                 importer,
                 wizards,
                 underling,
                 broker,
                 contract,
                 emissary,
                 guildmaster]


base = [moat,
        library,
        bureaucrat,
        adventurer,
        festival,
        feast,
        mine,
        witch,
        militia,
        chapel,
        cellar,
        laboratory,
        village,
        market,
        remodel,
        moneylender,
        chancellor,
        council_room,
        smithy,
        spy,
        throne_room,
        thief,
        woodcutter,
        workshop,
        gardens]

seaside = [ambassador,
           bazaar,
           caravan,
           cutpurse,
           embargo,
           explorer,
           fishing_village,
           ghost_ship,
           haven,
           island,
           lighthouse,
           lookout,
           merchant_ship,
           native_village,
           navigator,
           outpost,
           pearl_diver,
           pirate_ship,
           salvager,
           sea_hag,
           smugglers,
           tactician,
           treasure_map,
           treasury,
           warehouse,
           wharf]

alchemy = [transmute,
           vineyard,
           herbalist,
           apothecary,
           scrying_pool,
           university,
           alchemist,
           familiar,
           philosophers_stone,
           golem,
           apprentice,
           possession]

prosperity = [workers_village,
              bank,
              bishop,
              counting_house,
              venture,
              peddler,
              trade_route,
              city,
              royal_seal,
              kings_court,
              contraband,
              goons,
              loan,
              rabble,
              monument,
              mint,
              expand,
              mountebank,
              hoard,
              quarry,
              grand_market,
              forge,
              talisman,
              watchtower,
              vault]

# cornucopia

# hinterlands

dark_ages = [altar,
             armory,
             band_of_misfits,
             bandit_camp,
             beggar,
             catacombs,
             count,
             counterfeit,
             cultist,
             death_cart,
             forager,
             fortress,
             graverobber,
             hunting_grounds,
             ironmonger,
             junk_dealer,
             marauder,
             market_square,
             mystic,
             pillage,
             poor_house,
             procession,
             rebuild,
             rogue,
             sage,
             scavenger,
             squire,
             hermit,
             urchin,
             rats,
             storeroom,
             vagrant,
             wandering_minstrel,
             feodum,
             knights]

# guilds

# adventures

empires = [archive,
           capital,
           catapult_rocks,
           chariot_race,
           charm,
           city_quarter,
           crown,
           encampment_plunder,
           enchantress,
           engineer,
           farmers_market,
           forum,
           gladiator_fortune,
           groundskeeper,
           legionary,
           overlord,
           patrician_emporium,
           royal_blacksmith,
           sacrifice,
           settlers_bustling_village,
           temple,
           villa,
           wild_hunt,
           castles]

# nocturne

renaissance = [border_guard,
               ducat,
               lackeys,
               acting_troupe,
               cargo_ship,
               experiment,
               improve,
               flag_bearer,
               hideout,
               inventor,
               mountain_village,
               patron,
               priest,
               research,
               silk_merchant,
               old_witch,
               recruiter,
               scepter,
               scholar,
               sculptor,
               seer,
               spices,
               swashbuckler,
               treasurer,
               villain]

# menagerie

allies = [augurs,
          barbarian,
          bauble,
          broker,
          capital_city,
          carpenter,
          clashes,
          contract,
          courier,
          emissary,
          forts,
          galleria,
          guildmaster,
          highwayman,
          hunter,
          importer,
          innkeeper,
          marquis,
          merchant_camp,
          modify,
          odysseys,
          royal_gallery,
          sentinel,
          skirmisher,
          specialist,
          swap,
          sycophant,
          town,
          townsfolk,
          underling,
          wizards]

projects = [cathedral,
            city_gate,
            pageant,
            sewers,
            star_chart,
            exploration,
            fair,
            silos,
            sinister_plot,
            academy,
            capitalism,
            fleet,
            guildhall,
            piazza,
            road_network,
            barracks,
            crop_rotation,
            innovation,
            canal,
            citadel]

events = [triumph,
          annex,
          donate,
          advance,
          delve,
          tax,
          banquet,
          ritual,
          salt_the_earth,
          wedding,
          windfall,
          conquest,
          dominate]

landmarks = [aqueduct,
             arena,
             bandit_fort,
             basilica,
             baths,
             battlefield,
             colonnade,
             defiled_shrine,
             fountain,
             keep,
             labirynth,
             mountain_pass,
             museum,
             obelisk,
             orchard,
             palace,
             tomb,
             tower,
             triumphal_arch,
             wall,
             wolf_den]

ally_cards = [architects_guild,
              band_of_nomads,
              cave_dwellers,
              circle_of_witches,
              city_state,
              coastal_haven,
              crafters_guild,
              desert_guides,
              family_of_inventors,
              fellowship_of_scribes,
              forest_dwellers,
              gang_of_pickpockets,
              island_folk,
              league_of_bankers,
              league_of_shopkeepers,
              market_towns,
              mountain_folk,
              order_of_astrologers,
              order_of_masons,
              peaceful_cult,
              plateau_shepherds,
              trappers_lodge,
              woodworkers_guild]

# Card classes
# actioner = "Actioner"       # Give actions or play action cards
# drawer = "Drawer"           # Draw cards
# buyer = "Buyer"             # Grant buys
# moneymaker = "Moneymaker"   # Grant coins
# trasher = "Trasher"         # Possibility to trash cards
# attacker = "Attacker"       # Attack card
# reactioner = "Reactioner"   # Reaction card
# treasurer = "Treasurer"     # Treasure card
# alt_VP = "Alt_VP"           # Victory card
# duration = "Duration"       # Duration card
# other = "Other"             # Other cards

# card_class_dict = {
#     actioner: [village,
#                festival,
#                throne_room,
#                native_village,
#                fishing_village,
#                bazaar,
#                workers_village,
#                city,
#                kings_court,
#                university,
#                golem,
#                squire,
#                fortress,
#                procession,
#                wandering_minstrel,
#                bandit_camp]
# }

even_spread = "even spread"
weighted = "weighted"
random = "random"

type = random
sets = [base, seaside, prosperity, alchemy, dark_ages, empires, renaissance, allies]
landscape_cards = projects + events + landmarks

# weights must sum to 10
# weights = [1, 2, 2, 0, 0, 5]          # Renaissance
# weights = [1, 1, 1, 5, 1, 1]          # Alchemy
# weights = [2, 2, 2, 0, 2, 2]          # Not Alchemy
# weights = [4, 3, 3, 0, 0, 0]          # Simple
# weights = [5, 0, 5, 0, 0, 0]          # Base + Prosperity
weights = [0, 1, 1, 0, 1, 3, 1, 3]      # Empires + Allies
include = []
exclude = [possession, barbarian]

cards = []

if type == even_spread:
    np.random.shuffle(sets)
    for s in sets:
        np.random.shuffle(s)
    i = 0
    while len(cards) < 10 - len(include):
        c = sets[i % len(sets)][i // len(sets)]
        if c in exclude:
            sets[i % len(sets)].remove(c)
            continue
        cards.append(c)
        i += 1

elif type == weighted:
    for s in sets:
        np.random.shuffle(s)
    for i in range(len(weights)):
        weights[i] /= 10
    # print(f"weights: {weights}")
    while len(cards) < 10 - len(include):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            set_choice = np.random.choice(sets, p=weights)
        if not set_choice[0] in exclude:
            cards.append(set_choice[0])
        set_choice.pop(0)

else:
    for s in sets:
        cards += s
    np.random.shuffle(cards)
    for card in exclude:
        cards.remove(card)

selected_cards = include + cards[:10 - len(include)]

print(f"Cards: {selected_cards}")

if landscape_cards:
    num_side_cards = np.random.randint(1, 3)
    np.random.shuffle(landscape_cards)
    print(f"Extra cards: {landscape_cards[:num_side_cards]}")

if len(set(selected_cards).intersection(liasion_cards)) > 0:
    np.random.shuffle(ally_cards)
    print(f"Ally: {ally_cards[0]}")
