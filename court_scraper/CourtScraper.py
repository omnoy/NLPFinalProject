import requests
from tqdm import tqdm
from court_scraper.HtmlToJson import HtmlToJson
from court_scraper.ScraperConfig import ScraperConfig


class CourtScraper(ScraperConfig):

    def __init__(self):
        self.htmlToJson = HtmlToJson()

    def get_file(self, path: str, fileName: str,date:str):
        link = f"{self.urlDownload}?path={path}&fileName={fileName}&type=2"
        response = requests.get(url=link)

        if response.status_code == 200:
            return self.htmlToJson(html=response.text,link=link,date=date)

        raise Exception(
            "Request returned a non-200 status code. Expected 200, but received " + str(response.status_code) + ".")

    def search(self, year: int = 2023):

        payload = self.payload.copy()
        payload["Year"] = year
        response = requests.post(self.urlSearch, json=payload, verify=False)

        if response.status_code == 200:
            return response.json()

        raise Exception(
            "Request returned a non-200 status code. Expected 200, but received " + str(response.status_code) + ".")

    def get_by_year(self, year: int,limit:int = None):
        data = self.search(year=year)

        return [self.get_file(path=case['Path'], fileName=case['FileName'],date=case['VerdictsDtString']) for case in tqdm(data['data'][:limit])]
