from tkinter import *
from tkinter import font, PhotoImage
import tkinter.ttk
from PIL import Image
from PIL import ImageTk
from io import BytesIO

from SearchEngine import *

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
        self.currentSelectedCharacterLv = 0
        self.characterSelectRaidoButtons = []


        self.window.mainloop()

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
        for radio_button in self.characterSelectRaidoButtons:  # destroy the existing radio buttons
            radio_button.destroy()
        self.characterSelectRaidoButtons = []  # reset the list
        self.canvas.delete("all")

        for i, character in enumerate(search_engine.raidTeam_Info):
            image_url = character['image']
            if image_url is not None:  # Add check for None image_url
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

                radio_button = Radiobutton(self.canvas, text=character['CharacterName'],
                                           variable=self.currentSelectedCharacterLv, value=character['ItemMaxLevel'],
                                           command=lambda lv=character['ItemMaxLevel']: self.selectCharacter(lv))
                radio_button.place(x=680, y=start_y_position + i * 20 + 10)
                self.characterSelectRaidoButtons.append(radio_button)

                if i // 3 >= 2:  # From the 3rd row onwards
                    self.scrollable_frame.update_idletasks()  # Force the frame to update
                    new_height = self.scrollable_frame.winfo_height() + img_label.winfo_height() + radio_button.winfo_height()
                    self.scrollable_frame.configure(height=new_height)  # Update the frame's height

    def initPage1(self):
        self.initPage1Canvas()
        self.initPage1ButtonEntry()

    def search_raidTeam(self):
        characterName = self.entry.get()
        search_engine.SearchRaidTeam(characterName)
        search_engine.AddCharacterImages()
        self.DisplayRaidTeam()

    def selectCharacter(self, lv):
        self.currentSelectedCharacterLv = lv
        print('현재 레벨 : ', self.currentSelectedCharacterLv)


LostArk()