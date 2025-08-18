custo = int(input("Digite o custo de fábrica do carro:"))
distribuidor = custo//100 * 12
impostos = custo//100 * 30
custo += distribuidor + impostos
print(f"O valor do carro após adicionar os impostos e a parte do distribuidor é: \n{custo}")
