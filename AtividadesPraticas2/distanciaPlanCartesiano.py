import math

x1 = int(input("Entre com o primeiro valor para o primeiro plano cartesiano: "))
y1 = int(input("Entre com o segundo valor para o primeiro plano cartesiano: "))
x2 = int(input("Entre com o primeiro valor para o segundo plano cartesiano: "))
y2 = int(input("Entre com o segundo valor para o segundo plano cartesiano: "))
a = (x1-x2)**2 + (y1-y2)**2
b = math.sqrt(a)
if b >=10:
    print("longe")
else:
    print("perto")

