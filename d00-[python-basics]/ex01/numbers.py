with open("numbers.txt", 'r') as f:
    lines = "".join(f.readlines()).split(",")
    [print(i) for i in lines]
