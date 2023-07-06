from court_scraper.CourtScraper import CourtScraper

scrap = CourtScraper()

""" Get max 500 files - year param between 2005 to 2023 """
data = scrap.get_by_year(year=2005,limit=150)



#print("The keys from file:")
#print(data[0].keys())

#print("Link:")
#print(data[0]['link'])

for i in range(len(data)):
    try:
        print(data[i]['link'])
        print(data[i]['body'].find("ניתן היום,"))
    except:pass



#print("Verdict:")
#print(data[0]['פסק-דין'].replace("  ","").replace("\n\n",""))


