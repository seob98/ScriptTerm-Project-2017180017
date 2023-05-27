from tkinter import *
from tkinter import font, PhotoImage
import tkinter.ttk
from PIL import Image
from PIL import ImageTk
from io import BytesIO
from Equipment import *
from HoningMat import *

from SearchEngine import *
from Character import *

search_engine = SearchEngine()

class LostArk:
    def __init__(self):
        self.window = Tk()
        self.window.title('HoningCalc')
        self.window.geometry('830x600')
        self.window.configure(bg = 'white')
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='consolas')
        self.fontstyle2 = font.Font(self.window, size=15, weight='bold', family='consolas')
        self.initPages()
        self.initPage1()
        self.currentSelectedCharacterName = StringVar()
        self.currentSelectedCharacterName.set('선택안됨')
        self.currentSelectedCharacterLV = 0
        self.characterSelectRaidoButtons = []

        self.bonusDistanceX = 200       #재료-추가재료 이미지간 거리
        self.adjustX = 0                #재련재료 현황 adjust값들
        self.adjustY = 20

        self.characterNameLabel = None          #page2
        self.characterLvLabel = None            #page2
        self.equipment_listbox = None           #page2
        self.equipment_image = {}               #page2
        self.equipment_imageLabel = None        #page2

        self.HoningMat_TextLabel_Title = None           #page2
        self.HoningMat_TextLabel_TotalPrice = None      #page2
        self.HoningMat_TextLabel_HonorStone = None      #page2
        self.HoningMat_TextLabel_OffDefGem = None       #page2
        self.HoningMat_TextLabel_OrehaStone = None      #page2
        self.HoningMat_TextLabel_HonorShard = None      #page2
        self.HoningMat_TextLabel_Gold = None            #page2

        self.BonusMat_TextLabel_Title = None          #page2
        self.BonusMat_TextLabel_TotalPrice = None     #page2
        self.BonusMat_TextLabel_Solar1 = None              #page2
        self.BonusMat_TextLabel_Solar2 = None              #page2
        self.BonusMat_TextLabel_Solar3 = None              #page2
        self.BonusMat_TextLabel_Book = None                #page2
        self.BonusMat_TextLabel_Gold = None                #page2

        self.HoningShard_TextLabel_Guide1 = None
        self.HoningShard_TextLabel_Guide2 = None
        self.TextLabel_Guide = None

        self.HoningMat_Images = {}              #page2
        self.HoningMat_Labels = {}              #page2

        self.GoldImgLabel = None                #page2
        self.GoldImg = None                     #page2

        self.initPage2()

        self.window.mainloop()

    #page1

    def initPages(self):
        self.notebook = tkinter.ttk.Notebook(self.window, width=830, height=600)
        self.notebook.pack()

        self.page1 = Frame(self.window)
        self.notebook.add(self.page1, text='원정대')
        self.page2 = Frame(self.window)
        self.notebook.add(self.page2, text='재련')
        self.page3 = Frame(self.window)
        self.notebook.add(self.page3, text='지도')

    def initPage1Canvas(self):
        self.canvas = Canvas(self.page1)                        # 캔버스 위젯 생성
        self.scrollbar = Scrollbar(self.page1, orient="vertical", command=self.canvas.yview)   # 스크롤바 생성, 방향은 수직, 커맨드는 캔버스의 yview로 설정
        self.scrollable_frame = Frame(self.canvas)              # 캔버스 내부에 스크롤 가능한 프레임 생성
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")            # 스크롤 가능 영역 설정
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")  # 스크롤 가능한 프레임을 캔버스에 추가
        self.canvas.configure(yscrollcommand=self.scrollbar.set)  # 캔버스의 y스크롤 커맨드를 스크롤바 set으로 설정
        # Create MainFrame > Create A Canvas > Add a scrollbar to Canvas > Configure the Canvas

    def initPage1ButtonEntry(self):
        self.entry = Entry(self.page1)  # Entry 위젯 생성, 부모는 스크롤 가능한 프레임이 아니라 page1 프레임
        self.entry.place(x=600, y=4)
        self.button = Button(self.page1, text="Search",
                             command=self.search_raidTeam)  # Button 위젯 생성, 부모는 스크롤 가능한 프레임이 아니라 page1 프레임
        self.button.place(x=750, y=0)
        self.canvas.pack(side="left", fill="both", expand=True)  # 캔버스를 왼쪽에 팩, fill과 expand로 크기 조절
        self.scrollbar.pack(side="right", fill="y")  # 스크롤바를 오른쪽에 팩, fill로 크기 조절

    def DisplayRaidTeam(self):
        self.scrollable_frame.configure(height=0)
        if(len(self.characterSelectRaidoButtons) > 0):
            self.canvas.delete("all")

        for radio_button in self.characterSelectRaidoButtons:   # destroy the existing radio buttons
            radio_button.destroy()
        self.characterSelectRaidoButtons = []                   # reset the list

        for i, character in enumerate(search_engine.raidTeam_Info):
            image_url = character.Image
            if image_url is not None:
                response = requests.get(image_url)
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                img = img.resize((204, 236))
                img = ImageTk.PhotoImage(img)

                img_label = Label(self.canvas, image=img)
                img_label.image = img

                start_y_position = 40  # 캐릭터 이미지 배치
                x_position = (i % 3 + 1) * 800 / 3.6 - 210
                y_position = start_y_position + (i // 3) * 270
                self.canvas.create_window(x_position, y_position, window=img_label, anchor='nw')

                radio_button = Radiobutton(self.canvas, text=character.CharacterName,
                                           variable=self.currentSelectedCharacterName, value=character.CharacterName,
                                           command=lambda lv=character.ItemMaxLevel: self.selectCharacter_RadioButton(lv))
                radio_button.place(x=680, y=start_y_position + i * 20 + 10)
                self.characterSelectRaidoButtons.append(radio_button)

                if i // 3 >= 2:  # From the 3rd row onwards
                    self.scrollable_frame.update_idletasks()  # Force the frame to update
                    new_height = self.scrollable_frame.winfo_height() + img_label.winfo_height() + radio_button.winfo_height()
                    self.scrollable_frame.configure(height=new_height)  # Update the frame's height

                self.canvas.update_idletasks()                              # Force the canvas to update
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))  # Update the scrollable region

    def initPage1(self):
        self.initPage1Canvas()
        self.initPage1ButtonEntry()

    def search_raidTeam(self):
        characterName = self.entry.get()
        search_engine.SearchRaidTeam(characterName)
        search_engine.AddCharacterImage()
        self.DisplayRaidTeam()
        self.Page2_Equipments_Image_Ready()

    def selectCharacter_RadioButton(self, lv):
        self.currentSelectedCharacterLV = lv
        if self.characterNameLabel is not None and self.characterLvLabel is not None:
            self.characterNameLabel.config(
                text='캐릭터 이름: ' + self.currentSelectedCharacterName.get())  # Update name label text
            self.characterLvLabel.config(
                text='캐릭터 레벨: ' + str(self.currentSelectedCharacterLV))  # Update level label text
        print('선택된 캐릭터 레벨: ', self.currentSelectedCharacterLV)
        print('선택된 캐릭터 이름: ', self.currentSelectedCharacterName.get())

    #page2

    def initPage2(self):
        self.HoningMat_Img_Ready()

        self.characterNameLabel = Label(self.page2, text = '캐릭터 이름 : ' + self.currentSelectedCharacterName.get())       #라벨 : 캐릭터이름 (좌측상단)
        self.characterNameLabel.place(x=0, y=0)

        self.characterLvLabel = Label(self.page2, text='캐릭터 레벨: ' + str(self.currentSelectedCharacterLV))               #라벨 : 캐릭터레벨 (좌측상단)
        self.characterLvLabel.place(x=0, y=20)

        self.equipmentType_listbox = StringVar()
        self.equipmentType_listbox.set('무기')  # set default value                                                         #리스트박스 : 장비 파츠 (좌측상단)

        equipmentTypes = ['무기', '투구', '상의', '하의', '장갑', '어깨']
        self.equipment_listbox = Listbox(self.page2, height=len(equipmentTypes), width=10,
                                    listvariable=StringVar(value=equipmentTypes),
                                    bd=2, relief='sunken')
        self.equipment_listbox.place(x=0, y=40)  # Place the listbox right below the label
        self.equipment_listbox.bind('<<ListboxSelect>>', self.select_EquipmentType_Listbox)

        self.selectedItem_NameLabel = Label(self.page2, text = '')                  #라벨 : 아이템이름 (좌측)
        self.selectedItem_NameLabel.place(x=240 + self.adjustX, y=65)

        self.selectedItem_LvLabel = Label(self.page2, text='')                      #라벨 : 아이템레벨 (좌측)
        self.selectedItem_LvLabel.place(x=240 + self.adjustX, y=85)

        self.HoningMat_TextLabel_HonorStone = Label(self.page2, text='')                    #재련재료 텍스트라벨
        self.HoningMat_TextLabel_OffDefGem = Label(self.page2, text='')
        self.HoningMat_TextLabel_OrehaStone = Label(self.page2, text='')
        self.HoningMat_TextLabel_HonorShard = Label(self.page2, text='')
        self.HoningMat_TextLabel_Gold = Label(self.page2, text='')
        self.HoningMat_TextLabel_Title = Label(self.page2, text='재련 기본 재료')
        self.HoningMat_TextLabel_TotalPrice = Label(self.page2, text='')

        self.BonusMat_TextLabel_Title = Label(self.page2, text='')                    #추가재료 텍스트라벨
        self.BonusMat_TextLabel_TotalPrice = Label(self.page2, text='')
        self.BonusMat_TextLabel_Solar1 = Label(self.page2, text='')
        self.BonusMat_TextLabel_Solar2 = Label(self.page2, text='')
        self.BonusMat_TextLabel_Solar3 = Label(self.page2, text='')
        self.BonusMat_TextLabel_Book = Label(self.page2, text='')

        self.HoningMat_TextLabel_Esther = Label(self.page2, text='')
        self.HoningMat_TextLabel_Esther.place(x=220 + self.adjustX, y=170 + self.adjustY)

        #안내문 TextLabel
        self.HoningShard_TextLabel_Guide1 =  Label(self.page2, text='')
        self.HoningShard_TextLabel_Guide2 = Label(self.page2, text='')
        self.TextLabel_Guide = Label(self.page2, text='')

        self.HoningShard_TextLabel_Guide1.config(text=search_engine.honingShard_Info1)
        self.HoningShard_TextLabel_Guide1.place(x=10, y=520)
        self.HoningShard_TextLabel_Guide2.config(text=search_engine.honingShard_Info2)
        self.HoningShard_TextLabel_Guide2.place(x=10, y=540)
        self.TextLabel_Guide.config(text='* 모든 재료 가격은 현재 경매장 최저가가 기준')
        self.TextLabel_Guide.place(x=10, y=500)

        self.Esther_Image_Label = Label(self.page2, image=self.HoningMat_Images['에스더의 기운'])



    def Page2_Equipments_Image_Ready(self):
        equipment_image = {}
        for character in search_engine.raidTeam_Info:  # 이미지 : 장비파츠(좌측중간상단부)
            equipments = character.Equipments
            for gear_name, gear in equipments.items():
                if gear.ImageURL is not None:
                    response = requests.get(gear.ImageURL)
                    img_data = response.content
                    img = Image.open(BytesIO(img_data))
                    img = img.resize((64, 64))
                    img = ImageTk.PhotoImage(img)
                    self.equipment_image[(character.CharacterName,gear_name)] = img
                    self.equipment_imageLabel = Label(self.page2)
                    self.equipment_imageLabel.place(x=170 + self.adjustX,y=60)

    def select_EquipmentType_Listbox(self, event):
        for matName, matLabel in self.HoningMat_Labels.items():
            matLabel.config(image='')                   # 재료이미지

        self.equipment_imageLabel.config( image='')     # 장비 아이콘
        self.selectedItem_NameLabel.config(text='')     # 장비 이름
        self.selectedItem_LvLabel.config(text='')       # 아이템레벨

        self.GoldImgLabel.config(image='')
        self.HoningMat_TextLabel_Title.config(text='')
        self.HoningMat_TextLabel_TotalPrice.config(text='')
        self.HoningMat_TextLabel_HonorStone.config(text='')
        self.HoningMat_TextLabel_OffDefGem.config(text='')
        self.HoningMat_TextLabel_OrehaStone.config(text='')
        self.HoningMat_TextLabel_HonorShard.config(text='')
        self.HoningMat_TextLabel_Gold.config(text='')
        self.HoningMat_TextLabel_Esther.config(text='')

        self.BonusMat_TextLabel_Title.config(text='')
        self.BonusMat_TextLabel_Solar1.config(text='')
        self.BonusMat_TextLabel_Solar2.config(text='')
        self.BonusMat_TextLabel_Solar3.config(text='')
        self.BonusMat_TextLabel_Book.config(text='')
        self.BonusMat_TextLabel_TotalPrice.config(text='')
        self.Esther_Image_Label.config(image='')                          #초기화


        for matName, matImageLabel in self.HoningMat_Labels.items():
            matImageLabel.config(image='')

        if self.currentSelectedCharacterName.get() in ['선택안됨', '', None] :
            return


        index = self.equipment_listbox.curselection()[0]
        seltext = self.equipment_listbox.get(index)
        selectedCharacter = search_engine.GetCharacter(self.currentSelectedCharacterName.get())
        gear = selectedCharacter.Equipments[seltext]
        self.equipment_imageLabel.config(image=self.equipment_image[self.currentSelectedCharacterName.get(), seltext])  #장비 아이콘 ImageLabel

        self.selectedItem_NameLabel.config(text=gear.Name)                                  #장비 이름 TextLabel
        self.selectedItem_LvLabel.config(text='장비 레벨 : ' + str(gear.ItemLv))             #장비 아이템레벨 TextLabel

        matTotalPrice = 0
        bonusMatTotalPrice = 0
        mats, mats_bonus = gear.GetRequiredMat()

        #예외: 에스더 / 만렙 / 계승
        if '에스더' in mats:
            estherStoneCount=0
            estherLV = mats['에스더']
            if estherLV == 0:
                estherStoneCount = 1
            elif estherLV == 1:
                estherStoneCount = 2
            elif estherLV == 2:
                estherStoneCount = 5
            elif estherLV == 3:
                estherStoneCount = 10
            elif estherLV == 4:
                estherStoneCount = 10
            elif estherLV == 5:
                estherStoneCount = 20
            elif estherLV == 6:
                estherStoneCount = 20
            elif estherLV == 7:
                estherStoneCount = 30

            if estherLV == 8:
                self.HoningMat_TextLabel_Esther.config(text='8강 사장님은 가격보고 강화하는 사람들이 아닙니다')
                return
            else:
                honingMat_Item = search_engine.honingMat_Info['에스더의 기운']  # 재료 객체
                self.Esther_Image_Label.config(image=self.HoningMat_Images['에스더의 기운'])
                self.Esther_Image_Label.place(x=170+self.adjustX, y=150+self.adjustY)
                self.HoningMat_TextLabel_Esther.place(x=220+self.adjustX, y=170+self.adjustY)
                self.HoningMat_TextLabel_Esther.config(text='X ' + str(estherStoneCount) + ' = ' + '{:.2f}'.format(
                    estherStoneCount * honingMat_Item.CurrentMinPrice) + '골드')
                return

        elif '만렙' in mats:
            self.HoningMat_TextLabel_Esther.place(x=220 + self.adjustX, y=170 + self.adjustY)
            self.HoningMat_TextLabel_Esther.config(text='풀강입니다.')
            return

        elif '계승' in mats:
            self.HoningMat_TextLabel_Esther.place(x=220 + self.adjustX, y=170 + self.adjustY)
            self.HoningMat_TextLabel_Esther.config(text='계승하세요. 현재 단계 강화는 심한 돈낭비입니다.')
            return








        # 필수재료 이미지, 텍스트 출력 및 총 가격 계산
        for key, basicMat in mats.items():
            if '골드' in key:
                self.GoldImgLabel.config(image=self.GoldImg)
                self.GoldImgLabel.place(x=170+self.adjustX,y=350+self.adjustY)
                self.HoningMat_TextLabel_Gold.place(x=220 + self.adjustX, y=370 + self.adjustY)
                self.HoningMat_TextLabel_Gold.config(text='X ' + str(mats['골드']) + ' = ' + '{:.2f}'.format(mats['골드']) + '골드')
                matTotalPrice += mats['골드']
            else:
                honingMat_Item = search_engine.honingMat_Info[key]  # 재료 객체
                self.HoningMat_Labels[key].config(image=self.HoningMat_Images[key])
                if '돌파석' in key:
                    self.HoningMat_Labels[key].place(x=170+self.adjustX, y=150+self.adjustY)
                    self.HoningMat_TextLabel_HonorStone.place(x=225+self.adjustX, y=170+self.adjustY)
                    self.HoningMat_TextLabel_HonorStone.config(text='X ' + str(mats[key]) + ' = ' + '{:.2f}'.format(
                        mats[key] * honingMat_Item.CurrentMinPrice) + '골드')
                elif '수호' in key:
                    self.HoningMat_Labels[key].place(x=170+self.adjustX, y=200+self.adjustY)
                    self.HoningMat_TextLabel_OffDefGem.place(x=220+self.adjustX, y=220+self.adjustY)
                    self.HoningMat_TextLabel_OffDefGem.config(text='X ' + str(mats[key]) + ' = ' + '{:.2f}'.format(
                        mats[key] * honingMat_Item.CurrentMinPrice) + '골드')
                elif '파괴' in key:
                    self.HoningMat_Labels[key].place(x=170+self.adjustX, y=200+self.adjustY)
                    self.HoningMat_TextLabel_OffDefGem.place(x=220+self.adjustX, y=220+self.adjustY)
                    self.HoningMat_TextLabel_OffDefGem.config(text='X ' + str(mats[key]) + ' = ' + '{:.2f}'.format(
                        mats[key] * honingMat_Item.CurrentMinPrice) + '골드')
                elif '오레하' in key:
                    self.HoningMat_Labels[key].place(x=170+self.adjustX, y=250+self.adjustY)
                    self.HoningMat_TextLabel_OrehaStone.place(x=220+self.adjustX, y=270+self.adjustY)
                    self.HoningMat_TextLabel_OrehaStone.config(text='X ' + str(mats[key]) + ' = ' + '{:.2f}'.format(
                        mats[key] * honingMat_Item.CurrentMinPrice) + '골드')
                elif '파편' in key:
                    self.HoningMat_Labels[key].place(x=170+self.adjustX, y=300+self.adjustY)
                    self.HoningMat_TextLabel_HonorShard.place(x=220+self.adjustX, y=320+self.adjustY)
                    self.HoningMat_TextLabel_HonorShard.config(text='X ' + str(mats[key]) + ' = ' + '{:.2f}'.format(
                        mats[key] * honingMat_Item.CurrentMinPrice) + '골드')
                matTotalPrice += mats[key] * honingMat_Item.CurrentMinPrice

        # 추가재료 이미지, 텍스트 출력 및 총 가격 계산
        for key, bonusMat in mats_bonus.items():
            bonusMat_Item = search_engine.honingMat_Info[key]  # 재료 객체
            self.HoningMat_Labels[key].config(image=self.HoningMat_Images[key])
            if '은총' in key:
                self.HoningMat_Labels[key].place(x=170 +self.adjustX+ self.bonusDistanceX, y=150 + self.adjustY)
                self.BonusMat_TextLabel_Solar1.place(x=220 + self.adjustX + self.bonusDistanceX - 5, y=170 + self.adjustY)
                self.BonusMat_TextLabel_Solar1.config(text='X ' + str(mats_bonus[key]) + ' = ' + '{:.2f}'.format(
                    mats_bonus[key] * bonusMat_Item.CurrentMinPrice) + '골드')
            elif '축복' in key:
                self.HoningMat_Labels[key].place(x=170+self.adjustX+self.bonusDistanceX, y=200+self.adjustY)
                self.BonusMat_TextLabel_Solar2.place(x=220 + self.adjustX + self.bonusDistanceX - 5, y=220 + self.adjustY)
                self.BonusMat_TextLabel_Solar2.config(text='X ' + str(mats_bonus[key]) + ' = ' + '{:.2f}'.format(
                    mats_bonus[key] * bonusMat_Item.CurrentMinPrice) + '골드')
            elif '가호' in key:
                self.HoningMat_Labels[key].place(x=170 + self.bonusDistanceX, y=250+self.adjustY)
                self.BonusMat_TextLabel_Solar3.place(x=220 + self.bonusDistanceX - 5, y=270 + self.adjustY)
                self.BonusMat_TextLabel_Solar3.config(text='X ' + str(mats_bonus[key]) + ' = ' + '{:.2f}'.format(
                    mats_bonus[key] * bonusMat_Item.CurrentMinPrice) + '골드')
            elif '재봉술' in key:
                self.HoningMat_Labels[key].place(x=170+self.adjustX+self.bonusDistanceX,y=300+self.adjustY)
                self.BonusMat_TextLabel_Book.place(x=220 + self.adjustX + self.bonusDistanceX, y=320 + self.adjustY)
                self.BonusMat_TextLabel_Book.config(text='X ' + str(mats_bonus[key]) + ' = ' + '{:.2f}'.format(
                    mats_bonus[key] * bonusMat_Item.CurrentMinPrice) + '골드')
            elif '야금술' in key:
                self.HoningMat_Labels[key].place(x=170+self.adjustX+self.bonusDistanceX,y=300+self.adjustY)
                self.BonusMat_TextLabel_Book.place(x=220 + self.adjustX + self.bonusDistanceX, y=320 + self.adjustY)
                self.BonusMat_TextLabel_Book.config(text='X ' + str(mats_bonus[key]) + ' = ' + '{:.2f}'.format(
                    mats_bonus[key] * bonusMat_Item.CurrentMinPrice) + '골드')

            bonusMatTotalPrice += mats_bonus[key] * bonusMat_Item.CurrentMinPrice

        self.HoningMat_TextLabel_Title.config(text='필수 재료')                                        #필수재료 TextLabel
        self.HoningMat_TextLabel_Title.place(x=170+self.adjustX, y=120+self.adjustY)
        self.HoningMat_TextLabel_TotalPrice.config(text='합계 : ' + str(matTotalPrice) + '골드')        #필수재료 합계 TextLabel
        self.HoningMat_TextLabel_TotalPrice.place(x=170+self.adjustX, y=410 + self.adjustY)

        self.BonusMat_TextLabel_Title.config(text='추가 재료')                                          #추가재료 TextLabel
        self.BonusMat_TextLabel_Title.place(x=170 + self.adjustX + self.bonusDistanceX, y=120 + self.adjustY)
        self.BonusMat_TextLabel_TotalPrice.config(text='합계 : ' + str(bonusMatTotalPrice) + '골드')    #추가재료 합계 TextLabel
        self.BonusMat_TextLabel_TotalPrice.place(x=170 + +self.adjustX + self.bonusDistanceX, y=410 + self.adjustY)




    def HoningMat_Img_Ready(self):
        self.GoldImg = PhotoImage(file='Image/Gold48.png')
        self.GoldImgLabel = Label(self.page2, image=self.GoldImg)
        for name, item in search_engine.honingMat_Info.items():
            test = item.Icon
            response = requests.get(item.Icon)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((48, 48))
            photo = ImageTk.PhotoImage(img)
            self.HoningMat_Images[item.Name] = photo

        for matName, matImg in self.HoningMat_Images.items():
            label = Label(self.page2, image='')
            self.HoningMat_Labels[matName] = label





LostArk()