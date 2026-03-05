import math

graus = float(input("Digite o valor do ângulo em graus: "))

radianos = math.radians(graus)

seno = round (math.sin(radianos))
cosseno = round (math.cos(radianos))
tangente = round (math.sin(radianos))

print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")
