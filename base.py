from abc import ABC, abstractmethod
from typing import Dict, List


class FinderABC(ABC):

    @abstractmethod
    def get_offers(self) -> List[Dict]:
        ...
    
    @abstractmethod
    def get_notification_message(self, offer: Dict):
        ...

    @abstractmethod
    def get_offer_datetime(self, offer: Dict):
        ...

    @abstractmethod
    def find(self):
        ...


class BaseFinder(FinderABC):
    
    last_offer_update=None

    def _check_is_new(self, offer: Dict):
        offer_update = self.get_offer_datetime(offer) 

        return self.last_offer_update is not None and\
            self.last_offer_update < offer_update
    
    def find(self):
        offers = self.get_offers()
        if not offers:
            return []
        
        notifications = []
        
        for offer in offers:
            if self._check_is_new(offer):
                notifications.append(self.get_notification_message(offer))
            else:
                break
            
        
        if self.last_offer_update is None or notifications:
            self.last_offer_update = self.get_offer_datetime(offers[0]) 

        return notifications