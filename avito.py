import datetime
from typing import Dict
import requests
from base import BaseFinder


class AvitoFinder(BaseFinder):
    
    url = 'https://m.avito.ru/api/11/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=24&footWalkingMetro=15&locationId=653240&metroId[]=154&metroId[]=2346&metroId[]=164&metroId[]=165&metroId[]=166&metroId[]=160&metroId[]=2217&metroId[]=162&metroId[]=1016&metroId[]=212&metroId[]=2196&metroId[]=2132&metroId[]=167&metroId[]=169&metroId[]=170&metroId[]=171&metroId[]=172&metroId[]=173&metroId[]=174&metroId[]=175&metroId[]=176&metroId[]=2138&metroId[]=153&metroId[]=177&metroId[]=178&metroId[]=179&metroId[]=180&metroId[]=181&metroId[]=2122&metroId[]=182&metroId[]=183&metroId[]=184&metroId[]=185&metroId[]=155&metroId[]=186&metroId[]=187&metroId[]=188&metroId[]=191&metroId[]=189&metroId[]=190&metroId[]=192&metroId[]=194&metroId[]=195&metroId[]=196&metroId[]=2197&metroId[]=198&metroId[]=2216&metroId[]=199&metroId[]=200&metroId[]=201&metroId[]=202&metroId[]=1015&metroId[]=203&metroId[]=205&metroId[]=206&metroId[]=2137&metroId[]=207&metroId[]=208&metroId[]=163&metroId[]=157&metroId[]=158&metroId[]=156&metroId[]=2218&metroId[]=161&metroId[]=209&metroId[]=210&metroId[]=1017&metroId[]=211&params[110710][]=472003&params[110710][]=472002&params[201]=1060&params[2951-from-int]=2&params[504]=5256&params[550][]=5704&params[550][]=5703&priceMax=40000&priceMin=25000&sort=date&context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYys1LKzMvJzEtVsq4FBAAA__9-_ClVIgAAAA&page=1&lastStamp=1754082900&layoutRange=narrow&presentationType=serp'
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
        'cookie': '_ym_uid=1655915762390976460; u=2thjqelm.piam83.1fu2gnyxlii00; srv_id=uXa2_v8mz1CCgPKA.LjUXxphMtYDza7Na4sYVjaN7tmazyQ4k2YtXrIHZyd8WLVcrZbjebCeiqnT9gUtk0vZk.qbGtHhRnaf-d3Pt0IIICRizEnTw1VT8bvepoh4K5zZU=.web; buyer_location_id=653240; buyer_laas_location=653240; cfidsw-avito=+ct33omaThkVKfzQxWYMiXjtfGtBKi681Sk3ZccPggYMLVnR/c9RI1nVCibb+2KmZsIocBZBKlzPhxM/NfNm8/w7WQurXSBhMWHaybteCE4GKa8fCnvts60CN5K3PO26RHTcuMbGfh1eiBcKOw0rOCiT/FQfDUMyWsfb8g==; ma_id=7862769511737303560028; _ym_d=1753542710; _gcl_au=1.1.949818631.1753542710; _ga=GA1.1.565379850.1753542710; tmr_lvid=3c76707b4fc320f04e5acceb6c880b73; tmr_lvidTS=1655915761112; adrcid=ABXQRXPb30GOcnLtejF5JNQ; ma_cid=9163963081729961215; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; v=1754081925; _ym_isad=1; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1754168336910%2C%22sl%22%3A%7B%22224%22%3A1754081936910%2C%221228%22%3A1754081936910%7D%7D; _ym_visorc=b; ma_ss_64a8dba6-67f3-4fe4-8625-257c4adae014=1754081936668373234.3.1754081952.2.1754081936; f=5.8696cbce96d2947c36b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b93f5003b9de26797b433be0669ea77fc074c4a16376f87ccd915ac1de0d034112f12b79bbb67ac37d46b8ae4e81acb9fae2415097439d4047d50b96489ab264edc772035eab81f5e1e992ad2cc54b8aa8d99271d186dc1cd03de19da9ed218fe23de19da9ed218fe23de19da9ed218fe2e992ad2cc54b8aa846b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335cb88de1666d503ec6e2ddf0188effb19202c730c0109b9fbbf359236d9608bd58e77fa59952c1da0bc5584122abfc8baeb43d07de4f63d77bbe9d24f315d0ac0be2415097439d404746b8ae4e81acb9fa786047a80c779d5146b8ae4e81acb9fa23c6dffdfce826c22d38179306cb93212da10fb74cac1eabb3ae333f3b35fe91de6c39666ae9b0d73339614c6f29137599c7f25537e9455a; ft="5OLwvAqbkOFCJm2VpjudFP46a/JsKT0EYkEC+oQpQeMeNJCvOwaXANisJVrrZscGuz/cIrvaJbcrEeM99X7TYbhFs86z6z7fj2Jsy0NdipHizBClOzW9iYqKcOJ6bT8W6wBgWYSEK/xlMQfSSlYO7l37uv65dRV1GExkCnD47F4G4oXV8ksaj1sOb2EuWMdI"; sx=H4sIAAAAAAAC%2FwTAMQ4CIAwF0Lv82aEFCoURE2cXY1xbwAOYmBjC3X0bLuwSA9fqsiYpLSt1UTJXZxuKtvFFQ368P88efvdx69dXN1ww0bhI4qwl0jn%2FAAAA%2F%2F%2BeJCNDTAAAAA%3D%3D; __zzatw-avito=MDA0dBA=Fz2+aQ==; cfidsw-avito=QYm16AHuB6KwYQobrxAJOq1jadvPuI5M+9QXSVCsyNVrM8vJdrVuxYl8zQQPvuQTXqr7OjB2rKF71dm/P3chhOx+vRWdszwkfX80gqsv76N6yeD9uDnAIOugJyWK/WtuFLTWOXLHqdPxgxKTmBTkr3N1354nq9eSBRmtvQ==; sessid=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTQxNjg3NDEsImlhdCI6MTc1NDA4MjM0MSwidSI6MzcxNjc1NDIwLCJwIjozMDI2MjE3NDQsInMiOiI4MmU5MDgzNmNmODZjZmQwYjAwNWE2YWMzOGQ1Mzg1MS4xNzU0MDgyMzQxIiwiaCI6IjIxZTY4MWZiODc2ZjQ3Y2JhNjJmZTNjYjVhYjczNDE2XzE3NTQwODIzNDEiLCJ2IjpmYWxzZSwiZXh0cmEiOm51bGx9.7IEbByejpQo3eF9IA-NdpqrkTd_hzYbH_6oDh2BOQE_2T6TJB-L9C4doF4arYzlQwzutBIwY88EN2wOLMaeQMw; rt=f69186804cc5258915f288396c402231; pageviewCount=20; cssid=589721b4-72d2-448d-99d2-a517150af41d; cssid_exp=1754084523740; adrcid=ABXQRXPb30GOcnLtejF5JNQ; uxs_uid=2cc87ef0-6f1c-11f0-b681-f5642d58a02e; _mlocation=621540; _mlocation_mode=default; cartCounter=0; domain_sid=JX2s7d4yUaU3LHrMnwrib%3A1754082725822; _avisc=LWprp5qv2MqLlI0cj4fPn+cDerhCRMEHfBN81dJjIyo=; _inlines_order=params[504].params[550].price.params[2951].params[110710].categoryNodes.locationGroup.sort; pageviewCount=22; _ga_M29JC28873=GS2.1.s1754081936$o2$g1$t1754082938$j44$l0$h0; tmr_detect=0%7C1754082941180; csprefid=11b3ab3f-565a-4bec-8482-744e8e22102a'
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
                for item in response.json()['result']['items']
                if item['type'] == 'item'
            ]
            return items

        except:
            return []

    
    def get_offer_datetime(self, offer: Dict):
        time = datetime.datetime.fromtimestamp(offer['value']['time']) 
        return time
    
    def get_notification_message(self, offer: Dict):
        message = 'Появилось новое объявление на Avito: {url}'
        offer_uri = offer['value']['uri_mweb']  
        offer_url = self.offer_url.format(offer_uri=offer_uri)

        return message.format(url=offer_url)
    