import mysql.connector

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

def query_value_desc(cursor, window):
    query = ''' 
            SELECT player_name, age, position, nation, team, market_value 
            FROM player_stats 
            ORDER BY market_value DESC 
            LIMIT 300
            '''
    cursor.execute(query)
    window.destroy()


def query_value_incr(cursor, window):
    query = ''' 
            SELECT player_name, age, position, nation, team, market_value 
            FROM player_stats 
            WHERE market_value > 0
            ORDER BY market_value ASC 
            LIMIT 300
            '''
    cursor.execute(query)
    window.destroy()

def query_normal(cursor, window):
    query = ''' 
            SELECT player_name, age, position, nation, team, market_value 
            FROM player_stats 
            '''
    cursor.execute(query)
    window.destroy()

def query_search(cursor, window, input_picked):
    query = ''' 
            SELECT player_name, age, position, nation, team, market_value 
            FROM player_stats 
            WHERE nation LIKE %s OR team LIKE %s OR player_name LIKE %s or position LIKE %s
            '''
    search_pattern = f"%{input_picked}%"
    cursor.execute(query, (search_pattern, search_pattern, search_pattern, search_pattern))
    window.destroy()

def center_window(window, width=600, height=500):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')