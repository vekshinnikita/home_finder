import datetime
from typing import Dict
import requests
from base import BaseFinder
from utils import get_date_from_string


class AvitoFinder(BaseFinder):
    
    url = 'https://www.avito.ru/js/1/map/items?categoryId=24&locationId=653240&metroId%5B0%5D=153&metroId%5B1%5D=154&metroId%5B2%5D=155&metroId%5B3%5D=156&metroId%5B4%5D=157&metroId%5B5%5D=158&metroId%5B6%5D=160&metroId%5B7%5D=161&metroId%5B8%5D=162&metroId%5B9%5D=163&metroId%5B10%5D=164&metroId%5B11%5D=165&metroId%5B12%5D=166&metroId%5B13%5D=167&metroId%5B14%5D=169&metroId%5B15%5D=170&metroId%5B16%5D=171&metroId%5B17%5D=172&metroId%5B18%5D=173&metroId%5B19%5D=174&metroId%5B20%5D=175&metroId%5B21%5D=176&metroId%5B22%5D=177&metroId%5B23%5D=178&metroId%5B24%5D=179&metroId%5B25%5D=180&metroId%5B26%5D=181&metroId%5B27%5D=182&metroId%5B28%5D=183&metroId%5B29%5D=184&metroId%5B30%5D=185&metroId%5B31%5D=186&metroId%5B32%5D=187&metroId%5B33%5D=188&metroId%5B34%5D=189&metroId%5B35%5D=190&metroId%5B36%5D=191&metroId%5B37%5D=192&metroId%5B38%5D=194&metroId%5B39%5D=195&metroId%5B40%5D=196&metroId%5B41%5D=198&metroId%5B42%5D=199&metroId%5B43%5D=200&metroId%5B44%5D=201&metroId%5B45%5D=202&metroId%5B46%5D=203&metroId%5B47%5D=205&metroId%5B48%5D=206&metroId%5B49%5D=207&metroId%5B50%5D=208&metroId%5B51%5D=209&metroId%5B52%5D=210&metroId%5B53%5D=211&metroId%5B54%5D=212&metroId%5B55%5D=1015&metroId%5B56%5D=1016&metroId%5B57%5D=1017&metroId%5B58%5D=2122&metroId%5B59%5D=2132&metroId%5B60%5D=2137&metroId%5B61%5D=2138&metroId%5B62%5D=2196&metroId%5B63%5D=2197&metroId%5B64%5D=2216&metroId%5B65%5D=2217&metroId%5B66%5D=2218&metroId%5B67%5D=2346&priceMin=25000&priceMax=40000&correctorMode=0&page=6&map=1&params%5B201%5D=1060&params%5B504%5D%5B0%5D=5256&params%5B550%5D%5B0%5D=5702&params%5B550%5D%5B1%5D=5703&params%5B2951%5D%5Bfrom%5D=2&params%5B2953%5D%5Bfrom%5D=2&params%5B110710%5D%5B0%5D=472002&params%5B110710%5D%5B1%5D=472003&verticalCategoryId=1&rootCategoryId=4&localPriority=0&footWalkingMetro=15&disabledFilters%5Bids%5D%5B0%5D=byTitle&disabledFilters%5Bslugs%5D%5B0%5D=bt&subscription%5Bvisible%5D=true&subscription%5BisShowSavedTooltip%5D=false&subscription%5BisErrorSaved%5D=false&subscription%5BisAuthenticated%5D=true&viewPort%5Bwidth%5D=1180&viewPort%5Bheight%5D=391&sort=date&limit=30&countAndItemsOnly=1'
    headers = { 
        'authority': 'm.avito.ru',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'ru-RU,ru;q=0.9',
        'cookie': '_ym_uid=1655915762390976460; u=2thjqelm.piam83.1fu2gnyxlii00; srv_id=uXa2_v8mz1CCgPKA.LjUXxphMtYDza7Na4sYVjaN7tmazyQ4k2YtXrIHZyd8WLVcrZbjebCeiqnT9gUtk0vZk.qbGtHhRnaf-d3Pt0IIICRizEnTw1VT8bvepoh4K5zZU=.web; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; _ym_d=1729334032; _gcl_au=1.1.2088474388.1729334032; _ga=GA1.1.1109159657.1729334032; tmr_lvid=3c76707b4fc320f04e5acceb6c880b73; tmr_lvidTS=1655915761112; uxs_uid=a5b38100-8e05-11ef-8fe5-e1212a519af9; __zzatw-avito=MDA0dBA=Fz2+aQ==; cfidsw-avito=CnJAyEEZuf2vp1eyEa56MPdbx/a+bc0t0Tz9SdPRVBH8CcaWvNEggq61aZwMDD09RQ5WeLG6GAl5nuvGplc5/UZlf7OHJNKjtJiAaBLeGQHhlJ0XRBMa4bgSyXEUnIpIapN49lXPrwINTbwDKhde6U+tUcl1NWN0AbWz2g==; luri=sankt-peterburg; buyer_location_id=653240; v=1729407668; buyer_laas_location=653240; _ym_isad=1; domain_sid=JX2s7d4yUaU3LHrMnwrib%3A1729408281216; _ga_ZJDLBTV49B=GS1.1.1729407930.1.0.1729408328.0.0.0; _ga_WW6Q1STJ8M=GS1.1.1729407930.1.0.1729408328.0.0.0; _mlocation=621540; _mlocation_mode=default; redirectMav=1; _inlines_order=params[504].params[550].price.params[121907].categoryNodes.locationGroup; pageviewCount=68; sx=H4sIAAAAAAAC%2F5yUSZIqvQ6F98K4BpJtNb67cSMDSTaQSZf8wd5fUBHFLYbvbuCLE0ff0X8bCClXoRRK0YTg2TglSiHElFIm2%2Fz5b3Pd%2FNlY1zvt9sOAo3dTvZhOLHOPAx7HU5s2Xxvb%2FEFxMTgR1efXBth7VxxzBs3MwI64OCMxzjlE%2BSGXU7%2B4xkzny%2FlOx2V3cvttvXHf5%2Fk6xr9kAggkz68NeigkNVepGLWJuZqgImeHbBLjD1mmxRjcpNxSZ9d2DrBY%2F9DuXNfL9fhBBoovclWuCNk5BFXI3jPm0AKJsmpuP%2BQ2Hac4wXJQgi1Q3Q9TefR062QHcZt%2BtRGDd%2FD82jgxrwjZKAqUGDjGyNhiBg2uVf2b%2BTbUh9%2FvdcinbifataFbdwPP1tbp%2FtGzfmcOlX1iF2J0zhB9dIwOwAl5rVLdP2X2r57Jp1gikY%2FBhCCnFCAll2MUSzG929gO7bDb3m%2FTRWVKdh%2ForqOMmgPktZ1%2BkzWKf5FTdgFCswK5pAJBPGUUw5bRaXxbd1nul3mrD7rp0d86Z%2BUMvt1CX5cj8gc5Rv0m19Q8lNiElBVjMV8j8LfM2ehv5ut5F5IdkJoelnnkg%2FBlfPgR5v7YXz%2FaAMXn14aZuVThFjkSB44m2XysQlCK1Ld1FR9p2UHbSp7G8251B7mSu1zEPWh6yCeZX0vRbMIpFw8RMpSsIUgwjxoNU7T3Um7QDvtDSCfozz3NeBd90GOPj2U5HU0%2Be3b0%2FNpEzNlYs3ID9sjOgRpCCQldQnq7Me1nzjry3O%2FSVLeH7rDdptbMdQ9effttHQT3si761NSRxoI1k0dSVxobOBfUQvI%2F5P7gZrTduEykcr%2FTdMFMy8jr0do07D4uiPC6YM6YNTWuVbWKWktKnrMaUQiQyv9t3fe6XxfMJYfWCL1R0OaSgWBCJtQak5f0Q16uc%2B5GP6Tt9TLW1q0r9%2Bt5Pg%2FD6TTp7XODwT2%2FNiUXYY%2BWJOTG7MWL9wCYSII0fWcWd%2B3vNV5ude2Wbm%2FD8UznZd2JxwDL7XdmB%2B7VRnW1ARiiEoqBRSvldUK0RFRL%2FSEHGqPBPJz3NmPxckQ4TZeJS1jBDh%2FkAPQiGwTvi2oJkpJrWBMqW4rNmxMr5Z%2F%2BBr3aMN8ougKBKnlPzSfEmh2Zs1BQ3ktJ97LX9bQbR4%2FWHoexaNn3x2XPu3l76T6sYwzP5%2F8CAAD%2F%2F1Z6ZkGvBgAA; pageviewCount=72; _ga_M29JC28873=GS1.1.1729410691.5.1.1729417835.56.0.0; tmr_detect=1%7C1729417836138; f=5.e1ae7f0eb55e91e9af89b906f9d80c7916d443061c57ac4216d443061c57ac4216d443061c57ac4216d443061c57ac42cec4d980e289734fcec4d980e289734fcec4d980e289734f96a296658223dafb96a296658223dafb381ebd593ffbb4c30df103df0c26013a20f3d16ad0b1c5460df103df0c26013a0df103df0c26013adc5322845a0cba1a3dad307ec0108827a81beeec8dda10534288c41a710a38fe1b79bc6b7defe3bbdc0d86d9e44006d8143114829cf33ca746b8ae4e81acb9fa3de19da9ed218fe2fb0fb526bb39450a87829363e2d856a2b5b87f59517a23f23de19da9ed218fe23de19da9ed218fe2c772035eab81f5e187829363e2d856a2143114829cf33ca7bed76bde8afb15d28e3a80a29e104a6c2c61f4550df136d875c49cc99ba5a010af69a89f67cf0af31da9f488c469f07575ba275561814d8c0a798d854f9a0beec2aed610b1620960666620226e538b74e2415097439d404746b8ae4e81acb9fa46b8ae4e81acb9faf5b8e78c6f0f62a3201f15d5275b1ae06d6916f479205b462da10fb74cac1eab2da10fb74cac1eabc98d1c3ab1f148dcde91ea798e8647ca3aa92f6fd83fc007; ft="nC0LewIF/E9oImGtz2LPV4ijxr565NvwDsny3LYB/WpR5FjuEZ0jf5pBjZwTG9+iJoNiQtiGNWchhXXs/JkvHXCN/r9Oy/5ZN+7CSszAYt5Wz8egwgCNAPcTVZFJvRi9w75obW2LNj9wnzWup4o2Akmibg2b4HhfhQIuVPKV6n1paUxuVvyXrYPgE4u3NitA"'
    }

    offer_url = 'https://www.avito.ru{offer_uri}'


    def __init__(self):
        self.session = requests.Session()    
        self.session.headers.update(self.headers)   


    def get_offers(self):
        self.session.get('https://m.avito.ru/') 
        print(f'Request Avito')
        response = self.session.get(self.url)
        
        print(f'Avito status code: {response.status_code}')
        if response.status_code != 200:
            return []
        
        try:
            items = [
                item
                for item in response.json()['items']
            ]
            items.sort(key=lambda item: item['sortTimeStamp'], reverse=True)
            return items

        except:
            return []

    
    def get_offer_datetime(self, offer: Dict):
        time = datetime.datetime.fromtimestamp(offer['sortTimeStamp']/1000) 
        return time
    
    def get_notification_message(self, offer: Dict):
        message = 'Появилось новое объявление на Avito: {url}'
        offer_uri = offer['urlPath']
        offer_url = self.offer_url.format(offer_uri=offer_uri)

        return message.format(url=offer_url)
    