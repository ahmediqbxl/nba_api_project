# https://github.com/swar/nba_api

from nba_api.stats.static import players
from nba_api.stats.static import teams
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_active_players():
    '''Get all active players in the NBA.'''
    active_players = players.get_active_players()
    return active_players 

@app.route("/")
def get_teams():
    '''Get all teams in the NBA.'''
    teams = teams.get_teams()
    return teams