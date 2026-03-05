Bmenor = float(input("Digite o valor da base menor: "))
Bmaior = float(input("Digite o valor da base maior: "))
h = float(input("Digite a altura do tronco da pirâmide: "))

volume = h / 3 * (Bmaior ** 2 + Bmenor **2 + (Bmaior**2 * Bmenor**2)) ** 0.5

print(f"O volume do tronco da pirâmide é: {volume}")
