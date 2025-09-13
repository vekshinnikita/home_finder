import datetime
from typing import Dict
import requests
from base import BaseFinder
from utils import get_date_from_string


class AvitoFinder(BaseFinder):
    
    url = 'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=24&footWalkingMetro=15&localPriority=0&locationId=653240&metroId[]=154&metroId[]=2346&metroId[]=164&metroId[]=165&metroId[]=166&metroId[]=160&metroId[]=2217&metroId[]=162&metroId[]=1016&metroId[]=212&metroId[]=2196&metroId[]=2132&metroId[]=167&metroId[]=169&metroId[]=170&metroId[]=171&metroId[]=172&metroId[]=173&metroId[]=174&metroId[]=175&metroId[]=176&metroId[]=2138&metroId[]=153&metroId[]=177&metroId[]=178&metroId[]=179&metroId[]=180&metroId[]=181&metroId[]=2122&metroId[]=182&metroId[]=183&metroId[]=184&metroId[]=185&metroId[]=155&metroId[]=186&metroId[]=187&metroId[]=188&metroId[]=191&metroId[]=189&metroId[]=190&metroId[]=192&metroId[]=194&metroId[]=195&metroId[]=196&metroId[]=2197&metroId[]=198&metroId[]=2216&metroId[]=199&metroId[]=200&metroId[]=201&metroId[]=202&metroId[]=1015&metroId[]=203&metroId[]=205&metroId[]=206&metroId[]=2137&metroId[]=207&metroId[]=208&metroId[]=163&metroId[]=157&metroId[]=158&metroId[]=156&metroId[]=2218&metroId[]=161&metroId[]=209&metroId[]=210&metroId[]=1017&metroId[]=211&params[110710][0]=472002&params[110710][1]=472003&params[201]=1060&params[2951-from]=2&params[2953-from]=2&params[504]=5256&params[550][0]=5702&params[550][1]=5703&priceMax=40000&priceMin=25000&searchRadius=0&sort=date&context=H4sIAAAAAAAA_0q0MrKqLraysFJKK8rPDUhMT1WyLrYytVIqLk5LLAOxLSFS8QUYcrWAAAAA__8DBTAtPQAAAA&page=1&lastStamp=1757782080&layoutRange=narrow&pageId=H4sIAAAAAAAA_wE_AMD_YToyOntzOjExOiJ0b3RhbF9mb3VuZCI7aTo0MTc7czoxOiJ5IjtzOjE2OiJpSkM5ZElXeVNUak1MMmpJIjt9T9WkUD8AAAA&presentationType=serp'
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
        'cookie': '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
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
    