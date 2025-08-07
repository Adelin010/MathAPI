# Setting up the PYTHONPATH to use the imports
import sys, os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import clip
from random import randint

def currency_conv() -> None:
    data = [
        (100, 'USD', 'EUR', 0.83),
        (100, 'USD', 'CAD', 1.27),
        (100, 'CAD', 'EUR', 0.65)
    ]

    def results(t1: tuple, t2: tuple, t3: tuple) -> tuple:
        return (t1[0] * t1[len(t1)-1], t2[0] * t2[len(t2) -1], t3[0] * t3[len(t3) -1])

    res = results(*data)
    infos = [f"{dp[0]}{dp[1]} = {res}{dp[2]}" for dp, res in zip(data, res) ]
    clip("\n".join(infos))


def sum_odds() -> None:
    print("Sum of odds")
    clip(sum([i for i in range(101) if i & 1]))

def num_guessing_game() -> None:
    no = randint(1, 10)
    attempts = 3
    while attempts:
        x = int(input("Guess the number (between 1, 10): "))
        if x == no:
            clip("Guessed it, good job...")
            return 
        attempts -= 1

    clip(f"Lost the game, it was {no}...") 


def enum_list_items() -> None:
    fruits = ['apple', 'banana', 'cherry', 'date']
    res = [f"{idx+1}: {fr}({len(fr)}letters)" for idx, fr in enumerate(fruits)]
    clip('\n'.join(res))

def mutate_data() -> None:
    data = (
        ['2021-01-01', 20, 10],
        ['2021-01-02', 20, 18],
        ['2021-01-03', 10, 10],
        ['2021-01-04', 102, 100],
        ['2021-01-05', 45, 25]
    ) 

    # mutate
    max, max_idx = -10000, -1
    for idx, l in enumerate(data):
        max_idx
        diff = l[1] - l[2]
        if diff > max:
            max =  diff 
            max_idx = idx
        l.insert(1, diff)
    # find the date out
    data = [[str(k) for k in dp] for dp in data]
    clip(f"{'\n'.join([" ".join(dp) for dp in data])}\nThe date for the max: {data[max_idx][0]}")



if __name__ == "__main__":
    x = int(input("Insert the function you wanna check, range [1-5]: "))
    match x:
        case 1:
            currency_conv()
        case 2:
            sum_odds()
        case 3:
            num_guessing_game()
        case 4:
            enum_list_items()
        case 5:
            mutate_data()
