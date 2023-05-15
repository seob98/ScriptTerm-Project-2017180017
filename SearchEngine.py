import requests
import json

class SearchEngine:
    def __init__(self):
        self.JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAyNDExNDEifQ.CnRxSAg-TY9NwH8bhQ1MpTJQqwp-OETq5GxdiX_KKeK1POuQaHBwsW_U9YQgfrLiHU_nUaYZbm3RftSxW_k16OR-1k_Rq-ru2Du6LKywpOSgBfRBJFNkSVCJkox1MEhCG3c11N1HEiOjvuVymR8ha0qt9T-G416A0zmiP3dXX5wcXM2Qz9xausJaXxoVI9day180FJbAMumA4SRWnFrHKmBsIkLBMCq6jEwF62dK7bm3g6S2Q2ZA8nXChVwVye6-BNHtFKY75q5F7XwIK9GHuZCIu_KdVd8dafn83ERny5R8g3Ves5vLIrGf2SJY-Xqp9hA6Ed5zStY0cD9BqLLRiA'
        self.urls = {
            'market_option': 'https://developer-lostark.game.onstove.com/markets/options',
            'siblings': 'https://developer-lostark.game.onstove.com/characters/%EB%A6%B0%ED%8B%B0%EC%95%88/siblings',
            'character' : 'https://developer-lostark.game.onstove.com/armories/characters/%EB%A6%B0%ED%8B%B0%EC%95%88',
            'market': 'https://developer-lostark.game.onstove.com/markets/search' }
        self.headers = {
            "accept": "application/json",
            "authorization": "Bearer " +self.JWT_TOKEN,
            "Content-Type": "application/json" }
        self.categoriesCode = {}

        response = requests.get(self.urls['market_option'], headers=self.headers)
        options = response.json()

        # check status code
        if response.status_code == 200:
            pass
        else:
            print(f"Request failed with status code {response.status_code}")
            return
        categories_data = response.json()['Categories']

        for category in categories_data:
            if not category['Subs']:
                self.categoriesCode[category['CodeName']] = category['Code']
            else:
                for sub in category['Subs']:
                    self.categoriesCode[sub['CodeName']] = sub['Code']

        print(self.categoriesCode)
