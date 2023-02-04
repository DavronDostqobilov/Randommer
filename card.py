import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        headers1={
            "X-Api-key":api_key
        }
        poyload1={
            "results":1
        }
        URL=self.get_url()
        URL=f'{URL}Card'
        r=requests.get(URL,headers=headers1,params=poyload1)
        data=r.json()
        return data['type']



    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        headers={'X-Api-key':api_key}

        url=self.get_url()
        r=requests.get(f'{url}Card/Types',headers=headers)
        return r.json()
Card=Card()
print(Card.get_card('7b3b6035a5c94aee8908aaa68c9a6fe4'))
print(Card.get_card_types('7b3b6035a5c94aee8908aaa68c9a6fe4'))


