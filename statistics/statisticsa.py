import pandas as pd

data = pd.read_excel('CourtVerdicts.xlsx')
judge_dict = {}
for judges in data['השופט']:
    for judge in judges.split(","):
        if judge in judge_dict.keys():
            judge_dict[judge] += 1
        else:
            judge_dict[judge] = 0

judge_dict = dict(sorted(judge_dict.items(), key=lambda item: item[1]))
print(judge_dict)
