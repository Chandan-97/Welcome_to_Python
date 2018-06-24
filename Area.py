def getLength():
    length = float(input("Enter length (in metres): "))
    if length < 0:
        print("Length cannot be negative..!")
        getLength()
    return length   



def getBreadth():
    breadth: float = float(input("Enter length (in metres): "))
    if breadth < 0:
        print("Breadth cannot be negative..!")
        getBreadth()
    return breadth


def solve():
    l = getLength()
    b = getBreadth()
    print("Area of the room is: " + str(l * b) + " sq metre")


solve()
