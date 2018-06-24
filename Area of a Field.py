def getLength():
    length = float(input("Enter length (in feet): "))
    if length < 0:
        print("Length cannot be negative..!")
        getLength()
    return length



def getBreadth():
    breadth: float = float(input("Enter breadth (in feet): "))
    if breadth < 0:
        print("Breadth cannot be negative..!")
        getBreadth()
    return breadth


def solve():
    l = getLength()
    b = getBreadth()
    print("Area of the room is: " + str(l * b/43560) + " acres")


solve()
