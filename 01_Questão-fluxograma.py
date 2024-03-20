#fluxograma questão 1 
x=float(input(("Digite o valor de X: ")))
if x== 0 :
    print("ZERO")
if  not x== 0 :
    x==1
if x==1 :
    print("UM")
    if not x == 1 :
        x == 2 
if x == 2 :
    print("DOIS")
    if not  x == 1 and  x==0 and  x==2:
        print("ERRO")
else :
    print("ERRO")