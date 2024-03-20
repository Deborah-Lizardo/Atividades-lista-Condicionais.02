#Passo 1 : Identificar qual Universidade 
#if PUCPR :Aprovado, se média ≥ 7.0  
#Em exame, se 4.0 ≤ média < 7.0  
#Reprovado, se média < 4.0  
#If UNICAMP
#Aprovado, se média ≥ 5.0  
#UNICAMP 
#Em exame, se média < 5.0
print("Você passou de ano?")
codigo = input(print("Informe qual o código da sua universidade :"))
b1 = float(input("Qual a sua primeira nota do bimestre ? "))
b2 = float(input("Qual a sua segunda nota do bimestre ?"))
media = float((b1 + b2)/2)
media = (f"Sua nota final foi {media :.2f}")
if codigo == 1 and  media >=7.0: 
    float(print(f"Aprovado, sua média final semestre foi {media :.2f}. "))
if  codigo == 1 and media < 4.0 :
    float(print(f"Reprovado,sua média final semestre foi {media :.2f}. "))
elif codigo == 1 and media <= 4.0 and media < 7 :
    float(print(f"Em exame, sua média final semestre foi {media :.2f}. "))

if  codigo == 2 and media <5:
    float(print(f"Você foi reprovado,sua média final semestre foi {media :.2f}. "))
if codigo == 2 and media >=5:
    float(print(f"Você foi aprovado,sua média final semestre foi {media :.2f}. "))