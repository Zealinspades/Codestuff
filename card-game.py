    #This holds what the actual deck contains
    #Simple method of maintaining a consistent card state - will have to mess with this later
    #probably want a player class once cards work

import random

#make the deck a set - one of each thing in that list

class Deck:
    def __init__(self, CardNum, CardSuit, CardID, IsDrawn, CardOwnedBy, InPlay):
        self.CardNum = CardNum
        self.CardSuit = CardSuit
        self.CardID = CardID
        self.IsDrawn = IsDrawn
        self.CardOwnedBy = CardOwnedBy
        self.InPlay = InPlay

    def FetchCardNum(self):
        return self.CardNum

    def FetchCardSuit(self):
        return self.CardSuit

    def FetchCardID(self):
        return self.CardID

    def IsDrawn(self):
        return self.Drawn

    def OwnedBy(self):
        return self.CardOwnedBy

    def IsInPlay(self):
        return self.InPlay

    #This is intended to intialize the Deck class variables
    #This uses Tuple datatype
def SetDeck() :
        # it is very important this is held as the ascending value of suits because the whole program looks at it
        InitCardSuit = ['diamonds', 'clubs', 'hearts', 'spades']
        # it is very important this is held as the ascending value of face values because the whole program looks at it
        InitCardNum = [str(i) for i in range (2,11)] + ['jack', 'queen', 'king', 'ace']
        #iterate through 1-10 assigning numbers, then add JQKA - everything is stored as string.
        InitCardID = [f"{num}-{suit}" for suit in InitCardSuit for num in InitCardNum]
        #essentially this is i for i, but suit in a list of suits and for num in a list of numbers, including JQKA
        #I now have a complete list of all cards and their suits.
        InitDrawn = False
        #by default, cards are not drawn
        InitCardOwnedBy = ['Deck', 'Player1', 'Player2']
        #CardOwnedBy will track who 'owns' a card at any time.
        InitInPlay = False
        #by default, cards are not in play ie on the 'playing field'

        return InitCardSuit, InitCardNum, InitCardID, InitDrawn, InitCardOwnedBy, InitInPlay


InitCardSuit, InitCardNum, InitCardID, InitDrawn, InitCardOwnedBy, InitInPlay  = SetDeck()
# I'm going to flip, I was trying to debug this for half an hour only to find that setting variables this way depends on
# when you call on them - InitCardNum was called first, which lead to it getting the 'InitCardSuit' definition.
#I guess because they're different, identically named variables?

deck = Deck(CardSuit = InitCardSuit, CardNum = InitCardNum, CardID = InitCardID, Drawn = InitDrawn, CardOwnedBy = InitCardOwnedBy, InPlay = InitInPlay)


#just assigns numeric values to both suit and face value in ascending order and returns this result
def EstablishCardHierarchy() :

    TempCardNumValue = {num: i + 1 for i, num in enumerate(InitCardNum)}
    TempCardSuitValue = {suit: i + 1 for i, suit in enumerate(InitCardSuit)}

    return TempCardNumValue, TempCardSuitValue

    
def SimpleEvaluateCards (Card1, Card2) :

    #so this in theory compares two lists which hold the number and suit of a given card and return which single card is of higher value
    # return of 1 = Card 1 is the winner
    # return of -1 = Card 2 is the winner
    CardNumHierarchy, CardSuitHierarchy = EstablishCardHierarchy()

    Num1, Suit1 = Card1
    Num2, Suit2 = Card2

    try :
        if CardNumHierarchy[Num1] > CardNumHierarchy[Num2] :
            return 1
        #card1 is of a higher numerical value, return 1

        elif CardNumHierarchy[Num1] < CardNumHierarchy[Num2] :
            return -1
        #card1 is of a lower numerical value, return 'loss'

        else:
            #numbers are the same, compare suits
            if CardSuitHierarchy[Suit1] > CardSuitHierarchy[Suit2] :
                return 1
            #Suit is better, return 'wins'
            elif CardSuitHierarchy[Suit1] < CardSuitHierarchy[Suit2] :
                return -1
            #Suit is worse, return 'loss'
    except :
        print ("You're comparing two of the same card or something else broke - this should never occur")
        return None

#can currently compare two cards 
# remember to exclude the picked card somehow from the random result
def BetterOrWorseGame() :

    i = 0
    n = 2

    ValidSuit = ['diamonds', 'clubs', 'hearts', 'spades']
    ValidNum = [str(i) for i in range (2,11)] + ['jack', 'queen', 'king', 'ace']
    #must be lower because I strip the input

    while i < n :
        if i == 0 :
            response = input ("Enter a card value from 2-10, or a face card, or enter q to terminate the program.  ").strip().lower()
            if response in ValidNum :
                Player1Num = response
                print (f"Card chosen: {Player1Num.capitalize()}")
                i += 1
            elif response in ['q'] :
                print ("Program exited.")
                quit()
            else :
                print ('Your response must be a valid card - 2 through 10, or a face card.')
                i = 0
        if i == 1 :
            response = input ("Enter a valid card suit, or enter q to terminate the program.  ").strip().lower()
            if response in ValidSuit :
                Player1Suit = response
                print (f"Suit chosen: {Player1Suit.capitalize()}")
                i += 1
            elif response == 'q' :
                print ("Program exited.")
                quit()
            else :
                print ('Your response must be a valid suit - diamonds, clubs, hearts, or spades')
                i = 1
        if i >= 3 :
            print ("Something broke, you should be returned to your previous choice until you pick a valid face and suit.")
            quit()

    while True :
        Player2Num = random.choice(deck.FetchCardNum())
        Player2Suit = random.choice(deck.FetchCardSuit())
        if Player2Num == Player1Num and Player2Suit == Player1Suit :
            return True
            #restart the loop because the cards are identical - roll again
        if Player2Num != Player1Num or Player2Suit != Player1Suit :
            break
            #proceed once either the number or suit is different to the chosen card

    GameCard2 = [Player2Num, Player2Suit]
    GameCard1 = [Player1Num, Player1Suit]
    
    print (f"You have chosen : {Player1Num.capitalize()} of {Player1Suit.capitalize()}.")
    print (f"Your opponent has chosen : {Player2Num.capitalize()} of {Player2Suit.capitalize()}.")

    result = SimpleEvaluateCards(GameCard1, GameCard2)

    if result == 1:
        print(f"{str(GameCard1)} is better than {str(GameCard2)}, you win!")
    elif result == -1:
        print(f"{str(GameCard2)} is better than {str(GameCard1)}, you lose!")
    else:
        print(f"{GameCard1} and {GameCard2} are being evaluated as equal - this should never occur, or I just haven't implemented exclusive cards yet.")

BetterOrWorseGame()

'''
#just testing params

print (deck.FetchCardSuit())
print (deck.FetchCardNum())
print (type(deck.CardSuit))
print (type(deck.CardNum))
print ()
print (deck.CardID)
print ()

'''
'''
Current status: 


Have some hanging methods that I will need to put to use eventually
Player class needs to be built
Need to exclude same-cards from potential random pulls somehow

'''