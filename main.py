import requests
from bs4 import BeautifulSoup
import pandas as pd

# get web page info 
url = "https://www.dotabuff.com/players/97658618/matches"
headers = {"User-Agent": "Mozilla/5.0"} # user-agent header to mimic a real browser request.
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# parse html content from the bsoup data
matches_table = soup.find("table").tbody
rows = matches_table.find_all("tr")

# organize date in rows
matches_data = []

for row in rows:
    cols = row.find_all("td")
    match_data = {
        "hero_level": cols[0].text.strip(),
        "hero": cols[1].find("a").text.strip().replace("Immortal", "").strip(),
        #"result": cols[2].text.strip(),
        "date": cols[3].text.strip(),
        "type": cols[4].text.strip(),
        "duration": cols[5].text.strip(),
        "kda": cols[6].text.strip()
    }
    matches_data.append(match_data)

# process it with pandas
dataframe = pd.DataFrame(matches_data)

unique_heroes = dataframe["hero"].nunique() # calculate number of unique heroes played 
num_of_games = len(dataframe) # calculate number of games played
top3_most_played = dataframe["hero"].value_counts().nlargest(3) # calculate the top 3 most played heroes
win_count = dataframe["date"].str.contains('Won').sum() # win count of the games, used for the winrate
win_rate = round((win_count / num_of_games) * 100) # calculate winrate of all the num_of_games

#print(dataframe) # this would print the whole pandas table
print(f"In your past {num_of_games} games, you have played a total of {unique_heroes} different heroes.")
print(f"Winning {win_count} out of those {num_of_games} games, at a {win_rate}% win rate")

print("Your 3 most played heroes were:")
for hero, count in top3_most_played.items():
    print(f"{hero}: {count} games")

