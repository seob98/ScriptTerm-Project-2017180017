import requests
import json
from urllib.parse import quote

class SearchEngine:
    def __init__(self):
        self.JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAyNDExNDEifQ.CnRxSAg-TY9NwH8bhQ1MpTJQqwp-OETq5GxdiX_KKeK1POuQaHBwsW_U9YQgfrLiHU_nUaYZbm3RftSxW_k16OR-1k_Rq-ru2Du6LKywpOSgBfRBJFNkSVCJkox1MEhCG3c11N1HEiOjvuVymR8ha0qt9T-G416A0zmiP3dXX5wcXM2Qz9xausJaXxoVI9day180FJbAMumA4SRWnFrHKmBsIkLBMCq6jEwF62dK7bm3g6S2Q2ZA8nXChVwVye6-BNHtFKY75q5F7XwIK9GHuZCIu_KdVd8dafn83ERny5R8g3Ves5vLIrGf2SJY-Xqp9hA6Ed5zStY0cD9BqLLRiA'
        self.urls = {
            'market_option': 'https://developer-lostark.game.onstove.com/markets/options',
            'raid_team': 'https://developer-lostark.game.onstove.com/characters/%EB%A6%B0%ED%8B%B0%EC%95%88/siblings',
            'character' : 'https://developer-lostark.game.onstove.com/armories/characters/%EB%A6%B0%ED%8B%B0%EC%95%88',
            'market': 'https://developer-lostark.game.onstove.com/markets/search',
            'profiles' : 'https://developer-lostark.game.onstove.com/armories/characters/%EB%A6%B0%ED%8B%B0%EC%95%88/profiles'
        }
        self.headers = {
            "accept": "application/json",
            "authorization": "Bearer " +self.JWT_TOKEN,
            "Content-Type": "application/json" }
        self.categoriesCode = {}        #'장비 상자' : 10100 등이 저장되어 있다.
        self.raidTeam_Info = []         #캐릭터 이름, 아이템레벨, 이미지를 담고 있다.
        self.honingMat_Info = {}

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

    def SearchRaidTeam(self, character_name):
        self.raidTeam_Info = []
        character_name = quote(character_name)
        url = self.urls['raid_team'].replace('%EB%A6%B0%ED%8B%B0%EC%95%88', character_name)      # 캐릭터 이름을 url에 적용
        response = requests.get(url, headers=self.headers)                                      # url에 대한 요청 수행

        if response.status_code == 200:
            data = response.json()
            self.raidTeam_Info = [{'CharacterName': character['CharacterName'], 'ItemMaxLevel': character['ItemMaxLevel']}
                                  for character in data]        # 캐릭터 이름과 아이템 최대 레벨만 저장하는 리스트 생성
        else:
            print(f"Request failed with status code {response.status_code}")

    def RemoveCharacterWithNoImage(self):
        self.raidTeam_Info = [character for character in self.raidTeam_Info if character['image'] is not None]

    def AddCharacterImages(self):   #이미지가 NONE인놈은 원정대에서 추방
        for character in self.raidTeam_Info:
            url = self.urls['profiles'].replace('%EB%A6%B0%ED%8B%B0%EC%95%88', character['CharacterName'])  # 캐릭터 이름을 url에 적용
            response = requests.get(url, headers=self.headers)                                              # url에 대한 요청 수행

            if response.status_code == 200:
                data = response.json()
                character['image'] = data['CharacterImage']        # 이미지 URL을 characterInfo에 추가
            else:
                print(f"Request failed with status code {response.status_code}")

        self.RemoveCharacterWithNoImage()
        print(self.raidTeam_Info)

    def SearchHoningItems(self):
        HoningMatCategory = self.categoriesCode['재련 재료']
        AdditionalHoningMatCategory = self.categoriesCode['재련 추가 재료']




