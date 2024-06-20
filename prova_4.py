#GERADOR DE TABUADA

print("----------"*10)
print("\n\n")
print("                                        GERADOR DE TABUADA")
print("\n\n")
print("----------"*10)
print("\n\n")

num = int(input("Digite o número do qual você deseja calcular a tabuada: "))
print("\n\n")
print("----------"*10)
print("\n\n")
print(f"A Tabuada de {num}:")
print("\n")
for i in range (1, 11):
    multi = num * i
    print(f"{num} X {i} = {multi}")
    
print("\n\n")
print("----------"*10)