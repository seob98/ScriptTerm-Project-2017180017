import requests
import json
from urllib.parse import quote
from HoningMat import *
from Character import *
import re

class SearchEngine:
    def __init__(self):
        self.JWT_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAyNDExNDEifQ.CnRxSAg-TY9NwH8bhQ1MpTJQqwp-OETq5GxdiX_KKeK1POuQaHBwsW_U9YQgfrLiHU_nUaYZbm3RftSxW_k16OR-1k_Rq-ru2Du6LKywpOSgBfRBJFNkSVCJkox1MEhCG3c11N1HEiOjvuVymR8ha0qt9T-G416A0zmiP3dXX5wcXM2Qz9xausJaXxoVI9day180FJbAMumA4SRWnFrHKmBsIkLBMCq6jEwF62dK7bm3g6S2Q2ZA8nXChVwVye6-BNHtFKY75q5F7XwIK9GHuZCIu_KdVd8dafn83ERny5R8g3Ves5vLIrGf2SJY-Xqp9hA6Ed5zStY0cD9BqLLRiA'
        self.urls = {
            'market_option': 'https://developer-lostark.game.onstove.com/markets/options',
            'raid_team': 'https://developer-lostark.game.onstove.com/characters/%EB%A6%B0%ED%8B%B0%EC%95%88/siblings',
            'character' : 'https://developer-lostark.game.onstove.com/armories/characters/%EB%A6%B0%ED%8B%B0%EC%95%88',
            'character_equipment': 'https://developer-lostark.game.onstove.com/armories/characters/%EB%A6%B0%ED%8B%B0%EC%95%88',
            'market': 'https://developer-lostark.game.onstove.com/markets/items',
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

        self.SearchEveryHoningItem()

    def SearchRaidTeam(self, character_name):
        self.raidTeam_Info = []
        character_name = quote(character_name)
        url = self.urls['raid_team'].replace('%EB%A6%B0%ED%8B%B0%EC%95%88', character_name)     # 캐릭터 이름을 url에 적용
        response = requests.get(url, headers=self.headers)                                      # url에 대한 요청 수행

        if response.status_code == 200:
            data = response.json()
            self.raidTeam_Info = [Character(character['CharacterName'], character['ItemMaxLevel']) for character in data]        # 캐릭터 이름과 아이템 최대 레벨만 저장하는 리스트 생성
        else:
            print(f"Request failed with status code {response.status_code}")

    def RemoveCharacterWithNoImage(self):
        self.raidTeam_Info = [character for character in self.raidTeam_Info if character.Image is not None]

    def AddCharacterImage(self):  # 이미지가 NONE인놈은 원정대에서 추방
        for character in self.raidTeam_Info:
            url = self.urls['character_equipment'].replace('%EB%A6%B0%ED%8B%B0%EC%95%88',
                                                           character.CharacterName)  # 캐릭터 이름을 url에 적용
            response = requests.get(url, headers=self.headers)  # url에 대한 요청 수행

            if response.status_code == 200:
                data = response.json()
                character.SetImage(data['ArmoryProfile']['CharacterImage'])         #캐릭터 이미지 기록 완료
                if data['ArmoryProfile']['CharacterImage'] == None:
                    continue

                for i, equipment in enumerate(data['ArmoryEquipment']):
                    validTypes = ['무기', '투구', '상의', '하의', '장갑', '어깨']
                    itemName = equipment['Name']                    # itemName Here
                    itemType = equipment['Type']                    # itemType Here
                    imageURL = equipment['Icon']
                    if itemType not in validTypes:
                        continue
                    tooltip = equipment['Tooltip']
                    tooltip_data_str = tooltip.replace('\r\n', '').replace('\\', '')
                    tooltip_data = json.loads(tooltip_data_str)  # parse
                    item_level_str = tooltip_data['Element_001']['value']['leftStr2']
                    itemLv = int(item_level_str.split(' ')[3])          # itemLv Here
                    match = re.search(r'\+(\d+)', itemName)
                    if match:
                         enhanceLv = int(match.group(1))                # enhanceLv Here
                    else:
                        enhanceLv = 0  # 강화레벨 0을 위한 예외처리
                    character.SetEquipment(itemType, itemName, enhanceLv, itemLv, imageURL)
            else:
                print(f"Request failed with status code {response.status_code}")
        self.RemoveCharacterWithNoImage()
        print(self.raidTeam_Info)

    def SearchHoningItem(self, category_name, item_tier, item_name):
        if category_name not in self.categoriesCode:
            print(f"{category_name} is not a valid category name")
            return

        category_code = self.categoriesCode[category_name]
        data = {
            "Sort": "GRADE",
            "CategoryCode": category_code,
            "CharacterClass": None,
            "ItemTier": item_tier,
            "ItemGrade": None,
            "ItemName": item_name,
            "PageNo": 0,
            "SortCondition": "ASC"
        }

        response = requests.post(self.urls['market'], headers=self.headers, data=json.dumps(data))

        if response.status_code == 200:
            items = response.json()['Items']
            for i in items:
                name = i['Name']
                icon = i['Icon']
                yDayAvgPrice = i['YDayAvgPrice']
                recentPrice = i['RecentPrice']
                currentMinPrice = i['CurrentMinPrice']
                item_obj = HoningMat(name, icon, yDayAvgPrice, recentPrice, currentMinPrice)
                self.honingMat_Info[name] = item_obj
                print(f"Added item: {item_obj.Name}, Icon: {item_obj.Icon}, Yesterday Average Price: {item_obj.YDayAvgPrice}, Recent Price: {item_obj.RecentPrice}, Current Min Price: {item_obj.CurrentMinPrice}")
        else:
            print(f"Request failed with status code {response.status_code}")

    def SearchEveryHoningItem(self):    #돌파석
        self.SearchHoningItem('재련 재료', 3, '명예의 돌파석')
        self.SearchHoningItem('재련 재료', 3, '위대한 명예의 돌파석')
        self.SearchHoningItem('재련 재료', 3, '경이로운 명예의 돌파석')
        self.SearchHoningItem('재련 재료', 3, '찬란한 명예의 돌파석')
                                        #수호석
        self.SearchHoningItem('재련 재료', 3, '수호석 결정')
        self.SearchHoningItem('재련 재료', 3, '수호강석')
        self.SearchHoningItem('재련 재료', 3, '정제된 수호강석')
                                        #파괴석
        self.SearchHoningItem('재련 재료', 3, '파괴석 결정')
        self.SearchHoningItem('재련 재료', 3, '파괴강석')
        self.SearchHoningItem('재련 재료', 3, '정제된 파괴강석')
                                        #오레하
        self.SearchHoningItem('재련 재료', 3, '하급 오레하 융화제')
        self.SearchHoningItem('재련 재료', 3, '중급 오레하 융화제')
        self.SearchHoningItem('재련 재료', 3, '상급 오레하 융화제')
        self.SearchHoningItem('재련 재료', 3, '최상급 오레하 융화제')
                                        #책(숨결)
        self.SearchHoningItem('재련 추가 재료', 3, '태양의 은총')
        self.SearchHoningItem('재련 추가 재료', 3, '태양의 축복')
        self.SearchHoningItem('재련 추가 재료', 3, '태양의 가호')
                                        #책(방어구)
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 수선 기본')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 수선 응용')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 수선 심화')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 수선 숙련')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 수선 특화')
                                        #책(무기)
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 단조 기본')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 단조 응용')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 단조 심화')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 단조 숙련')
        self.SearchHoningItem('재련 추가 재료', 3, '재봉술 : 단조 특화')

    def GetCharacter(self, character_name):
        for character in self.raidTeam_Info:
            if character.CharacterName == character_name:
                return character
        return None







