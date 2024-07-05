# dotabuff matches summary

This script should take a dotabuff.com matches page from a players profile, and give a summary of stats in a quick glance.

I'm using BeautifulSoup to scrape the page and some very basic pandas function to organize and view the information in a table.

Most of the stats wil be based on the most recent 50 games(one page of matches).

Some stats planned are:
Number of unique heroes in the past 50 games, and the most played one.
Type of games - number of ranked / normal / turbo games.
Overall winrate past 50 games.