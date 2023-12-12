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
        inputs = [" ".join([j.capitalize() for j in i.strip().split(" ")]) for i in args[0].split(",") if len(i.strip()) > 0]
        for i in inputs:
            if i in states.keys():
                print(f'{capital_cities[states[i]]} is the capital of {i}')
            elif i in capital_cities.values():
                res = search_by_value(i)
                print(f'{i} is the capital of {res}')
            else:
                print(f'{i} is neither a capital city nor a state')

if __name__ == "__main__":
    main()