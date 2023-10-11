from nba.NBARepository import NBARepository

file = open("data/nba_salaries.csv")

nbaRepo = NBARepository(file)

salaries = nbaRepo.find({"select": ["Salary", "Position"]})
position_count = nbaRepo.countColumn("Position")

position_average_salaries = []
for pos_count in position_count:

    average_item = {}
    salary_sum = 0

    for salary in salaries:
        
        if salary["Position"] == pos_count["Position"]:
            salary_sum += int(salary["Salary"])

    average_item = {"Position": pos_count["Position"], "Average": salary_sum // pos_count["count"]}
    position_average_salaries.append(average_item) 


for row in position_average_salaries:
    print(row)
