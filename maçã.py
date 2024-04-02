num_macas = int(input("Digite o número de maçãs compradas: ")) 
if num_macas < 12:
    valor_total = num_macas * 0.30
else:
    valor_total = num_macas * 0.25
print(f"O valor total da compra é: R${valor_total:.2f}")

