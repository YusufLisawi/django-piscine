from beverages import *
import random

class CoffeeMachine:
    
    def __init__(self) -> None:
        self.broken = False
        self.drinks_served = 0
    
    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.name = 'empty cup'
            self.price = .90
            
        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"
    
    class BrokeMachineException(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.broken = False
        self.drinks_served = 0
    
    def serve(self, derived: HotBeverage) -> HotBeverage:
        if self.drinks_served > 10 or self.broken:
            self.broken = True
            raise CoffeeMachine.BrokeMachineException()
        self.drinks_served += 1
        return random.choice([derived, CoffeeMachine.EmptyCup()])

if __name__ == "__main__":
    machine = CoffeeMachine()
     
    for i in range(15):
        try:
            drink = machine.serve(random.choice([Cappuccino(), Tea(), Coffee(), Chocolate(), HotBeverage()]))
            print(f"Served: {drink.name}")
        except CoffeeMachine.BrokeMachineException:
            print("The machine is broken. Repairing...")
            machine.repair()
            print("Machine repaired. Starting again...")
        else:
            if machine.broken:
                print("The machine is broken. Repairing...")
                machine.repair()
                print("Machine repaired. Starting again...")