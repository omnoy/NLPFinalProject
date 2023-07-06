from court_scraper.CourtScraper import CourtScraper
from court_scraper.DocToXlsx import DocToXlsx
from court_scraper.ParseDocument import *


class CourtScraperToExcel:
    keys = ["תאריך", "קישור", "השופט", "התובע", "הנתבע", "פסק-דין"]

    def __init__(self):
        docto = DocToXlsx(keys=self.keys)
        temp_dict = {k: [] for k in self.keys}
        scrap = CourtScraper()
        datas = scrap.get_by_year(year=2005, limit=50)

        for data in datas:
            try:
                temp_dict['תאריך'] = data['date']
                temp_dict['קישור'] = data['link']
                temp_dict['השופט'] = ",".join(judge_parser(data['body']))
                temp_dict['התובע'] = plaintiff_name_parser(data['body'])
                temp_dict['הנתבע'] = ",".join(defendant_name_parser(data))
                temp_dict['פסק-דין'] = data['פסק-דין']
                docto.add(row=temp_dict)
            except:
                print(data.keys())
                print(data['link'])

        docto.save("CourtVerdicts")
