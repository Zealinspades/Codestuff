#global libraries called here

import random

     # Returns stats when called
class Hero:

    def __init__(self, HeroHP, HeroArmor, HeroMinDamage, HeroMaxDamage):
        self.hp = HeroHP
        self.mindmg = HeroMinDamage
        self.maxdmg = HeroMaxDamage
        self.amr = HeroArmor

    def FetchHP(self):    
        return self.hp
    
    def FetchArmor(self):
        return self.amr
       
    def FetchMinDamage(self):
        return self.mindmg

    def FetchMaxDamage(self):
        return self.maxdmg

class Goblin:

    def __init__(self, GoblinHP, GoblinMinDamage, GoblinMaxDamage, GoblinArmor):
        self.hp = GoblinHP
        self.mindmg = GoblinMinDamage
        self.maxdmg = GoblinMaxDamage
        self.amr = GoblinArmor

    def FetchHP(self):    
        return self.hp
    
    def FetchArmor(self):
        return self.amr
        
    def FetchMinDamage(self):
        return self.mindmg

    def FetchMaxDamage(self):
        return self.maxdmg

## Stat Selection!

## The Hero and Goblin have access to Critical Strikes on a maximum natural roll, which adds an extra die.

##
def HeroSelectionScreen() :

    # Am I making a fucking game now
    print ()
    print ('The time has come to choose your heros capabilities!')
    print ('The Goblin has 25 health, 2 armor, and a 1-6 damage range by default!')
    print ('By default, the Hero has 30 health, 1 armor, and a 1-6 damage range.')
    print ()

def CustomizePrompt(prompt) :
        while True :
            response = input (prompt).strip().lower()
            if response in ['yes', 'y'] :
                return True
            if response in ['no', 'n'] :
                return False
            else :
                print ('Your response must be \'yes\' or \'no\' (y/n)')
            print()

def EnforceStats(prompt) :
    while True :
        try :
            value = int(input(prompt))
            if value > 0 :
                return value
            else :
                print ('You must input a positive integer.')
        except ValueError :
            print ('You must input a positive integer.')

def CustomizeHandler() :
    
    CustomizeSelected = CustomizePrompt('Would you like to customize your Hero? If no, default stats will be used. ')

    if CustomizeSelected :

        ChosenHeroHP = EnforceStats('How much HP does your Hero have?  ')
        ChosenHeroArmor = EnforceStats('How much armor does your Hero have?  ')
        ChosenHeroMaxDamage = EnforceStats('How hard can your Hero possibly hit?  ')

    else :

        ChosenHeroHP = 30
        ChosenHeroArmor = 1
        ChosenHeroMaxDamage = 6

    hero = Hero(HeroHP = ChosenHeroHP, HeroArmor = ChosenHeroArmor, HeroMinDamage = 1, HeroMaxDamage = ChosenHeroMaxDamage)
    goblin = Goblin(GoblinHP = 25, GoblinMinDamage = 1, GoblinMaxDamage = 6, GoblinArmor = 2)
    return (hero, goblin)




def HeroAttack(hero, goblin):

    print()
    # spacing is nice

    HeroDamageRoll = (random.randrange(hero.FetchMinDamage(), hero.FetchMaxDamage() + 1))
    HeroDamageRoll = max(HeroDamageRoll, 0) 
    ## Ensuring it doesn't somehow go negative

    if HeroDamageRoll == hero.FetchMaxDamage():
        CritStrike = HeroDamageRoll + (random.randrange(hero.FetchMinDamage(), hero.FetchMaxDamage() + 1))
        print(f'The mighty hero lands a brutal strike for {max((CritStrike - goblin.FetchArmor()), 1)} damage!')
            #Trying to factor armor into damage without display negative values
        goblin.hp -= (CritStrike - goblin.FetchArmor())

    elif(HeroDamageRoll - goblin.FetchArmor()) <= 0 :
        print('The accursed goblin deflects the hero\'s blow and snarls!')

    else :
        if HeroDamageRoll > 0 and HeroDamageRoll < hero.FetchMaxDamage() :
            print(f'The mighty hero attacks for {max((HeroDamageRoll - goblin.FetchArmor()), 1)} damage!')
            goblin.hp -= (HeroDamageRoll - goblin.FetchArmor())

def EnemyAttack(hero, goblin):

    print()
    # spacing is nice

    GoblinDamageRoll = (random.randrange(goblin.FetchMinDamage(), goblin.FetchMaxDamage() + 1))
    GoblinDamageRoll = max(GoblinDamageRoll, 0)
    ## Ensuring it doesn't somehow go negative
    
    if GoblinDamageRoll == goblin.FetchMaxDamage():
        CritStrike = GoblinDamageRoll + (random.randrange(goblin.FetchMinDamage(), goblin.FetchMaxDamage() + 1))
        print(f'The Goblin slips your guard with a toothy grin for {max((CritStrike - hero.FetchArmor()), 1)} damage!')
        hero.hp -= (CritStrike - hero.FetchArmor())

    elif (GoblinDamageRoll- hero.FetchArmor()) <= 0 :
        print ('The goblin shrieks as its weapon skates off your armor!')

    else :
        hero.hp -= (GoblinDamageRoll - hero.FetchArmor())
        print (f'The accursed goblin has struck you for {max((GoblinDamageRoll - hero.FetchArmor()), 1)} damage!')
    

def IsBattleOver(hero, goblin) :

    if hero.FetchHP() <= 0 and goblin.FetchHP() <= 0 :
        print('        It's a draw! There's many goblins,')
        print('               but only one Hero...')
        print('╘═════════════════════════════════════════════════╛')
        return True

    if hero.FetchHP() <= 0:
        print('         ❉  The hero has been defeated! ❉')
        print('╘═════════════════════════════════════════════════╛')
        return True
    
    elif goblin.FetchHP() <= 0:
        print('        ✧  The goblin has been defeated! ✧')
        print('╘═════════════════════════════════════════════════╛')
        return True

    else :
        return False
    
def FinalStats(hero, goblin) :
    print()
    print ('The results are:')
    print (f'Hero's HP: {hero.FetchHP()}')
    print (f'Goblin's HP: {goblin.FetchHP()}')
    print()

def InitErrorCount() :
    global ErrorCount
    ErrorCount = 0

def DoBattleWrapper() :

    global ErrorCount
    while True :
        try:
            DoBattle()
               break
        except Exception:
            ErrorCount += 1
            print('An error has been logged while trying to do battle.')
            if ErrorCount >= 5:
                print ('Total sum of errors in program exceeds 4, program will shut down')
                quit()
            else :
                print (f'Retrying... Error Count is at {ErrorCount}')
                DoBattleWrapper()

def DoBattle() :

    print()
    print('An enemy joins the field! Win before turn 30!')
    print()
    print(f'Goblin Statistics: - HP: {goblin.FetchHP()}, Attack: {goblin.FetchMinDamage()}-{goblin.FetchMaxDamage()}, Armor: {goblin.FetchArmor()}')
    print(f'Hero's Statistics - HP: {hero.FetchHP()}, Attack: {hero.FetchMinDamage()}-{hero.FetchMaxDamage()}, Armor: {hero.FetchArmor()}')
    print()

    BattleOngoing = True
    CurrentTurn = 0

    while BattleOngoing:

        CurrentTurn += 1

        if IsBattleOver(hero, goblin):
            BattleOngoing = False
            FinalStats()
            print (f'Turns Taken: {CurrentTurn}')
            print()
            quit()
            #would put this in FinalStats but that would involve fucking with stuff

        elif CurrentTurn == 1:
            print ('╒══ The battle joins, to the victor the spoils! ══╕ ')

        elif 1 < CurrentTurn < 30 :
            EnemyAttack(hero, goblin)
            HeroAttack(hero, goblin)
            print()
            print(f'The Goblin has {goblin.FetchHP()} hit points left!')
            print(f'The Hero has {hero.FetchHP()} hit points left!')
            print()    
            print ('╘═════════════════════════════════════════════════╛')
            print()
            print (f'The current turn is {CurrentTurn}!')
            print()
            print ('╒═════════════════════════════════════════════════╕')
            ## Battle Continues

        elif CurrentTurn >= 30 :
            print ('╘══════════════ You both tire out! ══════════════╛')
            print()
            ## Trying to avoid infinites here
            BattleOngoing = False

        else :
            print ('Something pretty fucky is afoot if you get outside 1-30 turns')
            raise Exception()

HeroSelectionScreen()
hero, goblin = CustomizeHandler()
InitErrorCount()        
DoBattleWrapper()

# test commit
