import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        headers={'X-Api-Key': api_key}
        r=requests.get(f'{self.get_url()}SocialNumber',headers=headers)
        return r.json()
ans=SocialNumber()
print(ans.get_SocialNumber('7b3b6035a5c94aee8908aaa68c9a6fe4'))
