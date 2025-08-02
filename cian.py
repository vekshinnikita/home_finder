import datetime
import json
from typing import Dict
import requests
from base import BaseFinder, FinderABC
from utils import get_date_from_string



class CianFinder(BaseFinder):
    
    url = 'https://api.cian.ru/search-offers/v3/search-offers-desktop/'
    offer_url = 'https://spb.cian.ru/rent/flat/{id}/'
    filter = {
        "jsonQuery": {
            "_type": "flatrent",
            "sort": {
            "type": "term",
            "value": "creation_date_desc"
            },
            "engine_version": {
            "type": "term",
            "value": 2
            },
            "price": {
            "type": "range",
            "value": {
                "gte": 25000,
                "lte": 35000
            }
            },
            "currency": {
            "type": "term",
            "value": 2
            },
            "geo": {
            "type": "geo",
            "value": [
                {
                "type": "polygon",
                "name": "Область поиска",
                "coordinates": [
                    [
                    "30.3163868",
                    "60.0530472"
                    ],
                    [
                    "30.2806812",
                    "60.0489117"
                    ],
                    [
                    "30.2504688",
                    "60.0378838"
                    ],
                    [
                    "30.2243763",
                    "60.0254774"
                    ],
                    [
                    "30.2037769",
                    "60.0116924"
                    ],
                    [
                    "30.1955372",
                    "59.9951505"
                    ],
                    [
                    "30.1872974",
                    "59.9786087"
                    ],
                    [
                    "30.1818043",
                    "59.9593098"
                    ],
                    [
                    "30.1859242",
                    "59.9420786"
                    ],
                    [
                    "30.2024036",
                    "59.926226"
                    ],
                    [
                    "30.2257496",
                    "59.9145088"
                    ],
                    [
                    "30.255962",
                    "59.9048594"
                    ],
                    [
                    "30.2724415",
                    "59.8903852"
                    ],
                    [
                    "30.2930409",
                    "59.8772895"
                    ],
                    [
                    "30.2944141",
                    "59.8600584"
                    ],
                    [
                    "30.288921",
                    "59.8435165"
                    ],
                    [
                    "30.2930409",
                    "59.8269746"
                    ],
                    [
                    "30.3122669",
                    "59.8118112"
                    ],
                    [
                    "30.3452259",
                    "59.808365"
                    ],
                    [
                    "30.3795582",
                    "59.8076757"
                    ],
                    [
                    "30.4111439",
                    "59.8138789"
                    ],
                    [
                    "30.439983",
                    "59.8228391"
                    ],
                    [
                    "30.4674488",
                    "59.8331778"
                    ],
                    [
                    "30.5004078",
                    "59.8324886"
                    ],
                    [
                    "30.5292469",
                    "59.8242176"
                    ],
                    [
                    "30.5622059",
                    "59.8262854"
                    ],
                    [
                    "30.5306202",
                    "59.8324886"
                    ],
                    [
                    "30.5100208",
                    "59.8455842"
                    ],
                    [
                    "30.505901",
                    "59.8628154"
                    ],
                    [
                    "30.4949146",
                    "59.8793573"
                    ],
                    [
                    "30.482555",
                    "59.8952099"
                    ],
                    [
                    "30.4784351",
                    "59.9124411"
                    ],
                    [
                    "30.4743153",
                    "59.9296722"
                    ],
                    [
                    "30.4756886",
                    "59.9462141"
                    ],
                    [
                    "30.4798084",
                    "59.962756"
                    ],
                    [
                    "30.4633289",
                    "59.9792979"
                    ],
                    [
                    "30.4468495",
                    "59.9972183"
                    ],
                    [
                    "30.4289967",
                    "60.0116924"
                    ],
                    [
                    "30.4193836",
                    "60.0296128"
                    ],
                    [
                    "30.3919178",
                    "60.046844"
                    ],
                    [
                    "30.3658253",
                    "60.0571827"
                    ],
                    [
                    "30.3328663",
                    "60.0599396"
                    ],
                    [
                    "30.2999073",
                    "60.0551149"
                    ],
                    [
                    "30.3163868",
                    "60.0530472"
                    ]
                ]
                }
            ]
            },
            "bbox": {
            "type": "term",
            "value": [
                [
                30.1987187088,
                59.7513631609
                ],
                [
                30.7755009354,
                59.8808716541
                ]
            ]
            },
            "floorn": {
            "type": "range",
            "value": {
                "gte": 2
            }
            },
            "saved_search_id": {
            "type": "term",
            "value": 51596133
            },
            "for_day": {
            "type": "term",
            "value": "!1"
            },
            "repair": {
            "type": "terms",
            "value": [
                3,
                4
            ]
            },
            "room": {
            "type": "terms",
            "value": [
                1,
                9
            ]
            }
        }
        }

    def get_offers(self):
        print(f'Request Cian')
        response = requests.post(
            self.url,
            json=self.filter,
        )
        
        try:
            return response.json().get('offers', [])
        except:
            print(response.text)
            return []
    
    def get_offer_datetime(self, offer: Dict):
        datetime = get_date_from_string(offer['data']['updatedOn'])
        time_split = offer['data']['updatedAt'].split(',')[1].split(':')

        datetime = datetime.replace(
            hour = int(time_split[0]),
            minute = int(time_split[1])
        )
        return datetime
    
    def get_notification_message(self, offer: Dict):
        message = 'Появилось новое объявление на ЦИАН: {url}'
        offer_id = offer['id']  
        offer_url = self.offer_url.format(id=offer_id)

        return message.format(url=offer_url)
    
