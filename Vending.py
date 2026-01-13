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
def Drinkmenu(venderoruser):
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

    if venderoruser == "N":
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
    drinks[uschoice]['quantity'] -= 1

# If paid remove the customer's drink list that has been dispense
def removedrinkfromvend():
    # How many types drinks there are
    # print(len(set(drinkhold)))
    for item in range((len(set(drinkhold)))):
        for rmv in drinkhold:
            drinks[rmv]['quantity'] = drinks[rmv]['quantity'] - drinkhold.count(rmv)
            while rmv in drinkhold:
                drinkhold.remove(f"{rmv}")

# Check if customer keeps getting same drink even if the quantity is 1
def checkcustomerdrinklist(customerdrinkchoice):
    if customerdrinkchoice not in drinkhold:
        return True

    if drinks[customerdrinkchoice]['quantity'] >= drinkhold.count(customerdrinkchoice):
        return True
    
    return False

# Checking if the drink that the user wants is available
def customerdrinkselection (uschoice):
    if uschoice in drinks and drinks[uschoice]['quantity'] > 0 and checkcustomerdrinklist(uschoice):
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
        return "N"
    else:
        flagforid = False
        return drinkidname

def checkifdrinkexist(venderinput, exist, errorMsg):
    while True:
        checkdrinkid = input(exist).strip().upper()

        if checkdrinkid == "0":
            return "0"

        if venderinput == "1":
            if checkdrinkid in drinks:
                print(errorMsg)
                continue
            
            newdrinkid = checkifidistoolong(checkdrinkid)
            if newdrinkid == "N":
                continue
            return newdrinkid
        
        if venderinput == "2":
            if checkdrinkid in drinks:
                return checkdrinkid
            else:
                print(errorMsg)
                continue

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
            return "N"
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
            return None

def checkifpriceiszeroorneg(originalprice, errorMsg):
    while True:
        if originalprice <= 0:
            print(errorMsg)
            return None
        else:
            return originalprice

def roundingofpricedown(originalprice):
    return math.floor(originalprice * 10) / 10

def roundingofpriceup(originalprice):
    return math.ceil(originalprice * 10) / 10

flagforprice = True
def confirmationofprice(venderinputofprice):
    while flagforprice:
        roundup = roundingofpriceup(venderinputofprice)
        rounddown = roundingofpricedown(venderinputofprice)
        deci = checkhowmanydecimals(venderinputofprice)
        if deci == 1:
            return venderinputofprice
        else:
            print (f"Sorry your price has {deci} decimal places. Please type 'D' for {str(rounddown)}.")
            print(f"Or 'U' for {str(roundup)}.")
            checkvenderchoice = upordown(input("Enter choice: ").upper(), "Type 'U' or 'D' please !")
            print(checkvenderchoice)
            if checkvenderchoice == "U":
                return roundup
            if checkvenderchoice == "D":
                return rounddown

flagforquantity = True
def maximuminvendingmachine(enternoofdrinknumber):
    if enternoofdrinknumber == 0:
        return "0"
    if enternoofdrinknumber is None:
        return None
    if enternoofdrinknumber < 0:
        print("Quantity number invalid !")
        return "N"
    if enternoofdrinknumber > 50:
        print("Vending Machine can only hold maximum 50 drinks !")
        return "N"
    else:
        return enternoofdrinknumber

def checkingquantity(idofdrink, noofdrinksadding):
    current_quantity = drinks[idofdrink]['quantity']

    if noofdrinksadding == 0:
        return "0"
    
    else:
        if current_quantity > 5:
            print("No need to replenish. Quantity is greater than 5.")
            return None

        if current_quantity + noofdrinksadding > 50:
            print("Too many drinks added! Max capacity is 50.")
            return None

    return current_quantity + noofdrinksadding

def add_drink_type(drink_id, description, price, quantity):
    if drink_id != None and description != None and price != None and quantity != None:
            drinks[drink_id] = {
        "description": description,
        "price": price,
        "quantity": quantity
    }

def processofaddingnewdrink(venderinput):
    flagforid = True
    flagfordesc = True
    flagforprice = True
    flagforquantity = True

    #Id Check
    while flagforid:
        getdrinkid = checkifdrinkexist(venderinput, "Enter drink id: ", "Drink id exists !")
        # print(f"This is get id: {getdrinkid}")

        if getdrinkid == "0":
            return None
        
        if getdrinkid == "N":
            continue

        flagforid = False
    
    # Desc Check after id pass
    while flagfordesc:
        getdesc = descriptioncheck("Enter description of drink: ")
        # print(f"This is get desc: {getdesc}")

        if getdesc == "0":
            return None
        
        if getdesc == "N":
            continue

        flagfordesc = False
    
    # Price check
    while flagforprice:
        pric = input("Enter price: ")

        if pric == "0":
            return None
        
        if pric == "N":
            continue

        temppric = EnterFloat(pric, "Please enter a price")
        if temppric is None:
            continue
        
        price = checkifpriceiszeroorneg(temppric, "Please enter more than 0 !")
        if price is None:
            continue

        getprice = confirmationofprice(price)
        # print(f"This is get price: {getprice}")
        flagforprice = False

    # Quantity check
    while flagforquantity:
        quantity = maximuminvendingmachine(EnterInt(input("Enter quantity: "), "Please input a number !"))

        if quantity is None:
            continue

        if quantity == "N":
            continue

        if quantity == "0":
            return None
        
        # print(f"This is the quantity {quantity}")
        flagforquantity = False
    
    return getdrinkid, getdesc, getprice, quantity

def replenish_drink(drink_id, quantity):
    if drink_id != None and quantity != None:
        drinks[drink_id]['quantity'] = quantity
        print(f"Updated {drink_id} quantity to {quantity}\n")

def replenishdrinkprocess(venderinput):
    last_drink = None
    last_quantity = None

    while True:
        drink_id = checkifdrinkexist(venderinput, "Enter drink id: ", "Drink id does not exist!")
        if drink_id == "0":
            print("Goodbye!")
            break

        while True:
            add_quantity = EnterInt(input("Enter quantity: ").strip(), "Enter a number!")
            
            if add_quantity is None:
                continue
            
            if add_quantity == 0:
                print("Canceled replenishment for this drink.\n")
                break

            new_quantity = checkingquantity(drink_id, add_quantity)
            if new_quantity is None:
                continue

            replenish_drink(drink_id, new_quantity)
            last_drink = drink_id
            last_quantity = new_quantity
            break
    
    return last_drink, last_quantity

# Main loop
while True:
    vendOrUser = checkyesorno("Are you a vendor (Y/N)?: ", "Please enter a valid input ! </3")
    loop = 3
    if vendOrUser == "N":
        Drinkmenu(vendOrUser)
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
            result = processofaddingnewdrink(venderoption)

            if result is None:
                print("No drink added")
            else:
                drink_id, description, price, quantity = result
                add_drink_type(drink_id, description, price, quantity)
                print(f"Drink has been successfully added {description}!")

        # replenish drink
        if venderoption == "2":
            Drinkmenu(vendOrUser)
            print("Enter a drink id to replenish or type '0' to exit")
            
            updated_drink, updated_quantity = replenishdrinkprocess(venderoption)
            if updated_drink is not None and updated_quantity is not None:
                replenish_drink(updated_drink, updated_quantity)
            
        # exit
        if venderoption == "0":
            print("Goodbye V-vendor-san! u///u")
