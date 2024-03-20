#termômetro de ambiente :
# Passo 1 :Se (if) abaixo(<) de 15ºC --> print ("Está frio!!")
#Passo 2:Se (if) a temperatura estiver acima de 25ºC print ("Está calor!")
#Passo 3: else*(ou elif temp.amb. <25 e >15 ?), print ("temperatura agradável!") (entre 15 e 25)
temperatura_ambiente = int(input("Como está a temperatura hoje, em  ºC? "))
if temperatura_ambiente < 15 :
    print(f"Está frio hoje!Atualmemte está {temperatura_ambiente}ºC.")
if temperatura_ambiente > 25 :
    print(f"Está calor hoje!Atualmemte está {temperatura_ambiente}ºC")
else :
    print(f"Está uma temperatura agradável hoje!Atualmemte está {temperatura_ambiente}ºC")
