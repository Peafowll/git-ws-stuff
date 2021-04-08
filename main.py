import random
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
def attack(hp,ad,selflck,enemylck):
    hit=random.randint(1,100)
    dodge=random.randint(1,100)
    hit=hit+selflck
    dodge=dodge+enemylck
    #prints for debug
    print(f'Hit a fost {hit}, dodge a fost {dodge}\n')
    finalDmg=0
    if(hit>dodge):
        if(hit-dodge>40):
            damageOne=random.randint(int(ad/2),ad)
            damageTwo=random.randint(int(ad/2),ad)
            finalDmg=damageOne+damageTwo
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

