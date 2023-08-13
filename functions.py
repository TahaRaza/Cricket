import random
import os


def menu():
    while True:
        print(""
              "_________Menu_________\n"
              "Start a match       S\n"
              "Exit                X\n"
              "\n")
        user_input = str.upper(input("Enter a letter: "))
        match user_input:
            case 'S':
                match_starter()
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


def match_starter():
    global team1, team2
    clear()
    print(""
          "________Teams_________\n"
          "Pakistan            P\n"
          "India               I\n"
          "\n")
    tt = str.upper(input("Select First Team: "))
    match tt:
        case 'P':
            team1 = 'Pakistan'
        case 'I':
            team1 = 'India'
        case _:
            invalid_input()
            match_starter()

    tt = str.upper(input("Select Second Team: "))
    match tt:
        case 'P':
            team2 = 'Pakistan'
        case 'I':
            team2 = 'India'
        case _:
            invalid_input()
            match_starter()

    if toss():

        start_match(team1, team2, team1)
    else:

        start_match(team1, team2, team2)


def start_match(t1, t2, toss_winner):
    print(f'{toss_winner} won the toss!\n'
          'Press 0     to Ball\n'
          'Press 1     to Bat \n')
    user_input = str(input("Select: "))
    match user_input:
        case '0':
            print(f'{toss_winner} decided to Ball First!')
        case '1':
            print(f'{toss_winner} decided to Bat First!')
        case _:
            print(f'{toss_winner} decided to Batt First!')

    print(f"Match has been started between {t1} and {t2}.")
    pause()
    clear()


def toss():
    t = random.randint(0, 1)
    return 0 if t < 0.5 else 1


def clear():
    os.system('clear')  # This doesn't work
