# Passo 1: Informar idade
#Passo 2 : Informar peso
#Passo 3: Se maior de 15, e não pesar mais que 120 kg está liberado
#Passo 4 : Se não, (else) PROIBIDO
print ("Programa para identificar se o usuário está liberado para utlizar a montanha-russa")
peso = float(input("Informe o seu peso, em kilos :"))
idade = int(input("Informe a sua idade : "))
if idade >15 and peso <120:
    print("Liberado!Pode ir na montanha-russa.")
else:
    print("O visitante está proibido de entrar na montanha-russa.")
