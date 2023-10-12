import matplotlib.pyplot as plt

from .NBAService import NBAService

class NBAGraph:

    nbaService: NBAService

    def __init__(self, nbaService: NBAService) -> None:
        self.nbaService = nbaService 

    def showAverageSalaryForPosition(self):
        fig, ax = plt.subplots()
        average_salary_data = self.nbaService.getAverageSalaryForPosition();

        position = list(map(lambda av_data: av_data["Position"], average_salary_data))
        average_salary = list(map(lambda av_data: av_data["Average"], average_salary_data))

        ax.ticklabel_format(style="plain")
        ax.bar(position, average_salary)
        ax.set_ylabel('Average salary')
        ax.set_xlabel("Position")
        ax.set_title('Average salary for position')
        
        plt.show()

    def showAverageSalaryForTeam(self):
        fig, ax = plt.subplots()
        
        average_salary_data = self.nbaService.getAverageSalaryForTeam();

        team = list(map(lambda av_data: av_data["Team"], average_salary_data))
        average_salary = list(map(lambda av_data: av_data["Average"], average_salary_data))
        
        
        ax.ticklabel_format(style="plain")
        ax.set_yticklabels(team, fontsize=7)
        ax.barh(team, average_salary, align="center")
        
        
        ax.invert_yaxis()
        ax.set_ylabel('Average salary')
        ax.set_xlabel("Team")
        ax.set_title('Average salary for team')
        
        plt.show()

    def showAverageAgeForTeam(self):
        fig, ax = plt.subplots()
        
        average_salary_data = self.nbaService.getAverageAgeForTeam();

        team = list(map(lambda av_data: av_data["Team"], average_salary_data))
        average_salary = list(map(lambda av_data: av_data["Average"], average_salary_data))
        
        
        ax.ticklabel_format(style="plain")
        ax.set_yticklabels(team, fontsize=7)
        ax.barh(team, average_salary, align="center")
        
        
        ax.invert_yaxis()
        ax.set_ylabel('Average age')
        ax.set_xlabel("Team")
        ax.set_title('Average age for team')
        
        plt.show()