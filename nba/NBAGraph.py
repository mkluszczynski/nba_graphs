import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from .NBAService import NBAService

class NBAGraph:

    nbaService: NBAService

    def __init__(self, nbaService: NBAService) -> None:
        self.nbaService = nbaService 

    def showAverageSalaryForPosition(self):
        fig, ax = plt.subplots()
        average_salary_data = self.nbaService.getAverageSalaryForPosition()

        for x in average_salary_data:
            print(x)

        position = list(map(lambda av_data: av_data["Position"], average_salary_data))
        old_list = []
        young_list = []
        for av_data in average_salary_data:
            for age_data in av_data["Age"]:
                if age_data["Age"] == "Old":
                    old_list.append(age_data["Average"])
                
                else:
                    young_list.append(age_data["Average"])

        print(old_list)
        print(young_list)

        age_data = {"Old": np.array(old_list), "Young": np.array(young_list)}
        bottom = np.zeros(9)

        for age, age_d in age_data.items():
            p = ax.bar(position, age_d, 0.6, label=age, bottom=bottom)
            bottom += age_d

            ax.bar_label(p, label_type='center', fmt="{:}")


        ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.set_ylabel('Average salary')
        ax.set_xlabel("Position")
        ax.set_title('Average salary for position')
        ax.legend()
        plt.show()

    def showAverageSalaryForTeam(self):
        average_salary_data = self.nbaService.getAverageSalaryForTeam()

        team = list(map(lambda av_data: av_data["Team"], average_salary_data))
        average_salary = list(map(lambda av_data: av_data["Average"], average_salary_data))
        
        self.__showHorizontalSubplots(team, average_salary, "Team", "Average salary", "Average salary for team")

    def showSumSalaryForConf(self):
        sum_conf_data = self.nbaService.getSumSalaryForConf()

        conf = list(map(lambda sum_data: sum_data["Conf"], sum_conf_data))
        sum_salary = list(map(lambda sum_data: sum_data["Sum"], sum_conf_data))

        self.__showHorizontalSubplots(conf, sum_salary, "Conference", "Sum of salary", "Sum of salary by conference")

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