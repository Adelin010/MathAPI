# Setting up the PYTHONPATH to use the imports
import sys, os 
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import clip

def anagrams() -> None:
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    if Counter(word1) == Counter(word2):
        clip("They are anagrams...")
    else:
        clip("They are not...")


def inv_dict() -> None:
    grades = {
        "Alice": "A",
        "Bob": "B",
        "Charlie": "A",
        "Diana": "C"
    }

    res: dict[str, list] = {}
    for k, v in grades.items():
        if v not in res:
            res[v] = [k]
        else :
            res[v].append(k)
    
    clip(res)


def set_analysis() -> None:
    testing = {"Ana", "Bob", "Charlie", "Diana"}
    development = {"Charlie", "Eve", "Frank", "Ana"}
    devops = {"George", "Ana", "Bob", "Eve"}

    all_session = testing.intersection(development).intersection(devops)
    only_one_session = testing.difference(development).difference(devops)
    print("Are in all sessions")
    clip(all_session)

    print("Only in one session")
    clip(only_one_session)

    test_same_devep = testing.difference(development)
    print("All in testing are also in development")
    if len(test_same_devep) > 0:
        clip("Yes")
    else:
        clip("No")

    print("All attendees")
    clip(testing.union(development).union(devops))

    cpy_development = set([item for item in development])
    development = {}
    clip(f"Old development set: {development}\nNew development set: {cpy_development}") 

def data_compreh() -> None:
    
    sqrs = [item**2 for item in range(1, 11)]
    div7 = {item for item in range(1, 51) if item % 7 == 0}

    score = {"Alice": 85, "Bob": 59, "Charlie": 92}
    passed = {k:v for k, v in score.items() if v > 60}
    

    students = ["Michael", "David", "Liza"]
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    values = [True, False, True, False, False]

    res = { student : {weekday : val for weekday, val in zip(weekdays, values)} for student in students}
    
    print("List Squares")
    clip(sqrs)

    print("Set of divisible numbers with 7")
    clip(div7)

    print("Dict with scores bigger than 60")
    clip(passed)

    print("Double Dict Comprehension")
    clip(res)

if __name__ == "__main__":
    x = int(input("Insert the function you wanna check, range [1-4]: "))
    match x:
        case 1:
            anagrams()
        case 2:
            inv_dict()
        case 3:
            set_analysis()
        case 4:
            data_compreh()

