#nota = float(input("Digite a nota do aluno: "))
#if nota <5:
#        print("Reprovado")
#elif nota >=5 and nota<7:
#        print("Recuperação")
#elif nota >7:
#        print("Aprovado")
#else:
#        print("Nota inválida")
#
#
nota = float(input("Digite a nota do aluno: "))
if nota > 10 or nota < 0:
    print("Nota inválida")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    