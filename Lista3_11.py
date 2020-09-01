#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

for n in range(n1 + 1, n2) or range(n2 + 1, n1):
    print(n)
    soma = soma + n
print("A soma dos números que estão no intervalo é %s " % soma)
