for i in range(5):
    print("Olá!")

for i in range(1, 6):
   print("Contagem:", i)

senha = ""
while senha != "1234":          #se a condição for verdadeira, o loop continua. Neste caso, usar CTRL+C
    senha = input("Digite a senha: ")
print("Acesso permitido!")
