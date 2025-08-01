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
            "engine_version": {
            "type": "term",
            "value": 2
            },
            "price": {
            "type": "range",
            "value": {
                "gte": 25000,
                "lte": 40000
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
                    "30.3445069",
                    "60.035514"
                    ],
                    [
                    "30.2895752",
                    "60.035514"
                    ],
                    [
                    "30.2428833",
                    "60.035514"
                    ],
                    [
                    "30.1906983",
                    "60.0348246"
                    ],
                    [
                    "30.1577393",
                    "60.0279305"
                    ],
                    [
                    "30.146753",
                    "60.0106953"
                    ],
                    [
                    "30.1508728",
                    "59.9934601"
                    ],
                    [
                    "30.1742188",
                    "59.9769142"
                    ],
                    [
                    "30.1906983",
                    "59.959679"
                    ],
                    [
                    "30.198938",
                    "59.9417544"
                    ],
                    [
                    "30.2030579",
                    "59.9252086"
                    ],
                    [
                    "30.2099243",
                    "59.9079733"
                    ],
                    [
                    "30.222284",
                    "59.8921169"
                    ],
                    [
                    "30.2360169",
                    "59.8762605"
                    ],
                    [
                    "30.2538697",
                    "59.8610935"
                    ],
                    [
                    "30.2799622",
                    "59.8507524"
                    ],
                    [
                    "30.3129212",
                    "59.8473054"
                    ],
                    [
                    "30.3362671",
                    "59.8355854"
                    ],
                    [
                    "30.3678528",
                    "59.8286913"
                    ],
                    [
                    "30.3994385",
                    "59.823176"
                    ],
                    [
                    "30.4310242",
                    "59.8280019"
                    ],
                    [
                    "30.4557434",
                    "59.8397219"
                    ],
                    [
                    "30.4887024",
                    "59.8438583"
                    ],
                    [
                    "30.5189148",
                    "59.8514418"
                    ],
                    [
                    "30.5202881",
                    "59.868677"
                    ],
                    [
                    "30.5147949",
                    "59.8852228"
                    ],
                    [
                    "30.4969422",
                    "59.8997004"
                    ],
                    [
                    "30.4763428",
                    "59.9127992"
                    ],
                    [
                    "30.4722229",
                    "59.929345"
                    ],
                    [
                    "30.4749695",
                    "59.9458908"
                    ],
                    [
                    "30.4763428",
                    "59.9658837"
                    ],
                    [
                    "30.4763428",
                    "59.9831189"
                    ],
                    [
                    "30.4502503",
                    "59.9969071"
                    ],
                    [
                    "30.4227845",
                    "60.0065588"
                    ],
                    [
                    "30.3884522",
                    "60.0100059"
                    ],
                    [
                    "30.3554932",
                    "60.0169"
                    ],
                    [
                    "30.3280274",
                    "60.0265517"
                    ],
                    [
                    "30.2991883",
                    "60.035514"
                    ],
                    [
                    "30.3445069",
                    "60.035514"
                    ]
                ]
                }
            ]
            },
            "bbox": {
            "type": "term",
            "value": [
                [
                29.7567383234,
                59.7939687858
                ],
                [
                30.9103027766,
                60.0645087033
                ]
            ]
            },
            "foot_min": {
            "type": "range",
            "value": {
                "lte": 15
            }
            },
            "only_foot": {
            "type": "term",
            "value": "2"
            },
            "floorn": {
            "type": "range",
            "value": {
                "gte": 2
            }
            },
            "for_day": {
            "type": "term",
            "value": "!1"
            },
            "repair": {
            "type": "terms",
            "value": [
                2,
                3
            ]
            },
            "room": {
            "type": "terms",
            "value": [
                1,
                2
            ]
            },
            "sort": {
            "type": "term",
            "value": "creation_date_desc"
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
    
