import requests
import lxml.html
import re
from datetime import datetime, date


def get_rates(full_page):
    """
    Parsing a target page and getting data from currencies table
    """
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    tree = lxml.html.document_fromstring(full_page)

    # count how many target divs on page
    rows = tree.xpath('count(//*[@id="smTable"]/tbody/tr)')

    banks = []
    buy_rates = []
    sell_rates = []

    n = 1
    while n <= rows:
        bank = re.sub(r"[\['\]\\n]", "", str(tree.xpath(f'//*[@id="smTable"]/tbody/tr[{n}]/td[1]/a/text()')))
        buy = float(re.sub(r"[\['\]]", "", str(tree.xpath(f'//tbody[@class="list"]/tr[{n}]/td[@class="responsive-hide mfm-text-right mfm-pr0"]/text()'))))
        sell = float(re.sub(r"[\['\]]", "", str(tree.xpath(f'//*[@id="smTable"]/tbody/tr[{n}]/td[4]/text()'))))
        n = n + 1
        banks.append(bank)
        buy_rates.append(buy)
        sell_rates.append(sell)
        print(bank, buy, sell)

    return banks, buy_rates, sell_rates, timestamp


# target parse page
def parse(currency: str):
    if currency == 'usd':
        url = 'https://minfin.com.ua/currency/banks/usd/'
    elif currency == 'eur':
        url = 'https://minfin.com.ua/currency/banks/eur/'
    elif currency == 'gbp':
        url = 'https://minfin.com.ua/currency/banks/gbp/'
    elif currency == 'pln':
        url = 'https://minfin.com.ua/currency/banks/pln/'
    else:
        url = 'https://minfin.com.ua/currency/banks/usd/'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}

    full_page = requests.get(url, headers).text

    result = get_rates(full_page)

    return result
