import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.dotabuff.com/players/51367068/matches"
headers = {"User-Agent": "Mozilla/5.0"} # user-agent header to mimic a real browser request.
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

matches_table = soup.find('table').tbody
rows = matches_table.find_all('tr')

matches_data = []

for row in rows:
    cols = row.find_all('td')
    match_data = {
        'date': cols[0].text.strip(),
        'hero': cols[1].text.strip(),
        'result': cols[2].text.strip(),
        'kda': cols[3].text.strip(),
        'duration': cols[4].text.strip(),
        'type': cols[5].text.strip()
    }
    matches_data.append(match_data)


df = pd.DataFrame(matches_data)

unique_heroes = df["hero"].nunique()
num_of_games = len(df)

print(f"In your past {num_of_games} you have played {unique_heroes} different heroes.")