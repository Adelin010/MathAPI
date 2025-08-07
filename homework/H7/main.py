
# Setting up the PYTHONPATH to use the imports
import sys, os 


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.utils import clip
from H7.report.report import generate_report


def filter_file() -> None:
    FILE="students.txt"
    OUT="filtered.txt"
    students: list[str] = []
    with open(FILE, 'r') as file:
        student = file.readline()
        while student:
            if student[0] in 'AEIOU':
                students.append(student)
            student = file.readline()

    with open(OUT, 'w') as file:
        file.write("".join(students))


def rev() -> None:
    FILE="log.txt"
    REV="reversed.txt"

    data: str = ''
    with open(FILE, 'r') as file:
        data = file.read()
        # reset the pointer to the beginning
        file.seek(0)
    
    with open(REV, 'w') as file:
        file.write(data[::-1])


def report_disp() -> None:
    clip(generate_report({"Laura": 79, "Alex": 85, "John": 90, "Alec": 88})
)



if __name__ == "__main__":
    x = int(input("Insert the function you wanna check, range [1-3]: "))
    match x:
        case 1:
            filter_file()
        case 2:
            rev()
        case 3:
            report_disp()