
import random 
import time
from getpass import getpass #note for getpass to work, which censors the password, you need to run the program in the terminal. running it in IDLE will give an error
import re



users = [] 


def login_system(users):
    for i in range(1,3): #this loop runs twice, so that two users can input their credentials
        username = input(f"what is the correct username for player {i}?")#assign a correct username
        print("")
        password = getpass(f"what is the correct password for player {i}?") #assign a correct password
        users.append(username) #appends the list usernames with usernames so they can be accessed easily later in the program


        while True:
            usernameguess = input(f"input the username of player {i}:") #user inputs guess for the username
            print("")
            passwordguess = getpass(f"input the password of player {i}:")#user inputs guess for the password
            print("")
            if usernameguess.strip() == username.strip() and passwordguess.strip() == password.strip(): #if both guesses match the actuanl credentials
                print("system access granted!")
                break
            else:
                print("access denied. password and/or username incorrect.")
            


login_system(users)


cards = [["red", "black", "yellow"],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

deck = []

while len(deck) < 30: #generates a random sequence of the 30 cards, stored in a list
    random_colour = random.randint(0,2)
    random_number = random.randint(0,9)
    
    current_colour = cards[0][random_colour]
    current_number = cards[1][random_number]
    
    current_card = current_colour, current_number

    if current_card not in deck:
        deck.append(current_card)
    else:
        continue 
    
player1 = []
player2 = []


colour_wins = {  #colour win matchups - key is the winning colour in the match, value is the loser
    "red" : "black",
    "yellow" : "red",
    "black" : "yellow"
}


for i in range(0,30,2):
    
    card1 = deck[i] 
    card2 = deck[i+1]

    print(f"here's {users[0]}'s card, {card1}")
    #time.sleep(1)
    print(f"here's {users[1]}'s card, {card2}")
    #time.sleep(1)

    def player1win(player1,card1,card2):
        print(f"card 1,{card1[0]},{card1[1]} wins!")
        print("")
        return player1.extend((card1, card2)) #adds card1 and card2 to player 1's deck
    
    def player2win(player2,card1,card2):
        print(f"card 2, {card2[0]},{card2[1]} wins!")
        print("")
        return player2.extend((card1, card2)) #adds card1 and card2 to player 2's deck


    #game mechanics
    if card1[0] == card2[0]: #if the colour is the same
        if card1[1] > card2[1]: #larger number wins
            player1win(player1,card1,card2)
        else:
            player2win(player2,card1,card2)
            
    else: #if colour is different, find which one wins
        if colour_wins.get(card1[0]) == card2[0]: #if the value of the key equal to the colour of player 1's card in dict colour_wins is equal to pplayer 2's card, card 1 wins
            player1win(player1,card1,card2)
        else:
            player2win(player2,card1,card2)

winning_deck = []            
        

def neat_deck(winning_deck):
    for i in winning_deck:
        print(i)


if len(player1) > len(player2): #calcualtes the winner based on deck length
    print(f"{users[0]} is the winner! here's their deck: ")
    winning_deck = player1
    winner = users[0]
    neat_deck(winning_deck)
else:
    print(f"{users[0]} is the winner! here's their deck: ")
    winning_deck = player2
    winner = users[1]
    neat_deck(winning_deck)
    
deck_length = len(winning_deck)



def format_deck(winning_deck): #formatting the deck for the file 
    return "\n".join(", ".join(str(item) for item in card) for card in winning_deck) #inner join() joins the card colour and number together with a comma and makes it all a strng. the outer join loop joins all those wiht a new line
   
with open("winners.txt", "a+") as file:
    file.write(f"\n {winner}, deck length: {len(winning_deck)}")
    print("winner and deck written to file")


def get_deck_lengths(line):
    match = re.search('deck length:\s*(\d+)', line) #uses regex to find the sequence deck length, followed by a space, then followed by any number of digits for each line
    if match:
        return int(match.group(1)) #grabs what's inside the first parenthesis, i.e. the digits
    else:
        return 0 #returns 0 for lines w/ whitespace - error handling

    
def read_and_sort_file(filename="winners.txt"): 
    with open(filename,"r") as file:
        lines = file.readlines() #stores all the lines of the file as indexes in a list
    sorted_entries = sorted(lines, key=get_deck_lengths, reverse=True) #sort the lines, in order as determined by their deck lengths, returned highest to lowest
    return sorted_entries[0:5]   

print(read_and_sort_file("winners.txt"))

