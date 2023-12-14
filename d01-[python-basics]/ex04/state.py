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

def search_by_value(arg) -> str:
    for k, v in capital_cities.items():
        if v == arg:
            for key, val in states.items():
                if k == val:
                    return key
    return None

def main():
    if len(args) == 1:
        res = search_by_value(args[0])
        if res:
            print(res)
        else:
            print("Unknown capital city")

if __name__ == "__main__":
    main()