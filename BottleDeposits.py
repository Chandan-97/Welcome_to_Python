def getcountone():
    var = int(input("Enter number of type  1 containers: "))
    if var < 0:
        print("Enter positive value !")
        getcountone()
    return var

def getcounttwo():
    var = int(input("Enter number of type 2 containers: "))
    if var < 0:
        print("Enter positive value !")
        getcounttwo()
    return var

def cashback():
    type1  = getcountone()
    type2 = getcounttwo()
    rupees = 0.1 * type1 + 0.25*type2
    amt = round(rupees, 2)
    print("Cashback equals : $" + str(amt))

cashback()