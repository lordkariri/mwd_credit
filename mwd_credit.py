def main():
    valid = False
    ## takes whi 
    option = menu()
    ## calls the check my card function, and allows user to keep re-entering a card number until it is valid 
    if option == 1: 
        while not valid:
            card = input("\nplease enter your card number: ")
            valid = checkMyCard(card)
        print ("your card is valid")
        menu()
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        quit()
def menu():
    print ("\n1.	Check my Card\n2.	Import numbers to check\n3.	Generate a valid CC number\n4.	Quit\n")
    option = None
    ## makes sure option entered is valid, allows user to keep re-entering until it is valid  
    while option == None:
        try:
            option = int(input("please enter a number to go to a option: "))
            if option > 4 or option < 1:
                print ("\nnot valid\n")
                option = None
                
        except:
            print ("not valid\n")
    return option

def checkMyCard(card):
    try:
        
        
        
        if len(card) != 16: 
            return False
        # solved in one line for fun (long more organised version of Luhn's algorithm is commented below)
        if str(sum([int(x) for x in [char for char in "".join([str(x) for x in (([int(x)*2 for x in ([char for char in card][::2])]))])]]) + sum([int(x) for x in [char for char in card]][::-1][::2]))[-1] == "0": return True
        else: return False
        
        
    except:
        print ("\nnot valid\n")
        return False
        
def importNums():
    pass
def generateCC():
    pass
def quit():
    python.quit()



main()
    