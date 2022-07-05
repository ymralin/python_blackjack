import random
cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
available_cards = cards[:]
cards_in_game = []
player1_cards = []
cpu_cards = []

def draw_cards(player):
    card = available_cards[random.randint(0,len(available_cards)-1)]
    cards_in_game.append(card)
    if cards_in_game.count(card) == 4:
        available_cards.remove(card)
    if player == "player1":
        player1_cards.append(card)
    elif player == "cpu":
        cpu_cards.append(card)

def player_draw():
    draw_cards("player1")

def cpu_draw():
    draw_cards("cpu")

def count_points(cards):
    points=0
    for card in cards:
        if card in [2,3,4,5,6,7,8,9,10]:
            points+=card
        elif card in ["J","Q","K"]:
            points+=10
    aces_num=cards.count("A")
    for i in range(0,aces_num):
        if points<11:
            points+=11
        else:
            points+=1
    return points

def player_turn():
    player_turn = True
    while player_turn and count_points(player1_cards)<21:
        player_action = input("Do you want to draw a card? Y or N\n")
        if player_action.lower()=="y":
            player_draw()
            if count_points(player1_cards) <21:
                print(f"Your cards: {player1_cards}. Score: {count_points(player1_cards)}")
        else:
            player_turn = False

def cpu_turn():
    while count_points(cpu_cards)<17:
        cpu_draw()

def print_score():
    print(f"Your cards: {player1_cards}. Score: {count_points(player1_cards)}")
    print(f"CPU cards: {cpu_cards}. Score: {count_points(cpu_cards)}")


def game():
    player1_cards.clear()
    cpu_cards.clear()
    cards_in_game.clear()
    available_cards = cards[:]
    player_draw()
    cpu_draw()
    player_draw()
    cpu_draw()
    print(f"Your cards: {player1_cards}. Score: {count_points(player1_cards)}")
    print(f"first CPU card:[{cpu_cards[0]}].")
    if count_points(player1_cards) == 21:
        cpu_turn()
        if count_points(cpu_cards)<21:
            print_score()
            print("You won")
            return
        elif count_points(cpu_cards) == 21:
            print_score()
            print("Draw")
            return
        elif count_points(cpu_cards)>21:
            print_score()
            print("You won")
            return
    player_turn()
    if count_points(player1_cards)>21:
        print_score()
        print("You lose")
        return
    cpu_turn()
    if count_points(player1_cards) == 21:
        cpu_turn()
        if count_points(cpu_cards)<21:
            print_score()
            print("You won")
            return
        elif count_points(cpu_cards) == 21:
            print_score()
            print("Draw")
            return
        elif count_points(cpu_cards)>21:
            print_score()
            print("You won")
            return
    elif count_points(player1_cards) <21:
        if count_points(cpu_cards) < count_points(player1_cards) or count_points(cpu_cards)>21:
            print_score()
            print("You won")
        elif count_points(cpu_cards) == count_points(player1_cards):
            print_score()
            print("Draw")
        elif count_points(cpu_cards) > count_points(player1_cards) and count_points(cpu_cards)<=21:
            print_score()
            print("You lose")


replay = True

while replay:
    game()
    if_restart = input("Do you want to play again? Y or N\n")
    if if_restart.lower() == "y":
        replay = True
    elif if_restart.lower() == "n":
        replay = False
        print("Thanks for playing")
