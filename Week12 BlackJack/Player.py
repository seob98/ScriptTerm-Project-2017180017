class Player:   # 플레이어, 딜러
    def __init__(self, name):
        self.name = name
        self.cards = []         #Card 클래스 객체들을 갖는 리스트
        self.N = 0              #현재 갖고 있는 카드 개수
    def inHand(self):
        return self.N
    def addCard(self,c):        #인자 C : Card 클래스의 객체
        self.cards.append(c)
        self.N +=1
    def reset(self):            #초기화 함수
        self.N = 0
        self.cards.clear()
    def value(self):                #갖고 있는 카드들의 점수를 계산해서 반환 #ACE는 디폴트값 11로 계산. (2~10) 본래 숫자로. (JQK)는 10으로 계산
        value = 0                   #self.cards 리스트의 카드 점수 합산 #21이 넘어가면 ACE카드들 중 하나씩 1로 변경한다
        for i in range(len(self.cards)):
            value += self.cards[i].getValue()
        return value

