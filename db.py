import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('history.db')
    return __connection


def init_db(force: bool = False):
    """ Check if table exists, else make a new one
        :param force reinstall table
    """
    conn = get_connection()
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS usd, eur, gbp, pln')

    c.execute('''
        CREATE TABLE IF NOT EXISTS usd (
            id INTEGER PRIMARY KEY,
            bank VARCHAR(255) NOT NULL,
            buy FLOAT,
            sell FLOAT,
            parse_date TIMESTAMP NOT NULL
        )
    ''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS eur (
                id INTEGER PRIMARY KEY,
                bank VARCHAR(255) NOT NULL,
                buy FLOAT,
                sell FLOAT,
                parse_date TIMESTAMP NOT NULL
            )
        ''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS gbp (
                id INTEGER PRIMARY KEY,
                bank VARCHAR(255) NOT NULL,
                buy FLOAT,
                sell FLOAT,
                parse_date TIMESTAMP NOT NULL
            )
        ''')

    c.execute('''
            CREATE TABLE IF NOT EXISTS pln (
                id INTEGER PRIMARY KEY,
                bank VARCHAR(255) NOT NULL,
                buy FLOAT,
                sell FLOAT,
                parse_date TIMESTAMP NOT NULL
            )
        ''')

    conn.commit()


def add_data(currency: str, bank: str, buy: float, sell: float, parse_date: str):
    init_db()
    conn = get_connection()
    c = conn.cursor()
    c.execute(f'INSERT INTO {currency} (bank, buy, sell, parse_date) VALUES (? , ?, ?, ?)',
              (bank, buy, sell, parse_date))
    conn.commit()

def get_top_last(currency: str):
    """
    Get exchange rates of 10 most popular banks
    """
    conn = get_connection()
    c = conn.cursor()
    if currency == 'usd' or currency == 'eur':
        c.execute(f'''
        SELECT bank, buy, sell FROM {currency} WHERE parse_date IN (SELECT MAX(parse_date) FROM {currency}) 
        AND (bank='Альфа-Банк' OR bank='OTP Bak' OR bank='Укрэксимбанк' OR bank='Ощадбанк' OR bank='Приватбанк'  
        OR bank='А-Банк' OR bank='Пивденный' OR bank='Укрсиббанк' OR bank='Райффайзен Банк Аваль' OR bank='ПУМБ') 
        ORDER BY buy DESC LIMIT 10;
        ''')
    elif currency == 'gbp':
        c.execute(f'''
        SELECT bank, buy, sell FROM {currency} WHERE parse_date IN (SELECT MAX(parse_date) FROM {currency}) 
        AND (bank='Универсал Банк' OR bank='Укргазбанк'  OR bank='Укрэксимбанк' OR bank='Кредобанк' OR bank='Приватбанк'  
        OR bank='Пиреус Банк' OR bank='Пивденный' OR bank='Идея Банк' OR bank='Райффайзен Банк Аваль' OR bank='ПУМБ') 
        ORDER BY buy DESC LIMIT 10;
        ''')
    elif currency == 'pln':
        c.execute(f'''
        SELECT bank, buy, sell FROM {currency} WHERE parse_date IN (SELECT MAX(parse_date) FROM {currency}) 
        AND (bank='Укрэксимбанк' OR bank='Кредобанк'  OR bank='Креди Агриколь Банк' OR bank='Приватбанк' 
        OR bank='Мегабанк' OR bank='Райффайзен Банк Аваль' OR bank='Пивденный' OR bank='Идея Банк' 
        OR bank='Конкорд' OR bank='Укргазбанк') 
        ORDER BY buy DESC LIMIT 10;
        ''')
    result = c.fetchall()
    conn.commit()
    return result


def get_all_last(currency: str):
    """
    Get exchange rates from all banks
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute(f'''
    SELECT bank, buy, sell FROM {currency} WHERE parse_date IN (SELECT MAX(parse_date) FROM {currency}) 
    ORDER BY buy DESC LIMIT 60;
    ''')
    result = c.fetchall()
    conn.commit()
    return result


if __name__ == '__main__':
    init_db()
