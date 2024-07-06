title="Welcome to Trescented Candles!"
midtitle=title.center(75,"=")
print(midtitle)

print("")

loop = True

while loop:
    print("")
    border="_"
    bigborder=border.center(75,"_")
    print(bigborder)
    border_2="-"
    bigborder_2=border_2.center(75,"-")
    print("")
    
    print("Pick a candle of your choice to go!")

    print("")

    menu="AVAILABLE" 
    midmenu=menu.center(75,"-")
    print(midmenu)
    
    C1="Chamomile"
    C2="Fresh Bamboo"
    C3="Peppermint"
    C4="Cucumber Melon"
    C5="Lavender"
    S="Small"
    M="Medium"
    L="Large"

    print("[C1]",C1,"           ","S [150php]","...","M [180php]","...","L [200php]")
    print("[C2]",C2,"        ","S [150php]","...","M [180php]","...","L [200php]")
    print("[C3]",C3,"          ","S [150php]","...","M [180php]","...","L [200php]")
    print("[C4]",C4,"      ","S [160php]","...","M [190php]","...","L [280php]")
    print("[C5]",C5,"            ","S [175php]","...","M [200php]","...","L [300php]")

    print(bigborder)
    print("")

    print("NOTE: You could only pick one candle and one size at a time only")    
    order=input("What would you like to order? ")

    '''Order Code'''

    if order==C1 or order=="C1":
        loop=False
        quantity=int(input("How many do you want? "))
        size=input("What size are you choosing? ")
        cost_S=150*quantity
        cost_M=180*quantity
        cost_L=200*quantity
        if size=="S" or size==S or size=="small":
            print(bigborder_2)
            print("your order/s:",quantity,S,C1,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_S)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_S:
                print("")
                print("I received",payment,"php")
                change=payment-cost_S
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,S,C1,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_S:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,S,C1,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_S:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="M" or size==M or size=="medium":
            print(bigborder_2)
            print("your order/s:",quantity,M,C1,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_M)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_M:
                print("")
                print("I received",payment,"php")
                change=payment-cost_M
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,M,C1,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_M:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,M,C1,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_M:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="L" or size==L or size=="large":
            print(bigborder_2)
            print("your order/s:",quantity,L,C1,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_L)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_L:
                print("")
                print("I received",payment,"php")
                change=payment-cost_L
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,L,C1,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_L:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,L,C1,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_L:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        else:
            print("There are no sizes like that","Please pick again")
            loop=True

    elif order==C2 or order=="C2":
        loop=False
        quantity=int(input("How many do you want? "))
        size=input("What size are you choosing? ")
        cost_S=150*quantity
        cost_M=180*quantity
        cost_L=200*quantity
        if size=="S" or size==S or size=="small":
            print(bigborder_2)
            print("your order/s:",quantity,S,C2,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_S)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_S:
                print("")
                print("I received",payment,"php")
                change=payment-cost_S
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,S,C2,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_S:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,S,C2,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_S:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="M" or size==M or size=="medium":
            print(bigborder_2)
            print("your order/s:",quantity,M,C2,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_M)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_M:
                print("")
                print("I received",payment,"php")
                change=payment-cost_M
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,M,C2,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_M:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,M,C2,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_M:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="L" or size==L or size=="large":
            print(bigborder_2)
            print("your order/s:",quantity,L,C2,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_L)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_L:
                print("")
                print("I received",payment,"php")
                change=payment-cost_L
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,L,C2,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_L:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,L,C2,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_L:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        else:
            print("There are no sizes like that","Please pick again")
            loop=True

    elif order==C3 or order=="C3":
        loop=False
        quantity=int(input("How many do you want? "))
        size=input("What size are you choosing? ")
        cost_S=150*quantity
        cost_M=180*quantity
        cost_L=200*quantity
        if size=="S" or size==S or size=="small":
            print(bigborder_2)
            print("your order/s:",quantity,S,C3,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_S)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_S:
                print("")
                print("I received",payment,"php")
                change=payment-cost_S
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,S,C3,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_S:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,S,C3,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_S:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="M" or size==M or size=="medium":
            print(bigborder_2)
            print("your order/s:",quantity,M,C3,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_M)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_M:
                print("")
                print("I received",payment,"php")
                change=payment-cost_M
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,M,C3,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_M:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,M,C3,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_M:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="L" or size==L or size=="large":
            print(bigborder_2)
            print("your order/s:",quantity,L,C3,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_L)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_L:
                print("")
                print("I received",payment,"php")
                change=payment-cost_L
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,L,C3,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_L:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,L,C3,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_L:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        else:
            print("There are no sizes like that","Please pick again")
            loop=True
    elif order==C4 or order=="C4":
        loop=False
        quantity=int(input("How many do you want? "))
        size=input("What size are you choosing? ")
        cost_S=160*quantity
        cost_M=190*quantity
        cost_L=280*quantity
        if size=="S" or size==S or size=="small":
            print(bigborder_2)
            print("your order/s:",quantity,S,C4,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_S)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_S:
                print("")
                print("I received",payment,"php")
                change=payment-cost_S
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,S,C4,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_S:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,S,C4,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_S:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="M" or size==M or size=="medium":
            print(bigborder_2)
            print("your order/s:",quantity,M,C4,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_M)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_M:
                print("")
                print("I received",payment,"php")
                change=payment-cost_M
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,M,C4,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_M:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,M,C4,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_M:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="L" or size==L or size=="large":
            print(bigborder_2)
            print("your order/s:",quantity,L,C4,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_L)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_L:
                print("")
                print("I received",payment,"php")
                change=payment-cost_L
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,L,C4,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_L:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,L,C4,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_L:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        else:
            print("There are no sizes like that","Please pick again")
            loop=True
    elif order==C5 or order=="C5":
        loop=False
        quantity=int(input("How many do you want? "))
        size=input("What size are you choosing? ")
        cost_S=175*quantity
        cost_M=200*quantity
        cost_L=300*quantity
        if size=="S" or size==S or size=="small":
            print(bigborder_2)
            print("your order/s:",quantity,S,C5,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_S)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_S:
                print("")
                print("I received",payment,"php")
                change=payment-cost_S
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,S,C5,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_S:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,S,C5,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_S:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="M" or size==M or size=="medium":
            print(bigborder_2)
            print("your order/s:",quantity,M,C5,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_M)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_M:
                print("")
                print("I received",payment,"php")
                change=payment-cost_M
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,M,C5,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_M:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,M,C5,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_M:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        elif size=="L" or size==L or size=="large":
            print(bigborder_2)
            print("your order/s:",quantity,L,C5,"Candle/s")
            print(bigborder_2)
            print("Your total is",cost_L)
            print(bigborder_2)
            payment=int(input("Your payment is? "))
            if payment>cost_L:
                print("")
                print("I received",payment,"php")
                change=payment-cost_L
                print(bigborder_2)
                print("Enjoy your candle/s!")
                print("")
                print("you received:",quantity,L,C5,"Candle/s")
                print(bigborder_2)
                print("Don't forget your change!")
                print("")
                print("you received:",change,"php")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment==cost_L:
                print(bigborder_2)
                print("I received exact cash, here's your candle/s")
                print(bigborder_2)
                print("you received:",quantity,L,C5,"Candle/s")
                print("")
                again=input("Would you like to shop again(Y/N)? ")
                if again=="Y" or again=="Yes" or again=="yes":
                    loop=True
                else:
                    print("Have a nice day")
            elif payment<cost_L:
                print("")
                print("Uh oh! Looks like you don't have enough cash for the purchase, please pick something else")
                loop=True
        else:
            print("There are no sizes like that","Please pick again")
            loop=True

    else:
        print("We don't have that, please look again")
        loop=True
