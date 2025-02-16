"""width = float(input("Infome a largura : \n"))
height = float(input("Informe a alutra : \n "))
length = float(input("informe o comprimento : \n "))
area = width * length
volume = width * length * height
def get_size(width ,height, length ):
    #your code here
    print("O valor da área é de : ", area)
    print("O valor do volume é de : ", volume )
   
get_size(width, height, length)"""

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''nota = float(input("Digite uma nota entre 0 e 10 : \n"))

while (nota < 0 or nota > 10) :
    print("Valor invalido , tente novamente : ")
    float(input("Digite uma nota entre 0 e 10 : \n"))
else : 
    print(f"A nota {nota} é valida ")'''

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

'''UserName = str(input("Digite o nome de usuário : \n"))
PassWord = str(input("Digite a sua senha : \n"))

while(UserName == PassWord):
    print("Senha inválida \n")
    str(input("Digite o nome de usuário : \n"))
    str(input("Digite a sua senha :\n"))

else : 
     print("Cadastro conclúido")'''

#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# Inicializando a lista de médias
medias = []

# Loop para receber as notas de 10 alunos
for aluno in range(10):
    # Recebendo as 4 notas do aluno
    notas = []
    for i in range(4):
        nota = float(input(f'Digite a nota {i+1} do aluno {aluno+1}: '))
        notas.append(nota)
    
    # Calculando a média do aluno
    media = sum(notas) / 4
    medias.append(media)

# Contando o número de alunos com média maior ou igual a 7.0
alunos_acima_media = sum(1 for media in medias if media >= 7.0)

print(f'Número de alunos com média maior ou igual a 7.0: {alunos_acima_media}')
