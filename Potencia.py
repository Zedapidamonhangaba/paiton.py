Base = int(input("Digite o valor da Base: "))
Expoente = int(input("Digite o valor do Expoente: "))
R = Base 
for X in range(1,Expoente): 
    R = R*Base
print("Resultado:" , "{:.2f}".format(R))



