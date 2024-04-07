# Função quadrática: f(x) = ax²+bx+c
print("-==-" * 4)
print("\033[4;30;31mFUNÇÃO QUADRÁTICA\033[m")
print("-==-" * 4)
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
# zero da função
zero_funcao = b**2 - 4*a*c
if zero_funcao > 0:
    x1 = (-b + (zero_funcao ** 0.5)) / (2 * a)
    x2 = (-b - (zero_funcao ** 0.5)) / (2 * a)
    print(f"Zeros da função: {x1} e {x2}")
elif zero_funcao == 0:
    x = -b / (2 * a)
    print("Zero da função:", x)
else:
    print("A função NÃO possui raízes reais.")
# positivo ou negativo
if zero_funcao > 0:
    print("A função é POSITICA para todos os valores de x.")
elif zero_funcao == 0:
    print("A função é POSITIVA para um único valor de x.")
else:
    print("A função é NEGATIVA para todos os valores de x.")
# vértice da parábola
x_vertice = -b / (2 * a)
y_vertice = a * x_vertice**2 + b * x_vertice + c
print(F"O vértice da parábola é: {x_vertice}, {y_vertice}")
# crescente ou decrescente
if a > 0:
    print("A função é CRESCENTE para todos os valores de x.")
elif a < 0:
    print("A função é DECRESCENTE para todos os valores de x.")
else:
    print("A função NÃO é nem CRESCENTE nem DECRESCENTE.")
