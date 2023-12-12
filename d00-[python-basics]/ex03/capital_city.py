import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

args = sys.argv[1:]

if len(args) == 1:
    if args[0] in states.keys():
        print(capital_cities[states[args[0]]])
    else:
        print("Unknown state")