
class ScraperConfig:
    url = "https://supremedecisions.court.gov.il"

    urlSearch = f"{url}/Home/SearchVerdicts" # POST
    urlDownload = f"{url}/Home/Download" # GET

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/json;charset=UTF-8",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

    payload = {
                  "document": {
                    "Year": None,
                    "Counsel": [
                      {
                        "Text": "",
                        "textOperator": 2,
                        "option": "2",
                        "Inverted": False,
                        "Synonym": False,
                        "NearDistance": 3,
                        "MatchOrder": False
                      }
                    ],
                    "CaseNum": None,
                    "Technical": None,
                    "fromPages": None,
                    "toPages": None,
                    "dateType": 2,
                    "PublishFrom": None,
                    "PublishTo": None,
                    "publishDate": 8,
                    "translationDateType": 1,
                    "translationPublishFrom": "2023-06-20T14:05:05.444Z",
                    "translationPublishTo": "2023-07-20T14:05:05.444Z",
                    "translationPublishDate": 8,
                    "SearchText": [
                      {
                        "Text": "",
                        "textOperator": 1,
                        "option": "2",
                        "Inverted": False,
                        "Synonym": False,
                        "NearDistance": 3,
                        "MatchOrder": False
                      }
                    ],
                    "Judges": None,
                    "Parties": [
                      {
                        "Text": "",
                        "textOperator": 2,
                        "option": "2",
                        "Inverted": False,
                        "Synonym": False,
                        "NearDistance": 3,
                        "MatchOrder": False
                      }
                    ],
                    "Mador": None,
                    "CodeMador": [],
                    "TypeCourts": None,
                    "TypeCourts1": None,
                    "TerrestrialCourts": None,
                    "LastInyan": None,
                    "LastCourtsYear": None,
                    "LastCourtsMonth": None,
                    "LastCourtCaseNum": None,
                    "Old": False,
                    "JudgesOperator": 2,
                    "Judgment": None,
                    "Type": [
                      {
                        "parent": 2,
                        "value": 2,
                        "text": "פסק-דין"
                      }
                    ],
                    "CodeTypes": [
                      2
                    ],
                    "CodeJudges": [],
                    "Inyan": None,
                    "CodeInyan": [],
                    "AllSubjects": [
                      {
                        "Subject": None,
                        "SubSubject": None,
                        "SubSubSubject": None
                      }
                    ],
                    "CodeSub2": [],
                    "Category1": None,
                    "Category3": None,
                    "CodeCategory3": [],
                    "Volume": None,
                    "Subjects": None,
                    "SubSubjects": None,
                    "SubSubSubjects": None
                  },
                  "lan": "1"
                }
