# Setting up the PYTHONPATH to use the imports
import sys, os 
from functools import reduce 
from math import prod 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import clip

type Numeric = int | float 

class AgeAboveLimit(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg 

    def __str__(self) -> str:
        return f"Error of an age above the limit\n{self.msg}"
    


class AgeBelowLimit(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg 

    def __str__(self) -> str:
        return f"Error of an age above the limit\n{self.msg}"

def calculate(*numbers: Numeric, operation:str='+') -> Numeric:
    if len(numbers) == 0:
        return 0 
    if len(numbers) == 1:
        return numbers[0]
    match operation:
        case '+':
            return sum(numbers)
        case '-':
            return reduce(lambda x, y: x-y, numbers )
        case '*':
            return prod(numbers)
        case '/':
            res = numbers[0]
            for num in numbers[1:]:
                if num == 0: continue 
                res /= num
            return res 
        case _:
            return 0
def custom_calc() -> None: 
    print("Use cases for the calculate function")
    clip(f"{'':>9}Call: calculate(operation='-'): {calculate(operation='-')}\n\
        Call: calculate(1): {calculate(1)}\n\
        Call: calculate(1, 2, 10, 4) : {calculate(1, 2, 10, 4)}\n\
        Call: calculate(1, 10, 8, operation='-'): {calculate(1, 10, 8, operation='-')}") 


def sort_students() -> None:
    names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]
    scores = [85, 92, 78, 81, 67]

    desc_above_80 = sorted([(name, score) for name, score in zip(names, scores) if score >= 80], key= lambda x: -x[1])
    clip(desc_above_80)

    




def check_age() -> None :
    age = input("Enter a age between 0-120: ")
    try:
        age_int = int(age)
        if age_int > 120:
            raise AgeAboveLimit("Age must be  below 120")
        if age_int < 0:
            raise AgeBelowLimit("Age must not be negative")
        
        clip("Age is validated...")

    except ValueError:
        clip("Value Error at conversion from string to integer")
    except AgeAboveLimit as above:
        clip(above)
    except AgeBelowLimit as below:
        clip(below)



if __name__ == "__main__":
    x = int(input("Insert the function you wanna check, range [1-3]: "))
    match x:
        case 1:
            custom_calc()
        case 2:
            sort_students()
        case 3:
            check_age()

