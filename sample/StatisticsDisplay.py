import matplotlib.pyplot as plt
import numpy as np
from data_statistics.SentimentStatistics import sentiments_per_verdicts, sentiments_per_judge
from data_statistics.VerdictStatistics import num_of_verdicts_per_judge, subject_statistic

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# Judge Dict ------------------------------
judge_dict = num_of_verdicts_per_judge()

judges = [judge[::-1] for judge in list(judge_dict.keys())]
counts = list(judge_dict.values())

axs[0, 0].set_title("Number of Verdicts by each Judge")
axs[0, 0].bar(judges, counts)
axs[0, 0].set_xlabel('Judges')
axs[0, 0].set_ylabel('Number of Verdicts')
axs[0, 0].tick_params(axis='x', labelrotation=90)


# Subject/Verdict Statistics ---------------------------------
subject_dict = subject_statistic()

subjects = [subject[::-1] for subject in list(subject_dict.keys())][-11:-1]
counts = list(subject_dict.values())[-11:-1]

axs[0, 1].set_title("Number of Verdicts for the Top 10 Subjects")
axs[0, 1].bar(subjects, counts)
axs[0, 1].set_xlabel('Subjects')
axs[0, 1].set_ylabel('Number of Verdicts')
axs[0, 1].tick_params(axis='x', labelrotation=90)

# Sentiment Dict -------------------------------------------
sentiment_dict = sentiments_per_verdicts()

sentiments = list(sentiment_dict.keys())
sentiment_counts = list(sentiment_dict.values())

axs[1, 0].set_title("Number of Detected Sentiments in each Verdict")
axs[1, 0].pie(sentiment_counts, labels=sentiments, autopct="%1.1f%%", colors=['green', 'gray', 'red'])

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

for sentiment_name, sentiment_count in total_sentiment_counts.items():
    p = axs[1, 1].bar(judges, sentiment_count, width, label=sentiment_name, bottom=bottom)
    bottom += sentiment_count

axs[1, 1].tick_params(axis='x', labelrotation=90)
axs[1, 1].legend(loc="upper right")

# Display the plot
plt.tight_layout(pad=5)
plt.show()

