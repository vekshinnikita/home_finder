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
            "region": {
                "type": "terms",
                "value": [
                    2
                ]
            },
            "price": {
                "type": "range",
                "value": {
                    "lte": 40000
                }
            },
            "currency": {
                "type": "term",
                "value": 2
            },
            "foot_min": {
                "type": "range",
                "value": {
                    "lte": 20
                }
            },
            "only_foot": {
                "type": "term",
                "value": "2"
            },
            "publish_period": {
                "type": "term",
                "value": 604800
            },
            "saved_search_id": {
                "type": "term",
                "value": 45952085
            },
            "with_neighbors": {
                "type": "term",
                "value": True
            },
            "outdated_repair": {
                "type": "term",
                "value": False
            },
            "for_day": {
                "type": "term",
                "value": "!1"
            },
            "repair": {
                "type": "terms",
                "value": [
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
            "bbox": {
                "type": "term",
                "value": [
                    [
                        30.759691,
                        60.244837
                    ],
                    [
                        29.42981,
                        59.633783
                    ]
                ]
            },
            "sort": {
                "type": "term",
                "value": "creation_date_desc"
            }
        }
    }

    last_offer_update=None

    def get_offers(self):
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
    
