# Setting up the PYTHONPATH to use the imports
import sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import clip

def immutable():

    # id() -> returns the identity of an object which is guaranteed to be unique 
    # means 2 different objects will have different addresses
    a = 10 
    addr1 = id(a)


    # because each number is treated as an Object in python (stored in Heap)
    # and the variable a references them it means the addresses in memory are differents    
    a = 20 
    print(id(a) == addr1)

    # Also, although the variables have the same value normally if only the value had been stored
    # The addresses would be different (being that the variables are stored in different regions) 
    # yet here they don't only get the value, but reference the object Number(30) from Heap => same address
    b, c = 30, 30
    print(id(b) == id(c))
    
# leap year divided by 4
# !!EXCEPTION!! the century years (eg. 2000, 1900) must be divided by 400 
def leap_year() -> None:
    year = int(input("Enter the year to check if it's a leap year: "))
    if year/100 == year // 100:
        if year % 4 == 0 and year % 400 == 0:
            clip("Leap year...")
            return
    else:
        if year % 4 == 0:
            clip("Lear year...")
            return
    
    clip("Not a leap year...")
    

def ternary() -> None:
    x = int(input("Enter a number to check if positive/negative: "))
    clip(True if x >= 0 else False)

def boolean():
    x, y, z = 5, 0, -3
    print("All 3 greater then 0")
    clip(True if x >= 0 and y >= 0 and z >= 0 else False)
    print("Al least one equal to 0")
    clip(True if x == 0 or y == 0 or z == 0 else False)
    print("None negative")
    clip(True if x >= 0 and y >= 0 and z >= 0 else False)

def type_conv():
    x, y, z = 100, -30, 0
    print("Float/ Int/ Boolean conversion")
    clip(f"Float: {x/5}  Int: {int(x/5)}  Bool: {bool(x/5)}")
    print("Identity check where the results are mathematicaly the same")
    clip(f"Float div with conversion: {id(int(x/10))} \nInt div: {id(x//10)} \nAddition 10 for z: {id(z+10)}")

if __name__ == "__main__":
    x = int(input("Insert the function you wanna check, range [1-5]: "))
    match x:
        case 1:
            immutable()
        case 2:
            leap_year()
        case 3:
            ternary()
        case 4:
            boolean()
        case 5:
            type_conv()


