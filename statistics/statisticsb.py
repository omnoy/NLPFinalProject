import pandas as pd

def topic_statistic(topics:list):

    topic_count = {}
    count = 0
    for topic in topics:

        for t in topic.split(","):
            count += 1
            """ Add topic to dict """
            if t in topic_count.keys():
                topic_count[t] += 1
            else:
                topic_count[t] = 1

    return {key:topic_count[key]/count for key in topic_count.keys()}

data = pd.read_excel('CourtVerdicts.xlsx')

print(topic_statistic(data['נושא']))
