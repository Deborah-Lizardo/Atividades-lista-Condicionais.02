#Identificação de númeo par ou não;
# quando for par,artrmazenar valor em P
#Quando for ímpar,armazenar valor em I
#Exibir valor final
#Passo 1 : Valor ímpar ou par?
#Passo 2 : valor vinculado;
#Passo 3 : exibir valor final;
numero = float(input("Digite o seu número: "))
if numero %2 == 0 :
    float(input(f"O número inserido {numero:.0f} é par."))
    numero = ("P")
else :
    float(input(f"O número inserido {numero:.0f} é ìmpar."))
    numero = ("I")