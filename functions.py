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
                return
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
    team1, team2 = '', ''
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

    # Second Parameter is toss winner

    if toss():

        start_match(team2, team1)
        return
    else:

        start_match(team1, team2)
        return


def start_match(t1, t2):
    ballers, batters = [], []
    print(f'{t2} won the toss!\n'
          'Press 0     to Ball\n'
          'Press 1     to Bat \n')
    user_input = str(input("Select: "))
    match user_input:
        case '0':
            print(f'{t2} decided to Ball First!')
            file = first_three_Letters(t2) + 'Ball'
            ballers = load_ballers(file)
            file = first_three_Letters(t1) + 'Bat'
            batters = load_batters(file)

        case '1':
            print(f'{t2} decided to Bat First!')
            file = first_three_Letters(t2) + 'Bat'
            batters = load_batters(file)
            file = first_three_Letters(t1) + 'Ball'
            ballers = load_ballers(file)
        case _:
            print(f'{t2} decided to Bat First!')
            file = first_three_Letters(t2) + 'Bat'
            batters = load_batters(file)
            file = first_three_Letters(t1) + 'Ball'
            ballers = load_ballers(file)

    print(f"Match has been started between {t1} and {t2}.")
    pause()
    clear()
    play(batters, ballers)


def play(batters, ballers):
    over = 0
    batters[0].is_on_strike = True
    ballers[over].is_balling = True
    print('Match has Started!!\n '
          f'It\'s {batters[0].first_name} {batters[0].last_name} Verses {ballers[0].first_name} {ballers[0].last_name}')

    scoring(ballers, batters, over)  # Working Perfectly till here


def scoring(ballers, batters, over):
    playing_batters = [batters[0], batters[1]]  # Here is  an issue, please check
    option = scoring_menu()
    total_wickets, total_runs, extra_runs = 0, 0, 0
    if ballers[over].no_of_balls > 6:
        over += 1
    match option:
        case 'O':
            total_wickets += 1
            ballers[over].no_of_balls += 1
            playing_batters[0].balls_played += 1
            playing_batters[0].is_on_strike = False
            out = out_menu()
            match out:
                case 'R':
                    r = input("How many runs were taken before run out: ")
                    total_runs += r
                    playing_batters[0].runs += r
                    playing_batters.append(batters[total_wickets + 1])
                    if r % 2 == 0:
                        playing_batters.pop(playing_batters[0])
                        playing_batters[1].is_on_strike = True
                        playing_batters.reverse()

                    else:
                        playing_batters.pop(playing_batters[1])
                        playing_batters[1].is_on_strike = True
                        playing_batters.reverse()
                case 'B':
                    playing_batters.append(batters[total_wickets + 1])
                    playing_batters.pop(playing_batters[0])
                    playing_batters[1].is_on_strike = True
                    playing_batters.reverse()

        case 'B':
            r = int(print('Was it a six or four (Enter number): '))
            playing_batters[0].runs += r
            total_runs += r
            ballers[over].no_of_balls += 1
            playing_batters[0].balls_played += 1
        case 'N':
            ballers[over].no_of_balls += 1
            total_runs += 1
            extra_runs += 1
        case 'D':
            ballers[over].no_of_balls += 1
        case 'W':
            extra_runs += 1


def display_scores(total_wickets, total_runs, extra_runs):
    print(f'{total_runs}-{total_wickets}'
          f'Extras: {extra_runs}')


def out_menu():
    print('\n\n')
    print("--------------------------------\n"
          "Press R for Run out\n"
          "Press B for Bowled\n"
          )
    user_input = str.upper(input('Enter a Letter: '))
    return user_input


def scoring_menu():
    print('\n\n')
    print("--------------------------------\n"
          "Press O for Out\n"
          "Press B for Boundary\n"
          "Press N for No Ball\n"
          "Press D for Dot Ball\n"
          "Press W for Wide Ball\n")
    user_input = str.upper(input('What happened on this Ball: '))
    return user_input


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
    ws = wb[team]
    for r in range(2, 13):  # 2 to 12+1
        first_name = str(ws.cell(row=r, column=1).value)
        last_name = str(ws.cell(row=r, column=2).value)
        age = int(ws.cell(row=r, column=3).value)
        runs = int(ws.cell(row=r, column=4).value)
        balls_played = int(ws.cell(row=r, column=5).value)
        is_on_strike = bool(ws.cell(row=r, column=6).value)
        is_batting = bool(ws.cell(row=r, column=7).value)
        batters.append(Batter(first_name, last_name, age, runs, balls_played, is_on_strike, is_batting))
        return batters


def clear():
    os.system('cls')


def find_bat(text):  # function to find "bat" in the string
    if text.find("bat") != -1 or text.find("Bat") != -1:
        return "Yes"
    else:
        return "No"


def find_ball(text):  # function to find "ball" in the string
    if text.find("ball") != -1 or text.find("Ball") != -1:
        return "Yes"
    else:
        return "No"


def first_three_Letters(string):
    return str(string[:3])
