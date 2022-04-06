# Feito por Beatriz Duque

import random

def conferir(resp):
    num=['1','2','3','4','5','6','7','8','9','10']
    if resp.upper()=="ARRISCAR":
        print('ARRISQUE!:')
        resp=str(input())
        if resp.upper()==esc_palavra.upper():
            print('Parabéns, Você acertou!!!')
            acertos=tam
        else:
            tentativas=6
    else:
        while resp in num:
            print('Entrada inválida, digite novamente:')
            resp=str(input())
            
   
            
def gerarForca(tema):
    x=0
    global tam
    global esc_palavra
    esc_palavra= random.choice(tema)
    tam= len(esc_palavra)
    for i in range(0,tam,1):
        if i != '':
            respondendo.append(lacuna)
        else:
            respondendo.apend(espaço)
    print(respondendo)

def Respondendo(esc_palavra):
    global resp
    erros=0
    tentativas=-1
    acertos=0
    while acertos!=tam:
        resp=str(input('Digite a letra:'))
        conferir(resp)
        while resp.lower() in o_input:
            resp=str(input('Resposta já digitada, digite novamente:'))
            
        if resp.upper()=='FIM':
            print('Fim do jogo, obrigada por jogar')
            break
        
        if resp.lower() in esc_palavra.lower():
            
            for i in range(0,tam,1):
                if esc_palavra[i].lower()==resp.lower():
                    respondendo[i]=resp.lower()
                    acertos=acertos+1
                    o_input.append(resp)
                    
            print(respondendo)
        
        elif resp.lower() not in esc_palavra.lower():
            tentativas=tentativas+1
            erros=erros+1
            if erros<=6:
                print('   ')
                print(erradas[tentativas])
                print('   ')
                print(respondendo)

        if erros>6:
            print('Você perdeu')
            break
        if erros== len(erradas):
            print('Você perdeu')
            break

    if acertos==tam:
        print('Parabéns, você acertou a palavra!')


def Main():
    gerarForca(esctema)
    Respondendo(esc_palavra)

    
#codigo principal
erradas=['O','O\n|\n',' O\n |\n/',' O\n |\n/ \\n',' O\n-|\n/ \\n',' O\n-|-\n/ \\n']
err=len(erradas)
o_input=[]                           
esportes=['basquete','volei','handball','futebol','natação','judô']
jogos=['Fifa','CSGO','StreetFigther','MortalKombat']
filmes=['ToyStory','Vingadores','Grease','']
respondendo=[]
temas=[esportes,jogos,filmes]
lacuna='__'
espaço='  '

print('JOGO DA FORCA\n'
      'Para parar de jogar, digite "fim"\n')
print('_________________________________________\n')
esctema=random.choice(temas)
if esctema==esportes:
    print('TEMA DA VEZ: ESPORTES')
    print('_________________________________________\n')
elif esctema==jogos:
    print('TEMA DA VEZ:JOGOS')
    print('_________________________________________\n')
else:
    print('TEMA DA VEZ:FILMES')
    print('_________________________________________\n')
    
Main()
    
        
        
    
    
    
    
    
