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
    print("\n\n"
          "________Teams_________\n"
          "Pakistan            P\n"
          "India               I\n"
          "\n\n")
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
    print(f'\n\n{t2} won the toss!\n'
          'Press 0     to Ball\n'
          'Press 1     to Bat \n')
    user_input = str(input("Select: "))
    match user_input:
        case '0':
            print(f'\n\n{t2} decided to Ball First!\n\n')
            file = first_three_Letters(t2) + 'Ball'
            ballers = load_ballers(file)
            file2 = first_three_Letters(t2) + 'Bat'
            pass_batters = load_batters(file2)
            file = first_three_Letters(t1) + 'Bat'
            batters = load_batters(file)
            file2 = first_three_Letters(t1) + 'Ball'
            pass_ballers = load_ballers(file2)

        case '1':
            print(f'\n\n{t2} decided to Bat First!\n\n')
            file = first_three_Letters(t2) + 'Bat'
            file2 = first_three_Letters(t2) + 'Ball'
            batters = load_batters(file)
            pass_ballers = load_ballers(file2)
            file = first_three_Letters(t1) + 'Ball'
            file2 = first_three_Letters(t1) + 'Bat'
            ballers = load_ballers(file)
            pass_batters = load_batters(file2)

        case _:
            print(f'\n\n{t2} decided to Bat First!\n\n')
            file = first_three_Letters(t2) + 'Bat'
            file2 = first_three_Letters(t2) + 'Ball'
            batters = load_batters(file)
            pass_ballers = load_ballers(file2)
            file = first_three_Letters(t1) + 'Ball'
            file2 = first_three_Letters(t1) + 'Bat'
            ballers = load_ballers(file)
            pass_batters = load_batters(file2)

    print(f"\n\nMatch has been started between {t1} and {t2}.")
    clear()
    play1(batters, ballers, pass_batters, pass_ballers)


def play1(batters, ballers, pass_batters, pass_ballers):
    over = 0
    batters[0].is_on_strike = True
    ballers[over].is_balling = True
    print(f'It\'s {batters[0].first_name} {batters[0].last_name} Verses {ballers[0].first_name} {ballers[0].last_name}')

    scoring1(ballers, batters, over, pass_batters, pass_ballers)


def scoring1(ballers, batters, over, pass_batters, pass_ballers):
    playing_batters = [batters[0], batters[1]]
    total_wickets, total_runs, extra_runs = 0, 0, 0
    while True:
        option = scoring_menu()
        if ballers[over].no_of_balls > 6:
            over += 1
        match option:
            case 'O':
                total_wickets += 1
                ballers[over].wickets += 1
                ballers[over].no_of_balls += 1
                playing_batters[0].balls_played += 1
                playing_batters[0].is_on_strike = False
                if total_wickets < 10:
                    playing_batters.append(batters[total_wickets + 1])
                    playing_batters[2].is_on_strike = True
                out = out_menu()
                match out:
                    case 'R':
                        r = int(input("How many runs were taken before run out: "))
                        total_runs += r
                        playing_batters[0].runs += r
                        ballers[over].runs_given += r
                        if r % 2 == 0:
                            playing_batters.pop(0)
                            playing_batters.reverse()

                        else:
                            playing_batters.pop(1)
                            playing_batters.reverse()
                    case 'B':  # this B is for Bowled
                        playing_batters.pop(0)
                        playing_batters.reverse()

            case 'B':  # This B is for Boundary
                r = int(input('Was it a six or four (Enter number): '))
                playing_batters[0].runs += r
                total_runs += r
                ballers[over].no_of_balls += 1
                playing_batters[0].balls_played += 1
                ballers[over].runs_given += r
            case 'N':
                r = int(input("How many runs were made on this NO Ball: "))
                total_runs += r + 1
                extra_runs += 1
                ballers[over].runs_given += r + 1
                print("It\'s a Free Hit")
            case 'D':
                ballers[over].no_of_balls += 1
            case 'W':
                total_runs += 1
                extra_runs += 1
            case 'R':
                r = int(input("How many runs were made on this Ball (1, 2 or 3): "))
                ballers[over].no_of_balls += 1
                ballers[over].runs_given += r
                playing_batters[0].runs += r
                playing_batters[0].balls_played += 1
                total_runs += r
                if r % 2 != 0:
                    playing_batters.reverse()
            case 'E':
                return
        if ballers[over].no_of_balls > 5:
            over += 1
            if over > 4 or total_wickets == 10:
                print("\nThe Innings has ended!\n")
                print_all(batters, ballers)
                play2(pass_batters, pass_ballers)
                return

            print("Over ended!!\n"
                  f"{ballers[over].first_name} {ballers[over].last_name}\'s over has started.\n")
        if total_wickets < 10:
            display_scores(total_wickets, total_runs, extra_runs, ballers[over], playing_batters[0], playing_batters[1])
        else:
            display_scores1(total_wickets, total_runs, extra_runs, ballers[over], playing_batters[0])
            print("\nThe Innings has ended!\n")
            print_all(batters, ballers)
            play2(pass_batters, pass_ballers)
            return


def play2(batters, ballers):
    over = 0
    batters[0].is_on_strike = True
    ballers[over].is_balling = True
    print(f'It\'s {batters[0].first_name} {batters[0].last_name} Verses {ballers[0].first_name} {ballers[0].last_name}')

    scoring2(ballers, batters, over)


def scoring2(ballers, batters, over):
    playing_batters = [batters[0], batters[1]]
    total_wickets, total_runs, extra_runs = 0, 0, 0
    while True:
        option = scoring_menu()
        if ballers[over].no_of_balls > 6:
            over += 1
        match option:
            case 'O':
                total_wickets += 1
                ballers[over].wickets += 1
                ballers[over].no_of_balls += 1
                playing_batters[0].balls_played += 1
                playing_batters[0].is_on_strike = False
                if total_wickets < 10:
                    playing_batters.append(batters[total_wickets + 1])
                    playing_batters[2].is_on_strike = True
                out = out_menu()
                match out:
                    case 'R':
                        r = int(input("How many runs were taken before run out: "))
                        total_runs += r
                        playing_batters[0].runs += r
                        ballers[over].runs_given += r
                        if r % 2 == 0:
                            playing_batters.pop(0)
                            playing_batters.reverse()

                        else:
                            playing_batters.pop(1)
                            playing_batters.reverse()
                    case 'B':  # this B is for Bowled

                        playing_batters.pop(0)
                        playing_batters.reverse()

            case 'B':  # This B is for Boundary
                r = int(input('Was it a six or four (Enter number): '))
                playing_batters[0].runs += r
                total_runs += r
                ballers[over].no_of_balls += 1
                playing_batters[0].balls_played += 1
                ballers[over].runs_given += r
            case 'N':
                r = int(input("How many runs were made on this NO Ball: "))
                total_runs += r + 1
                extra_runs += 1
                ballers[over].runs_given += r + 1
                print("It\'s a Free Hit")
            case 'D':
                ballers[over].no_of_balls += 1
            case 'W':
                total_runs += 1
                extra_runs += 1
            case 'R':
                r = int(input("How many runs were made on this Ball (1, 2 or 3): "))
                ballers[over].no_of_balls += 1
                ballers[over].runs_given += r
                playing_batters[0].runs += r
                playing_batters[0].balls_played += 1
                total_runs += r
                if r % 2 != 0:
                    playing_batters.reverse()
            case 'E':
                break
        if ballers[over].no_of_balls > 5:
            over += 1
            if over > 4 or total_wickets == 10:
                print("\nThe Match has ended!\n")
                print_all(batters, ballers)
                return

            print("Over ended!!\n"
                  f"{ballers[over].first_name} {ballers[over].last_name}\'s over has started.\n")
        if total_wickets < 10:
            display_scores(total_wickets, total_runs, extra_runs, ballers[over], playing_batters[0], playing_batters[1])
        else:
            display_scores1(total_wickets, total_runs, extra_runs, ballers[over], playing_batters[0])
            print("\nThe Match has ended!\n")
            print_all(batters, ballers)
            return


def print_all(batters, ballers):
    print("Batting: \n\n")
    for i in range(0, len(batters)):
        print(f"{batters[i].first_name} {batters[i].last_name} ({batters[i].age} years old) "
              f" {batters[i].runs} on {batters[i].balls_played} balls\n\n")
    print("Balling: \n\n")
    for i in range(0, len(ballers)):
        print(f"{ballers[i].first_name} {ballers[i].first_name} ({ballers[i].age} years old) "
              f"Eco: {ballers[i].economy()} |  {ballers[i].wickets} - {ballers[i].runs_given}\n\n")


def display_scores(total_wickets, total_runs, extra_runs, baller, batter1, batter2):
    ballers_over = int(baller.no_of_balls / 6)
    ballers_balls = int(baller.no_of_balls % 6)  # ov.er will make over in the format Overs.balls
    print(f'{total_runs}-{total_wickets}\n'
          f'Extras: {extra_runs}\n\n'
          f'Batters: \n'
          f'{batter1.first_name} {batter1.last_name} : {batter1.runs}* - {batter1.balls_played}\n'
          f'{batter2.first_name} {batter2.last_name} : {batter2.runs} - {batter2.balls_played}\n'
          f'Ballers: \n'
          f'{baller.first_name} {baller.last_name} : {baller.wickets} - {baller.runs_given} '
          f'({ballers_over}.{ballers_balls})\n')

def display_scores1(total_wickets, total_runs, extra_runs, baller, batter1):
    ballers_over = int(baller.no_of_balls / 6)
    ballers_balls = int(baller.no_of_balls % 6)  # ov.er will make over in the format Overs.balls
    print(f'{total_runs}-{total_wickets}\n'
          f'Extras: {extra_runs}\n\n'
          f'Batters: \n'
          f'{batter1.first_name} {batter1.last_name} : {batter1.runs}* - {batter1.balls_played}\n'
          f'Ballers: \n'
          f'{baller.first_name} {baller.last_name} : {baller.wickets} - {baller.runs_given} '
          f'({ballers_over}.{ballers_balls})\n')


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
          "Press W for Wide Ball\n"
          "Press R for Runs Taken Between the Wicket\n"
          "Press E to  End match due to Rain\n")
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
