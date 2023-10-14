from .NBARepository import NBARepository

class NBAService:

    nbaRepo: NBARepository

    def __init__(self, nbaRepo) -> None:
        self.nbaRepo = nbaRepo

    def getAverageSalaryForPosition(self) -> list[dict]:
        return self.__getAverage("Position", "Salary")

    def getAverageSalaryForTeam(self) -> list[dict]:
        return self.__getAverage("Team", "Salary")
    
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