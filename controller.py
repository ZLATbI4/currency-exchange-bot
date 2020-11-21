import parser
import db
import re


def write_fresh_data():
    """
    Getting a new data from parser and record to DB
    """
    # collect a new data
    fresh = parser.parse()

    # write to db
    i = 0
    while i < len(fresh[0]):
        db.add_data(fresh[0][i], fresh[1][i], fresh[2][i], fresh[3])
        i = i + 1


def last_report_top():
    write_fresh_data()
    data = db.get_top_last()

    clean_data = ''

    n = 0
    while n < len(data):
        row = re.sub(r"[\(',\)]", "", str(data[n]))
        clean_data = clean_data + '* ' + row + '\n' + '\t'
        n = n + 1

    report = f""" 
    СВЕЖИЙ КУРС ДОЛЛАРА 🇺🇸 TOP-10
БАНК | ПОКУПКА | ПРОДАЖА 
 {clean_data}
    """
    return report


def last_report_all():
    write_fresh_data()
    data = db.get_all_last()

    clean_data = ''

    n = 0
    while n < len(data):
        row = re.sub(r"[\(',\)]", "", str(data[n]))
        clean_data = clean_data + '* ' + row + '\n' + '\t'
        n = n + 1

    report = f""" 
    СВЕЖИЙ КУРС ДОЛЛАРА 🇺🇸 FULL
БАНК | ПОКУПКА | ПРОДАЖА 
 {clean_data}
    """
    return report
