nome = str(input("Digite o nome do aluno: "))
idade = int(input("Digite a idade do aluno: "))

if idade < 6:
    print("Idade insuficiente")
elif idade == 6:
    print("Dente de leite")
elif (idade >= 7) and (idade < 11):
    print("Junior")
elif (idade >= 11) and (idade < 17):
    print("Mirim")
elif (idade >= 17) and (idade < 20):
    print("Dub-20")
else:
    print("Profissional")