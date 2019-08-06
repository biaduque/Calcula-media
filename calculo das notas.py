from os import system, name #necessário para a função clear()
import time



def clear():
    if name=='nt':
        _=system('cls') #variavel que usa o codigo pra limpar a tela
    else:
        _=system('clear') #variavel que usa o codigo pra limpar a tela
    return _


def NotaComum(notas):
    i=0
    soma=0
    while i != notas:
        i=i+1
        nota1=float(input('Digite a nota do aluno:'))
        soma=soma+nota1
    média= soma/notas
    if média<6:
        vermelho.append(1)
    print('Média do aluno',aluno,'=',média)
    Faltas(a)

def NotaComPeso(notas):
    i=0
    soma=0
    for i in range(0,notas,1):
        nota1=float(input('Digite a nota do aluno:'))
        soma=soma+(nota1*peso1[i])
    média=soma/10
    if média<6:
        vermelho.append(1)
    print('Média do aluno',aluno,'=',média)
    Faltas(a)
    
def Faltas(a):
    presença=0
    b= int(input('Digite o total de faltas do aluno:'))
    presença= (100*b)/a
    presença=100-presença
    print('Porcentagem de presença:',presença)

def Fim():
    False

#inicio do programa

print('\n'
        '            ╔═════════════════════════════════════════════════════════════════════╗\n'
        '            ║        Olá Professora Karina! Por favor, digite sua senha:          ║\n'
        '            ╠═════════════════════════════════════════════════════════════════════╣\n' )
senha=str(input('Senha:'))

if senha.upper()=='KARINA':
    print('Senha correta!Seja bem vinda!')
    time.sleep(2)
    clear()
    aceitos=[0,1,2,3,4,5,6,7,8,9]
    vermelho=[]
    peso1=[]
    x=int(input('Digite a quantidade de alunos a serem analisádos:'))
    notas= int(input('Digite a quantidade de avaliações do seu aluno:'))
    a= int(input('Digite o total de aulas:'))
    escolha=int(input('Digite (1) para alunos com média simples e (2) para media com pesos:'))
    aluno=1
    if escolha==1:
        for i in range (0,x,1):
            print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » Aluno',aluno,' « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
            NotaComum(notas)
            aluno+=1
    else:
        for i in range(0,notas,1):
            notaverm=0
            x2=int(input('Digite o peso da avaliação:'))
            peso1.append(x2)
            print(peso1)
        for i in range(0,x,1):
            print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » Aluno',aluno,' « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
            NotaComPeso(notas)
            aluno+=1
    x2= len(vermelho)
    print('╔════════════════════════════════════════════════════════════════╗')
    print('║A quantidade de alunos com notas inferiores a 6 é:',x2,'        ║')
    print('╚════════════════════════════════════════════════════════════════╝')
    print('Digite enter para finalizar')
    input()
    Fim()

    

else:
    print('Senha incorreta. Por favor, feche o programa pressionando enter')
    input()
    
