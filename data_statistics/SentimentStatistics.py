import pandas as pd
import tkinter as tk
from tkinter import messagebox

def sentiments_per_judge():
    data = pd.read_excel("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sample\\CourtVerdicts.xlsx")
    data = data.reset_index()
    judge_dict = {}
    for index, row in data.iterrows():
        judges = row['השופט']
        for judge in judges.split(","):
            if judge.startswith(" השופט") or judge.startswith(" השופט") or judge.startswith(
                    " הנשיא") or judge.startswith(" המשנה"):
                if judge not in judge_dict.keys():
                    judge_dict[judge] = {}
                    judge_dict[judge]['positive'] = 0
                    judge_dict[judge]['neutral'] = 0
                    judge_dict[judge]['negative'] = 0

                judge_dict[judge][row['sentiment']] += 1

    return judge_dict

def sentiments_per_verdicts():
    data = pd.read_excel("C:\\Users\\dnoy1\\PycharmProjects\\NLPFinalProject\\sample\\CourtVerdicts.xlsx")
    data = data.reset_index()
    sentiment_dict = {}
    sentiment_dict['positive'] = 0
    sentiment_dict['neutral'] = 0
    sentiment_dict['negative'] = 0
    for index, row in data.iterrows():
        sentiment = row['sentiment']
        sentiment_dict[sentiment] += 1

    return sentiment_dict

