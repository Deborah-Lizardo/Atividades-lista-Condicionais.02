#Fazer um fluxograma e seu respectivo programa em Python para ler 
#a nota de um estudante. Se a  nota está igual ou acima de 7, 
#informar “Estudante aprovado”, se a  nota estiver entre 4 (inclusive) 
#e 7 (exclusive), informar “Estudante em recuperação"  e se estiver 
#abaixo de 4 informar “Estudante reprovado”.
# Programa o qual interpretará o boletim escolar 
nota_aluno = int(input("Informe a sua nota : "))
if nota_aluno < 4 :
    print("Estudante reprovado.")
if nota_aluno >=7 :
    print("Estudante aprovado.")
elif nota_aluno >=4 and nota_aluno <7 :
    print("Estudante em recuperação.")
