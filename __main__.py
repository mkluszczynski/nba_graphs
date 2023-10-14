import os

from nba.NBARepository import NBARepository
from nba.NBAService import NBAService
from nba.NBAGraph import NBAGraph

file = open("data/nba_salaries.csv")

nbaRepo = NBARepository(file)
nbaService = NBAService(nbaRepo)
nbaGraph = NBAGraph(nbaService)

commands = [
    {"title": "Exit", "function": exit},
    {"title": "Average salary for position", "function": nbaGraph.showAverageSalaryForPosition},
    {"title": "Average salary for team", "function": nbaGraph.showAverageSalaryForTeam},
    {"title": "Average age for team", "function": nbaGraph.showAverageAgeForTeam},
    {"title": "Average points per game for team", "function": nbaGraph.showAveragePointsPerGameForTeam},
    {"title": "Sum of points for team", "function": nbaGraph.showSumPointsPerGameForTeam},
    {"title": "Salary per minute for player", "function": nbaGraph.showBestSalaryPerMinute}
]

while(True):
    for index, command in enumerate(commands):
        print(str(index) + ". " + command["title"])

    user_input = int(input("Select graph: "))
    commands[user_input]["function"]()
    os.system("clear")

