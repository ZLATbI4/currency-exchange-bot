import mysql.connector
import logging
import time

__connection = None
logging.basicConfig(level=logging.INFO)


def get_connection():
    global __connection
    retry_count = 1
    if __connection is None:
        while retry_count <= 5:
            try:
                __connection = mysql.connector.connect(user = 'root', host = 'mysql-curbot', database = 'curbot')
                if __connection.is_connected():
                    db_info = str(__connection.get_server_info())
                    logging.info(f"Connected to MySQL Server version: {db_info} ")
                    cursor = __connection.cursor()
                    cursor.execute("select database();")
                    record = str(cursor.fetchone()[0])
                    logging.info(f"You're connected to database: {record}")
                    break

            except mysql.connector.errors.InterfaceError as e:
                logging.error(f"Error while connecting to MySQL \n {e.msg} \n retry={str(retry_count)}")
                retry_count = retry_count + 1
                time.sleep(10)

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
            id INT(12) AUTO_INCREMENT PRIMARY KEY,
            bank VARCHAR(255) NOT NULL,
            buy FLOAT(8, 2),
            sell FLOAT(8, 2),
            parse_date TIMESTAMP NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS eur (
            id INT(12) AUTO_INCREMENT PRIMARY KEY,
            bank VARCHAR(255) NOT NULL,
            buy FLOAT(8, 2),
            sell FLOAT(8, 2),
            parse_date TIMESTAMP NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS gbp (
            id INT(12) AUTO_INCREMENT PRIMARY KEY,
            bank VARCHAR(255) NOT NULL,
            buy FLOAT(8, 2),
            sell FLOAT(8, 2),
            parse_date TIMESTAMP NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS pln (
            id INT(12) AUTO_INCREMENT PRIMARY KEY,
            bank VARCHAR(255) NOT NULL,
            buy FLOAT(8, 2),
            sell FLOAT(8, 2),
            parse_date TIMESTAMP NOT NULL
        )
    ''')

    conn.commit()


def add_data(currency: str, bank: str, buy: float, sell: float, parse_date: str):
    init_db()
    conn = get_connection()
    c = conn.cursor()
    c.execute(f'INSERT INTO {currency} (bank, buy, sell, parse_date) VALUES ("{bank}" , {buy}, {sell}, STR_TO_DATE("{parse_date}","%Y-%m-%d %H:%i:%s"))')
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
        OR bank='А-Банк' OR bank='Пивденный' OR bank='Укрсиббанк' OR bank='Райффайзен Банк' OR bank='ПУМБ') 
        ORDER BY buy DESC LIMIT 10;
        ''')
    elif currency == 'gbp':
        c.execute(f'''
        SELECT bank, buy, sell FROM {currency} WHERE parse_date IN (SELECT MAX(parse_date) FROM {currency}) 
        AND (bank='Универсал Банк' OR bank='Укргазбанк'  OR bank='Укрэксимбанк' OR bank='Кредобанк' OR bank='Приватбанк'  
        OR bank='Пиреус Банк' OR bank='Пивденный' OR bank='Идея Банк' OR bank='Райффайзен Банк' OR bank='ПУМБ') 
        ORDER BY buy DESC LIMIT 10;
        ''')
    elif currency == 'pln':
        c.execute(f'''
        SELECT bank, buy, sell FROM {currency} WHERE parse_date IN (SELECT MAX(parse_date) FROM {currency}) 
        AND (bank='Укрэксимбанк' OR bank='Кредобанк'  OR bank='Креди Агриколь Банк' OR bank='Приватбанк' 
        OR bank='Мегабанк' OR bank='Райффайзен Банк' OR bank='Пивденный' OR bank='Идея Банк' 
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