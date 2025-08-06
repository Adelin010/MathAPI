import sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from H8.shape import Shape, Circle, Rectangle
from utils.utils import clip
from H8.bankAccount import BankAccount
from H8.notificationSystem import EmailNotification, SMSNotification

def main(): 

    c1 = Circle(12.0)
    c2 = Circle(13)
    r1 = Rectangle(5, 10)
    r2 = Rectangle(2, 4)
    circles = [c1 , c2]
    rectangles = [r1, r2]
    clip(c1.__doc__)

    print("Full information of the objects")
    for r, c in zip(rectangles, circles):
        clip(r)
        clip(c)

    # Bank Account
    clip("Task 2.")
    bank =  BankAccount()
    try:
        bank.balance = -10
    except Exception as e:
        print("EXCEPTION")
        print(e)
    
    bank.balance = 100
    bank.withdraw(30)
    print(f"Bank Balance: {bank.balance}")
    try:
        bank.deposite(-10)
    except Exception as e:
        print("EXCEPTION")
        print(e)
    
    bank.deposite(130)
    print(f"Bank Balance: {bank.balance}")

    clip("Task 3.")

    # Duck typing example
    for obj in [SMSNotification("1. SMS"), EmailNotification("1. Email"), SMSNotification("2. SMS")]:
        obj.send()




if __name__ == "__main__":
    main()