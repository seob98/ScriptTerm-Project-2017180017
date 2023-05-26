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
        self.characterNameLabel = None          #page2
        self.characterLvLabel = None            #page2
        self.equipment_listbox = None           #page2
        self.equipment_image = {}               #page2
        self.equipment_imageLabel = None        #page2

        self.HoningMat_Labels = {}
        #self.blankImg = {}                     #page2
        #self.blankImgLabel = None              #page2
        self.GoldImgLabel = None

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
        self.ItemLabel_Ready()

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

        #self.blankImg = PhotoImage(file='Image/Blank.png')
        #self.blankImgLabel = Label(self.page2, image=self.blankImg)
        #self.blankImgLabel.place(x=180,y=100)

        self.selectedItem_NameLabel = Label(self.page2, text = '')                  #라벨 : 아이템이름 (좌측)
        self.selectedItem_NameLabel.place(x=240, y=65)

        self.selectedItem_LvLabel = Label(self.page2, text='')                      #라벨 : 아이템레벨 (좌측)
        self.selectedItem_LvLabel.place(x=240, y=85)

    def Page2_Equipments_Image_Ready(self):
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
                    self.equipment_imageLabel.place(x=170,y=60)

    def select_EquipmentType_Listbox(self, event):
        if self.currentSelectedCharacterName.get() in ['선택안됨', '', None] :
            return
        index = self.equipment_listbox.curselection()[0]
        seltext = self.equipment_listbox.get(index)
        selectedCharacter = search_engine.GetCharacter(self.currentSelectedCharacterName.get())
        gear = selectedCharacter.Equipments[seltext]
        self.equipment_imageLabel.config(image=self.equipment_image[self.currentSelectedCharacterName.get(), seltext])

        self.selectedItem_NameLabel.config(text=gear.Name)
        self.selectedItem_LvLabel.config(text='장비 레벨 : ' + str(gear.ItemLv))

        mats, mats_bonus = gear.GetRequiredMat()

        for key, basicMat in mats.items():
            if '골드' in key:
                continue
            elif '돌파석' in key:
                self.HoningMat_Labels[key].place(x=250,y=150)
            elif '수호' in key:
                self.HoningMat_Labels[key].place(x=250, y=200)
            elif '파괴' in key:
                self.HoningMat_Labels[key].place(x=250, y=200)
            elif '오레하' in key:
                self.HoningMat_Labels[key].place(x=250,y=250)
            elif '파편' in key:
                self.HoningMat_Labels[key].place(x=250,y=300)

        self.GoldImgLabel.place(x= 200,y =180)

    def ItemLabel_Ready(self):
        p = PhotoImage(file='Image/Gold3.png')
        self.GoldImgLabel = Label(self.page2, image=p)
        self.images = []  # 가비지 셀렉션에 이미지가 포함되는 문제를 방지해야한다.
        for name, item in search_engine.honingMat_Info.items():
            test = item.Icon
            response = requests.get(item.Icon)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((32, 32))
            photo = ImageTk.PhotoImage(img)
            self.images.append(photo)
            gear_label = Label(self.page2, image=photo)
            self.HoningMat_Labels[item.Name] = gear_label


LostArk()