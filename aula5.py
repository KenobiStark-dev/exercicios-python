frutas = ["maçã", "banana", "laranja"]  #uma lista armazena itens usando colchetes [], separados por vírgula
print(frutas)

print(frutas[0])    #a contagem começa do 0, então frutas[0] é "maçã"
print(frutas[1])
print(frutas[2])

frutas.append("amora")
print(frutas[3])   #não é necessário colocar o índice, pois o append adiciona no final da lista
frutas.append("abacaxi")
frutas.append("melancia")   #append adiciona apenas uma fruta na lista. Se eu quiser adicionar mais itens, devo usar append várias vezes ou extend com colchetes []
print(frutas[4])
print(frutas[5])
print(len(frutas))
for fruta in frutas:
    print("Eu gosto de", fruta)
if "abacaxi" in frutas:
    print("Tem abacaxi!")
    