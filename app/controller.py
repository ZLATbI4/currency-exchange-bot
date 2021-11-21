import logging
import parser
import db
import re
import logging


def write_fresh_data(currency: str):
    """
    Getting a new data from parser and record to DB
    """
    logging.info(f"Parse {currency} rates and write into db")
    # collect a new data
    fresh = parser.parse(currency)

    # write to db
    i = 0
    while i < len(fresh[0]):
        db.add_data(currency, fresh[0][i], fresh[1][i], fresh[2][i], fresh[3])
        i = i + 1
        
    logging.info(f"Finish {currency} parse/record task")


def last_report_top(currency: str):
    # write_fresh_data(currency)
    data = db.get_top_last(currency)

    clean_data = ''

    n = 0
    while n < len(data):
        row = re.sub(r"[\(',\)]", "", str(data[n]))
        clean_data = clean_data + '* ' + row + '\n' + '\t'
        n = n + 1

    if currency == 'usd':
        report = f"ТЕКУЩИЙ КУРС ДОЛЛАРА 🇺🇸 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report
    elif currency == 'eur':
        report = f"ТЕКУЩИЙ КУРС ЕВРО 🇪🇺 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report
    elif currency == 'gbp':
        report = f"ТЕКУЩИЙ КУРС ФУНТА 🇬🇧 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report
    elif currency == 'pln':
        report = f"ТЕКУЩИЙ КУРС ЗЛОТОГО 🇵🇱 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report


def last_report_all(currency: str):
    # write_fresh_data(currency)
    data = db.get_all_last(currency)

    clean_data = ''

    n = 0
    while n < len(data):
        row = re.sub(r"[\(',\)]", "", str(data[n]))
        clean_data = clean_data + '* ' + row + '\n' + '\t'
        n = n + 1

    if currency == 'usd':
        report = f"ТЕКУЩИЙ КУРС ДОЛЛАРА 🇺🇸 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report
    elif currency == 'eur':
        report = f"ТЕКУЩИЙ КУРС ЕВРО 🇪🇺 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report
    elif currency == 'gbp':
        report = f"ТЕКУЩИЙ КУРС ФУНТА 🇬🇧 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report
    elif currency == 'pln':
        report = f"ТЕКУЩИЙ КУРС ЗЛОТОГО 🇵🇱 TOП\nБАНК | ПОКУПКА | ПРОДАЖА\n {clean_data}"
        return report


def start():
    start_message = """Бот показывает текущий курс валюты по банкам Украины 🇺🇸🇪🇺🇬🇧🇵🇱

Курс по всем банкам:
 /all_usd - текущий курс доллара 🇺🇸
 /all_eur - текущий курс евро 🇪🇺
 /all_gbp - текущий курс фунта стерлингов 🇬🇧
 /all_pln - текущий курс злотого 🇵🇱

Курс по 10 самым популярным банкам:
 /top_usd - текущий курс доллара 🇺🇸
 /top_eur - текущий курс евро 🇪🇺
 /top_gbp - текущий курс фунта стерлингов 🇬🇧
 /top_pln - текущий курс злотого 🇵🇱
 """
    return start_message
