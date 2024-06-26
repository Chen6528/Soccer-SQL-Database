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
