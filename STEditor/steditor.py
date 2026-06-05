import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def svim():
    name=input("Filename with extension: ")
    clear()
    lines = []
    print("Svim - 1.0.0")
    while True:
        code=input()
        if code == ":sq":
            with open(name, 'w') as f:
                wcode="\n".join(lines)
                f.write(wcode)
                clear()
                break
        elif code == ":q":
            ch=input("Are you sure? Changes will be lost.")
            if ch.upper() == "Y":
                clear()
                break
            else:
                pass
        elif code == ":s":
            with open(name, 'w') as f:
                wcode = "\n".join(lines)
                f.write(wcode)
    
        else:
            lines.append(code)
svim()