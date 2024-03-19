#Passo 1 : Informar a idade
#Passo 2 :Informar o tempo de serviço
# if possuir mais de 65 ou igual 
# 30 anos de serviço ou mais 
#Ou 60 anos de serviço and 25 de serviço
print("Você pode se aposentar?")
idade = int(input("Informe a sua idade : "))
temp_servico = int(input("Você trabalha a quantos anos? "))
if idade >= 65  or temp_servico >= 30 :
    print("Pode se aposentar.")

elif temp_servico >= 25 or idade >= 60:
    print("Pode se aposentar.")

else :
    print("Não pode se aposentar.")