import matplotlib.pyplot as plt
import numpy as np
from data_statistics.SentimentStatistics import sentiments_per_verdicts, sentiments_per_judge
from data_statistics.VerdictStatistics import num_of_verdicts_per_judge, subject_statistic

# Judge Dict ------------------------------
judge_dict = num_of_verdicts_per_judge()

judges = [judge[::-1] for judge in list(judge_dict.keys())]
counts = list(judge_dict.values())

plt.subplot(2,2,1)
plt.bar(judges, counts)
plt.xlabel('Judges')
plt.ylabel('Number of Verdicts')
plt.xticks(rotation=90, ha="right")


# Subject/Verdict Statistics ---------------------------------
subject_dict = subject_statistic()

subjects = [subject[::-1] for subject in list(subject_dict.keys())][-11:-1]
counts = list(subject_dict.values())[-11:-1]

plt.subplot(2,2,2)
plt.bar(subjects, counts)
plt.xlabel('Subjects')
plt.ylabel('Number of Verdicts')
plt.xticks(rotation=90, ha="right")

# Sentiment Dict -------------------------------------------
sentiment_dict = sentiments_per_verdicts()

sentiments = list(sentiment_dict.keys())
sentiment_counts = list(sentiment_dict.values())

plt.subplot(2, 2, 3)
plt.pie(sentiment_counts, labels=sentiments)

# Sentiments by Judge -----------------------------------------
judge_sentiment_dict = sentiments_per_judge()

judges = [judge[::-1] for judge in list(judge_sentiment_dict.keys())]
sentiment_counts = list(judge_sentiment_dict.values())
total_sentiment_counts = {'positive': [], 'neutral': [], 'negative': []}

for sentiment_count in sentiment_counts:
    for sent_key in sentiment_count.keys():
        total_sentiment_counts[sent_key].append(sentiment_count[sent_key])

width = 0.5
bottom = np.zeros(len(judges))

plt.subplot(2, 2, 4)
for sentiment_name, sentiment_count in total_sentiment_counts.items():
    p = plt.bar(judges, sentiment_count, width, label=sentiment_name, bottom=bottom)
    plt.xticks(rotation=90, ha="right")
    bottom += sentiment_count

plt.legend(loc="upper right")

# Display the plot
plt.tight_layout()
plt.show()

