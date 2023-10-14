import matplotlib.pyplot as plt

from .NBAService import NBAService

class NBAGraph:

    nbaService: NBAService

    def __init__(self, nbaService: NBAService) -> None:
        self.nbaService = nbaService 

    def showAverageSalaryForPosition(self):
        fig, ax = plt.subplots()
        average_salary_data = self.nbaService.getAverageSalaryForPosition()

        position = list(map(lambda av_data: av_data["Position"], average_salary_data))
        average_salary = list(map(lambda av_data: av_data["Average"], average_salary_data))

        ax.ticklabel_format(style="plain")
        ax.bar(position, average_salary)
        ax.set_ylabel('Average salary')
        ax.set_xlabel("Position")
        ax.set_title('Average salary for position')
        
        plt.show()

    def showAverageSalaryForTeam(self):
        average_salary_data = self.nbaService.getAverageSalaryForTeam()

        team = list(map(lambda av_data: av_data["Team"], average_salary_data))
        average_salary = list(map(lambda av_data: av_data["Average"], average_salary_data))
        
        self.__showHorizontalSubplots(team, average_salary, "Team", "Average salary", "Average salary for team")

    def showAverageAgeForTeam(self):
        average_age_data = self.nbaService.getAverageAgeForTeam()

        team = list(map(lambda av_data: av_data["Team"], average_age_data))
        average_age = list(map(lambda av_data: av_data["Average"], average_age_data))
        
        self.__showHorizontalSubplots(team, average_age, "Team", "Average age", "Average age for team")

    def showAveragePointsPerGameForTeam(self):
        average_pts_data = self.nbaService.getAveragePointPerGameForTeam()

        team = list(map(lambda av_data: av_data["Team"], average_pts_data))
        average_pts = list(map(lambda av_data: av_data["Average"], average_pts_data))

        self.__showHorizontalSubplots(team, average_pts, "Team", "Average points per game", "Average point per game for team")

    def showSumPointsPerGameForTeam(self):
        sum_pts_data = self.nbaService.getSumPointPerGameForTeam()

        team = list(map(lambda av_data: av_data["Team"], sum_pts_data))
        sum_pts = list(map(lambda av_data: av_data["Sum"], sum_pts_data))

        self.__showHorizontalSubplots(team, sum_pts, "Team", "Sum of points per game", "Sum of points per game for team")

    def showBestSalaryPerMinute(self, top = 20):
        salary_per_minute = self.nbaService.getSalaryPerMinute()[0:top]

        players = list(map(lambda data: data["Name"], salary_per_minute))
        salary = list(map(lambda data: data["SalaryPerMinute"], salary_per_minute))

        self.__showHorizontalSubplots(players, salary, "Player", "Salary per minute", "Salary per minute for player")

    def __showHorizontalSubplots(self, xdata: list, ydata: list, xlabel: str, ylabel: str, title: str):

        fig, ax = plt.subplots()
        
        ax.ticklabel_format(style="plain")
        ax.set_yticklabels(xdata, fontsize=7)
        ax.barh(xdata, ydata, align="center")
        
        
        ax.invert_yaxis()
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        
        plt.show()