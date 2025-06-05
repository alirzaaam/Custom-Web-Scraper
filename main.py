from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()

URL = "https://www.nba.com/stats/leaders"
driver.get(URL)

# Wait for data to load
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

table = soup.find('table')
# Skip header  
rows = table.find_all('tr')[1:]  

data = []
for row in rows:
    cols = row.find_all('td')
    if cols:
        player = cols[1].text.strip()
        points = cols[2].text.strip()
        gp = cols[3].text.strip()
        min = cols[4].text.strip()
        pts = cols[5].text.strip()
        data.append([player, points, gp, min, pts])

df = pd.DataFrame(data, columns=["Player", "Points", "GP", "MIN", "PTS"])
df.to_csv("nba_leader_stats.csv", index=False)