from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

wiki_url = 'https://tr.wikipedia.org/wiki/%C3%9Clke_%C3%A7ap%C4%B1nda_2023_T%C3%BCrkiye_genel_se%C3%A7imleri_i%C3%A7in_yap%C4%B1lan_anketler'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table that has a class attribute that starts with "wikitable sortable"
election_survey = soup.find('table', attrs={'class': re.compile('^wikitable sortable')})

# Use the pandas read_html function to parse the HTML table into a DataFrame
df = pd.read_html(str(election_survey))[0]
df.to_csv('election_survey.csv', index=False)

print(df)