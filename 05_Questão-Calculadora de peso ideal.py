#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um fluxograma e seu respectivo programa em python que 
# calcuse seu peso ideal, utilizando as seguintes fórmulas: 
#a. Para homens: (72.7*h) – 58 
#b. Para mulheres: (62.1*h)-44,7 kg (sendo h = altura)
#Dados de entrada : altura e sexo da pessoa
#Calcular peso ideal segundo o sexo
print("Calculadora de peso ideal")
sexo_biologico= print(input(("Qual seu sexo biológico?")))
altura = float(input("Informe a sua altura : "))
mulher = (62.1 * altura) - 44.7
homem = (72.7 * altura) - 58
peso_1 = mulher
peso_1 = float((62.1 * altura) - 44.7)
if sexo_biologico == mulher:
    peso_1 = float(62.1 * altura - 44.7)
print(f"Seu peso ideal é {peso_1 :.1f} kg")
peso_2 = homem
peso_2 = (72.7 * altura) - 58
if sexo_biologico == homem:
    peso_2 = float(72.7 * altura - 58)
    float(print(f"Seu peso ideal é {peso_2:.1f} kg"))   