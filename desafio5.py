compras = []
for i in range (3):
    compras.append(input("O que falta na lista? "))
print(compras)
for item in compras:                    #Treinar mais pra aprender seu uso correto. Acredito que seja uma forma de percorrer a lista, mas ainda não compreendi direito
    print(item)
print(len(compras))                     #Parece simples, mas ainda preciso reforçar o esforço pra compreender direito essa linha
procurado = input("O que você procura? ")
if procurado in compras:
    print("Está na lista!")             #conceito de printar algo se a condição for verdadeira, caso contrário, usar o else
else:                                   #se for falso, então faça isso
    print("Não está na lista!")
                                        #Esse exigiu bastante, me intidimidei com os comandos pois pareciam complexos e eu só pensava de forma rasa. Em um momento, achei que isso não era pra mim, mas não queria deixar essa linha de código me vencer assim.
                                        # Depois de pensar e testar no papel, voltei ajustando e consegui fazer funcionar. 
                                        #  