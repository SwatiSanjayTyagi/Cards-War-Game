import traceback
import random
try:
    class Deck:
        def __init__(self):
            suits = ['H','D','S','C']
            ranks = ['2','3','4','5','6','7','8','9','10','J', 'Q','K','A']    
            allcards = []
            # creating a pool of all cards from suits and ranks
            self.suits = suits # for fetching data from suits
            self.ranks = ranks # for fetching data from ranks
            self.allcards = allcards # for fetching data from allcards
            for cardtype in self.suits:
                for cardrank in self.ranks:
                    self.allcards.append(cardtype+cardrank)
        def cardshuffle(self):
            #for shuffling the cards
            random.shuffle(self.allcards)
            return self.allcards
        def cardssplit(self):
            #for splitting the cards between players
            self.player1cards = self.allcards[:26] #from 0-26
            self.player2cards = self.allcards[26:] #from 27-till the end
            return self.player1cards , self.player2cards , self.ranks
    class Player():
        def __init__(self,plyname,cards): #assign cards to respective users
            self.plyname = plyname
            self.cards = cards
    class Hand():
        #gamestatus has two flags 'G' and 'W' 
        def setgamestatus(self,gamestatus): #if its a normal game the element at 
            self.gamestatus = gamestatus 
            if ( self.gamestatus  == "G" ) :
                return 0 #index 0 is to be taken
            else:
                return 3 #else element at index 3 is to be taken

        def addcard(self,plyname,cards): #appends the list
            self.plyname = plyname
            self.cards = cards
            self.plyname.append(self.cards)
                        
        def removecard(self,n): #pops the list
            self.n = n
            player1.cards.pop(self.n)
            player2.cards.pop(self.n)

    deck_obj = Deck()
    deck_obj.cardshuffle()
    (ply1cards,ply2cards,ranks) = deck_obj.cardssplit()
    plyname1 = input("Please enter the name of first player: ")
    plyname2 = input("Please enter the name of second player: ")
    player1 = Player(plyname1,ply1cards)
    player2 = Player(plyname2,ply2cards)
    print (player1.plyname + ' has the following cards : ')
    print (player1.cards)
    print (player2.plyname + ' has the following cards : ')
    print (player2.cards)
    print (len(player1.cards) , len(player2.cards))
    hand_obj = Hand()
    while (len(player1.cards) > 0 and  len(player2.cards) > 0) :
        choice = input("Are you sure you want to continue with the game? Y/N: ")
        
        if choice.upper() == 'Y' :
            n = hand_obj.setgamestatus("G") # G = game W = war
            print (player1.plyname + "'s card: " + player1.cards[n])
            print (player2.plyname + "'s card: " + player2.cards[n])
            position1 = ranks.index(player1.cards[n][1:])
            position2 = ranks.index(player2.cards[n][1:])
            if position1 > position2:
                print (player1.plyname + " has won")
                hand_obj.addcard(player1.cards,player1.cards[n])
                hand_obj.addcard(player1.cards,player2.cards[n])
                hand_obj.removecard(n)
            elif position1 < position2:
                print (player2.plyname + " has won")
                hand_obj.addcard(player2.cards,player1.cards[n])
                hand_obj.addcard(player2.cards,player2.cards[n])
                hand_obj.removecard(n)
            else:
                print ("it's a war")
                if (len(player1.cards) >= 5 and  len(player2.cards) >= 5):
                    n = hand_obj.setgamestatus("W") # G = game W = war
                    print (player1.plyname + "'s card: " + player1.cards[n])
                    print (player2.plyname + "'s card: " + player2.cards[n])
                    warposition1 = ranks.index(player1.cards[n][1:])
                    warposition2 = ranks.index(player2.cards[n][1:])
                    if warposition1 > warposition2:
                        print (player1.plyname + " has won")
                        for i in range(n+1):
                            hand_obj.addcard(player1.cards,player1.cards[i])
                            hand_obj.addcard(player1.cards,player2.cards[i])
                            hand_obj.removecard(i)
                    elif warposition1 < warposition2:
                        print (player2.plyname + " has won")
                        for i in range(n+1):
                            hand_obj.addcard(player2.cards,player1.cards[i])
                            hand_obj.addcard(player2.cards,player2.cards[i])
                            hand_obj.removecard(i)
                    else:
                        print ("It's a war for the another time")
                        break
                else:
                    print ("Insufficient cards")
                    break
        else:
            break
        print ("Number of cards with " + player1.plyname + " and " + player2.plyname + " : " + str(len(player1.cards)) + " , " + str(len(player2.cards)))
    if (len(player1.cards) > len(player2.cards)):
        print ("Congratulations!!! player " + player1.plyname + " has won the game.")
    elif (len(player1.cards) < len(player2.cards)) :
        print ("Congratulations!!! player " + player2.plyname + " has won the game.")
    else:
        print ("It's a draw!!!")

except:
    print ("Please contact our developers at ##########.")
    print ("Inconvenience is regretted")
finally:
    print ("Game Over!!!")
