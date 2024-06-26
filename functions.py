import mysql.connector
import pandas as pd


def convert_to_usd(value, conversion_rate=1.07):
    value = value.replace('€', '').strip()
    factor = 1
    
    if 'm' in value.lower():
        factor = 1000000
        value = value.lower().replace('m', '')
    elif 'k' in value.lower():
        factor = 1000
        value = value.lower().replace('k', '')
    try:
        euro_val = float(value) * factor
        value_usd = euro_val * conversion_rate
        value_in_millions = float(value_usd / 1000000)
        return round(value_in_millions, 2)
    except ValueError:
        return None
    
def connect_to_database(user, password, host, database):
    connection = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return connection


def fetch_data(query, cursor):
    cursor.execute(query)
    rows = cursor.fetchall()
    return pd.DataFrame(rows)


def show_highest_value_players(cursor):
    query = ''' 
            SELECT player_name, age, nation, team, market_value 
            FROM player_stats 
            ORDER BY market_value DESC 
            LIMIT 100
            '''
    df = fetch_data(cursor, query)
    df.columns = ['Name', 'Age', 'Nation', 'Team', 'Value']
    return df

def show_oldest_players(cursor):
    query = ''' 
            SELECT player_name, age, nation, team, market_value 
            FROM player_stats 
            ORDER BY age DESC 
            LIMIT 100
            '''
    df = fetch_data(cursor, query)
    df.columns = ['Name', 'Age', 'Nation', 'Team', 'Value']
    return df

def show_players_by_nation(cursor, nation):
    query = f''' 
            SELECT player_name, age, nation, team, market_value 
            FROM player_stats 
            WHERE nation = '{nation}'
            ORDER BY market_value DESC 
            '''
    df = fetch_data(cursor, query)
    df.columns = ['Name', 'Age', 'Nation', 'Team', 'Value']
    return df

def show_players_by_team(cursor, team):
    query = f''' 
            SELECT player_name, age, nation, team, market_value 
            FROM player_stats 
            WHERE team = '{team}'
            ORDER BY market_value DESC 
            '''
    df = fetch_data(cursor, query)
    df.columns = ['Name', 'Age', 'Nation', 'Team', 'Value']
    return df

