import random
import matplotlib.pyplot as plt

if __name__ == "__main__":
	casos = 100
	dado1 = 0
	dado2 = 0
	resultados = []
	valorRepetido = False
	
	for turno in range(1, casos + 1):
		dado1 = random.randrange(1,7)
		dado2 = random.randrange(1,7)
		suma = dado1 + dado2
		
		for datos in resultados:
			if datos["suma"] == suma:
				datos["frecuencia"] += 1
				valorRepetido = True
				break
		
		if not valorRepetido:
			resultados.append({"suma": suma, "frecuencia": 1})
		valorRepetido = False

	print("Total de casos: ", casos)
	print("Suma\t\tFrecuencia\t\tProbabilidad")

	print("Lista: ",len(resultados))
	for datos in resultados:
		print(datos["suma"], "\t\t", datos["frecuencia"], "\t\t", (datos["frecuencia"] / casos))
		
	plt.hist(datos["suma"])
	plt.title("Casos: " + str(casos))
	plt.xlabel("Suma")
	plt.ylabel("Frecuencia")
	plt.show()
