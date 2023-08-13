import random


def my_menu():
    while True:
        print(""
              "_________Menu_________\n"
              "Start a match       S\n"
              "Exit                X\n"
              "\n")
        user_input = str.upper(input("Enter a letter: "))
        match user_input:
            case 'S':
                team1 = input("Enter First Team: ")
                team2 = input("Enter Second Team: ")
                start_match(team1, team2)
            case 'X':
                return
            case _:
                invalid_input()


def pause():
    try:
        input("\n\nPress any key to continue")
    except KeyboardInterrupt:
        pass


def invalid_input():
    try:
        input("\n\nInvalid Input!!\n Press any key to retry\n")
    except KeyboardInterrupt:
        pass


def start_match(t1, t2):
    print(f"Match has been started between {t1} and {t2}.")
    pause()
    clear()


def toss():
    t = random.randint(0, 1)
    return 0 if t < 0.5 else 1


def clear():
    print('\n ' * 20)
