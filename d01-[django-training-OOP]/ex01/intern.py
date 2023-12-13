class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name.") -> None:
       self.name = name 
    
    def __str__(self) -> str:
        return self.name

    def work(self) -> Exception:
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return Coffee()
    
    
class Coffee:
    def __str__(self) -> str:
        return "This is the worst coffe you ever tasted."

if __name__ == "__main__":
    mark = Intern('Mark')
    noname = Intern()

    print(mark)
    print(noname)

    print(mark.make_coffee())

    try:
        mark.work()
    except Exception as e:
        print(e)