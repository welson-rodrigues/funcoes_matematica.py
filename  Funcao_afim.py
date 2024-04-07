# Função afim: f(x) = ax+b
print("-==-" * 3)
print("\033[4;30;31mFUNÇÃO AFIM\033[m")
print("-==-" * 3)
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
if a == 0:
    print("A função é CONSTANTE!")
    if b == 0:
        print("TODOS os números reais são ZEROS desta função!")
    else:
        if b > 0:
            print("A função é POSITIVA para todo valor de X.")
        else:
            print("A função é NEGATIVA para todo o valor de X.")
else:
    funcao = -b / a
    print(f"O ZERO da função é {funcao}")
    if a > 0:
        print("A função é CRESCENTE!")
    elif a == 0:
        print("Como já dito, a função é CONSTANTE!")
    else:
        print("A função é DECRESCENTE!")
    print(f"Para todo valor de X MENOR que {-b/a} a função é NEGATIVA.")
    print(f"Para todo valor de X MAIOR que {-b/a} a função é POSITIVA.")

