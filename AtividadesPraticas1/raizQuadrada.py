import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = float(b**2 - 4*(a*c))

if delta >= 0:
    raizDelta = math.sqrt(float(delta))

    Resultado1 = (-b - raizDelta )/ 2 * a
    Resultado2 = (-b + raizDelta )/ 2 * a


    print(Resultado1)
    print(Resultado2)

    print("Os módulos da sua equação",a,"x^2 +",b,"x+",c,"= 0 são: ",Resultado1, "e ",Resultado2)

else:
     print("Impossivel terminar o calculo, certifique-se de que delta não se torne um valor negativo.")