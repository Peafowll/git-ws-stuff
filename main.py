import random
mobs={
    'dummy':[100,5,5,5,10]
}
classes={
    'warrior':[60,15,10,15],
    'mage':[30,10,60,20],
    'ranger':[35,35,15,15],
    'bandit':[30,20,5,45]
}
def attack(hp,ad,selflck,enemylck):
    dodgeChanceMin=int(enemylck/3)
    dodgeChanceMax=int(enemylck*1.25)
    hitChanceMin=int(selflck/2)
    hitChanceMax=int(selflck*2)
    hit=random.randint(hitChanceMin,hitChanceMax)
    dodge=random.randint(dodgeChanceMin,dodgeChanceMax)
    #prints for debug
    print(f'Hit a fost {hit}, dodge a fost {dodge}\n')
    finalDmg=0
    if(hit>dodge):
        if(hit>=2*dodge):
            damageOne=random.randint(int(ad/2),ad)
            damageTwo=random.randint(int(ad/2),ad)
            hp=hp-finalDmg
            print(f'Crit!\n')
        else:
            finalDmg=random.randint(int(ad/2),ad)
            hp=hp-finalDmg
    #print for debug
    print(f'HP a ramas {hp} dupa un atac care a dat {finalDmg}')
    return hp
#gameloop
name=str(input('Care este numele tau?'))

print(f'{name},alege-ti o clasa intre warrior, mage , ranger si bandit.')
playerClassChoice=str(input('Ce clasa iti alegi?'))
playerClassChoice=playerClassChoice.lower()
while playerClassChoice not in classes:
    playerClassChoice=str(input('Clasa selectata nu e in lista. Incearca din nou '))
    playerClassChoice=playerClassChoice.lower()
playerClass=playerClassChoice
playerStats=classes[playerClass]
enemyStats=mobs['dummy']
#enemyStats = [ int(x) for x in enemyStats ]
#playerStats = [ int(x) for x in playerStats ]
print(f'enemyhp={enemyStats[0]}, playerstr={playerStats[1]} enemyluck={enemyStats[3]} playerluck={playerStats[3]}')
attack(enemyStats[0],playerStats[1],playerStats[3],enemyStats[3])
#print(playerclass)