from base import BaseFinder


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
            "lte": 35000
        }
        },
        "currency": {
        "type": "term",
        "value": 2
        },
        "foot_min": {
        "type": "range",
        "value": {
            "lte": 25
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
        "value": 45900301
        },
        "with_neighbors": {
        "type": "term",
        "value": False
        },
        "outdated_repair": {
        "type": "term",
        "value": False
        },
        "for_day": {
        "type": "term",
        "value": "!1"
        },
        "pets": {
        "type": "term",
        "value": True
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
            1
        ]
        },
        "sort": {
        "type": "term",
        "value": "creation_date_desc"
        }
    }
    }

    last_offer_update=datetime.datetime(2024,9,16,10,10,10)

    def get_offers(self):
        response = requests.post(
            self.url,
            json=self.filter,
        )

        return response.json().get('offers', [])
    
    def get_offer_datetime(self, offer: Dict):
        return get_date_from_string(offer['data']['updatedOn'])
    
    def get_notification_message(self, offer: Dict):
        message = 'Появилось новое объявление на ЦИАН: {url}'
        offer_id = offer['id']  
        offer_url = self.offer_url.format(id=offer_id)

        return message.format(url=offer_url)
    