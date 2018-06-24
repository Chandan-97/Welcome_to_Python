def getcost():
    cost = float(input("Enter cost of meal: "))
    if cost < 0:
        print("Enter valid cost !")
        getcost()
    return cost

def showbill():
    cost = getcost()
    tax = 0.3*cost
    tip = 0.18*cost
    print("Meal  :   " +str(round(cost, 2)) + "\nTax   :  " + str(round(tax, 2)) + "\nTip   :  " + str(round(tip, 2)))
    print("---------------" + "\nTotal :  " + str(round((cost+tax+tip), 2)))

showbill()