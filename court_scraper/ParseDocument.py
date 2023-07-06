import re

RESPONDENTS = "המשיבים"
RESPONDENT_M = "המשיב"
RESPONDENT_F = "המשיבה"


def judge_parser(text: str) -> list:
    judges = re.findall(f"כבוד.+\n", text)
    judges = [j.replace("\n", "").replace("כבוד", "") for j in judges]
    return judges


def plaintiff_name_parser(text: str):
    text = " ".join(text.replace("\xa0", "").replace("\n", " ").split(" "))

    pos_end = text.find("נ ג ד")
    pos_start = 0
    for c in range(pos_end, 0, -1):
        if text[c] == ":":
            pos_start = c + 1
            break

    return text[pos_start:pos_end]


def defendant_name_parser(data: dict):
    if RESPONDENTS in data.keys():
        text = data[RESPONDENTS].replace("\r", "")
        res = re.findall("\d\..+", text)
        return [r.split(". ")[-1] for r in res]
    elif RESPONDENT_M in data.keys():
        text = data[RESPONDENT_M].replace("\r", "")
    elif RESPONDENT_F in data.keys():
        text = data[RESPONDENT_F].replace("\r", "")
    else:
        raise Exception(f"Key Error: {data.keys()}")

    res = re.findall(".+", text)

    if res is None:
        raise Exception(f"String not found: {text}")

    return [res[0]]
