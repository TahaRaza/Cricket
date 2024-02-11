import openpyxl
from TeamClass import Team  # Use lowercase for module names
from MatchClass import Match


def main():
    """Loads teams from an Excel file, prompts for team selection,
       creates Team objects, simulates a match, and displays results."""

    try:
        workbook = openpyxl.load_workbook('Teams.xlsx')
    except FileNotFoundError:
        print("Error: Teams.xlsx file not found.")
        return

    team_names = sorted([sheet.title for sheet in workbook.worksheets])

    display_team_choices(team_names)
    team_A_name = get_team_choice(team_names)
    team_names.remove(team_A_name)

    display_team_choices(team_names)
    team_B_name = get_team_choice(team_names)

    team_A = Team(team_A_name)
    team_B = Team(team_B_name)

    match = Match(team_A, team_B)
    match.simulate_match()

    # Show Match result Here


def display_team_choices(team_names):
    """Displays numbered options for team selection."""

    for i, team in enumerate(team_names, start=1):
        print(f"{i}: {team}")
    print()


def get_team_choice(team_names):
    """Prompts for team selection and validates input."""

    while True:
        choice = input(f"Enter team name (1-{len(team_names)}): ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(team_names):
                return team_names[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and", len(team_names))
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()

# Show Match Result
# Pick Type of Match i.e. No of Overs
