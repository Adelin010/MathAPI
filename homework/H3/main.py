import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import clip


def list_prep() -> None:
    numbers = [10, 20, 30, 40, 50]
    print("First Elem")
    clip(numbers[0])
    print("Last Elem")
    clip(numbers[-1])
    print("Middle Elem")
    clip(numbers[len(numbers)//2])

    # insert 
    numbers.append(60)
    print("Insert 60")
    clip(numbers)

    numbers.insert(1, 15)
    print("Insert 15 at index 1")
    clip(numbers)

    numbers.pop()
    print("Last number removed")
    clip(numbers)

    print("List Length")
    clip(len(numbers))

    print("Sorted list")
    clip(sorted(numbers, reverse=True))


def  change_word() -> None:
    sentence = input("Write a sentence: ")
    word = input("Input a word to be replaced: ")
    replacement = input("Input the word with whom to replace: ")
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i] == word:
            words[i] = replacement

    clip(' '.join(words))


def palindrom() -> None:

    word = input("Enter the word: ")
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            clip("Not a palindrom...")
            return 
    clip("Palindrom...")

def f_formating() -> None:
    name = "Alice"
    age = 30
    balance = 1234.56789
    membership_date = "2023-08-12"
    status = True

    print("1. Print Sentence with info")
    clip(f"Hallo, this is {name} which is {age} years old.\nThe balance of\
her card is {balance:>10.2f}\nmember since {membership_date} \
            \nActive member: {'Yes' if status else 'No'}")

    

if __name__ == "__main__":
    x = int(input("Insert the function you wanna check, range [1-4]: "))
    match x:
        case 1:
            list_prep()
        case 2:
            change_word()
        case 3:
            palindrom()
        case 4:
            f_formating()

