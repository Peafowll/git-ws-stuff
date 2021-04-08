

classes={
    'warrior':[60,15,10,15],
    'mage':[30,10,60,20],
    'ranger':[35,35,15,15],
    'bandit':[30,20,5,45]
}
#gameloop
name=str(input('Care este numele tau?'))
print(f'{name},alege-ti o clasa intre warrior, mage , ranger si bandit.')
playerClassChoice=str(input('Ce clasa iti alegi?'))
playerClassChoice=playerClassChoice.lower()
while playerClassChoice not in classes:
    playerClassChoice=str(input('Clasa selectata nu e in lista. Incearca din nou '))
    playerClassChoice=playerClassChoice.lower()
playerclass=playerClassChoice
playerStats=classes[playerStats]
print(playerclass)