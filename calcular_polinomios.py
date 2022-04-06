'''
    PROJETO 03- ALGORITMOS E PROGRAMÇÃO II 
    FEITO POR BEATRIZ DUQUE 31906621
    FEITO POR JOÃO PEDRO    31954062
'''
from os import system, name #necessário para a função clear()

def clear(): #Limpa a tela
  if name == 'nt':
    _ = system('cls') #Variável que usa o código para limpar a tela
  else:
    _ = system('clear') #Variável que usa o código para limpar a tela
  return _



def printaPolinomio(v):
    '''Função criada para printar o polinômio que o usuário digitou'''
    print('Polinômio:')
    for i in range(len(v)-1,-1,-1):
        
        #a função se iniciará no maior polinômio e irá até o polinômio elevado a 0 1
        
        if i==0: #esse if foi criado apenas para printar a parênteses final caso seja
                 #último elemento do polinômio (aquele elevado a 1)
            print(v[i])
        elif v[i]!= 0:  #essa condição é dada para os valores do vetor que nao são armazenados, logo ficam em
                        #0, por exemplo, se um polinômio não possuir nenhum x^4, a posição 4 do vetor receberá 0.
            print("(",v[i],"x^",i,end=" ) +")


def poliInserir(v):  #função Input onde o usuário digitará o polinômio 1 ou 2
    n = 0 #os números que multiplicarão x^y
    qtd = 0
    for x in range(len(v)):
        print("Digite o número que multiplicará o termo X elevado a",x,":")
        n = int(input())
        v[x] = n #cada posição do vetor corresponde a um grau de elevação
        qtd = qtd +1
    return qtd



def SomaPoli(v1,v2,grau1,grau2):

    tam1 = grau1
    tam2 = grau2
    if tam1>tam2: #na soma de polinômios, o polinômio resultado tem o tamanho do maior 
        v3=[0]*tam1
    else:
        v3=[0]*tam2
    '''Função feita para somar os dois polinômios digitados pelo usuário'''
    aux=0 #variável auxiliar para guardar a posição que o for vai parar no vet
          #menor
    #esse if vai definir qual o maior dos polinômios, para que assim, o menor seja rodado e o restante do maior que não for somado, apenas copiado
    if len(v1)>len(v2):
        v=v1
        vmenor=v2
    else:
        v=v2
        vmenor=v1
    for i in range(len(vmenor)):
        v3[i]= v[i]+vmenor[i]
        aux+=1
    #quando o vetor menor parar de ser somado, o maior será apenas
    #alocado no final do vetor 3
    if len(v1)>len(v2) or len (v2)>len(v1):
        for j in range(aux,len(v)):
            v3[j]=v[j]
    return v3

def MultPoli(v1,v2,grau1,grau2):
    tam3=0
    tam3= len(v1)+len(v2) #na multiplicação de polinômios, o polinômio resultado tem tamanho da soma dos maiores graus dos dois fatores 
    v3=[0]*tam3
    result = 0
    for x in range(grau1-1,-1,-1): #começa do final do vetor 
        for y in range(grau2-1,-1,-1):
            result = v1[x]*v2[y] #multiplica um fator pelo outro (distributiva)
            if v3[x+y] == 0:
                v3[x+y] = result #o resultado é armazenado no vetor 3
            else:
                v3[x+y]= result + v3[x+y]
    return v3   

def calculaPoli(v,parametro):
    conta=0
    for i in range(0,len(v),1):
        conta2= v[i]*(parametro**i)
        conta=conta+conta2
    return conta


def main():
    esc=0
    print('''
    ╔═══════════════════════════════════════════════════════CALCULADORA DE POLINÔMIOS════════════════════════════════════════════════════════════╗
    ║        Instruções:                                                                                                                         ║
    ║       »Olá usuário, essa é uma calculadora de polinômios. Aqui, você podera calcular até dois polinômios (multiplicando-os ou somando-os), ║
    ║       além de conseguir calcular o resultado deles em função de determinado parâmetro.                                                     ║
    ║       »Para escolher alguma opção, basta escolher o número desta de acordo com o painel de opções.                                         ║
    ║       »Aperte ENTER para continuar                                                                                                         ║
    ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝                                                          
    '''
    )
    input()
    clear() #limpa a tela 
    while esc!=6:
        print('══════════════════════════════════PAINEL DE OPÇÕES═════════════════════════════\n'
              '\n'
              '1- Inserir o Polinômio 1 \n'
              '2- Inserir o Polinômio 2\n'
              '3- Somar Polinômios\n'
              '4- Multiplicar Polinômios\n'
              '5- Calcular polinômio\n'
              '6- sair\n'
              '════════════════════════════════════════════════════════════════════════════════')
        esc=int(input())
        if esc==1: 
            #chama função de inserir o polinômio 1 e calculá-lo 
            grau1 = int(input("Digite o grau do polinômio 1:"))
            grau1 = grau1 + 1 #o tamanho do vetor será definido de acordo com o grau escolhido
            v1 = [0]*grau1
            qtd1=poliInserir(v1)
            printaPolinomio(v1)
        elif esc==2:
            #chama função de inserir o polinômio 2
            grau2 = int(input("Digite o grau do polinômio 2:"))
            grau2 = grau2 + 1
            v2 = [0]*grau2
            qtd2=poliInserir(v2)
            printaPolinomio(v2)
        elif esc==3:
            #chama função de somar poli

            if v1 or v2==0:
                print('Não foi possível calcular, pois um dos polinômios ainda não foi adicionado') #caso o usuário escolha a opção sem ter adicionado os dois polinomios 
            else:
                v3=SomaPoli(v1,v2,grau1,grau2)
                printaPolinomio(v3)


        elif esc==4:
            #chama função de multiplicar poli
            if v1 or v2==0:
                print('Não foi possível calcular, pois um dos polinômios ainda não foi adicionado') #caso o usuário escolha a opção sem ter adicionado os dois polinomios 
            else:
                v3=MultPoli(v1,v2,grau1,grau2)
                printaPolinomio(v3)
        elif esc==5:
            #calcula os valores 
            v=int(input('1- para calcular o polinômio 1 | 2- para calcular o polinômio 2'))
            parametro=int(input('Digite o parâmetro que calculará o polinômio:'))
            if v==1:
                conta=calculaPoli(v1,parametro)
                printaPolinomio(v1)
            else:
                conta=calculaPoli(v2,parametro)
                printaPolinomio(v2)
            print('P (',parametro,' )=',conta)


#inicio do programa 
main()