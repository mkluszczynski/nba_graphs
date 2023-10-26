from .consts.ConferenceData import CONF_DATA
from .NBARepository import NBARepository

class NBAService:

    nbaRepo: NBARepository

    def __init__(self, nbaRepo) -> None:
        self.nbaRepo = nbaRepo

    def getAverageSalaryForPosition(self) -> list[dict]:
        average_data = self.nbaRepo.find({"select": ["Position", "Salary", "Age"]})
        group_count = self.nbaRepo.countColumn("Position")

        average_list = []
        for g_count in group_count:

            average_item = {}
            young_sum = 0
            young_count = 0
            old_sum = 0
            old_count = 0

            for av_data in average_data:
                
                if int(av_data["Age"]) <= 25:
                    if av_data["Position"] == g_count["Position"]:
                        young_sum += int(float(av_data["Salary"])) 
                        young_count += 1
                else:
                    if av_data["Position"] == g_count["Position"]:
                        old_sum += int(float(av_data["Salary"]))
                        old_count += 1

            print(old_count)
            print(young_count)
            average_item = {"Position": g_count["Position"], "Age": [{"Age": "Old", "Average": old_sum // (old_count if old_count != 0 else 1)}, {"Age": "Young", "Average": young_sum // (young_count if young_count != 0 else 1)}]}
            average_list.append(average_item) 

        return average_list

    def getAverageSalaryForTeam(self) -> list[dict]:
        team_list = self.__getAverage("Team", "Salary")

        final_team_list = []
        for team in team_list:
            if str(team["Team"]).find("/") == -1:
                final_team_list.append(team)

        return final_team_list
    
    def getSumSalaryForConf(self):
        team_list = self.getAverageSalaryForTeam()

        final_list = []
        for conf in CONF_DATA:
            conf_sum = 0
            for team in team_list:
                if conf["Team"] == team["Team"]:
                    conf_sum += team["Average"]

            list_item = {"Conf": conf["Conference"], "Sum": conf_sum}
            final_list.append(list_item)

        return final_list
    
    def getAverageAgeForTeam(self):
        return self.__getAverage("Team", "Age")

    def getAveragePointPerGameForTeam(self):
        return self.__getAverage("Team", "PTS")
    
    def getSumPointPerGameForTeam(self):
        return self.__getSum("Team", "PTS")

    def getSalaryPerMinute(self):
        player_data = self.nbaRepo.find({"select": ["Player Name", "Salary", "GP", "MP"]})

        salary_per_min_data = []
        for player in player_data:
            minutes_played = int(player["GP"]) * float(player["MP"])            
            salary_per_min = int(player["Salary"]) // minutes_played

            per_min_item = {}
            per_min_item["Name"] = player["Player Name"]
            per_min_item["SalaryPerMinute"] = salary_per_min
            salary_per_min_data.append(per_min_item)

        return sorted(salary_per_min_data, key=lambda data: data["SalaryPerMinute"], reverse=True) 

    def __getAverage(self, group_column, average_column):
        average_data = self.nbaRepo.find({"select": [group_column, average_column]})
        group_count = self.nbaRepo.countColumn(group_column)

        average_list = []
        for g_count in group_count:

            average_item = {}
            sum = 0

            for av_data in average_data:
                
                if av_data[group_column] == g_count[group_column]:
                    sum += int(float(av_data[average_column]))

            average_item = {group_column: g_count[group_column], "Average": sum // g_count["count"]}
            average_list.append(average_item) 

        return average_list
    
    def __getSum(self, group_column, sum_column):
        average_data = self.nbaRepo.find({"select": [group_column, sum_column]})
        group_count = self.nbaRepo.countColumn(group_column)

        average_list = []
        for g_count in group_count:

            average_item = {}
            sum = 0

            for data in average_data:
                
                if data[group_column] == g_count[group_column]:
                    sum += int(float(data[sum_column]))

            average_item = {group_column: g_count[group_column], "Sum": sum}
            average_list.append(average_item) 

        return average_list