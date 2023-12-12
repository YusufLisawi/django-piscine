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
    for k, v in capital_cities.items():
        if v == args[0]:
            for key, val in states.items():
                if k == val:
                    print(key)
                    exit()
    print("Unknown capital city")
        