valor_n = int(input ("Digite el numero para sacar los multiplos: "))
valor_m = int(input ("Digite la cantidad a sacar del multiplo: "))

def generar_multiplos(valor_n,valor_m):
    return [valor_n * i for i in range(1, valor_m + 1)]

print(generar_multiplos(valor_n,valor_m))
