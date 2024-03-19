#Passo 1 : Informar a idade
#Passo 2 : if menor  de 16 == não é eleitor
#Passo 3 : if maior de 16 == eleitor facultativo
#Passo 4 :elif entre 18 e 65 eleitor obrigatório
print("Programa para identificar  eleitor")
idade = int(input("Informe a sua idade : "))
if idade <16 :
    print("Não é eleitor.")
elif idade >=16 and idade <= 18:
    print("Eleitor facultativo.")
elif idade >=18 and idade <= 65:
    print("Eleitor obrigatório.")