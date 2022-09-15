import pandas as pd
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        self.data  = requests.get(url).text
        self.soup = BeautifulSoup(data,"html5lib")
        self.tables = soup.find_all('table')
        
    def extract(self):
        Contracts_out_for_bid = pd.DataFrame(columns=["Event_ID", "Event_Name", "End_Date"])

        for row in tables[0].tbody.find_all("tr"):
            col = row.find_all("td")
            if (col != []):
                Event_ID = col[0].text.strip()
                Event_Name = col[1].text
                End_Date = col[2].text.strip()
                Contracts_out_for_bid = Contracts_out_for_bid.append({"Event_ID":Event_ID, "Event_Name":Event_Name, "End_Date":End_Date}, ignore_index=True)

        
        return Contracts_out_for_bid

s=Scraper('https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid')
s.extract()
