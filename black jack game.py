def blackjack(cards):#black jack game as function
    pb=True#player not busted
    db=True#dealer not busted
    import random
    u1=random.choice(cards)#cards for user
    u2=random.choice(cards)
    
    total=0
    ace=0
    l=[u1,u2]  #cards of user
    print("The Player's hand:",'\n1  ',u1,'\n2  ',u2)

    
    for i in l:
        if i in ['J','K','Q']:
            total+=10#value of J,K,Q is 10
        elif i=='Ace':
            total+=11#ace can have value 1 or 11 so for first ace it will enable value of ace as 11
            ace+=1#while keeping count of ace such that if it reappears the value for ace will be entered as 1
        else:
            total+=i#other cards have value as per their number
        while total>21 and ace>0:#condition if more than one ace and total goes over 21 appear
            total-=10
            ace-=1
    if total>21:#player loses if total goes above 21
            print('busted!you lost!dealer wins')
            pb=False#the player not busted will turn false
    print('your total;',total)
    


    
    d1=random.choice(cards)#cards of dealer
    d2=random.choice(cards)
    print("The Dealer's hand:\n",d1)#only one card of dealer will be showed
    l1=[d1,d2]
    t=0
    a=0
    for i in l1:    
        if i in ['J','K','Q']:#value of J,K,Q is 10
                    t+=10
        elif i=='Ace':
                    t+=11#ace can have value 1 or 11 so for first ace it will enable value of ace as 11
                    a+=1#while keeping count of ace such that if it reappears the value for ace will be entered as 1
        else:
                    t+=i#other cards have value as per their number   
        while t>21 and a>0:#condition if more than one ace and total goes over 21 appear
                    t-=10
                    a-=1
    if t>21:#dealer loses if total goes above 21
        print('Dealer busted! You win!')
        db=False#the dealer not busted will turn false
        
        
    
    choice=input(''' would you like to:
1 Hit
2 Stand
enter your choice(1/2);''')#two choices will be offered to player whether to stand or hit
    if choice=='1':#if player chooses hit means they get to draw one more card to increase their total value after seeing dealer's first card
        u3=random.choice(cards)
        l.append(u3)#new card will be added to the list of player's card
        print(l)
        if u3 in ['J','K','Q']:#value of J,K,Q is 10
                total+=10
        elif u3=='Ace':
                total+=11#ace can have value 1 or 11 so for first ace it will enable value of ace as 11
                ace+=1#while keeping count of ace such that if it reappears the valu fo ace will be entered as 1
        else:
                total=total+u3#total will be updated
        while total>21 and ace>0:#condition if more than one ace and total goes over 21 appear
                total-=10
                ace-=1
        if total>21:#player loses if total goes above 21
                print('busted!you lost!dealer wins')
                pb=False#player not busted will turn false
                print("dealer's cards;",l1)             
        if t<=16:#same choice appear for dealer to hit or stand if dealer's count is below 16 it will automatically hit and hence a card will be drawn and added to dealer's card
            print('dealer drew one more card')
            d3=random.choice(cards)
            l1.append(d3)
            print("dealer's card;", l1)  
            if d3 in ['J','K','Q']:#value of J,K,Q is 10
                    t+=10
            elif d3=='Ace':
                    t+=11#ace can have value 1 or 11 so for first ace it will enable value of ace as 11
                    a+=1#while keeping count of ace such that if it reappears the valu fo ace will be entered as 1
            else:
                    t=t+d3#total will be updated
            while t>21 and a>0:#condition if more than one ace and total goes over 21 appear
                    t-=10
                    a-=1
            if t>21:#dealer loses if total goes above 21
                print('Dealer busted! You win!')
                db=False#dealer not busted will be false


                
        print("dealer's cards;",l1)
        print("Dealer's total;",t)#total of dealer will be displayed
         
        print('your total;',total)#total of player will be displayed
    else:
        print('your cards;',l)#total of player will be displayed
        print("dealer's cards;",l1)#total of dealer will be displayed    
        if t<=16:#same choice appear for dealer to hit or stand if dealer's count is below 16 it will automatically hit and hence a card will be drawn and added to dealer's card
            print('dealer drew one more card')
            d3=random.choice(cards)
            l1.append(d3)
            print("dealer's card;", l1)
            for i in l1:
                if i in ['J','K','Q']:#value of J,K,Q is 10
                    t+=10
                elif i=='Ace':
                    t+=11#ace can have value 1 or 11 so for first ace it will enable value of ace as 11
                    a+=1#while keeping count of ace such that if it reappears the valu fo ace will be entered as 1
                else:
                    t=t+i#total will be updated
                while t>21 and a>0:#condition if more than one ace and total goes over 21 appear
                    t-=10
                    a-=1
            if t>21:#dealer loses if total goes above 21
                print('Dealer busted! You win!')
                db=False#dealer not busted will be false
        print("Dealer's total;",t)
    

    if  db and  pb: #if both pb and db are True then 
        if total>t:#if player's total is greater than dealer's 
            print('you win!')#you win will be printed
        elif t==total:#if both of their totals are equal then 
            print('Tie!!!')#tie will be printed
        else:#if dealer's total is greater than players
            print('Dealer wins!!')#dealer win will be printed
cards=[2,3,4,5,6,8,9,10,'J','K','Q','Ace']#list of card in a deck
def main_menu():#main menu function for the game
    print('''Basic Blackjack Rules
The goal is to beat the dealer by getting as close to 21 as you can without going over (busting).​

Each player receives two cards face up; the dealer gets one card face up and one face down ("hole card").​

Number cards count as their value, face cards (J, Q, K) count as 10, and Aces can be worth 1 or 11.​

If the first two cards are an Ace and a ten-value card, that is a "blackjack" and usually wins instantly with a special payout.''')#basic rules of the game that will be printed
    while True:#for endless loop game
        try:
            ch=int(input('WOULD YOU LIKE TO PLAY PRESS 1 FOR YES, 2 FOR NO;'))
            if ch==1:
                blackjack(cards)#the game is called and will be started if ch is 1
            elif ch==2:
                print("Thank you for playing")
                break#else loop will break   
            else:
                print("Invalid choice")
        except:
            if ValueError:
                print("Enter number only")
    
main_menu()#main menu called 
    
            
        
    
    
    
