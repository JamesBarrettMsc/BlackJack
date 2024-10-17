import random
import sys
import os
import time
from termcolor import colored



################
def generate_deck()-> list:
    deck =[]
    suits = ['Heart', 'Diamonds', 'Spades', 'Clubs']
    faceCard = ['Ace', 'Jack', 'Queen', 'King']

    for s in suits:
        for value in range(2, 11):
            deck.append(str(value)+" "+s)
            
        for value in faceCard:
            deck.append(str(value)+" "+s)
            
    random.shuffle(deck)
    return deck
        
################
def draw_cards(deck,num_of_cards)-> list:
    hand=[]
    
    if(len(deck)<num_of_cards):
        print("Out of cards")
        sys.exit()
    
    for num in range(num_of_cards):
        hand.append(deck[0]) 
        deck.pop(0)
    return hand

################
def calculate_hand(hand)-> int:
    value=0
    for card in hand:
        value+=int(card.replace("Heart","").replace("Diamonds","").replace( "Spades","").replace("Clubs","").replace("Queen","12")
        .replace("Jack","11").replace("King","13").replace("Ace","1"))
        
    if value<10 and any("Ace" in s for s in hand):
        value+=10
        
    return value
        
################
def render_hand_cli(hand, number_Face_down=0, name=" Player ")->str:
    
    ascii_hand=""
    indent=0
    
    for card in hand[:len(hand)-number_Face_down]:
        card_str= (card.replace("Heart","♥").replace("Diamonds","♦").replace( "Spades","♠").replace("Clubs","♣")
        .replace("Queen","Q").replace("Jack","J").replace("King","K").replace("Ace","A"))
        
        indent+=1
        
        ascii_hand+=("░"*indent )
        ascii_hand+=("┏-------┓\n")
        
        ascii_hand+=("░"*indent )
        ascii_hand+=("| "+card_str.rjust(4, ' ')+"  |\n" )
    
    
    for nun in range(number_Face_down):
       indent+=1
       ascii_hand+=("░"*indent )
       ascii_hand+=("┏-------┓\n")
       
       ascii_hand+=("░"*indent )
       ascii_hand+="| ▓ ▓ ▓ |\n"
       #ascii_hand+=colored("| ▓ ▓ ▓ |\n",'red' )
        
    #ascii_hand+=("░"*(indent+10))
    
    columns=0
    ascii_rows= ascii_hand.split("\n")
    
    for row in ascii_rows:
        if len(row)>columns:columns=len(row)
        
    ascii_hand_tep=""
    
    for row in ascii_rows:
        ascii_hand_tep+= row.ljust(columns, '░')+"░\n"

    ascii_hand=("░"*(columns+1))+"\n"+ascii_hand_tep
    
    
    ##(NEW)
    ###############################################################
    heder="░"*indent+"░░░░░░░░░░\n"
    heder+= "░"*indent+name+"░░"
    ascii_hand =heder+"\n"+ascii_hand
    ###############################################################
    ###############################################################
    
    
    return ascii_hand
    

################
def  render_interlace_hand_cli (hand_A, hand_B)-> str:
    
    ascii_hand=""
    a=hand_A.split("\n")
    b=hand_B.split("\n")
    
    for num in range(len(a)-1):
        ascii_hand+=(a[num])
        
        if (len(b)-1>=num):
            ascii_hand+=(b[num])
        
        ascii_hand+=("\n")
    
    for num in range(len(a)-1,len(b)):
        ascii_hand+=("░"*(len(a)//2)+("░"*9)+b[num]+"\n")
       

    columns=0
    ascii_rows= ascii_hand.split("\n")
    
    for row in ascii_rows:
        if len(row)>columns:columns=len(row)
        
    ascii_hand_tep=""
    
    for row in ascii_rows[:-2]:
        ascii_hand_tep+= row.ljust(columns, '░')+"\n"

    if( '|' in (ascii_hand_tep.split("\n"))[-2]):ascii_hand_tep+= ''.ljust(columns, '░')+"\n"

    ascii_hand= ascii_hand_tep
    
    return ascii_hand



    
    color_palette = {
        "░": colored("░",'green'), "♥": colored("♥",'red'), "♦": colored("♦",'red'),
        "♣": colored("♣",'white',attrs=['reverse']),"♠": colored("♠",'white',attrs=['reverse']),
        "▓": colored("▓",'yellow'), "-": colored("-",'blue'), "|": colored("|",'blue'),
        "┓": colored("┓",'blue'), "┏": colored("┏",'blue'), ":": colored(":",'cyan')
    }

    ascii_hand=""

    for singleChr in ascii_str:
        try:
            ascii_hand+=color_palette[singleChr]
        except:
            ascii_hand+=singleChr
    
    print(ascii_hand)
    
    
def delay_animation_cli(seconds,color='red'):
    time_elapsed=0
    frames =[" (/)"," (-)"," (\\)"," (|)"," (-)",]
    
    while(time_elapsed<seconds):
        for s in range(4):
            time.sleep(.25)
            print("Thinking",colored(frames[s],color),end=" \r\r")
        time_elapsed+=1





#######################################################################
#######################################################################
def dealer_round(dealer_hand, player_hand):
    
    table_value=calculate_hand(player_hand)
    
    os.system('cls')
    print_color("::: ::::::::::::::::::::::::::: ::: \n")
    
    print_color(render_hand_cli(dealer_hand,0,name=" Player "))
    print_color(render_hand_cli(player_hand,0,name=" Player "))
    
    
    while(table_value<21):
        
        os.system('cls')
        print_color("::: ::::::::::::::::::::::::::: ::: \n")
        
        print_color(render_hand_cli(player_hand,0," Player "))
        print_color(render_hand_cli(dealer_hand,0," Player "))
        print_color("Dealer\n Hand Value:: "+str(calculate_hand(dealer_hand)))
   
        if(calculate_hand(dealer_hand)<= table_value):
            delay_animation_cli(3)  
            dealer_hand.append(deck[0]) 
            deck.pop(0)
        else:
            break
        
    input("Press Enter to continue...")


while True:
    

    os.system('cls')
    #os.system('COLOR 2A')

    deck = generate_deck()

    dealer_hand=draw_cards(deck,2)

    print_color(render_hand_cli(dealer_hand,1," Dealer "))


    player_hand = draw_cards(deck,2)

    print_color(render_hand_cli(player_hand,0," Player "))
    print_color("Player\n Hand Value:: "+str(calculate_hand(player_hand)))
    print_color("::::::::::::::::: ")

    while(calculate_hand(player_hand)<21):
        if  'y' in input(":: Would you like to\ndraw another card (y/N)::").lower().strip():
            os.system('cls')
            

     
            
        
            print_color(render_hand_cli(dealer_hand,1," Dealer "))
            
            indent=len(player_hand)
            #print_color('░'*indent+"░░░░░░░░░░░")
            player_hand += draw_cards(deck,1)
            print_color(render_hand_cli(player_hand,0," Player "))
                        
            print_color("Player\n Hand Value:: "+str(calculate_hand(player_hand)))
            
            
        else:
            break
        
        

    input("Press Enter to continue...")

    os.system('cls')
    print_color("::: ::::::::::::::::::::::::::: ::: ")
    print_color("░░ Dealer Round ░░")

    #indent=len(player_hand)
    #print_color('░'*indent+"░░░░░░░░░░░")
    #print_color('░'*indent+"░ Player ░░")
    print_color(render_hand_cli(player_hand))

    #indent=len(dealer_hand)
    #print_color('░'*indent+"░░░░░░░░░░░")
    #print_color('░'*indent+"░ Dealer ░░")
    dealer_round(dealer_hand,player_hand)


    os.system('cls')
    print_color("::: ::::::::::::::::::::::::::: ::: ")

    print()

    table=render_interlace_hand_cli(render_hand_cli(player_hand), render_hand_cli(dealer_hand))
    columns= len(table.split("\n")[-2])

    print_color("".ljust(columns, '░'))
    print_color("░ Player ░░░░░ Dealer ".ljust(columns, '░'))


    print_color(table)

    print_color("Player :"+str(calculate_hand(player_hand)))
    print_color("Dealer :"+str(calculate_hand(dealer_hand)))


    if(calculate_hand(player_hand)>21):
        print_color("Bust!")
        
    elif(calculate_hand(player_hand)==21):
        print_color("BlackJack!")

    elif(calculate_hand(dealer_hand)>21):
        print_color("Players Wins")

    elif(calculate_hand(player_hand)>calculate_hand(dealer_hand)):
        print_color("Player Wins")
        
    elif(calculate_hand(player_hand)==calculate_hand(dealer_hand)):
        print_color("Draw")

    else:
        print_color("Player Loses")

    if 'y' in input("Quit (y/N)").strip().lower():
        break



