class Card:
    def __init__(self, number):         #인자는 0~51 랜덤숫자를 인자로 전달받는다. 문양이 4개, 카드가짓수는 13개.
        self.x = number // 13           #0~51 // 13 = 문양
        self.value = number % 13 + 1    #13가지 숫자
    def getsuit(self):      #초기화에 따른 무늬 반환
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        return suits[self.x]
    def filename(self):
        return self.getsuit() + str(self.value) + '.png'
    def getValue(self):     #1~10 : 기존숫자    JQK : 10
        if self.value > 10:
            return 10
        else:
            return self.value
