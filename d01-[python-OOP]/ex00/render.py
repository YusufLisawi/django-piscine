import sys, os
from settings import name, surname, title, age, profession

def read_file(filename: str) -> str:
    with open(filename, 'r') as f:
        return "".join(f.readlines())
        

def write_file(filename: str, html: str) -> None:
    with open(filename, 'w') as f:
        f.write(html) 

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        exit(1)
    if os.path.exists(args[0]) == False or args[0].endswith(".template") == False:
        exit(1)
    template = read_file(args[0])
    html = template.format(name=name,
                           title=title,
                           surname=surname,
                           age=age,
                           profession=profession)
    
    write_file(args[0].replace('.template', '.html'), html)
    
if __name__ == "__main__":
    main()