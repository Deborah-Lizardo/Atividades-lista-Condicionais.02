#Passo 1 : Identificar qual Universidade 
#if PUCPR :Aprovado, se média ≥ 7.0  
#Em exame, se 4.0 ≤ média < 7.0  
#Reprovado, se média < 4.0  
#If UNICAMP
#Aprovado, se média ≥ 5.0  
#UNICAMP 
#Em exame, se média < 5.0
print ("Você passou de ano?")
universidade = ("PUCPR") or ("UNICAMP")
input(print("Informe qual a sua universidade :"))
b1 = float(input("Qual a sua primeira nota do bimestre ? "))
b2 = float(input("Qual a sua segunda nota do bimestre ?"))
media = (b1 + b2)/2
if universidade == "PUCPR" and  media >=7.0: 
    print(f"Aprovado, sua média final semestre foi {media :.2f}. ")
if universidade == "PUCPR" and media < 4.0 :
    print(f"Reprovado,sua média final semestre foi {media :.2f}. ")
elif universidade == "PUCPR" and media <= 4.0 and media < 7 :
    print(f"Em exame, sua média final semestre foi {media :.2f}. ")

if universidade == "UNICAMP" and media <5:
    print("Você foi reprovado,sua média final semestre foi {media :.2f}. ")
if universidade == "UNICAMP"and media >=5:
    print("Você foi aprovado,sua média final semestre foi {media :.2f}. ")