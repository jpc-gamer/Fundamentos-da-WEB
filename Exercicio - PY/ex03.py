valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite o percentual da multa (%): "))
qntDias = int(input("Digite a quantidade de dias atrasados: "))

prestacao = valorPrestacao + (valorPrestacao * (multa / 100) * qntDias)

print(f"O valor da prestação com multa é: {prestacao:.2f}")
 
