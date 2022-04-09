a = int(input("ingrese un numero : "))

f = int(input("ingrese un numero para finalizar : 5"))
suma = 0

print("LOS NUMEROS PARES SON : ")
while a <= f:
    if a % 2 == 0:
        print(a)
    a+=1
    suma=suma + 1

print("LA SUMA DE LOS NUMEROS ES : ", suma)
        