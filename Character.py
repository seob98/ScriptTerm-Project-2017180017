class Character:
    def __init__(self, characterName, itemMaxLevel):
        self.CharacterName = characterName
        self.ItemMaxLevel = itemMaxLevel
        self.CharacterImage = ''
        self.EquipLv = { '투구': [0, 0], '상의': [0, 0], '하의': [0, 0], '장갑': [0, 0], '어깨': [0, 0], '무기': [0, 0]}

    def SetImageAndEquipLv(self, characterImage, helmetEnhanceLv, topEnhanceLv, bottomEnhanceLv, glovesEnhanceLv, shouldersEnhanceLv, weaponEnhanceLv,
                           helmetItemLv, topItemLv, bottomItemLv, glovesItemLv, shouldersItemLv, weaponItemLv):
        self.CharacterImage = characterImage
        self.EquipLv = {
            '투구': {'강화 레벨': helmetEnhanceLv, '아이템 레벨': helmetItemLv },
            '상의': {'강화 레벨': topEnhanceLv, '아이템 레벨': topItemLv},
            '하의': {'강화 레벨': bottomEnhanceLv, '아이템 레벨': bottomItemLv},
            '장갑': {'강화 레벨': glovesEnhanceLv, '아이템 레벨': glovesItemLv},
            '어깨': {'강화 레벨': shouldersEnhanceLv, '아이템 레벨': shouldersItemLv},
            '무기': {'강화 레벨': weaponEnhanceLv, '아이템 레벨': weaponItemLv}
        }

    def GetItemLv(self, partsName):
        if partsName in self.EquipLv:
            return self.EquipLv[partsName]['아이템 레벨']
        else:
            return None

    def GetEnhanceLv(self, partsName):
        if partsName in self.EquipLv:
            return self.EquipLv[partsName]['강화 레벨']
        else:
            return None


