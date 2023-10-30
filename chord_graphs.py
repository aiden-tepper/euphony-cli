import networkx as nx

Major = nx.DiGraph()

major_chords = ["I", "viidim/iii", "V/iii", "viidim/vi", "V/vi", "viidim/ii", "V/ii", "viidim/V", "VIV", "viidim/IV", "V/IV", "iii", "vi", "IV", "ii", "viidim", "V6/4", "N6", "+6", "V"]
Major.add_nodes_from(major_chords)

major_transitions = [
    ("I", "viidim/iii"),
    ("I", "V/iii"),
    ("I", "viidim/vi"),
    ("I", "V/vi"),
    ("I", "viidim/ii"),
    ("I", "V/ii"),
    ("I", "viidim/V"),
    ("I", "V/V"),
    ("I", "viidim/IV"),
    ("I", "V/IV"),
    ("I", "iii"),
    ("I", "vi"),
    ("I", "IV"),
    ("I", "ii"),
    ("I", "viidim"),
    ("I", "V6/4"),
    ("I", "N6"),
    ("I", "+6"),
    ("I", "V"),

    ("viidim/iii", "V/vi"),
    ("viidim/iii", "viidim/vi"),
    ("viidim/iii", "iii"),
    ("V/iii", "V/vi"),
    ("V/iii", "viidim/vi"),
    ("V/iii", "iii"),

    ("viidim/vi", "viidim/ii"),
    ("viidim/vi", "V/ii"),
    ("viidim/vi", "vi"),
    ("V/vi", "viidim/ii"),
    ("V/vi", "V/ii"),
    ("V/vi", "vi"),

    ("viidim/ii", "viidim/V"),
    ("viidim/ii", "V/V"),
    ("viidim/ii", "ii"),
    ("V/ii", "viidim/V"),
    ("V/ii", "V/V"),
    ("V/ii", "ii"),

    ("viidim/V", "viidim/IV"),
    ("viidim/V", "V/IV"),
    ("viidim/V", "viidim"),
    ("viidim/V", "V6/4"),
    ("viidim/V", "+6"),
    ("viidim/V", "N6"),
    ("viidim/V", "V"),
    ("V/V", "viidim/IV"),
    ("V/V", "V/IV"),
    ("V/V", "viidim"),
    ("V/V", "V6/4"),
    ("V/V", "+6"),
    ("V/V", "N6"),
    ("V/V", "V"),

    ("viidim/IV", "IV"),
    ("V/IV", "IV"),

    ("iii", "viidim/vi"),
    ("iii", "V/vi"),
    ("iii", "viidim/ii"),
    ("iii", "V/ii"),
    ("iii", "IV"),
    ("iii", "vi"),

    ("vi", "viidim/V"),
    ("vi", "V/V"),
    ("vi", "viidim/ii"),
    ("vi", "V/ii"),
    ("vi", "IV"),
    ("vi", "ii"),
    ("vi", "V"),

    ("IV", "viidim/V"),
    ("IV", "V/V"),
    ("IV", "I"),
    ("IV", "ii"),
    ("IV", "viidim"),
    ("IV", "V6/4"),
    ("IV", "+6"),
    ("IV", "N6"),
    ("IV", "V"),

    ("ii", "I"),
    ("ii", "viidim"),
    ("ii", "V6/4"),
    ("ii", "+6"),
    ("ii", "N6"),
    ("ii", "V"),

    ("viidim", "V6/4"),
    ("viidim", "+6"),
    ("viidim", "N6"),
    ("viidim", "V"),
    ("viidim", "I"),

    ("+6", "V6/4"),
    ("V6/4", "V"),
    ("N6", "V"),
    ("V", "I"),
    ("V", "vi")
]
Major.add_edges_from(major_transitions)

Major.edges["IV", "I"]["note"] = "Plagal Cadence"
Major.edges["viidim", "I"]["note"] = "Leading Tone Cadence"
Major.edges["V", "I"]["note"] = "Authentic Cadence"
Major.edges["V", "vi"]["note"] = "Deceptive Cadence"


Minor = nx.DiGraph()

minor_chords = ["viidim/IV", "V7/IV", "viidim/VII", "V7/VII", "viidim/III", "V7/III", "viidim/vi", "V7/vi", "viidim/V", "V/V", "iv", "VII", "III", "VI", "iv", "iidim", "N6", "+6", "V6/4", "viidim", "V", "i", "I"]
Minor.add_nodes_from(minor_chords)

minor_transitions = [
    ("i", "viidim/IV"),
    ("i", "V7/IV"),
    ("i", "viidim/VII"),
    ("i", "V7/VII"),
    ("i", "viidim/III"),
    ("i", "V7/III"),
    ("i", "viidim/vi"),
    ("i", "V7/vi"),
    ("i", "viidim/V"),
    ("i", "V/V"),
    ("i", "iv"),
    ("i", "VII"),
    ("i", "III"),
    ("i", "VI"),
    ("i", "iv"),
    ("i", "iidim"),
    ("i", "N6"),
    ("i", "+6"),
    ("i", "V6/4"),
    ("i", "viidim"),
    ("i", "V"),

    ("viidim/IV", "viidim/VII"),
    ("viidim/IV", "V7/VII"),
    ("viidim/IV", "iv"),
    ("V7/IV", "viidim/VII"),
    ("V7/IV", "V7/VII"),
    ("V7/IV", "iv"),

    ("viidim/VII", "viidim/III"),
    ("viidim/VII", "V7/III"),
    ("viidim/VII", "VII"),
    ("V7/VII", "viidim/III"),
    ("V7/VII", "V7/III"),
    ("V7/VII", "VII"),

    ("viidim/III", "viidim/vi"),
    ("viidim/III", "V7/vi"),
    ("viidim/III", "III"),
    ("V7/III", "viidim/vi"),
    ("V7/III", "V7/vi"),
    ("V7/III", "III"),

    ("viidim/vi", "VI"),
    ("viidim/vi", "iv"),
    ("viidim/vi", "iidim"),
    ("V7/vi", "VI"),
    ("V7/vi", "iv"),
    ("V7/vi", "iidim"),

    ("viidim/V", "V6/4"),
    ("viidim/V", "viidim"),
    ("viidim/V", "V"),
    ("V7/V", "V6/4"),
    ("V7/V", "viidim"),
    ("V7/V", "V"),

    ("iv", "viidim/III"),
    ("iv", "V7/iii"),
    ("iv", "VII"),

    ("VII", "III"),
    ("VII", "i"),

    ("III", "viidim/vi"),
    ("III", "V7/vi"),
    ("III", "VI"),

    ("VI", "iv"),
    ("VI", "iidim"),
    ("VI", "N6"),
    ("VI", "+6"),

    ("iv", "viidim/V"),
    ("iv", "V/V"),
    ("iv", "V6/4"),
    ("iv", "viidim"),
    ("iv", "V"),

    ("iidim", "viidim/V"),
    ("iidim", "V/V"),
    ("iidim", "V6/4"),
    ("iidim", "viidim"),
    ("iidim", "V"),

    ("V6/4", "I"),
    ("viidim", "i"),
    ("viidim", "V"),
    ("V", "i"),
    ("V", "VI"),
    ("V", "N6"),
    ("V", "+6"),
    ("N6", "V"),
    ("+6", "V")
]
Minor.add_edges_from(minor_transitions)

Minor.edges["VII", "i"]["note"] = "Aeolian Cadence"
Minor.edges["viidim", "i"]["note"] = "Leading Tone Cadence"
Minor.edges["V", "i"]["note"] = "Authentic Cadence"
Minor.edges["V", "VI"]["note"] = "Deceptive Cadence"
Minor.edges["V6/4", "I"]["note"] = "Picardy Cadence"