import functions as f
from MatchClass import Match
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose_teams')
def choose_teams():
    # Fetch team options from logic in functions.py
    team_options = f.get_team_options()
    return render_template('choose_teams.html', teams=team_options)


@app.route('/choose_options', methods=['POST'])
def choose_options():
    team_A = request.form['team_A']
    team_B = request.form['team_B']
    # Get other options from form data
    match_type = request.form['matchType']
    stadium_name = request.form['stadium']

    match = Match(team1=team_A, team2=team_B, match_type=match_type, stadium=stadium_name)
    winner, scorecard = match.simulate_match()

    return render_template('results.html', winner=winner, scorecard=scorecard)
