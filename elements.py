
ELEMENTS = {
    1: {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic_number": 1,
        "isotopes": {
            1: {"name": "Protium (Hydrogen-1)", "unstable": False},
            2: {"name": "Deuterium (Hydrogen-2)", "unstable": False},
            3: {"name": "Tritium (Hydrogen-3)", "unstable": True},
        },
        "fact": "Lightest element."
    },
    2: {
        "name": "Helium",
        "symbol": "He",
        "atomic_number": 2,
        "isotopes": {
            3: {"name": "Helium-3", "unstable": False},
            4: {"name": "Helium-4", "unstable": False},
        },
        "fact": "Used in balloons."
    },
    3: {
        "name": "Lithium",
        "symbol": "Li",
        "atomic_number": 3,
        "isotopes": {
            6: {"name": "Lithium-6", "unstable": False},
            7: {"name": "Lithium-7", "unstable": False},
        },
        "fact": "In batteries."
    },
    4: {
        "name": "Beryllium",
        "symbol": "Be",
        "atomic_number": 4,
        "isotopes": {
            9: {"name": "Beryllium-9", "unstable": False},
        },
        "fact": "In aerospace."
    },
    5: {
        "name": "Boron",
        "symbol": "B",
        "atomic_number": 5,
        "isotopes": {
            10: {"name": "Boron-10", "unstable": False},
            11: {"name": "Boron-11", "unstable": False},
        },
        "fact": "Essential for plants."
    },
    6: {
        "name": "Carbon",
        "symbol": "C",
        "atomic_number": 6,
        "isotopes": {
            12: {"name": "Carbon-12", "unstable": False},
            13: {"name": "Carbon-13", "unstable": False},
            14: {"name": "Carbon-14", "unstable": True},
        },
        "fact": "Organic backbone."
    },
    7: {
        "name": "Nitrogen",
        "symbol": "N",
        "atomic_number": 7,
        "isotopes": {
            14: {"name": "Nitrogen-14", "unstable": False},
            15: {"name": "Nitrogen-15", "unstable": False},
        },
        "fact": "Makes up 78% of air."
    },
    8: {
        "name": "Oxygen",
        "symbol": "O",
        "atomic_number": 8,
        "isotopes": {
            16: {"name": "Oxygen-16", "unstable": False},
            17: {"name": "Oxygen-17", "unstable": False},
            18: {"name": "Oxygen-18", "unstable": False},
        },
        "fact": "Used in respiration."
    },
    9: {
        "name": "Fluorine",
        "symbol": "F",
        "atomic_number": 9,
        "isotopes": {
            19: {"name": "Fluorine-19", "unstable": False},
        },
        "fact": "Most reactive element."
    },
    10: {
        "name": "Neon",
        "symbol": "Ne",
        "atomic_number": 10,
        "isotopes": {
            20: {"name": "Neon-20", "unstable": False},
            21: {"name": "Neon-21", "unstable": False},
            22: {"name": "Neon-22", "unstable": False},
        },
        "fact": "Glows in tubes."
    },
    11: {
        "name": "Sodium",
        "symbol": "Na",
        "atomic_number": 11,
        "isotopes": {
            23: {"name": "Sodium-23", "unstable": False},
        },
        "fact": "Highly reactive."
    },
    12: {
        "name": "Magnesium",
        "symbol": "Mg",
        "atomic_number": 12,
        "isotopes": {
            24: {"name": "Magnesium-24", "unstable": False},
            25: {"name": "Magnesium-25", "unstable": False},
            26: {"name": "Magnesium-26", "unstable": False},
        },
        "fact": "In chlorophyll."
    },
    13: {
        "name": "Aluminium",
        "symbol": "Al",
        "atomic_number": 13,
        "isotopes": {
            27: {"name": "Aluminium-27", "unstable": False},
        },
        "fact": "Earth's abundant metal."
    },
    14: {
        "name": "Silicon",
        "symbol": "Si",
        "atomic_number": 14,
        "isotopes": {
            28: {"name": "Silicon-28", "unstable": False},
            29: {"name": "Silicon-29", "unstable": False},
            30: {"name": "Silicon-30", "unstable": False},
        },
        "fact": "Used in chips."
    },
    15: {
        "name": "Phosphorus",
        "symbol": "P",
        "atomic_number": 15,
        "isotopes": {
            31: {"name": "Phosphorus-31", "unstable": False},
        },
        "fact": "Vital for DNA."
    },
    16: {
        "name": "Sulfur",
        "symbol": "S",
        "atomic_number": 16,
        "isotopes": {
            32: {"name": "Sulfur-32", "unstable": False},
            33: {"name": "Sulfur-33", "unstable": False},
            34: {"name": "Sulfur-34", "unstable": False},
            36: {"name": "Sulfur-36", "unstable": False},
        },
        "fact": "Used to vulcanize rubber."
    },
    17: {
        "name": "Chlorine",
        "symbol": "Cl",
        "atomic_number": 17,
        "isotopes": {
            35: {"name": "Chlorine-35", "unstable": False},
            37: {"name": "Chlorine-37", "unstable": False},
        },
        "fact": "Used in disinfectants."
    },
    18: {
        "name": "Argon",
        "symbol": "Ar",
        "atomic_number": 18,
        "isotopes": {
            36: {"name": "Argon-36", "unstable": False},
            38: {"name": "Argon-38", "unstable": False},
            40: {"name": "Argon-40", "unstable": False},
        },
        "fact": "Inert lighting gas."
    },
    19: {
        "name": "Potassium",
        "symbol": "K",
        "atomic_number": 19,
        "isotopes": {
            39: {"name": "Potassium-39", "unstable": False},
            40: {"name": "Potassium-40", "unstable": True},
            41: {"name": "Potassium-41", "unstable": False},
        },
        "fact": "Essential electrolyte."
    },
    20: {
        "name": "Calcium",
        "symbol": "Ca",
        "atomic_number": 20,
        "isotopes": {
            40: {"name": "Calcium-40", "unstable": False},
            42: {"name": "Calcium-42", "unstable": False},
            43: {"name": "Calcium-43", "unstable": False},
            44: {"name": "Calcium-44", "unstable": False},
            46: {"name": "Calcium-46", "unstable": True},
            48: {"name": "Calcium-48", "unstable": True},
        },
        "fact": "Teeth and bones."
    },
    21: {"name":"Scandium","symbol":"Sc","atomic_number":21,"isotopes":{45:"Scandium-45"},"fact":"Aerospace alloy."},
    22: {"name":"Titanium","symbol":"Ti","atomic_number":22,"isotopes":{48:"Titanium-48"},"fact":"Strong & light."},
    23: {"name":"Vanadium","symbol":"V","atomic_number":23,"isotopes":{51:"Vanadium-51"},"fact":"Steel alloying."},
    24: {"name":"Chromium","symbol":"Cr","atomic_number":24,"isotopes":{52:"Chromium-52"},"fact":"Shiny steel."},
    25: {"name":"Manganese","symbol":"Mn","atomic_number":25,"isotopes":{55:"Manganese-55"},"fact":"Steel production."},
    26: {"name":"Iron","symbol":"Fe","atomic_number":26,"isotopes":{56:"Iron-56"},"fact":"Most-used metal."},
    27: {"name":"Cobalt","symbol":"Co","atomic_number":27,"isotopes":{59:"Cobalt-59"},"fact":"Battery cobalt."},
    28: {"name":"Nickel","symbol":"Ni","atomic_number":28,"isotopes":{58:"Nickel-58"},"fact":"Corrosion-resistant."},
    29: {"name":"Copper","symbol":"Cu","atomic_number":29,"isotopes":{63:"Copper-63"},"fact":"Good conductor."},
    30: {"name":"Zinc","symbol":"Zn","atomic_number":30,"isotopes":{64:"Zinc-64"},"fact":"Galvanizes steel."},
    31: {"name":"Gallium","symbol":"Ga","atomic_number":31,"isotopes":{69:"Gallium-69"},"fact":"Melts above room temp."},
    32: {"name":"Germanium","symbol":"Ge","atomic_number":32,"isotopes":{74:"Germanium-74"},"fact":"Optics & semiconductors."},
    33: {"name":"Arsenic","symbol":"As","atomic_number":33,"isotopes":{75:"Arsenic-75"},"fact":"Toxic."},
    34: {"name":"Selenium","symbol":"Se","atomic_number":34,"isotopes":{80:"Selenium-80"},"fact":"In glassmaking."},
    35: {"name":"Bromine","symbol":"Br","atomic_number":35,"isotopes":{79:"Bromine-79"},"fact":"Liquid element."},
    36: {"name":"Krypton","symbol":"Kr","atomic_number":36,"isotopes":{84:"Krypton-84"},"fact":"Lighting gas."},
    37: {"name":"Rubidium","symbol":"Rb","atomic_number":37,"isotopes":{85:"Rubidium-85"},"fact":"Reactive metal."},
    38: {"name":"Strontium","symbol":"Sr","atomic_number":38,"isotopes":{88:"Strontium-88"},"fact":"Fireworks red color."},
    39: {"name":"Yttrium","symbol":"Y","atomic_number":39,"isotopes":{89:"Yttrium-89"},"fact":"LED phosphors."},
    40: {"name":"Zirconium","symbol":"Zr","atomic_number":40,"isotopes":{90:"Zirconium-90"},"fact":"Used in reactors."},
    41: {"name":"Niobium","symbol":"Nb","atomic_number":41,"isotopes":{93:"Niobium-93"},"fact":"Superconductors."},
    42: {"name":"Molybdenum","symbol":"Mo","atomic_number":42,"isotopes":{98:"Molybdenum-98"},"fact":"Steel alloying."},
    43: {"name":"Technetium","symbol":"Tc","atomic_number":43,"isotopes":{},"fact":"No stable isotopes."},
    44: {"name":"Ruthenium","symbol":"Ru","atomic_number":44,"isotopes":{102:"Ruthenium-102"},"fact":"Electronics."},
    45: {"name":"Rhodium","symbol":"Rh","atomic_number":45,"isotopes":{103:"Rhodium-103"},"fact":"Catalyst metal."},
    46: {"name":"Palladium","symbol":"Pd","atomic_number":46,"isotopes":{106:"Palladium-106"},"fact":"Catalytic converters."},
    47: {"name":"Silver","symbol":"Ag","atomic_number":47,"isotopes":{107:"Silver-107"},"fact":"Conducts electricity."},
    48: {"name":"Cadmium","symbol":"Cd","atomic_number":48,"isotopes":{114:"Cadmium-114"},"fact":"Used in batteries."},
    49: {"name":"Indium","symbol":"In","atomic_number":49,"isotopes":{115:"Indium-115"},"fact":"Touchscreens."},
    50: {"name":"Tin","symbol":"Sn","atomic_number":50,"isotopes":{120:"Tin-120"},"fact":"Soldering metal."},
    51: {"name":"Antimony","symbol":"Sb","atomic_number":51,"isotopes":{121:"Antimony-121"},"fact":"Flame retardants."},
    52: {"name":"Tellurium","symbol":"Te","atomic_number":52,"isotopes":{130:"Tellurium-130"},"fact":"Solar cells."},
    53: {"name":"Iodine","symbol":"I","atomic_number":53,"isotopes":{127:"Iodine-127"},"fact":"Important nutrient."},
    54: {"name":"Xenon","symbol":"Xe","atomic_number":54,"isotopes":{132:"Xenon-132"},"fact":"Lighting & anaesthetic."},
    55: {"name":"Cesium","symbol":"Cs","atomic_number":55,"isotopes":{133:"Cesium-133"},"fact":"Atomic clocks."},
    56: {"name":"Barium","symbol":"Ba","atomic_number":56,"isotopes":{138:"Barium-138"},"fact":"Gastrografin contrast."},
    57: {"name":"Lanthanum","symbol":"La","atomic_number":57,"isotopes":{139:"Lanthanum-139"},"fact":"Camera lenses."},
    58: {"name":"Cerium","symbol":"Ce","atomic_number":58,"isotopes":{140:"Cerium-140"},"fact":"Catalysts."},
    59: {"name":"Praseodymium","symbol":"Pr","atomic_number":59,"isotopes":{141:"Praseodymium-141"},"fact":"Magnetic alloys."},
    60: {"name":"Neodymium","symbol":"Nd","atomic_number":60,"isotopes":{142:"Neodymium-142"},"fact":"Strong magnets."},
    61: {"name":"Promethium","symbol":"Pm","atomic_number":61,"isotopes":{},"fact":"No stable isotopes."},
    62: {"name":"Samarium","symbol":"Sm","atomic_number":62,"isotopes":{152:"Samarium-152"},"fact":"Permanent magnets."},
    63: {"name":"Europium","symbol":"Eu","atomic_number":63,"isotopes":{153:"Europium-153"},"fact":"TV phosphors."},
    64: {"name":"Gadolinium","symbol":"Gd","atomic_number":64,"isotopes":{158:"Gadolinium-158"},"fact":"MRI contrast."},
    65: {"name":"Terbium","symbol":"Tb","atomic_number":65,"isotopes":{159:"Terbium-159"},"fact":"Green phosphors."},
    66: {"name":"Dysprosium","symbol":"Dy","atomic_number":66,"isotopes":{164:"Dysprosium-164"},"fact":"Data storage."},
    67: {"name":"Holmium","symbol":"Ho","atomic_number":67,"isotopes":{165:"Holmium-165"},"fact":"Lasers."},
    68: {"name":"Erbium","symbol":"Er","atomic_number":68,"isotopes":{166:"Erbium-166"},"fact":"Fiber optics."},
    69: {"name":"Thulium","symbol":"Tm","atomic_number":69,"isotopes":{169:"Thulium-169"},"fact":"Medical devices."},
    70: {"name":"Ytterbium","symbol":"Yb","atomic_number":70,"isotopes":{174:"Ytterbium-174"},"fact":"Atomic clocks."},
    71: {"name":"Lutetium","symbol":"Lu","atomic_number":71,"isotopes":{175:"Lutetium-175"},"fact":"PET scanners."},
    72: {"name":"Hafnium","symbol":"Hf","atomic_number":72,"isotopes":{180:"Hafnium-180"},"fact":"Nuclear control rods."},
    73: {"name":"Tantalum","symbol":"Ta","atomic_number":73,"isotopes":{181:"Tantalum-181"},"fact":"Used in electronics."},
    74: {"name":"Tungsten","symbol":"W","atomic_number":74,"isotopes":{184:"Tungsten-184"},"fact":"Filaments."},
    75: {"name":"Rhenium","symbol":"Re","atomic_number":75,"isotopes":{186:"Rhenium-186"},"fact":"Jet engines."},
    76: {"name":"Osmium","symbol":"Os","atomic_number":76,"isotopes":{192:"Osmium-192"},"fact":"Dense metal."},
    77: {"name":"Iridium","symbol":"Ir","atomic_number":77,"isotopes":{193:"Iridium-193"},"fact":"High corrosion resistance."},
    78: {"name":"Platinum","symbol":"Pt","atomic_number":78,"isotopes":{195:"Platinum-195"},"fact":"Catalysis / jewelry."},
    79: {"name":"Gold","symbol":"Au","atomic_number":79,"isotopes":{197:"Gold-197"},"fact":"Conductive/jewelry."},
    80: {"name":"Mercury","symbol":"Hg","atomic_number":80,"isotopes":{202:"Mercury-202"},"fact":"Thermometers."},
    81: {"name":"Thallium","symbol":"Tl","atomic_number":81,"isotopes":{205:"Thallium-205"},"fact":"Semiconductors."},
    82: {"name":"Lead","symbol":"Pb","atomic_number":82,"isotopes":{208:"Lead-208"},"fact":"Dense, radiation shield."},
    83: {"name": "Bismuth", "symbol": "Bi", "atomic_number": 83, "isotopes": {209: {"name": "Bismuth-209", "unstable": False}}, "fact": "Heaviest stable isotope."},
    84: {"name": "Polonium", "symbol": "Po", "atomic_number": 84, "isotopes": {210: {"name": "Polonium-210", "unstable": True}}, "fact": "Highly radioactive."},
    85: {"name": "Astatine", "symbol": "At", "atomic_number": 85, "isotopes": {210: {"name": "Astatine-210", "unstable": True}}, "fact": "Rare halogen."},
    86: {"name": "Radon", "symbol": "Rn", "atomic_number": 86, "isotopes": {222: {"name": "Radon-222", "unstable": True}}, "fact": "Radioactive gas."},
    87: {"name": "Francium", "symbol": "Fr", "atomic_number": 87, "isotopes": {223: {"name": "Francium-223", "unstable": True}}, "fact": "Extremely rare."},
    88: {"name": "Radium", "symbol": "Ra", "atomic_number": 88, "isotopes": {226: {"name": "Radium-226", "unstable": True}}, "fact": "Used in early cancer treatments."},
    89: {"name": "Actinium", "symbol": "Ac", "atomic_number": 89, "isotopes": {227: {"name": "Actinium-227", "unstable": True}}, "fact": "Radioactive glow."},
    90: {"name": "Thorium", "symbol": "Th", "atomic_number": 90, "isotopes": {232: {"name": "Thorium-232", "unstable": True}}, "fact": "Potential nuclear fuel."},
    91: {"name": "Protactinium", "symbol": "Pa", "atomic_number": 91, "isotopes": {231: {"name": "Protactinium-231", "unstable": True}}, "fact": "Very rare and radioactive."},
    92: {"name": "Uranium", "symbol": "U", "atomic_number": 92, "isotopes": {238: {"name": "Uranium-238", "unstable": True}}, "fact": "Nuclear fuel."},
    93: {"name": "Neptunium", "symbol": "Np", "atomic_number": 93, "isotopes": {237: {"name": "Neptunium-237", "unstable": True}}, "fact": "First transuranic element."},
    94: {"name": "Plutonium", "symbol": "Pu", "atomic_number": 94, "isotopes": {239: {"name": "Plutonium-239", "unstable": True}}, "fact": "Used in nuclear weapons."},
    95: {"name": "Americium", "symbol": "Am", "atomic_number": 95, "isotopes": {241: {"name": "Americium-241", "unstable": True}}, "fact": "Used in smoke detectors."},
    96: {"name": "Curium", "symbol": "Cm", "atomic_number": 96, "isotopes": {247: {"name": "Curium-247", "unstable": True}}, "fact": "Named after Marie Curie."},
    97: {"name": "Berkelium", "symbol": "Bk", "atomic_number": 97, "isotopes": {247: {"name": "Berkelium-247", "unstable": True}}, "fact": "Named after Berkeley."},
    98: {"name": "Californium", "symbol": "Cf", "atomic_number": 98, "isotopes": {251: {"name": "Californium-251", "unstable": True}}, "fact": "Neutron source."},
    99: {"name": "Einsteinium", "symbol": "Es", "atomic_number": 99, "isotopes": {252: {"name": "Einsteinium-252", "unstable": True}}, "fact": "Named after Einstein."},
    100: {"name": "Fermium", "symbol": "Fm", "atomic_number": 100, "isotopes": {257: {"name": "Fermium-257", "unstable": True}}, "fact": "Discovered in H-bomb debris."},
    101: {"name": "Mendelevium", "symbol": "Md", "atomic_number": 101, "isotopes": {258: {"name": "Mendelevium-258", "unstable": True}}, "fact": "Named after Mendeleev."},
    102: {"name": "Nobelium", "symbol": "No", "atomic_number": 102, "isotopes": {259: {"name": "Nobelium-259", "unstable": True}}, "fact": "Named after Nobel."},
    103: {"name": "Lawrencium", "symbol": "Lr", "atomic_number": 103, "isotopes": {262: {"name": "Lawrencium-262", "unstable": True}}, "fact": "Named after Ernest Lawrence."},
    104: {"name": "Rutherfordium", "symbol": "Rf", "atomic_number": 104, "isotopes": {267: {"name": "Rutherfordium-267", "unstable": True}}, "fact": "Named after Rutherford."},
    105: {"name": "Dubnium", "symbol": "Db", "atomic_number": 105, "isotopes": {268: {"name": "Dubnium-268", "unstable": True}}, "fact": "Named after Dubna, Russia."},
    106: {"name": "Seaborgium", "symbol": "Sg", "atomic_number": 106, "isotopes": {271: {"name": "Seaborgium-271", "unstable": True}}, "fact": "Named after Glenn Seaborg."},
    107: {"name": "Bohrium", "symbol": "Bh", "atomic_number": 107, "isotopes": {270: {"name": "Bohrium-270", "unstable": True}}, "fact": "Named after Niels Bohr."},
    108: {"name": "Hassium", "symbol": "Hs", "atomic_number": 108, "isotopes": {277: {"name": "Hassium-277", "unstable": True}}, "fact": "Named after Hesse, Germany."},
    109: {"name": "Meitnerium", "symbol": "Mt", "atomic_number": 109, "isotopes": {278: {"name": "Meitnerium-278", "unstable": True}}, "fact": "Named after Lise Meitner."},
    110: {"name": "Darmstadtium", "symbol": "Ds", "atomic_number": 110, "isotopes": {281: {"name": "Darmstadtium-281", "unstable": True}}, "fact": "Discovered in Darmstadt."},
    111: {"name": "Roentgenium", "symbol": "Rg", "atomic_number": 111, "isotopes": {282: {"name": "Roentgenium-282", "unstable": True}}, "fact": "Named after Röntgen."},
    112: {"name": "Copernicium", "symbol": "Cn", "atomic_number": 112, "isotopes": {285: {"name": "Copernicium-285", "unstable": True}}, "fact": "Named after Copernicus."},
    113: {"name": "Nihonium", "symbol": "Nh", "atomic_number": 113, "isotopes": {286: {"name": "Nihonium-286", "unstable": True}}, "fact": "Discovered in Japan."},
    114: {"name": "Flerovium", "symbol": "Fl", "atomic_number": 114, "isotopes": {289: {"name": "Flerovium-289", "unstable": True}}, "fact": "Named after Flerov Lab."},
    115: {"name": "Moscovium", "symbol": "Mc", "atomic_number": 115, "isotopes": {290: {"name": "Moscovium-290", "unstable": True}}, "fact": "Named after Moscow."},
    116: {"name": "Livermorium", "symbol": "Lv", "atomic_number": 116, "isotopes": {293: {"name": "Livermorium-293", "unstable": True}}, "fact": "Named after Livermore Lab."},
    117: {"name": "Tennessine", "symbol": "Ts", "atomic_number": 117, "isotopes": {294: {"name": "Tennessine-294", "unstable": True}}, "fact": "Named after Tennessee."},
    118: {"name": "Oganesson", "symbol": "Og", "atomic_number": 118, "isotopes": {294: {"name": "Oganesson-294", "unstable": True}}, "fact": "Named after Yuri Oganessian."}
}
