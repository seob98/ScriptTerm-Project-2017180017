from Equipment import *

class Character:
    def __init__(self, characterName, itemMaxLevel):
        self.CharacterName = characterName
        self.ItemMaxLevel = itemMaxLevel
        self.Image = None
        self.Equipments = { '투구': Equipment('', True, 0,0, None), '상의': Equipment('', False, 0,0, None), '하의': Equipment('', False, 0,0, None),
                            '장갑': Equipment('', False, 0,0, None), '어깨': Equipment('', False, 0,0, None), '무기': Equipment('', False, 0,0, None)}

    def SetImage(self, image):
        self.Image = image

    def SetEquipment(self, itemType, itemName, enhanceLv, itemLv, imageURL):
        if itemType == '무기':
            self.Equipments[itemType] = Equipment(itemName, True, enhanceLv, itemLv , imageURL)
        else:
            self.Equipments[itemType] = Equipment(itemName, False, enhanceLv, itemLv, imageURL)

        #name, isWeapon, enhanceLv, itemLv

    def GetItemLv(self, partsName):
        if partsName in self.Equipments:
            return self.Equipments[partsName].ItemLv
        else:
            return None

    def GetEnhanceLv(self, partsName):
        if partsName in self.Equipments:
            return self.Equipments[partsName].EnhanceLv
        else:
            return None


