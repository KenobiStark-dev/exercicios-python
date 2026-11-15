numero = int(input("Escolha um número (0 para sair): "))
while numero !=0:
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
    numero = int(input("Escolha um número (0 para sair): "))
print("Programa encerrado.")

