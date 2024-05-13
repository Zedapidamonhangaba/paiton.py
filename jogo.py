import random
continuar = "S"

while continuar == "S" :
    ns = random.randint(1,10)
    T = 3
    while(T > 0):
        print("você tem", T, "Tentativa(s)")
        T = T - 1
        nc = int(input("digite um número entre 1 a 10: "))

        if (ns == nc):
            print("você acertou!")
            T = 0
        else:
            print("você errou.")
    continuar = input("deseja continuar? (S)im")
