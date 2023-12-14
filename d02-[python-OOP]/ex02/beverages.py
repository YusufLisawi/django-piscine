class HotBeverage:
    def __init__(self) -> None:
        self.price = .30
        self.name = 'hot beverage'

    def description(self) -> str:
        return "Just some hot water in a cup"
    
    def __str__(self) -> str:
        return f'name : {self.name}\nprice : {self.price}\ndescription : {self.description()}'

class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.price = .40
        self.name = 'coffee'
    
    def description(self) -> str:
        return 'A coffee, to stay awake.'

class Tea(HotBeverage):
    def __init__(self) -> None:
        self.name = "tea"
        self.price = .30

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name = "chocolate"
        self.price = .50
    
    def description(self) -> str:
        return 'Chocolate, sweet chocolate...'

class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name = 'cappuccino'
        self.price = .45
    
    def description(self) -> str:
        return "Un po' di Italila nella sua tazza!"
    

if __name__ == "__main__":
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())