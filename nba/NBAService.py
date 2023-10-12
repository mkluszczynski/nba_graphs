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
    
    def __getAverage(self, group_column, average_column):
        average_data = self.nbaRepo.find({"select": [group_column, average_column]})
        group_count = self.nbaRepo.countColumn(group_column)

        average_list = []
        for g_count in group_count:

            average_item = {}
            sum = 0

            for salary in average_data:
                
                if salary[group_column] == g_count[group_column]:
                    sum += int(salary[average_column])

            average_item = {group_column: g_count[group_column], "Average": sum // g_count["count"]}
            average_list.append(average_item) 

        return average_list