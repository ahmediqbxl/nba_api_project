# https://github.com/swar/nba_api
# run with flask using python -m flask run

from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playercareerstats, playerfantasyprofile, playerdashboardbylastngames
from nba_api.stats.static import players, teams

def get_active_players():
    """Get all active players in the NBA."""
    active_players = players.get_active_players()
    return active_players 

def get_all_players():
    """Get all players in NBA history"""
    all_players = players.get_players()
    return all_players

def get_player_id_from_name(full_name: str):
    """Get player ID from name"""
    player = players.find_players_by_full_name(full_name)
    return player[0]['id']

def get_teams():
    """Get all teams in the NBA."""
    all_teams = teams.get_teams()
    return all_teams

def get_career_stats(full_name: str):
    """Get stats of a player"""
    player_id = get_player_id_from_name(full_name)
    stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    return stats

def get_todays_scoreboard():
    """Get today's scoreboard"""
    games = scoreboard.ScoreBoard()
    return games

def get_fantasy_stats(full_name: str):
    player_id = get_player_id_from_name(full_name)
    stats = playerfantasyprofile.PlayerFantasyProfile(player_id=player_id)
    return stats

def get_player_dashboard_by__last_n_games(full_name: str, last_games: str):
    player_id = get_player_id_from_name(full_name)
    stats = playerdashboardbylastngames.PlayerDashboardByLastNGames(player_id=player_id, last_n_games=last_games)
    return stats

# print(get_career_stats("Nikola Jokic").get_dict())
print(get_player_dashboard_by__last_n_games('Nikola Jokic', '5').get_dict())