import random, time
mobs={
    'mimic':[50,10,10,40],
    'dryad':[70,10,60,25],
    'chompy dingus':[50,10,10,25],
    'mind flayer':[100,15,30,20],
    'goblin':[20,5,10,70],
    'dummy':[100,10,10,10]
}
classes={
    'warrior':[60,20,10,10],
    'mage':[30,10,60,20],
    'ranger':[20,30,25,15],
    'bandit':[30,15,5,50]
    
}
def eattack(hp,ad,selflck,enemylck):
    hit=random.randint(1,100)
    dodge=random.randint(1,100)
    hit=hit+int(selflck*0.8)
    dodge=dodge+int(enemylck*0.4)
    #prints for debug
    #print(f'Hit a fost {hit}, dodge a fost {dodge}\n')
    finalDmg=0
    if(hit>dodge):
        if(hit-dodge>40):
            damageOne=random.randint(int(ad/2),ad)
            damageTwo=random.randint(int(ad/2),ad)
            finalDmg=damageOne+damageTwo
            hp=hp-finalDmg
            print(f'Crit!\nTi-ai luat {finalDmg} damage!')
        else:
            finalDmg=random.randint(int(ad/2),ad)
            hp=hp-finalDmg
            print(f'Ti-ai luat {finalDmg} damage!')
    else:
        print(f'Inamicul a ratat!')
    #print for debug
    #print(f'HP a ramas {hp} dupa un atac care a dat {finalDmg}')
    return hp
def pattack(hp,ad,selflck,enemylck,isw,php):
    hit=random.randint(1,100)
    dodge=random.randint(1,100)
    hit=hit+int(selflck*0.8)
    dodge=dodge+int(enemylck*0.4)
    #prints for debug
    #print(f'Hit a fost {hit}, dodge a fost {dodge}\n')
    finalDmg=0
    if(hit>dodge):
        if(hit-dodge>40):
            damageOne=random.randint(int(ad/2),ad)
            damageTwo=random.randint(int(ad/2),ad)
            finalDmg=damageOne+damageTwo
            if isw==1 and php < 30:
                finalDmg += finalDmg//4
            hp=hp-finalDmg
            print(f'Crit!\nAi dat {finalDmg} damage!')
        else:
            finalDmg=random.randint(int(ad/2),ad)
            if isw==1 and php < 30:
                finalDmg += finalDmg//4
            hp=hp-finalDmg
            print(f'Ai dat {finalDmg} damage!')
    else:
        print(f'Ai ratat!')
    #print for debug
    #print(f'HP a ramas {hp} dupa un atac care a dat {finalDmg}')
    return hp
def heal(hp,inteligence):
    healing = random.randint(inteligence//5,15)
    hp += healing
    print(f'Ti-ai dat heal {healing} HP.')
    return hp
def deathCheck(playerHP,mobHP):
    if(playerHP<=0 or mobHP<=0):
        return False
    return True
def coup(ehp,emhp,pad):
    coupDmg=emhp-ehp
    coupDmg=int(coupDmg*(3/4))
    coupDmg=coupDmg+random.randint(int(pad/1.75),pad)
    ehp=ehp-coupDmg
    print("Ai lovit un punct deja ranit al inamicului, dand "+str(coupDmg)+" damage")
    return ehp



#game
name=str(input('Care este numele tau?'))
print(f'{name},alege-ti o clasa intre warrior, mage , ranger si bandit.')
playerClassChoice=str(input('Ce clasa iti alegi?'))
playerClassChoice=playerClassChoice.lower()
while playerClassChoice not in classes:
    playerClassChoice=str(input('Clasa selectata nu e in lista. Incearca din nou '))
    playerClassChoice=playerClassChoice.lower()
playerClass=playerClassChoice
playerStats=classes[playerClass]
iswarrior = 0
if playerClass == "warrior":
    iswarrior = 1
maxHP=playerStats[0]
enemyName, enemyStats = random.choice(list(mobs.items()))
print(f"Te bati cu un {enemyName}.")
enemyMaxHP=enemyStats[0]
moves=['attack','heal','special']
movesString=' '.join([str(elem) for elem in moves])
playerSpecial=1
shadowSneak=0
#enemyStats = [ int(x) for x in enemyStats ]
#playerStats = [ int(x) for x in playerStats ]
while(deathCheck(playerStats[0],enemyStats[0])):
    print(f'Tu ai {playerStats[0]}HP iar {enemyName} are {enemyStats[0]}HP')
    #playermoves
    moveChoice=str(input('Poti alege din urmatoare lista de miscari:'+' '+movesString.capitalize()+' '))
    moveChoice=moveChoice.lower()
    while(moveChoice not in moves):
        moveChoice=str(input('Miscare invalida.Poti alege din urmatoarea lista de miscari:'+' '+movesString.capitalize()+' '))
    if moveChoice=='attack':
        enemyStats[0]= pattack(enemyStats[0],playerStats[1],playerStats[3],enemyStats[3],iswarrior,playerStats[0])
        if enemyStats[0]<=0:
            break
    if moveChoice=='heal':
        playerStats[0]= heal(playerStats[0],playerStats[2])
        if playerStats[0]>maxHP:
            playerStats[0]=maxHP
            print('Nu poti sa iti dau heal peste hp maxim, deci stagnezi pe '+str(maxHP)+'HP')
    if moveChoice=='special' and playerClass=='warrior':
        print("Nu ai un atac special, dar dai extra damage sub jumate HP!")
    elif moveChoice=='special' and playerClass=='ranger' and playerSpecial==1:
        enemyStats[0]=coup(enemyStats[0],enemyMaxHP,playerStats[1])
        playerSpecial=0
        if enemyStats[0]<=0:
            break
    elif moveChoice=='special' and playerClass=='mage' and playerSpecial==1:
        wandFizzle=random.randint(1,10)
        if wandFizzle>1 and wandFizzle<=4:
            print("Incerci sa iti aduni energie pentru un spell mare, dar te distrage un fluture!")
        if wandFizzle>4 and wandFizzle<=7:
            print("Spellul tau mare e gata, dar din bageheta iese confeti.")
        if wandFizzle >8 and wandFizzle<=10:
            print("Spui cuvintele latine obscure ale spellului tau suprem gresit, iar bagheta se transforma in jeleu.")
        if wandFizzle==1:
            print("Incantezi perfect cel mai greu spell al tau si iese o bila de foc din bagheta!")
            fireBallDmg=random.randint(80,100)
            enemyStats[0]=enemyStats[0]-fireBallDmg
            print(f'Dai un imens {fireBallDmg} damage!')
            if enemyStats[0]<=0:
                break
        playerSpecial=0
    elif moveChoice=='special' and playerClass=='bandit' and playerSpecial==1:
        print('Te ascunzi in umbre, luandut-i 0 damage de la urmatoarele 3 atacuri!')
        shadowSneak=3
        playerSpecial=0
    elif(moveChoice=='special' and playerSpecial==0):
        print("Ti-ai folosit deja speciala, si ti-ai pierdut turnul!")
    #enemymoves
    time.sleep(2)
    if(shadowSneak==0):
        playerStats[0]=eattack(playerStats[0],enemyStats[1],enemyStats[3],playerStats[3])
    else:
        print('Inamicul nu te-a vazut si te-a ratat!')
        shadowSneak=shadowSneak-1
    if playerStats[0]<=0:
        break
    time.sleep(1)

if(playerStats[0]<=0):
    print(f'Game over!')
else:
    print(f'A winner is you!')    