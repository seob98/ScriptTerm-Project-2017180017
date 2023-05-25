from Equipment import *

class Character:
    def __init__(self, characterName, itemMaxLevel):
        self.CharacterName = characterName
        self.ItemMaxLevel = itemMaxLevel
        self.Image = None
        self.Equipments = { '투구': Equipment('', True, 0,0), '상의': Equipment('', False, 0,0), '하의': Equipment('', False, 0,0),
                            '장갑': Equipment('', False, 0,0), '어깨': Equipment('', False, 0,0), '무기': Equipment('', False, 0,0)}

    def SetImage(self, image):
        self.Image = image

    def SetEquipment(self, itemType, itemName, EnhanceLv, itemLv):
        equipment = self.Equipments[itemType]
        equipment.Name = itemName
        equipment.EnhanceLv = EnhanceLv
        equipment.ItemLv = itemLv

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


