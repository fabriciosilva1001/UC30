distancia = 450
consumo_km_l = 8
preco_litro = 5.50

litros_consumidos = distancia / consumo_km_l
custo_total = litros_consumidos * preco_litro

print(f"Distância percorrida: {distancia} km")
print(f"Consumo do veículo: {consumo_km_l} km/l")
print(f"Preço da gasolina: R$ {preco_litro}")
print(f"Total de litros consumidos: {litros_consumidos:.2f} L")
print(f"Custo total da viagem: R$ {custo_total:.2f}")