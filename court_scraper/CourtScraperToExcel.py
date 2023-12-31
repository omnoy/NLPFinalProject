from court_scraper.CourtScraper import CourtScraper
from court_scraper.DocToXlsx import DocToXlsx
from court_scraper.ParseDocument import *


class CourtScraperToExcel:
    keys = ["תאריך", "קישור", "השופט", "התובע", "הנתבע", "פסק-דין"]

    def __init__(self, year: int, limit: int):
        docto = DocToXlsx(keys=self.keys)
        temp_dict = {k: [] for k in self.keys}
        scrap = CourtScraper()
        datas = scrap.get_by_year(year=year, limit=limit)

        for data in datas:
            try:
                temp_dict['תאריך'] = data['date']
                temp_dict['קישור'] = data['link']
                temp_dict['השופט'] = ",".join(judge_parser(data['body']))
                temp_dict['התובע'] = plaintiff_name_parser(data['body'])
                temp_dict['הנתבע'] = ",".join(defendant_name_parser(data))
                temp_dict['פסק-דין'] = verdict_parser(data['פסק-דין'])
                docto.add(row=temp_dict)
            except:
                pass
        self.docto = docto

    def get_df(self):
        return self.docto
