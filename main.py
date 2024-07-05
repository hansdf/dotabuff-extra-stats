import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.dotabuff.com/players/86738694/matches"
headers = {"User-Agent": "Mozilla/5.0"} # user-agent header to mimic a real browser request.
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

matches_table = soup.find("table").tbody
rows = matches_table.find_all("tr")

matches_data = []

for row in rows:
    cols = row.find_all("td")
    match_data = {
        "hero_level": cols[0].text.strip(),
        "hero": cols[1].text.strip(),
        "result": cols[2].text.strip(),
        "result": cols[3].text.strip(),
        "type": cols[4].text.strip(),
        "duration": cols[5].text.strip(),
        "date": cols[6].text.strip()
    }
    matches_data.append(match_data)


df = pd.DataFrame(matches_data)

unique_heroes = df["hero"].nunique()
num_of_games = len(df)

print(f"In your past {num_of_games} games, you have played a total of {unique_heroes} different heroes.")

win_count = df["result"].str.contains('Won').sum()
win_rate = round((win_count / num_of_games) * 100)

print(f"Winning {win_count} out of those 50 games, at a {win_rate}% winrate")