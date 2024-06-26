import requests
from bs4 import BeautifulSoup
import pandas as pd
import links
from functions import *

'''
Webscraping for data to populate the database
'''

PlayerList = []
AgeList = []
PositionsList = []
NationList = []
ValuesList = []
TeamsList = []
count = 0


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

teams = ['Manchester City', 'Arsenal FC', 'Chelsea FC', 'Liverpool FC', 'Tottenham Hotspur', 'Manchester United', 'Aston Villa',
         'Newcastle United', 'Crystal Palace', 'West Ham United', 'Brentford FC', 'Nottingham Forest',
         'AFC Bournemouth', 'Wolverhampton Wanderers FC', 'Everton FC', 'Fulham FC', 'Burnley FC', 'Sheffield United', 'Luton Town',
         'Real Madrid', 'FC Barcelona', 'Real Sociedad', 'Atletico de Madrid', 'Athletic Bilbao', 'Girona FC', 'Valencia FC', 'Villarreal FC',
         'Sevilla FC', 'Real Betis', 'Celta de Vigo', 'Deportivo Alaves', 'UD Las Palmas', 'Getafe CF', 'CA Osasuna', 'RCD Mallorca',
         'UD Almeria', 'Granada CF', 'Rayo Vallecano', 'Cadiz CF',
         'Paris Saint-Germain', 'AS Monaco', 'LOSC Lille', 'Stade Rennais FC', 'OGC Nice', 'Lyon', 'Marseille', 'RC Lens', 'RC Strasbourg Alsace',
         'FC Toulouse', 'Stade Brestois 29', 'Stade Reims', 'FC Lorient', 'Montepellier HSC', 'FC Nantes', 'Le Havre AC', 'FC Metz', 'Clermont Foot 63',
         'Inter Milan', 'AC Milan', 'Napoli', 'Juventus FC', 'Atalanta BC', 'AS Roma', 'Bologna FC 1909', 'ACF Fiorentina', 'SS Lazio',
         'Torino FC', 'Genoa CFC', 'AC Monza', 'Udinese Calcio', 'US Sassuolo', 'Frosinone Calcio', 'US Lecce', 'Cagliari Calcio', 'Hellas Verona',
         'US Salernitana 1919', 'FC Empoli',
         'Bayern Munich', 'Bayer Leverkusen', 'RB Leipzig', 'Borrusia Dortmund', 'VfB Stuttgart', 'Eintracht Frankfurt', 'WfL Wolfburg', 'SC Freilburg', 
         'Borrusia Monchengladbach', 'TSG 1899 Hoffenheim', 'FC Union Berline', 'FSV Mainz 05', 'FC Augsburg', 'SV Werder Bremen', 'FC Koln', 'FC Heidenheim 1846',
         'VfL Bochum', 'SV Darmstadt 98']

for url in links:
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    players_name = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    players_age = soup.find_all("td", {"class": "zentriert"})
    players_nationality = soup.find_all("td", {"class": "zentriert"})
    players_value = soup.find_all("td", {"class": "rechts hauptlink"})
    players_position = soup.select("td.posrela td:not([class])")
    players_team = teams[count]

    for i in range (0, len(players_name)):
        PlayerList.append(str(players_name[i]).split('" class', 1)[0].split('<img alt="', 1)[1])
        TeamsList.append(teams[count])
    
    for i in range (1, len(players_name)*3, 3):
        AgeList.append(str(players_age[i]).split("(",1)[1].split(")", 1)[0])
    for td in players_position:
        position = td.get_text(strip=True)
        if position: 
            PositionsList.append(position)
    for i in range (2, len(players_name)*3, 3):
        NationList.append(str(players_nationality[i]).split('title="', 1)[1].split('"/', 1)[0])

    for value in players_value:
        euro_value = value.get_text(strip=True)
        if euro_value != '-':
            usd_value = convert_to_usd(euro_value)
            ValuesList.append(float(usd_value))
    count+=1 #change team name after each
