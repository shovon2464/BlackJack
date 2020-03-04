import cards
import player

end_of_play = False
playing = False
turn = 0

def check_play():
    while True:
        try:
            ans = str(input("Press any key to play"))
        except:
            print("Whoops! please enter a key")
            continue
        else:
            print("The game is loading for you")
            return True
            break
    return False
def check_replay():
    while True:
        try:
            ans = str(input("Press any key to replay"))
        except:
            print("Whoops! please enter a key")
            continue
        else:
            print("The game is loading for you")
            return True
            break
    return False

def deal(comp,human,deck):
    human.hand.addCard(deck.sendCard())
    human.hand.addCard(deck.sendCard())
    comp.hand.addCard(deck.sendCard())
    comp.hand.addCard(deck.sendCard())

def place_the_bet(human):
    while True:
        try:
            bet = int(input("Please enter your bet: "))
            if (bet>human.bank):
                print("This surpasses your net amount, try less amount")
                continue
        except:
            print("This is not a number, try to put a number")
            continue
        else:
            return bet
            break

    return 0

def ask_to_hit():
    while True:
        try:
            result = input("Do you want to hit? Press H to confirm")
            if (result.lower() == 'h'):
                return True
                break
            return False
            break
        except:
            print("Please enter a button")
            continue

    return False

def hit(deck):
    return deck.sendCard()

def check_for_bust(human):
    remain = 21-human.hand.points
    if (remain>0):
        return 1
    elif (remain == 0):
        return 2
    else:
        return 3

def check_for_bust_comp(comp):
    remain = 17-comp.hand.points
    if (remain>0):
        return 1
    elif remain == 0:
        return 2
    else:
        return 3

def push(human,comp):
    if (human.points == 21) and (comp.points == 21):
        return True
    else:
        return False


def players_play(human,comp,deck,bet):
    global turn
    global playing
    while (turn==0):
        result = ask_to_hit()
        if result:
            card = hit(deck)
            human.hit_for_human(card)
            print(human)
            if (check_for_bust(human) == 3):
                print("You lose the game")
                human.bank -= bet
                comp.bank += bet
                replay(human, comp)
            elif (check_for_bust(human) == 2):
                print("You won the game")
                human.bank += bet
                comp.bank -= bet
                replay(human, comp)
        else:
            turn = 1
    return

def comps_play(human,comp,deck,bet):
    global playing
    global turn
    while (turn == 1):
        card = hit(deck)
        comp.hit_for_human(card)
        print(comp)
        if check_for_bust_comp(comp)==3:
            playing = False
            print("You won the game")
            human.bank += bet
            comp.bank -= bet
            replay(human,comp)
            break
        elif check_for_bust_comp(comp)==1:
            continue
        else:
            print("Computer has won the game")
            human.bank -= bet
            comp.bank += bet
            replay(human,comp)
            break



def replay(human,comp):
    global turn
    turn = 0

    temp1 = human.bank
    temp2 = comp.bank
    human = player.Player()
    human.bank = temp1
    comp = player.Player()
    comp.bank = temp2
    global playing
    print('Thanks for playing again, do you want to really play')
    playing = check_replay()
    if playing:
        deck = cards.Deck()
        bet = place_the_bet(human)
        print("Your bet is {}".format(bet))
        deal(comp, human, deck)
        print("Your {}".format(human.show_first_deal()))
        print("Computer's {}".format(comp.show_first_deal_private()))

        if push(human,comp):
            print("The game tied")
            replay(human,comp)

        if (check_for_bust(human) == 3):
            print("You lose the game")
            replay(human, comp)
        elif (check_for_bust(human) == 2):
            print("You won the game")
            replay(human, comp)

        while playing:
            players_play(human,comp,deck,bet)
            if playing:
                comps_play(human,comp,deck,bet)
    else:
        print("Thanks for playing")
        del human
        del comp



playing = check_play()


def play():
    if playing:
        deck = cards.Deck()
        comp = player.Player()
        human = player.Player()
        bet = place_the_bet(human)
        print("Your bet is {}".format(bet))
        deal(comp, human, deck)
        print("Your {}".format(human.show_first_deal()))
        print("Computer's {}".format(comp.show_first_deal_private()))

        if push(human,comp):
            print("The game tied")
            replay(human,comp)

        if (check_for_bust(human)==3):
            print("You lose the game")
            replay(human, comp)
        elif (check_for_bust(human)==2):
            print("You won the game")
            replay(human, comp)

        while playing:
            players_play(human,comp,deck,bet)
            if playing:
                comps_play(human,comp,deck,bet)

play()













