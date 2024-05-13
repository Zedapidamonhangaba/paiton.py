import random
continuar = "S"
Perro = 0
Pacerto = 0

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
            Pacerto = Pacerto + 1
        else:
            print("você errou.")
            Perro = Perro + 1
        print("Numero de acerto:", Pacerto)
        print("Numero de erros:", Perro)
        
    continuar = input("deseja continuar? (S)im ")
    
