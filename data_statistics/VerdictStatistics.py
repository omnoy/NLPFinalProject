import pandas as pd


def num_of_verdicts_per_judge():
    data = pd.read_excel("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sample\\CourtVerdicts.xlsx")
    judge_dict = {}
    for judges in data['השופט']:
        for judge in judges.split(","):
            if judge.startswith(" השופט") or judge.startswith(" השופט") or judge.startswith(" הנשיא") or judge.startswith(" המשנה"):
                if judge in judge_dict.keys():
                    judge_dict[judge] += 1
                else:
                    judge_dict[judge] = 1

    return dict(sorted(judge_dict.items(), key=lambda item: item[1]))


def subject_statistic():
    data = pd.read_excel("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sample\\CourtVerdicts.xlsx")
    subjects = data['tfidf subjects']
    subject_count_dict = {}
    for subject in subjects:
        for t in subject.split(","):
            """ Add topic to dict """
            if t in subject_count_dict.keys():
                subject_count_dict[t] += 1
            else:
                subject_count_dict[t] = 1
    subject_count_dict = dict(sorted(subject_count_dict.items(), key=lambda item: item[1]))
    return subject_count_dict