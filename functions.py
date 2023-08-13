import random
import os
from openpyxl import load_workbook
from BallerClass import Baller
from BallerClass import Batter


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


# not completed

def start_match(t1, t2, toss_winner):
    print(f'{toss_winner} won the toss!\n'
          'Press 0     to Ball\n'
          'Press 1     to Bat \n')
    user_input = str(input("Select: "))
    match user_input:
        case '0':
            print(f'{toss_winner} decided to Ball First!')
            if toss_winner == 'Pakistan':
                load_ballers('PakBall')
            else:
                load_ballers('IndBall')  # not completed

        case '1':
            print(f'{toss_winner} decided to Bat First!')
            if toss_winner == 'Pakistan':
                load_ballers('PakBat')
            else:
                load_ballers('IndBat')
        case _:
            print(f'{toss_winner} decided to Batt First!')
            if toss_winner == 'Pakistan':
                load_ballers('PakBat')
            else:
                load_ballers('IndBat')

    print(f"Match has been started between {t1} and {t2}.")
    pause()
    clear()


def toss():
    t = random.randint(0, 1)
    return 0 if t < 0.5 else 1


def load_ballers(team):
    ballers = []
    # Load the workbook
    wb = load_workbook('Teams.xlsx')
    # accessing first sheet by its name
    ws = wb[team]
    for r in range(2, 7):  # 2 to 6+1
        first_name = str(ws.cell(row=r, column=1).value)
        last_name = str(ws.cell(row=r, column=2).value)
        age = int(ws.cell(row=r, column=3).value)
        runs = int(ws.cell(row=r, column=4).value)
        balls_played = int(ws.cell(row=r, column=5).value)
        is_on_strike = bool(ws.cell(row=r, column=6).value)
        is_batting = bool(ws.cell(row=r, column=7).value)
        wickets = int(ws.cell(row=r, column=8).value)
        runs_given = int(ws.cell(row=r, column=9).value)
        is_balling = bool(ws.cell(row=r, column=10).value)
        no_of_balls = int(ws.cell(row=r, column=11).value)
        ballers.append(Baller(first_name, last_name, age, runs, balls_played, is_on_strike, is_batting,
                              wickets, runs_given, is_balling, no_of_balls))
        return ballers


def load_batters(team):
    batters = []
    # Load the workbook
    wb = load_workbook('Teams.xlsx')
    # accessing first sheet by its name 'Bat'
    ws = wb['Bat']
    for r in range(2, 13):  # 2 to 12+1
        first_name = str(ws.cell(row=r, column=1).value)
        last_name = str(ws.cell(row=r, column=2).value)
        age = int(ws.cell(row=r, column=3).value)
        runs = int(ws.cell(row=r, column=4).value)
        balls_played = int(ws.cell(row=r, column=5).value)
        is_on_strike = bool(ws.cell(row=r, column=6).value)
        is_batting = bool(ws.cell(row=r, column=7).value)
        batters.append(Batter(first_name, last_name, age, runs, balls_played, is_on_strike, is_batting))


def clear():
    os.system('clear')  # This doesn't work
