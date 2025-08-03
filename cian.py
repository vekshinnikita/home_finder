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
                        "type": "underground",
                        "id": 171
                    },
                    {
                        "type": "underground",
                        "id": 172
                    },
                    {
                        "type": "underground",
                        "id": 173
                    },
                    {
                        "type": "underground",
                        "id": 174
                    },
                    {
                        "type": "underground",
                        "id": 175
                    },
                    {
                        "type": "underground",
                        "id": 176
                    },
                    {
                        "type": "underground",
                        "id": 177
                    },
                    {
                        "type": "underground",
                        "id": 178
                    },
                    {
                        "type": "underground",
                        "id": 179
                    },
                    {
                        "type": "underground",
                        "id": 180
                    },
                    {
                        "type": "underground",
                        "id": 181
                    },
                    {
                        "type": "underground",
                        "id": 182
                    },
                    {
                        "type": "underground",
                        "id": 191
                    },
                    {
                        "type": "underground",
                        "id": 192
                    },
                    {
                        "type": "underground",
                        "id": 193
                    },
                    {
                        "type": "underground",
                        "id": 194
                    },
                    {
                        "type": "underground",
                        "id": 195
                    },
                    {
                        "type": "underground",
                        "id": 197
                    },
                    {
                        "type": "underground",
                        "id": 198
                    },
                    {
                        "type": "underground",
                        "id": 199
                    },
                    {
                        "type": "underground",
                        "id": 200
                    },
                    {
                        "type": "underground",
                        "id": 201
                    },
                    {
                        "type": "underground",
                        "id": 202
                    },
                    {
                        "type": "underground",
                        "id": 204
                    },
                    {
                        "type": "underground",
                        "id": 205
                    },
                    {
                        "type": "underground",
                        "id": 206
                    },
                    {
                        "type": "underground",
                        "id": 207
                    },
                    {
                        "type": "underground",
                        "id": 208
                    },
                    {
                        "type": "underground",
                        "id": 210
                    },
                    {
                        "type": "underground",
                        "id": 211
                    },
                    {
                        "type": "underground",
                        "id": 212
                    },
                    {
                        "type": "underground",
                        "id": 213
                    },
                    {
                        "type": "underground",
                        "id": 214
                    },
                    {
                        "type": "underground",
                        "id": 218
                    },
                    {
                        "type": "underground",
                        "id": 219
                    },
                    {
                        "type": "underground",
                        "id": 220
                    },
                    {
                        "type": "underground",
                        "id": 221
                    },
                    {
                        "type": "underground",
                        "id": 222
                    },
                    {
                        "type": "underground",
                        "id": 224
                    },
                    {
                        "type": "underground",
                        "id": 225
                    },
                    {
                        "type": "underground",
                        "id": 226
                    },
                    {
                        "type": "underground",
                        "id": 227
                    },
                    {
                        "type": "underground",
                        "id": 230
                    },
                    {
                        "type": "underground",
                        "id": 231
                    },
                    {
                        "type": "underground",
                        "id": 232
                    },
                    {
                        "type": "underground",
                        "id": 241
                    },
                    {
                        "type": "underground",
                        "id": 242
                    },
                    {
                        "type": "underground",
                        "id": 246
                    },
                    {
                        "type": "underground",
                        "id": 247
                    },
                    {
                        "type": "underground",
                        "id": 355
                    },
                    {
                        "type": "underground",
                        "id": 356
                    },
                    {
                        "type": "underground",
                        "id": 357
                    },
                    {
                        "type": "underground",
                        "id": 382
                    }
                ]
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
            "floor": {
                "type": "range",
                "value": {
                    "gte": 2
                }
            },
            "publish_period": {
                "type": "term",
                "value": -2
            },
            "saved_search_id": {
                "type": "term",
                "value": 51623902
            },
            "for_day": {
                "type": "term",
                "value": "0"
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
            hour=int(time_split[0]),
            minute=int(time_split[1])
        )
        return datetime

    def get_notification_message(self, offer: Dict):
        message = 'Появилось новое объявление на ЦИАН: {url}'
        offer_id = offer['id']
        offer_url = self.offer_url.format(id=offer_id)

        return message.format(url=offer_url)
