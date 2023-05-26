class Equipment:
    Equip_1302 = {
        1: 1304,
        2: 1307,
        3: 1310,
        25: 1430,
    }
    for i in range(4, 25):
        Equip_1302[i] = 1310 + (i - 3) * 5

    Equip_1340 = {}
    for i in range(1, 26):
        if i <= 15:
            Equip_1340[i] = 1340 + i * 5
        elif 16 <= i <= 24:
            Equip_1340[i] = 1340 + 75 + (i - 15) * 15
        else:
            Equip_1340[i] = 1575

    Equip_1390 = {}
    for i in range(1, 21):
        Equip_1390[i] = 1390 + i * 10

    Equip_1525 = {}
    for i in range(1, 26):
        Equip_1525[i] = 1525 + i * 5        #장비 등급 분류

    def __init__(self, name, isWeapon, enhanceLv, itemLv, imageURL):
        self.Name = name
        self.IsWeapon = isWeapon
        self.EnhanceLv = enhanceLv
        self.ItemLv = itemLv
        self.ItemGrade = 0
        self.CheckItemGrade()
        self.ImageURL = imageURL
        self.Esther = False

    def CheckItemGrade(self):
        # Check if this item's level matches the level for its enhancement state in each dictionary
        if self.ItemLv == Equipment.Equip_1302.get(self.EnhanceLv):
            self.ItemGrade = 1302
        elif self.ItemLv == Equipment.Equip_1340.get(self.EnhanceLv):
            self.ItemGrade = 1340
        elif self.ItemLv == Equipment.Equip_1390.get(self.EnhanceLv):
            self.ItemGrade = 1390
        elif self.ItemLv == Equipment.Equip_1525.get(self.EnhanceLv):
            self.ItemGrade = 1525

    def GetRequiredMat(self):
        if self.Esther:
            return {'에스더'}, {'에스더'}

        if self.IsWeapon:
            if self.ItemGrade == 1302:
                return self.GetWeaponRequiredHoningMat_1302()
            elif self.ItemGrade == 1340:
                return self.GetWeaponRequiredHoningMat_1340()
            elif self.ItemGrade == 1390:
                return self.GetWeaponRequiredHoningMat_1390()
            elif self.ItemGrade == 1525:
                return self.GetWeaponRequiredHoningMat_1525()
        else:
            if self.ItemGrade == 1302:
                return self.GetArmorRequiredHoningMat_1302()
            elif self.ItemGrade == 1340:
                return self.GetArmorRequiredHoningMat_1340()
            elif self.ItemGrade == 1390:
                return self.GetArmorRequiredHoningMat_1390()
            elif self.ItemGrade == 1525:
                return self.GetArmorRequiredHoningMat_1525()

        return None, None


    def GetArmorRequiredHoningMat_1302(self):
        HoningMat = {}
        AdditionalHoingMat = {}
        if self.EnhanceLv in [6,7,8]:
            HoningMat['수호석 결정'] = 156
            HoningMat['명예의 돌파석'] = 4
            HoningMat['하급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 42
        elif self.EnhanceLv in [9,10,11]:
            HoningMat['수호석 결정'] = 192
            HoningMat['명예의 돌파석'] = 6
            HoningMat['하급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 50
        elif self.EnhanceLv in [12,13,14]:
            HoningMat['수호석 결정'] = 228
            HoningMat['명예의 돌파석'] = 8
            HoningMat['하급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 60
        elif self.EnhanceLv >= 15:
            HoningMat['계승'] = 1

        AdditionalHoingMat['재봉술 : 수선 기본'] = 1
        return HoningMat, AdditionalHoingMat

    def GetArmorRequiredHoningMat_1340(self):
        HoningMat = {}              #초반 유물
        AdditionalHoingMat = {}
        if self.EnhanceLv == 6:                     #목표 7
            HoningMat['수호석 결정'] = 162
            HoningMat['위대한 명예의 돌파석'] = 3
            HoningMat['중급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 43
        if self.EnhanceLv == 7:                     #목표 8
            HoningMat['수호석 결정'] = 162
            HoningMat['위대한 명예의 돌파석'] = 4
            HoningMat['중급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 43
        if self.EnhanceLv == 8:                     #목표 9
            HoningMat['수호석 결정'] = 162
            HoningMat['위대한 명예의 돌파석'] = 4
            HoningMat['중급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 43
        if self.EnhanceLv == 9:                     #목표 10
            HoningMat['수호석 결정'] = 199
            HoningMat['위대한 명예의 돌파석'] = 4
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 53
        if self.EnhanceLv == 10:                     #목표 11
            HoningMat['수호석 결정'] = 119
            HoningMat['위대한 명예의 돌파석'] = 4
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 53
        if self.EnhanceLv == 11:                     # 목표 12
            HoningMat['수호석 결정'] = 199
            HoningMat['위대한 명예의 돌파석'] = 5
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 53
        if self.EnhanceLv == 12:                     # 목표 13
            HoningMat['수호석 결정'] = 237
            HoningMat['위대한 명예의 돌파석'] = 5
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 63
        if self.EnhanceLv == 13:                     # 목표 14
            HoningMat['수호석 결정'] = 237
            HoningMat['위대한 명예의 돌파석'] = 5
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 63
        if self.EnhanceLv == 14:                     # 목표 15
            HoningMat['수호석 결정'] = 237
            HoningMat['위대한 명예의 돌파석'] = 5
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 63
        if self.EnhanceLv == 15:                     # 목표 16
            HoningMat['수호석 결정'] = 480
            HoningMat['위대한 명예의 돌파석'] = 10
            HoningMat['중급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 151
        if self.EnhanceLv == 16:                     # 목표 17
            HoningMat['수호석 결정'] = 480
            HoningMat['위대한 명예의 돌파석'] = 11
            HoningMat['중급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 204
        if self.EnhanceLv == 17:                     # 목표 18
            HoningMat['수호석 결정'] = 480
            HoningMat['위대한 명예의 돌파석'] = 11
            HoningMat['중급 오레하 융화 재료'] = 8
            HoningMat['명예의 파편'] = 277
        if self.EnhanceLv == 18:                     # 목표 19
            HoningMat['수호석 결정'] = 780
            HoningMat['위대한 명예의 돌파석'] = 18
            HoningMat['중급 오레하 융화 재료'] = 14
            HoningMat['명예의 파편'] = 536
            HoningMat['골드'] = 350
        if self.EnhanceLv == 19:                     # 목표 20
            HoningMat['수호석 결정'] = 780
            HoningMat['위대한 명예의 돌파석'] = 20
            HoningMat['중급 오레하 융화 재료'] = 14
            HoningMat['명예의 파편'] = 728
            HoningMat['골드'] = 350
        if self.EnhanceLv >= 20:                     #강화단계 : 20. 강화 멈추고 아브렐슈드 레이드로 진입
            HoningMat['계승'] = 1

        if self.EnhanceLv in range(6,15):
            AdditionalHoingMat['재봉술 : 수선 응용'] = 1

        return HoningMat, AdditionalHoingMat

    def GetArmorRequiredHoningMat_1390(self):
        HoningMat = {}
        AdditionalHoingMat = {}
        if self.EnhanceLv in [11,12]:       #목표 12,13
            HoningMat['수호강석'] = 390
            HoningMat['경이로운 명예의 돌파석'] = 11
            HoningMat['상급 오레하 융화 재료'] = 5
            HoningMat['명예의 파편'] = 600
            HoningMat['골드'] = 480
        elif self.EnhanceLv == 13:          #목표 14
            HoningMat['수호강석'] = 420
            HoningMat['경이로운 명예의 돌파석'] = 12
            HoningMat['상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 840
            HoningMat['골드'] = 520
        elif self.EnhanceLv == 14:          #목표 15
            HoningMat['수호강석'] = 450
            HoningMat['경이로운 명예의 돌파석'] = 12
            HoningMat['상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 840
            HoningMat['골드'] = 560
        elif self.EnhanceLv == 15:          #목표 16
            HoningMat['수호강석'] = 540
            HoningMat['경이로운 명예의 돌파석'] = 13
            HoningMat['상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 1440
            HoningMat['골드'] = 670
        elif self.EnhanceLv == 16:          #목표 17
            HoningMat['수호강석'] = 570
            HoningMat['경이로운 명예의 돌파석'] = 14
            HoningMat['상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 1440
            HoningMat['골드'] = 720
        elif self.EnhanceLv == 17:          #목표 18
            HoningMat['수호강석'] = 660
            HoningMat['경이로운 명예의 돌파석'] = 17
            HoningMat['상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 2160
            HoningMat['골드'] = 810
        elif self.EnhanceLv == 18:          #목표 19
            HoningMat['수호강석'] = 690
            HoningMat['경이로운 명예의 돌파석'] = 18
            HoningMat['상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 2160
            HoningMat['골드'] = 860
        elif self.EnhanceLv == 19:          #목표 20
            HoningMat['수호강석'] = 780
            HoningMat['경이로운 명예의 돌파석'] = 19
            HoningMat['상급 오레하 융화 재료'] = 18
            HoningMat['명예의 파편'] = 3000
            HoningMat['골드'] = 960
        elif self.EnhanceLv >= 20:          #강화단계 : 20. 강화 멈추고 일리아칸 레이드로 진입
            HoningMat['계승'] = 1


        if self.EnhanceLv in [11, 12]:                  # 숨결            목표 : 12~13
            AdditionalHoingMat['태양의 은총'] = 24
            AdditionalHoingMat['태양의 축복'] = 12
            AdditionalHoingMat['태양의 가호'] = 4
        elif self.EnhanceLv in range(13,19):            #                목표 : 14~19
            AdditionalHoingMat['태양의 은총'] = 36
            AdditionalHoingMat['태양의 축복'] = 18
            AdditionalHoingMat['태양의 가호'] = 6
        elif self.EnhanceLv >= 19:                      #                목표 : 20이상
            AdditionalHoingMat['태양의 은총'] = 48
            AdditionalHoingMat['태양의 축복'] = 24
            AdditionalHoingMat['태양의 가호'] = 8

        if self.EnhanceLv in range(12, 15):             # 책              목표 : 13~15
            AdditionalHoingMat['재봉술 : 수선 숙련'] = 1
        elif self.EnhanceLv in range(15, 19):           #                 목표 : 16~19
            AdditionalHoingMat['재봉술 : 수선 특화'] = 1

        return HoningMat, AdditionalHoingMat

    def GetArmorRequiredHoningMat_1525(self):
        HoningMat = {}
        AdditionalHoingMat = {}
        if self.EnhanceLv == 9:             #목표 10
            HoningMat['정제된 수호강석'] = 410
            HoningMat['찬란한 명예의 돌파석'] = 9
            HoningMat['최상급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 3500
            HoningMat['골드'] = 700
        elif self.EnhanceLv == 10:          #목표 11
            HoningMat['정제된 수호강석'] = 410
            HoningMat['찬란한 명예의 돌파석'] = 9
            HoningMat['최상급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 3500
            HoningMat['골드'] = 740
        elif self.EnhanceLv == 11:          #목표 12
            HoningMat['정제된 수호강석'] = 410
            HoningMat['찬란한 명예의 돌파석'] = 9
            HoningMat['최상급 오레하 융화 재료'] = 5
            HoningMat['명예의 파편'] = 4000
            HoningMat['골드'] = 770
        elif self.EnhanceLv == 12:          #목표 13
            HoningMat['정제된 수호강석'] = 460
            HoningMat['찬란한 명예의 돌파석'] = 12
            HoningMat['최상급 오레하 융화 재료'] = 5
            HoningMat['명예의 파편'] = 4000
            HoningMat['골드'] = 820
        elif self.EnhanceLv == 13:          #목표 14
            HoningMat['정제된 수호강석'] = 490
            HoningMat['찬란한 명예의 돌파석'] = 13
            HoningMat['최상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 4500
            HoningMat['골드'] = 860
        elif self.EnhanceLv == 14:          #목표 15
            HoningMat['정제된 수호강석'] = 550
            HoningMat['찬란한 명예의 돌파석'] = 14
            HoningMat['최상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 4500
            HoningMat['골드'] = 910
        elif self.EnhanceLv == 15:          #목표 16
            HoningMat['정제된 수호강석'] = 660
            HoningMat['찬란한 명예의 돌파석'] = 15
            HoningMat['최상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 5000
            HoningMat['골드'] = 970
        elif self.EnhanceLv == 16:          #목표 17
            HoningMat['정제된 수호강석'] = 730
            HoningMat['찬란한 명예의 돌파석'] = 18
            HoningMat['최상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 5000
            HoningMat['골드'] = 1030
        elif self.EnhanceLv == 17:          #목표 18
            HoningMat['정제된 수호강석'] = 770
            HoningMat['찬란한 명예의 돌파석'] = 19
            HoningMat['최상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 6000
            HoningMat['골드'] = 1100
        elif self.EnhanceLv == 18:          #목표 19
            HoningMat['정제된 수호강석'] = 810
            HoningMat['찬란한 명예의 돌파석'] = 21
            HoningMat['최상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 6000
            HoningMat['골드'] = 1190
        elif self.EnhanceLv == 19:          #목표 20
            HoningMat['정제된 수호강석'] = 940
            HoningMat['찬란한 명예의 돌파석'] = 23
            HoningMat['최상급 오레하 융화 재료'] = 18
            HoningMat['명예의 파편'] = 8000
            HoningMat['골드'] = 1290
        elif self.EnhanceLv == 20:          #목표 21
            HoningMat['정제된 수호강석'] = 1030
            HoningMat['찬란한 명예의 돌파석'] = 25
            HoningMat['최상급 오레하 융화 재료'] = 18
            HoningMat['명예의 파편'] = 9000
            HoningMat['골드'] = 1410
        elif self.EnhanceLv == 21:          #목표 22
            HoningMat['정제된 수호강석'] = 1120
            HoningMat['찬란한 명예의 돌파석'] = 28
            HoningMat['최상급 오레하 융화 재료'] = 18
            HoningMat['명예의 파편'] = 9000
            HoningMat['골드'] = 1560
        elif self.EnhanceLv == 22:          #목표 23
            HoningMat['정제된 수호강석'] = 1250
            HoningMat['찬란한 명예의 돌파석'] = 31
            HoningMat['최상급 오레하 융화 재료'] = 18
            HoningMat['명예의 파편'] = 11000
            HoningMat['골드'] = 1750
        elif self.EnhanceLv == 23:          #목표 24
            HoningMat['정제된 수호강석'] = 1460
            HoningMat['찬란한 명예의 돌파석'] = 35
            HoningMat['최상급 오레하 융화 재료'] = 27
            HoningMat['명예의 파편'] = 11000
            HoningMat['골드'] = 1970
        elif self.EnhanceLv == 24:          #목표 25
            HoningMat['정제된 수호강석'] = 1620
            HoningMat['찬란한 명예의 돌파석'] = 38
            HoningMat['최상급 오레하 융화 재료'] = 27
            HoningMat['명예의 파편'] = 11000
            HoningMat['골드'] = 2250

        if self.EnhanceLv in range(9, 13):              # 숨결        목표 : 10~13
            AdditionalHoingMat['태양의 은총'] = 24
            AdditionalHoingMat['태양의 축복'] = 12
            AdditionalHoingMat['태양의 가호'] = 4
        elif self.EnhanceLv in range(13,19):            #             목표 : 14~19
            AdditionalHoingMat['태양의 은총'] = 36
            AdditionalHoingMat['태양의 축복'] = 18
            AdditionalHoingMat['태양의 가호'] = 6
        elif self.EnhanceLv >= 19:                      #             목표 : 20이상
            AdditionalHoingMat['태양의 은총'] = 48
            AdditionalHoingMat['태양의 축복'] = 24
            AdditionalHoingMat['태양의 가호'] = 8

        return HoningMat, AdditionalHoingMat

    def GetWeaponRequiredHoningMat_1302(self):
        HoningMat = {}
        AdditionalHoingMat = {}
        if self.EnhanceLv in [6,7,8]:
            HoningMat['파괴석 결정'] = 129
            HoningMat['명예의 돌파석'] = 4
            HoningMat['하급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 30
        elif self.EnhanceLv in [9,10,11]:
            HoningMat['파괴석 결정'] = 160
            HoningMat['명예의 돌파석'] = 5
            HoningMat['하급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 37
        elif self.EnhanceLv in [12,13,14]:
            HoningMat['파괴석 결정'] = 190
            HoningMat['명예의 돌파석'] = 5
            HoningMat['하급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 44
        elif self.EnhanceLv >= 15:
            HoningMat['계승'] = 1

        AdditionalHoingMat['재봉술 : 단조 기본'] = 1
        return HoningMat, AdditionalHoingMat

    def GetWeaponRequiredHoningMat_1340(self):
        HoningMat = {}              #초반 유물
        AdditionalHoingMat = {}
        if self.EnhanceLv == 6:                     #목표 7
            HoningMat['파괴석 결정'] = 269
            HoningMat['위대한 명예의 돌파석'] = 5
            HoningMat['중급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 62
        if self.EnhanceLv == 7:                     #목표 8
            HoningMat['파괴석 결정'] = 269
            HoningMat['위대한 명예의 돌파석'] = 6
            HoningMat['중급 오레하 융화 재료'] = 2
            HoningMat['명예의 파편'] = 62
        if self.EnhanceLv == 8:                     #목표 9
            HoningMat['파괴석 결정'] = 269
            HoningMat['위대한 명예의 돌파석'] = 6
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 62
        if self.EnhanceLv == 9:                     #목표 10
            HoningMat['파괴석 결정'] = 332
            HoningMat['위대한 명예의 돌파석'] = 6
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 77
        if self.EnhanceLv == 10:                     #목표 11
            HoningMat['파괴석 결정'] = 332
            HoningMat['위대한 명예의 돌파석'] = 6
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 77
        if self.EnhanceLv == 11:                     # 목표 12
            HoningMat['파괴석 결정'] = 332
            HoningMat['위대한 명예의 돌파석'] = 7
            HoningMat['중급 오레하 융화 재료'] = 3
            HoningMat['명예의 파편'] = 77
        if self.EnhanceLv == 12:                     # 목표 13
            HoningMat['파괴석 결정'] = 394
            HoningMat['위대한 명예의 돌파석'] = 7
            HoningMat['중급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 91
        if self.EnhanceLv == 13:                     # 목표 14
            HoningMat['파괴석 결정'] = 394
            HoningMat['위대한 명예의 돌파석'] = 8
            HoningMat['중급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 91
        if self.EnhanceLv == 14:                     # 목표 15
            HoningMat['파괴석 결정'] = 394
            HoningMat['위대한 명예의 돌파석'] = 8
            HoningMat['중급 오레하 융화 재료'] = 4
            HoningMat['명예의 파편'] = 91
        if self.EnhanceLv == 15:                     # 목표 16
            HoningMat['파괴석 결정'] = 801
            HoningMat['위대한 명예의 돌파석'] = 15
            HoningMat['중급 오레하 융화 재료'] = 8
            HoningMat['명예의 파편'] = 217
        if self.EnhanceLv == 16:                     # 목표 17
            HoningMat['파괴석 결정'] = 801
            HoningMat['위대한 명예의 돌파석'] = 17
            HoningMat['중급 오레하 융화 재료'] = 10
            HoningMat['명예의 파편'] = 295
        if self.EnhanceLv == 17:                     # 목표 18
            HoningMat['파괴석 결정'] = 801
            HoningMat['위대한 명예의 돌파석'] = 20
            HoningMat['중급 오레하 융화 재료'] = 11
            HoningMat['명예의 파편'] = 400
        if self.EnhanceLv == 18:                     # 목표 19
            HoningMat['파괴석 결정'] = 1300
            HoningMat['위대한 명예의 돌파석'] = 30
            HoningMat['중급 오레하 융화 재료'] = 18
            HoningMat['명예의 파편'] = 776
            HoningMat['골드'] = 710
        if self.EnhanceLv == 19:                     # 목표 20
            HoningMat['파괴석 결정'] = 1300
            HoningMat['위대한 명예의 돌파석'] = 32
            HoningMat['중급 오레하 융화 재료'] = 20
            HoningMat['명예의 파편'] = 1054
            HoningMat['골드'] = 730
        if self.EnhanceLv >= 20:                     #강화단계 : 20. 강화 멈추고 아브렐슈드 레이드로 진입
            HoningMat['계승'] = 1

        if self.EnhanceLv in range(6,15):
            AdditionalHoingMat['재봉술 : 단조 응용'] = 1

        return HoningMat, AdditionalHoingMat

    def GetWeaponRequiredHoningMat_1390(self):
        HoningMat = {}
        AdditionalHoingMat = {}
        if self.EnhanceLv in [11,12]:       #목표 12,13
            HoningMat['파괴강석'] = 650
            HoningMat['경이로운 명예의 돌파석'] = 18
            HoningMat['상급 오레하 융화 재료'] = 8
            HoningMat['명예의 파편'] = 1000
            HoningMat['골드'] = 800
        elif self.EnhanceLv == 13:          #목표 14
            HoningMat['파괴강석'] = 700
            HoningMat['경이로운 명예의 돌파석'] = 20
            HoningMat['상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 1400
            HoningMat['골드'] = 870
        elif self.EnhanceLv == 14:          #목표 15
            HoningMat['파괴강석'] = 750
            HoningMat['경이로운 명예의 돌파석'] = 20
            HoningMat['상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 1400
            HoningMat['골드'] = 940
        elif self.EnhanceLv == 15:          #목표 16
            HoningMat['파괴강석'] = 900
            HoningMat['경이로운 명예의 돌파석'] = 22
            HoningMat['상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 2400
            HoningMat['골드'] = 1120
        elif self.EnhanceLv == 16:          #목표 17
            HoningMat['파괴강석'] = 950
            HoningMat['경이로운 명예의 돌파석'] = 24
            HoningMat['상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 2400
            HoningMat['골드'] = 1200
        elif self.EnhanceLv == 17:          #목표 18
            HoningMat['파괴강석'] = 1100
            HoningMat['경이로운 명예의 돌파석'] = 28
            HoningMat['상급 오레하 융화 재료'] = 20
            HoningMat['명예의 파편'] = 3600
            HoningMat['골드'] = 1350
        elif self.EnhanceLv == 18:          #목표 19
            HoningMat['파괴강석'] = 1150
            HoningMat['경이로운 명예의 돌파석'] = 30
            HoningMat['상급 오레하 융화 재료'] = 20
            HoningMat['명예의 파편'] = 3600
            HoningMat['골드'] = 1440
        elif self.EnhanceLv == 19:          #목표 20
            HoningMat['파괴강석'] = 1300
            HoningMat['경이로운 명예의 돌파석'] = 32
            HoningMat['상급 오레하 융화 재료'] = 30
            HoningMat['명예의 파편'] = 5000
            HoningMat['골드'] = 1600
        elif self.EnhanceLv >= 20:          #강화단계 : 20. 강화 멈추고 일리아칸 레이드로 진입
            HoningMat['계승'] = 1


        if self.EnhanceLv in [11, 12]:                  # 숨결            목표 : 12~13
            AdditionalHoingMat['태양의 은총'] = 24
            AdditionalHoingMat['태양의 축복'] = 12
            AdditionalHoingMat['태양의 가호'] = 4
        elif self.EnhanceLv in range(13,19):            #                목표 : 14~19
            AdditionalHoingMat['태양의 은총'] = 36
            AdditionalHoingMat['태양의 축복'] = 18
            AdditionalHoingMat['태양의 가호'] = 6
        elif self.EnhanceLv >= 19:                      #                목표 : 20이상
            AdditionalHoingMat['태양의 은총'] = 48
            AdditionalHoingMat['태양의 축복'] = 24
            AdditionalHoingMat['태양의 가호'] = 8

        if self.EnhanceLv in range(12, 15):             # 책              목표 : 13~15
            AdditionalHoingMat['재봉술 : 단조 숙련'] = 1
        elif self.EnhanceLv in range(15, 19):           #                 목표 : 16~19
            AdditionalHoingMat['재봉술 : 단조 특화'] = 1

        return HoningMat, AdditionalHoingMat

    def GetWeaponRequiredHoningMat_1525(self):
        HoningMat = {}
        AdditionalHoingMat = {}
        if self.EnhanceLv == 9:             #목표 10
            HoningMat['정제된 파괴강석'] = 650
            HoningMat['찬란한 명예의 돌파석'] = 15
            HoningMat['최상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 6500
            HoningMat['골드'] = 1170
        elif self.EnhanceLv == 10:          #목표 11
            HoningMat['정제된 파괴강석'] = 650
            HoningMat['찬란한 명예의 돌파석'] = 15
            HoningMat['최상급 오레하 융화 재료'] = 7
            HoningMat['명예의 파편'] = 6500
            HoningMat['골드'] = 1240
        elif self.EnhanceLv == 11:          #목표 12
            HoningMat['정제된 파괴강석'] = 650
            HoningMat['찬란한 명예의 돌파석'] = 15
            HoningMat['최상급 오레하 융화 재료'] = 8
            HoningMat['명예의 파편'] = 6500
            HoningMat['골드'] = 1290
        elif self.EnhanceLv == 12:          #목표 13
            HoningMat['정제된 파괴강석'] = 700
            HoningMat['찬란한 명예의 돌파석'] = 19
            HoningMat['최상급 오레하 융화 재료'] = 8
            HoningMat['명예의 파편'] = 8000
            HoningMat['골드'] = 1360
        elif self.EnhanceLv == 13:          #목표 14
            HoningMat['정제된 파괴강석'] = 750
            HoningMat['찬란한 명예의 돌파석'] = 20
            HoningMat['최상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 8000
            HoningMat['골드'] = 1430
        elif self.EnhanceLv == 14:          #목표 15
            HoningMat['정제된 파괴강석'] = 800
            HoningMat['찬란한 명예의 돌파석'] = 21
            HoningMat['최상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 8000
            HoningMat['골드'] = 1520
        elif self.EnhanceLv == 15:          #목표 16
            HoningMat['정제된 파괴강석'] = 950
            HoningMat['찬란한 명예의 돌파석'] = 22
            HoningMat['최상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 9000
            HoningMat['골드'] = 1610
        elif self.EnhanceLv == 16:          #목표 17
            HoningMat['정제된 파괴강석'] = 1000
            HoningMat['찬란한 명예의 돌파석'] = 24
            HoningMat['최상급 오레하 융화 재료'] = 12
            HoningMat['명예의 파편'] = 9000
            HoningMat['골드'] = 1720
        elif self.EnhanceLv == 17:          #목표 18
            HoningMat['정제된 파괴강석'] = 1050
            HoningMat['찬란한 명예의 돌파석'] = 26
            HoningMat['최상급 오레하 융화 재료'] = 20
            HoningMat['명예의 파편'] = 12000
            HoningMat['골드'] = 1840
        elif self.EnhanceLv == 18:          #목표 19
            HoningMat['정제된 파괴강석'] = 1100
            HoningMat['찬란한 명예의 돌파석'] = 28
            HoningMat['최상급 오레하 융화 재료'] = 20
            HoningMat['명예의 파편'] = 14000
            HoningMat['골드'] = 1980
        elif self.EnhanceLv == 19:          #목표 20
            HoningMat['정제된 파괴강석'] = 1250
            HoningMat['찬란한 명예의 돌파석'] = 30
            HoningMat['최상급 오레하 융화 재료'] = 30
            HoningMat['명예의 파편'] = 14000
            HoningMat['골드'] = 2150
        elif self.EnhanceLv == 20:          #목표 21
            HoningMat['정제된 파괴강석'] = 1350
            HoningMat['찬란한 명예의 돌파석'] = 33
            HoningMat['최상급 오레하 융화 재료'] = 30
            HoningMat['명예의 파편'] = 15000
            HoningMat['골드'] = 2350
        elif self.EnhanceLv == 21:          #목표 22
            HoningMat['정제된 파괴강석'] = 1450
            HoningMat['찬란한 명예의 돌파석'] = 36
            HoningMat['최상급 오레하 융화 재료'] = 30
            HoningMat['명예의 파편'] = 15000
            HoningMat['골드'] = 2600
        elif self.EnhanceLv == 22:          #목표 23
            HoningMat['정제된 파괴강석'] = 1600
            HoningMat['찬란한 명예의 돌파석'] = 40
            HoningMat['최상급 오레하 융화 재료'] = 30
            HoningMat['명예의 파편'] = 17000
            HoningMat['골드'] = 2910
        elif self.EnhanceLv == 23:          #목표 24
            HoningMat['정제된 파괴강석'] = 1850
            HoningMat['찬란한 명예의 돌파석'] = 44
            HoningMat['최상급 오레하 융화 재료'] = 45
            HoningMat['명예의 파편'] = 19000
            HoningMat['골드'] = 3290
        elif self.EnhanceLv == 24:          #목표 25
            HoningMat['정제된 파괴강석'] = 2150
            HoningMat['찬란한 명예의 돌파석'] = 48
            HoningMat['최상급 오레하 융화 재료'] = 45
            HoningMat['명예의 파편'] = 22000
            HoningMat['골드'] = 3750

        if self.EnhanceLv in range(9, 13):              # 숨결        목표 : 10~13
            AdditionalHoingMat['태양의 은총'] = 24
            AdditionalHoingMat['태양의 축복'] = 12
            AdditionalHoingMat['태양의 가호'] = 4
        elif self.EnhanceLv in range(13,19):            #             목표 : 14~19
            AdditionalHoingMat['태양의 은총'] = 36
            AdditionalHoingMat['태양의 축복'] = 18
            AdditionalHoingMat['태양의 가호'] = 6
        elif self.EnhanceLv >= 19:                      #             목표 : 20이상
            AdditionalHoingMat['태양의 은총'] = 48
            AdditionalHoingMat['태양의 축복'] = 24
            AdditionalHoingMat['태양의 가호'] = 8

        return HoningMat, AdditionalHoingMat