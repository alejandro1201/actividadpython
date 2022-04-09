print("calcula los numeros potenciales de 2")
numero = 2
exponente=int(input("Digite un numero para sacar el exponente: "))

def generar_potencias(numero,exponente):
    resultado=1
    for i in range(exponente):
        resultado *= numero
    return resultado

print(generar_potencias(numero,exponente))
