from nba.NBARepository import NBARepository
from nba.NBAService import NBAService
from nba.NBAGraph import NBAGraph

file = open("data/nba_salaries.csv")

nbaRepo = NBARepository(file)
nbaService = NBAService(nbaRepo)
nbaGraph = NBAGraph(nbaService)



for row in nbaService.getAverageSalaryForTeam():
    print(row)

# nbaGraph.showAverageSalaryForPosition()
# nbaGraph.showAverageSalaryForTeam()
# nbaGraph.showAverageAgeForTeam()
# nbaGraph.showAveragePointsPerGameForTeam()
# nbaGraph.showSumPointsPerGameForTeam()
