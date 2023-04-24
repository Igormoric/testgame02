

import random, time, sys
import pygame
import item as item


pygame.init()

limitemapx=800  #tamanho do mapa
limitemapy=800
raio=1
passos=5


#colors
WHITE = (255,255,255)
RED = (255,0,0) #personagem
GREEN = (0,255,0)   #chao
BLACK = (0,0,0) 
YELLOW = (255,255,0)    #coins
BROWN = (205, 127, 50)  #caixas

window = pygame.display.set_mode((limitemapx,limitemapy), 0, 32)
window.fill(BLACK)

def reset(mapa):
    if mapa==1:
        global resettime
        resettime=100
        global itens
        itens=[]
        global cena
        cena=[]
        global coins
        coins=[]
        global itemc
        itemc=[]
        itens.append(item.chara(50,150,RED,25,50))
        itens.append(cena)
        itens.append(coins)
        itens.append(itemc)
        itens[1].append(item.cena(50,250,GREEN,500,20))
        itens[1].append(item.cena(50,550,GREEN,700,20))
        itens[2].append(item.item(200,150,YELLOW,10,10))
        itens[2].append(item.item(250,150,YELLOW,10,10))
        itens[2].append(item.item(300,150,YELLOW,10,10))
        itens[2].append(item.item(350,80,YELLOW,10,10))
        itens[3].append(item.item(100,100,BROWN,25,25))
        itens[3].append(item.item(400,100,BROWN,25,25))

reset(1)


while True:
    window.fill(BLACK)
    itens[0].desenha(window)
    for i1 in range(1,4):   #desenha tudo q esta ativo
        for i2 in itens[i1]:
            if i2.ativo==True:
                i2.desenha(window)


    pygame.display.update()
    time.sleep(0.01)

    itens[0].gravi()


    for i in range(len(itens[3])):
        
        if(itens[0].itemrl.colliderect(itens[3][i].itemrc)): #chara caixa
            if(itens[0].velx<0):
                itens[3][i].velx=itens[0].velx
        elif(itens[0].itemrr.colliderect(itens[3][i].itemrc)): #chara caixa
            if(itens[0].velx>0):
                itens[3][i].velx=itens[0].velx

        else:
            itens[3][i].velx=0
    
      
            
    for i in range(len(itens[3])):  #gravidade nas caixas
        itens[3][i].gravi()
            
    
    for i in itens[2]:    #chara coins
        if(itens[0].itemrc.colliderect(i.itemrc)):    #ve se esta tocando a moeda
            if i.ativo:
                itens[0].ponto+=1
                i.ativo=False
    if itens[0].ponto > 0:  #muda ou reseta o mapa
        if itens[0].ponto % len(itens[2]) == 0:
            resettime-=1
            if resettime == 0:
                reset(1)


    itens[0].move(itens,passos)
    for i in range(len(itens[3])):  #move nas caixas
        itens[3][i].move(itens,passos)

    if(itens[0].itemrc.y > limitemapy+200): #se cair reinicia
     

    for event in pygame.event.get():    #movimenta o personagem
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                continue
                itens[0].vely=1
            if event.key == pygame.K_LEFT:
                itens[0].velx=-1
            if event.key == pygame.K_RIGHT:
                itens[0].velx=1
            if event.key == pygame.K_UP:    #da um pulo
                if itens[0].vely==0:
                    itens[0].vely=-20
            if event.key == pygame.K_r: #reseta o jogo
                reset(1)
            if event.key == pygame.K_q:   #sai do jogo
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYUP:  #para o personagem
            if event.key == pygame.K_LEFT:
                itens[0].velx=0
            if event.key == pygame.K_RIGHT:
                itens[0].velx=0


        if event.type == pygame.QUIT:   #sai do jogo
            pygame.quit()
            sys.exit()
		     
    continue

