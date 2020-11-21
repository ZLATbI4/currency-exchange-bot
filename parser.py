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
    usd_rows = tree.xpath('count(//*[@id="latest_currency_container"]/tbody[1]/tr)')

    banks = []
    usd_buy_rates = []
    usd_sell_rates = []

    n = 1
    while n <= usd_rows:
        bank = re.sub(r"[\['\]]", "", str(tree.xpath(f'//*[@id="latest_currency_container"]/tbody[1]/tr[{n}]/th/a/text()')))
        buy_usd = float(re.sub(r"[\['\]]", "", str(tree.xpath(f'//*[@id="latest_currency_container"]/tbody[1]/tr[{n}]/td[1]/span/span/text()'))))
        sell_usd = float(re.sub(r"[\['\]]", "", str(tree.xpath(f'//*[@id="latest_currency_container"]/tbody[1]/tr[{n}]/td[2]/span/span/text()'))))
        n = n + 1
        banks.append(bank)
        usd_buy_rates.append(buy_usd)
        usd_sell_rates.append(sell_usd)
    return banks, usd_buy_rates, usd_sell_rates, timestamp


# target parse page
def parse():
    url = 'https://finance.i.ua'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'}

    full_page = requests.get(url, headers).text

    result = get_rates(full_page)

    return result
