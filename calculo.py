def retangulo(tipoR, Largura, Altura):
    r = 0 
    if tipoR == "Area":
        r = Largura * Altura 
    elif tipoR == "Perimetro":
        r = 2 * (Largura + Altura)
    return r 

def circulo(tipoC, raio):
    c = 0 
    if tipoC == "area":
        c = 3.14 * (raio * 2)
    elif tipoC == "perimetro":
        c = 2 * 3.14 * raio
    return c

re = retangulo("Area", 15, 4.5)
print(f'area:{re}')

ci = circulo("area", 5)
print(f'area:{ci}')
