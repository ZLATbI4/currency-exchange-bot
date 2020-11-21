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
        c.execute('DROP TABLE IF EXISTS currencies')

    c.execute('''
        CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER PRIMARY KEY,
            bank VARCHAR(255) NOT NULL,
            buy_usd FLOAT,
            sell_usd FLOAT,
            parse_date TIMESTAMP NOT NULL
        )
    ''')

    conn.commit()


def add_data(bank: str, buy_usd: float, sell_usd: float, parse_date: str):
    init_db()
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO currencies (bank, buy_usd, sell_usd, parse_date) VALUES (? , ?, ?, ?)',
              (bank, buy_usd, sell_usd, parse_date))
    conn.commit()


def get_bank_history(bank: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT bank, buy_usd, sell_usd, parse_date FROM currencies WHERE bank = ? LIMIT 10', (bank, ))
    result = c.fetchall()
    conn.commit()
    return result


def get_top_last():
    """
    Get exchange rates of 10 most popular banks
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
    SELECT bank, buy_usd, sell_usd FROM currencies WHERE parse_date IN (SELECT MAX(parse_date) FROM currencies) 
    AND (bank='Monobank' OR bank='ПриватБанк'  OR bank='Укрэксимбанк'  OR bank='Ощадбанк'  OR bank='Альфа-банк'  
    OR bank='А-Банк' OR bank='Пивденний' OR bank='УкрСиббанк' OR bank='Укргазбанк' OR bank='ПУМБ') 
    ORDER BY buy_usd DESC LIMIT 10;
    ''')
    result = c.fetchall()
    conn.commit()
    return result


def get_all_last():
    """
    Get exchange rates from all banks
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
    SELECT bank, buy_usd, sell_usd FROM currencies WHERE parse_date IN (SELECT MAX(parse_date) FROM currencies) 
    ORDER BY buy_usd DESC LIMIT 51;
    ''')
    result = c.fetchall()
    conn.commit()
    return result


if __name__ == '__main__':
    init_db()

    #add_data('Альфа Банк', 28.15, 28.20, '2020-11-20 23:30:04')

    # q = get_top_last()
    # print(q)

