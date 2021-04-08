import random, time
mobs={
    'mimic':[45,20,10,5],
    'dryad':[60,5,60,20],
    'chompy dingus':[50,10,10,10],
    'mind flayer':[70,15,30,20],
    'goblin':[10,5,10,55],
    'dummy':[100,10,10,10]
}
classes={
    'warrior':[60,20,10,10],
    'mage':[30,10,60,20],
    'ranger':[35,35,15,15],
    'bandit':[30,15,5,50]
    
}
def eattack(hp,ad,selflck,enemylck):
    hit=random.randint(1,100)
    dodge=random.randint(1,100)
    hit=hit+selflck
    dodge=dodge+enemylck
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
def pattack(hp,ad,selflck,enemylck):
    hit=random.randint(1,100)
    dodge=random.randint(1,100)
    hit=hit+selflck
    dodge=dodge+enemylck
    #prints for debug
    #print(f'Hit a fost {hit}, dodge a fost {dodge}\n')
    finalDmg=0
    if(hit>dodge):
        if(hit-dodge>40):
            damageOne=random.randint(int(ad/2),ad)
            damageTwo=random.randint(int(ad/2),ad)
            finalDmg=damageOne+damageTwo
            hp=hp-finalDmg
            print(f'Crit!\nAi dat {finalDmg} damage!')
        else:
            finalDmg=random.randint(int(ad/2),ad)
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
maxHP=playerStats[0]
enemyStats=mobs['dummy']
moves=['attack','heal','shield']
movesString=' '.join([str(elem) for elem in moves])
#enemyStats = [ int(x) for x in enemyStats ]
#playerStats = [ int(x) for x in playerStats ]
while(deathCheck(playerStats[0],enemyStats[0])):
    print(f'Tu ai {playerStats[0]}HP iar dummy are {enemyStats[0]}HP')
    #playermoves
    moveChoice=str(input('Poti alege din urmatoare lista de miscari:'+' '+movesString.capitalize()+' '))
    moveChoice=moveChoice.lower()
    while(moveChoice not in moves):
        moveChoice=str(input('Miscare invalida.Poti alege din urmatoarea lista de miscari:'+' '+movesString.capitalize()+' '))
    if moveChoice=='attack':
        enemyStats[0]= pattack(enemyStats[0],playerStats[1],playerStats[3],enemyStats[3])
        if enemyStats[0]<=0:
            break
    if moveChoice=='heal':
        playerStats[0]= heal(playerStats[0],playerStats[2])
        if playerStats[0]>maxHP:
            playerStats[0]=maxHP
            print('Nu poti sa iti dau heal peste hp maxim, deci stagnezi pe '+str(maxHP)+'HP')
    #enemymoves
    time.sleep(2)
    enemyChoice=1
    if(enemyChoice==1):
        playerStats[0]=eattack(playerStats[0],enemyStats[1],enemyStats[3],playerStats[3])
        if playerStats[0]<=0:
            break
    time.sleep(1)

if(playerStats[0]<=0):
    print(f'Game over!')
else:
    print(f'A winner is you!')    
    


#print(playerclass)
