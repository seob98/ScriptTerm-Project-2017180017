from tkinter import *
from tkinter import font, PhotoImage
from winsound import *
from Card import *
from Player import *
import random

class BlackJack:
    def hitPlayer(self,n):      #인자 n: 위치변수
        newCard = Card(self.cardDeck[self.deckN])   #새로운 Card 객체를 생성한다. 0~51사이 수 전달
        self.deckN +=1                              #카드덱 인덱스 증가
        self.player.addCard(newCard)
        p = PhotoImage(file = 'cards/' + newCard.filename())
        self.LCardsPlayer.append(Label(self.window,image=p))
        self.LCardsPlayer[self.player.inHand()-1].image = p   #파이썬에서 라벨 이미지 레퍼렌스를 갖고 있어야 이미지가 보인다
        self.LCardsPlayer[self.player.inHand()-1].place(x=250+n*30,y=350)
        self.LplayerPts.configure(text=str(self.player.value()))
        PlaySound('sounds/cardFlip.wav',SND_FILENAME)

    def hitDealer(self,n):      #인자 n: 위치변수
        newCard = Card(self.cardDeck[self.deckN])   #새로운 Card 객체를 생성한다. 0~51사이 수 전달
        self.deckN +=1                              #카드덱 인덱스 증가
        self.dealer.addCard(newCard)
        p = PhotoImage(file = 'cards/' + newCard.filename())
        self.LCardsDealer.append(Label(self.window,image=p))
        self.LCardsDealer[self.dealer.inHand()-1].image = p   #파이썬에서 라벨 이미지 레퍼렌스를 갖고 있어야 이미지가 보인다
        self.LCardsDealer[self.dealer.inHand()-1].place(x=280+n*30,y=150)

    def hitDealerDown(self):      #인자 n: 위치변수
        newCard = Card(self.cardDeck[self.deckN])   #새로운 Card 객체를 생성한다. 0~51사이 수 전달
        self.deckN +=1                              #카드덱 인덱스 증가
        self.dealer.addCard(newCard)
        p = PhotoImage(file = 'cards/b2fv.png')
        self.LCardsDealer.append(Label(self.window,image=p))
        self.LCardsDealer[self.dealer.inHand()-1].image = p   #파이썬에서 라벨 이미지 레퍼렌스를 갖고 있어야 이미지가 보인다
        self.LCardsDealer[self.dealer.inHand()-1].place(x=250,y=150)

    def deal(self):     #플레이어/딜러에게 카드 2장 전달한다.
        self.player.reset() #초기화
        self.dealer.reset() #초기화
        random.shuffle(self.cardDeck)   #카드덱 셔플
        self.deckN= 0                   #카드덱 인덱스 초기화

        self.hitPlayer(0)               #플레이어에게 첫번째 카드를 0번 위치에 전달한다.
        self.hitPlayer(1)               #플레이어에게 두번째 카드를 1번 위치에 전달한다.
        self.nCardsPlayer = 1           #현재 플레이어 카드의 위치 = 1

        self.hitDealerDown()            #딜러에게 첫번째 카드를 뒤집어서 전달한다.
        self.hitDealer(0)               #딜러에게 두번째 카드를 0번위치에 전달한다.
        self.nCardsDealer = 0           #현재 딜러 카드의 위치 = 0

    def checkWinner(self):  #승패를 결정한다
        p = PhotoImage(file = "cards/" + self.dealer.cards[0].filename())
        self.LCardsDealer[0].configure(image = p) #이미지 레퍼런스 변경
        self.LCardsDealer[0].image = p #파이썬은 라벨 이미지가 필요
        self.LdealerPts.configure(text= str(self.dealer.value()))

        if self.player.value() > 21:
            self.Lstatus.configure(text = 'Player Busts')
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        elif self.dealer.value() > 21:
            self.Lstatus.configure(text = 'Dealer Busts')
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        elif self.dealer.value() == self.player.value():
            self.Lstatus.configure(text = 'Push')
            self.playerMoney += self.betMoney
        elif self.dealer.value() < self.player.value():
            self.Lstatus.configure(text = 'You won')
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)
        else:
            self.Lstatus.configure(text='You lost')
            PlaySound('sounds/wrong.wav', SND_FILENAME)

        self.betMoney = 0
        self.LplayerMoney.configure(text = 'you have $' + str(self.playerMoney))
        self.LbetMoney.configure(text = "$" + str(self.betMoney))

        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def pressedB50(self):
        if self.playerMoney >= 50:
            self.betMoney += 50
            self.LbetMoney.configure(text = '$' + str(self.betMoney))
            self.playerMoney -=50
            self.LplayerMoney.configure(text = 'You have $' + str(self.playerMoney))
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)
    def pressedB10(self):
        if self.playerMoney >= 10:
            self.betMoney += 10
            self.LbetMoney.configure(text = '$' + str(self.betMoney))
            self.playerMoney -=10
            self.LplayerMoney.configure(text = 'You have $' + str(self.playerMoney))
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)
    def pressedB1(self):
        if self.playerMoney >= 1:
            self.betMoney += 1
            self.LbetMoney.configure(text = '$' + str(self.betMoney))
            self.playerMoney -=1
            self.LplayerMoney.configure(text = 'You have $' + str(self.playerMoney))
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('sounds/chip.wav', SND_FILENAME)
    def pressedHit(self):
        self.nCardsPlayer += 1                  #새로운 카드 위치 1 증가
        self.hitPlayer(self.nCardsPlayer)       #새로운 위치에 플레이어 카드 추가
        if self.player.value() > 21:
            self.checkWinner()
    def pressedStay(self):
        while self.dealer.value() < 17:
            self.nCardsDealer +=1
            self.hitDealer(self.nCardsDealer)   #새로운 위치에 딜러 카드 추가
        self.checkWinner()      #승패 결정
    def pressedDeal(self):
        self.deal()
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Hit['state'] = 'active'
        self.Hit['bg'] = 'white'
        self.Stay['state'] = 'active'
        self.Stay['bg'] = 'white'

    def pressedAgain(self):
        self.Again['state'] = 'disable'
        self.Again['bg'] = 'gray'
        self.B1['state'] = 'active'
        self.B1['bg'] = 'white'
        self.B10['state'] = 'active'
        self.B10['bg'] = 'white'
        self.B50['state'] = 'active'
        self.B50['bg'] = 'white'
        self.Lstatus.configure(text='')
        self.betMoney = 0
        for i in range(len(self.LCardsPlayer)):
            self.LCardsPlayer[i].configure(image="", background='green')
        for i in range(len(self.LCardsDealer)):
            self.LCardsDealer[i].configure(image="", background='green')
        self.LbetMoney.configure(text='')
        self.LplayerPts.configure(text='')
        self.LdealerPts.configure(text='')
        self.LCardsDealer = []
        self.LCardsPlayer = []
        self.player.reset()
        self.dealer.reset()
        self.deckN = 0


    def setupButton(self):
        self.B50 = Button(self.window,text='Bet 50',width=6,height=1,font=self.fontstyle2,command=self.pressedB50)
        self.B50.place(x=50,y=500)
        self.B10 = Button(self.window, text='Bet 10', width=6, height=1, font=self.fontstyle2, command=self.pressedB10)
        self.B10.place(x=150, y=500)
        self.B1 = Button(self.window, text='Bet 1', width=6, height=1, font=self.fontstyle2, command=self.pressedB1)
        self.B1.place(x=250, y=500)
        self.Hit = Button(self.window, text='Hit', width=6, height=1, font=self.fontstyle2, command=self.pressedHit)
        self.Hit.place(x=400, y=500)
        self.Stay = Button(self.window, text='Stay', width=6, height=1, font=self.fontstyle2, command=self.pressedStay)
        self.Stay.place(x=500, y=500)
        self.Deal = Button(self.window, text='Deal', width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text='Again', width=6, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)
        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
    def setupLabel(self):
        self.LbetMoney = Label(text = '$0',width=4,height=1,font=self.fontstyle,bg='green',fg='cyan')
        self.LbetMoney.place(x=200,y=450)
        self.LplayerMoney = Label(text = 'you have $1000',width=15,height=1,font=self.fontstyle,bg='green',fg='cyan')
        self.LplayerMoney.place(x=500,y=450)
        self.LplayerPts = Label(text = '',width=4,height=1,font=self.fontstyle2,bg='green',fg='white')
        self.LplayerPts.place(x=300,y=300)
        self.LdealerPts = Label(text = '',width=4,height=1,font=self.fontstyle2,bg='green',fg='white')
        self.LdealerPts.place(x=300,y=100)
        self.Lstatus = Label(text = '',width=15,height=1,font=self.fontstyle,bg='green',fg='white')
        self.Lstatus.place(x=500,y=300)

    def __init__(self):
        self.window = Tk()
        self.window.title('Black Jack')
        self.window.geometry('800x600')
        self.window.configure(bg = 'green')
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='consolas')
        self.fontstyle2 = font.Font(self.window, size=15, weight='bold', family='consolas')
        self.setupButton()
        self.setupLabel()
        self.player = Player('player')
        self.dealer = Player('dealer')

        self.betMoney = 0
        self.playerMoney = 1000
        self.nCardsPlayer = 0       #플레이어 카드 위치 변수
        self.nCardsDealer = 0       #딜러 카드 위치 변수
        self.LCardsPlayer = []      #플레이어 카드 이미지 라벨 리스트
        self.LCardsDealer = []      #딜러 카드 이미지 라벨 리스트
        self.cardDeck = [i for i in range(52)]
        self.deckN = 0              #카드덱에서 선택하는 숫자 인덱스

        self.window.mainloop()

BlackJack()