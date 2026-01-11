# Library imported
import math

# Drinks dictionary
drinks = {''
          'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
          'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
          'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50},
          'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 1},
          '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 0},
          'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 0},
          'LT': {'description': 'Lemon Tea', 'price': 1.1, 'quantity': 50}}

# Remove drinks once the customer pays drinks
drinkhold = []

# Drinks menu
def Drinkmenu():
    # print("{h1:5} {h2:15} {h3:9}".format(h1 = "Name", h2 = "Description", h3 = "Price"))
    for nme, descpric in drinks.items():
        dnme = nme
        desc = descpric['description']
        dpric = descpric['price']
        dquant = descpric['quantity']
        if dquant == 0:
            print(f"{dnme}. {desc:13} (S${dpric:.1f}) ***Out of stock***")
        else:
            print(f"{dnme}. {desc:13} (S${dpric:.1f}) Qty: {dquant:}")
    print("0. Exit / Payment")

# Vender menu
def VenderMenu():
    print("Welcome to ABC Machine.")
    print("Select from the following choices to continue:")
    print("1. Add Drink Type")
    print("2. Replenish Drink")
    print("0. Exit")

# user input for checking drinks
userchoice = ""
def druschoice(inputofuser ,errormsg):
    while True:
        # Get input and convert to uppercase, taking only the first character
        global userchoice
        userchoice = input(inputofuser).strip().upper()
        if userchoice in drinks:
            return userchoice
        elif userchoice == "0":
            return userchoice
        else:
            print(errormsg)

# Checking of yes or no
def checkyesorno(inputofuser, errorMsg):
    while True:
        user_input = input(inputofuser).strip().upper()
        if user_input == 'Y' or user_input == 'N':
            return user_input
        else:
            print(errorMsg)

# float check
def EnterFloat(inputofuser, errorMsg):
    while True:
        try:
            return float(inputofuser)
        except:
            print(errorMsg)
            return None

# integer check
def EnterInt(inputofuser, errorMsg):
    while True:
        try:
            return int(inputofuser)
        except:
            print(errorMsg)
            return None

# Calculating drink total
drinkstotal = 0
end = True
def drinkscal():
    global drinkstotal
    drinkstotal += 1

# Calculating the amount of drink customer order
needpay = 0
def drinkamt(uschoice):
    global needpay
    if uschoice in drinks and drinks[uschoice]['quantity'] > 0:
        needpay += drinks[uschoice]['price']

# Cancellation of purchase
def cancelofpurchase(inputofuser, errorMsg):
    while True:
        user_input = input(inputofuser).strip().upper()
        if user_input == 'Y' or user_input == 'N':
            if user_input == 'Y':
                resetallvalues()
                break
            if user_input == 'N':
                break
        else:
            print(errorMsg)

#Reset of customer order
def resetallvalues():
    global needpay
    needpay = 0
    global drinkstotal
    drinkstotal = 0
    global loop
    loop = 0
    global drinkhold
    drinkhold.clear()

# Calculating if user has paid or not
def drinkpayment(paymentno, errorMsg):
    print(f"Please pay: ${paymentno:.2f}")
    print("Indicate your payment:")
    while needpay != 0:
        Tenpay = input("Enter no. of $10 notes: ")
        if EnterInt(Tenpay.isnumeric(), "Enter a number please please for $10!"):
            usercash = float(int(Tenpay) * 10)
            if usercash > paymentno:
                print(f"Please collect your change: ${usercash - paymentno:.2f}")
                removedrinkfromvend()
                resetallvalues()
            else:
                Fivepay = input("Enter no. of $5 notes: ")
                if EnterInt(Fivepay.isnumeric(), "Enter a number please please for $5!"):
                    usercash = float((int(Tenpay) * 10) + (int(Fivepay) * 5))
                    if usercash > paymentno:
                        print(f"Please collect your change: ${usercash - paymentno:.2f}")
                        resetallvalues()
                    else:
                        Twopay = input("Enter no. of $2 notes: ")
                        if EnterInt(Twopay.isnumeric(), "Enter a number please please for $2!"):
                            usercash = float(int((Tenpay) * 10) + (int(Fivepay) * 5) + (int(Twopay) * 2))
                            if usercash > paymentno:
                                print(f"Please collect your change: ${usercash - paymentno:.2f}")
                                resetallvalues()
                            else:
                                print(errorMsg)
                                cancelofpurchase("Do you want to cancel the purchase? Y/N: ", "Please type 'Y' or 'N'")

# Get the customer drink list
def drinkgetfromcustomer(uschoice):
    drinkhold.append(f"{uschoice}")

# If paid remove the customer's drink list that has been dispense
def removedrinkfromvend():
    # How many types drinks there are
    # print(len(set(drinkhold)))
    for item in range((len(set(drinkhold)))):
        for rmv in drinkhold:
            drinks[rmv]['quantity'] = drinks[rmv]['quantity'] - drinkhold.count(rmv)
            while rmv in drinkhold:
                drinkhold.remove(f"{rmv}")

# Checking if the drink that the user wants is available
def customerdrinkselection (uschoice):
    if uschoice in drinks and drinks[uschoice]['quantity'] > 0:
        drinkscal()
        drinkgetfromcustomer(uschoice)
        print(f"No. of drinks selected = {drinkstotal}")
    elif uschoice == "0":
        pass
    else:
        print("I do not have that drink please choose another !")

# ================================================= Vender logic ============================================================================
def checkvenderoption(venderinput, errorMsg):
    while True:
        venderchoice = input(venderinput).strip()
        if venderchoice == "1" or venderchoice == "2" or venderchoice == "0":
            return venderchoice
        else:
            print(errorMsg)

flagforid = True
def checkifidistoolong(drinkidname):
    global flagforid
    if len(drinkidname) > 2:
        drinkidname = drinkidname[:2]
        print(f"The name is too long ! I'm going to take {drinkidname} ok ?")
        while True:
            yesnoreturn = checkyesorno("Enter 'Y' to continue or 'N' to exit: ", "Invalid input type 'Y' or 'N' !")
            if yesnoreturn == "Y":
                flagforid = False
                return drinkidname
            if yesnoreturn == "N":
                print("Try again then !")
                return yesnoreturn
    elif len(drinkidname) < 2:
        print(f"The name is too short !")
        return 0
    else:
        flagforid = False
        return drinkidname

def checkifdrinkexist(exist, errorMsg):
    while True:
        checkdrinkid = input(exist).strip().upper()
        if checkdrinkid in drinks:
            print(errorMsg)

        elif checkdrinkid == "0":
            #print("Goodbye !")
            return checkdrinkid
        else:
            newdrinkid = checkifidistoolong(checkdrinkid)
            if newdrinkid == "N":
                return newdrinkid
            else:
                return newdrinkid

flagfordesc = True
def descriptioncheck(desc):
    global flagfordesc
    desc = input(desc).strip().title()
    while True:
        if desc == "0":
            return "0"
        elif len(desc) > 13:
            desc = desc[:12]
            print(f"Your description for the drink is too long I'll take onlty {desc} is that ok ?")
            while True:
                yesornoturn = checkyesorno("Enter 'Y' to continue or else type 'N': ", "Invalid input type 'Y' or 'N' !")
                if yesornoturn == "Y":
                    print(desc)
                    return desc
                if yesornoturn == "N":
                    flagfordesc = False
                    # print("Goodbye !")
                    # print(f"this is yesornoturn: {yesornoturn}")
                    return yesornoturn
        elif len(desc) < 3:
            print(f"Your description for the drink is too short please type more")
        else:
            flagfordesc = False 
            return desc

# checking of how many decimals the vender put
def checkhowmanydecimals(originalprice):
    pricestring = str(originalprice)

     # Check if a decimal point exists
    if '.' in pricestring:
    # Split the string by the decimal point and return the length of the second part
        return len(pricestring.split('.')[1])
    else:
    # If no decimal point, return 0
        return 0

def upordown(venerinput, errormsg):
    while True:
        if venerinput == "U" or venerinput == "D":
            return venerinput
        else:
            print(errormsg)
            #return None

def checkifpriceiszeroorneg(originalprice, errorMsg):
    if originalprice <= 0:
        print(errorMsg)
        return None
    else:
        return originalprice

def roundingofpricedown(originalprice):
    rounddown = int(originalprice * 10)/10
    return float(rounddown)

def roundingofpriceup(originalprice):
    roundup = int(originalprice * 10) / 10
    if (originalprice * 10) % 1 != 0:
        roundup += 0.1
    return float(roundup)

flagforprice = True
def confirmationofprice(venderinputofprice):
    global flagforprice
    while flagforprice:
        roundup = roundingofpriceup(venderinputofprice)
        rounddown = roundingofpricedown(venderinputofprice)
        deci = checkhowmanydecimals(venderinputofprice)
        print (f"Sorry your price has {deci} decimal places. Please type 'D' for {str(rounddown)}.")
        print(f"Or 'U' for {str(roundup)}.")
        checkvenderchoice = upordown(input("Enter choice: ").upper(), "Type 'U' or 'D' please !")
        print(checkvenderchoice)
        if checkvenderchoice == "U":
            flagforprice = False
            return roundup
        if checkvenderchoice == "D":
            flagforprice = False
            return rounddown

def checkingquantity():
    pass

def processofaddingnewdrink():
    flagforid = True
    flagfordesc = True
    flagforprice = True

    #Id Check
    while flagforid:
        getdrinkid = checkifdrinkexist("Enter drink id: ", "Drink id exists !")
        print(f"This is get id: {getdrinkid}")

        if getdrinkid == "0":
            return "0"
        
        if getdrinkid == "N":
            continue

        flagforid = False
    
    # Desc Check after id pass
    while flagfordesc:
        getdesc = descriptioncheck("Enter description of drink: ")
        print(f"This is get desc: {getdesc}")

        if getdesc == "0":
            return "0"
        
        if getdesc == "N":
            continue

        flagfordesc = False
    
    # Price check
    while flagforprice:
        pric = input("Enter price: ")
        if pric == "0":
            return
        
        if pric == "N":
            continue
        
        tempprice = EnterFloat(pric, "Please enter a price !")
        if tempprice is not None:
            continue

        price = checkifpriceiszeroorneg(tempprice, "Please enter more than 0 !")
        if price is not None:
            getprice = confirmationofprice(price)
            print(f"This is get price: {getprice}")

        flagforprice = False


def add_drink_type(drink_id, description, price, quantity):
    pass

def replenish_drink(drink_id, quantity):
    pass

# Main loop
while True:
    vendOrUser = checkyesorno("Are you a vendor (Y/N)?: ", "Please enter a valid input ! </3")
    loop = 3
    if vendOrUser == "N":
        Drinkmenu()
        while True and loop == 3:
            customerdrinkselection(druschoice("Enter Choice: ", "Enter a drink name that is in the menu !"))
            if userchoice in drinks:
                drinkamt(userchoice)
            if userchoice == "0":
                while True:
                    if needpay != 0 and drinkstotal != 0:
                        drinkpayment(needpay, "Not enough ! Please pay or exit !")
                    else:
                        print("Thank you and Goodbye !")
                        loop = 0
                        break

    if vendOrUser == "Y":
        VenderMenu()
        venderoption = checkvenderoption("Enter choice: ", "Please center a valid input ! >:( ").strip()
        
        # add drink type
        if venderoption == "1":
            print("If you do not wish to add press '0' !")
            processofaddingnewdrink()

        # replenish drink
        if venderoption == "2":
            pass
        # exit
        if venderoption == "0":
            print("Goodbye V-vendor-san! u///u")
            break
