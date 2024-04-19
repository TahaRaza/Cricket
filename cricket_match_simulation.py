import functions as f
from MatchClass import Match


def main():
    """Loads teams from an Excel file, prompts for team selection,
       creates Team objects, simulates a match, and displays results."""

    from catboost import CatBoostRegressor
    import pandas as pd

    # Load the model
    path = "./catboost_model"
    # Load the model
    loaded_model = CatBoostRegressor()
    loaded_model.load_model(path)

    # Now you can use the loaded model for predictions or further analysis
    # Prepare your input data
    example_input = pd.DataFrame({'venue': ["Lahore"],
                                  'bat_team': ['Lahore Qalanders'],
                                  'bowl_team': ['Islamabad United'],
                                  'runs': [100],
                                  'wickets': [5],
                                  'overs': [10],
                                  'runs_last_5': [10],
                                  'wickets_last_5': [0],
                                  'striker': [100],
                                  'non-striker': [100]})

    # Make predictions
    example_prediction = loaded_model.predict(example_input)
    print(example_prediction[0])

    team_A, team_B = f.choose_team()
    match_type = f.choose_match_type()
    stadium_name = f.choose_location()

    match = Match(team1=team_A, team2=team_B, match_type=match_type, stadium=stadium_name)
    winner, scorecard = match.simulate_match()


if __name__ == "__main__":
    main()

# TO-DO
