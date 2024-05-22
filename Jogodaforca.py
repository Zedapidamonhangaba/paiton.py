def Forca(tentativa):
    f1 = "     +--------+  "
    f2 = "     |        |  "
    f3 = "     |        O  "
    f4 = "     |       /|\ " 
    f5 = "     |        |  "
    f6 = "     |       / \ "
    f7 = " ____|____       "

    if tentativa >= 1:
        f2 = "  |       | "
     if tentativa >= 1:
        f2 = "  |       | "

    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)
    

def Continue():
    while True:
        print("" * 20)
        novamete = input("Quer jogar de novo S/N: ").upper()
        if novamete == "S":
            Acabou = True
            break
        elif novamete == "N":
            Acabou = False
            break
        else:
            print("Digite S ou N")
    return Acabou 

Jogar = True
x=0
while Jogar :
    Forca(x)
    Jogar = Continue()
    x = x + 1 


