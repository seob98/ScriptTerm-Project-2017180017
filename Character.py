class Character:
    def __init__(self, characterName, itemMaxLevel):
        self.CharacterName = characterName
        self.ItemMaxLevel = itemMaxLevel
        self.CharacterImage = ''
        self.EquipLv ={ '투구': 0, '상의': 0, '하의': 0, '장갑': 0, '어깨': 0, '무기': 0}

    def SetImageAndEquipLv(self, characterImage, helmetLevel, topLevel, bottomLevel, glovesLevel, shouldersLevel, weaponLevel):
        self.CharacterImage = characterImage
        self.EquipLv['투구'] = helmetLevel
        self.EquipLv['상의'] = topLevel
        self.EquipLv['하의'] = bottomLevel
        self.EquipLv['장갑'] = glovesLevel
        self.EquipLv['어깨'] = shouldersLevel
        self.EquipLv['무기'] = weaponLevel