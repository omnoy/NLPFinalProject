import matplotlib.pyplot as plt

from data_statistics.SentimentStatistics import sentiments_per_verdicts
from data_statistics.VerdictStatistics import num_of_verdicts_per_judge, subject_statistic

# Judge Dict
judge_dict = num_of_verdicts_per_judge()

names = [name[::-1] for name in list(judge_dict.keys())]
counts = list(judge_dict.values())

plt.subplot(2,2,1)
plt.bar(names, counts)
plt.xlabel('Judges')
plt.ylabel('Number of Verdicts')
plt.xticks(rotation=90, ha="right")


# Subject/Verdict Statistics
subject_dict = subject_statistic()

subjects = [subject[::-1] for subject in list(subject_dict.keys())][-11:-1]
counts = list(subject_dict.values())[-11:-1]

plt.subplot(2,2,2)
plt.bar(subjects, counts)
plt.xlabel('Subjects')
plt.ylabel('Number of Verdicts')
plt.xticks(rotation=90, ha="right")

# Sentiment Dict
sentiment_dict = sentiments_per_verdicts()

sentiments = list(sentiment_dict.keys())
sentiment_counts = list(sentiment_dict.values())

plt.subplot(2, 2, 3)
plt.pie(sentiment_counts, labels=sentiments)

plt.subplot(2, 2, 4)



# Display the plot
plt.tight_layout()
plt.show()

