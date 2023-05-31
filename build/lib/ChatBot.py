import asyncio
from telegram import Bot
from Equipment import *
from HoningMat import *
from Character import *
from SearchEngine import *
from tkinter import Tk, IntVar

class ChatBot:
    def __init__(self, search_engine):
        self.chat_id = 6063773939
        self.token = '5514217942:AAEhndvld96JvXZBqnCb1szx8BKa92svTjY'
        self.bot = Bot(self.token)
        self.search_engine = search_engine
        self.loop = asyncio.new_event_loop()

    async def send_message(self, msg):
        await self.bot.send_message(chat_id=self.chat_id, text=msg)

    def send_message_sync(self, gear, mats, bonus_mats, character, exclude_materials):
        character_name = character.CharacterName
        gear_name = gear.Name
        mats, mats_bonus = gear.GetRequiredMat()

        if '계승' in mats:
            msg = character_name + '의 <' + gear_name + '>\n해당 장비는 계승을 진행하고 강화하세요. \n현재 단계에서 강화는 매우 비효율적입니다.'
            self.loop.run_until_complete(self.send_message(msg))
            return
        if '만렙' in mats:
            msg = character_name + '의 <' + gear_name + '>\n해당 장비는 강화단계가 최고 단계입니다. \n이 이상 강화는 할 수 없습니다.'
            self.loop.run_until_complete(self.send_message(msg))
            return
        if '저렙' in mats:
            msg = character_name + '해당 캐릭터는 아이템 레벨이 너무 낮습니다.\n스토리 익스프레스/하이퍼 익스프레스 진행 후 1304를 레벨을 장착하고 메시지를 호출해주세요.'
            self.loop.run_until_complete(self.send_message(msg))
            return
        if '에스더' in mats:
            estherLV = mats['에스더']
            if estherLV == 8:
                msg = character_name + '의 <' + gear_name + '>\n사장님, 실례가 안된다면 10멸 하나만 사주십시오.'
                self.loop.run_until_complete(self.send_message(msg))
                return
            amounts = {0:1, 1:2, 2:5, 3:10,4:10,5:20,6:20,7:30}
            esther_stone = self.search_engine.honingMat_Info['에스더의 기운']
            required_stones = amounts[estherLV]
            msg1 = character_name + '의 <' + gear_name + '>\n강화를 위해서 필요한 재료는 다음과 같습니다:\n'
            msg2 = '에스더의 기운 X ' + str(required_stones) + ' = ' + '{:.2f}'.format(esther_stone.CurrentMinPrice * required_stones)
            self.loop.run_until_complete(self.send_message(msg1 + msg2))
            return

        shorten_names = ['수호', '돌파석', '파괴', '오레하', '파편', '은총', '축복', '가호', '야금술', '재봉술']

        total_price_mats = 0
        total_price_bonus_mats = 0

        msg = character_name + '의 <' + gear_name + '>\n강화를 위해서 필요한 재료는 다음과 같습니다:\n'

        msg += '<기본 재료>\n'
        for mat_name, required_count in mats.items():
            if mat_name == '골드':
                one_line = str(required_count) + ' 골드\n '
                total_price_mats += required_count
            else:
                for short_name in shorten_names:
                    if short_name in mat_name:
                        search_keyword = short_name

                if exclude_materials[search_keyword].get() == 1:
                    one_line = '(' + mat_name + ' : 귀속 재료로 처리합니다)\n'
                else:
                    basic_mat = self.search_engine.honingMat_Info[mat_name]
                    one_line = mat_name + ' X ' + str(mats[mat_name]) + ' = ' + '{:.2f}'.format(
                        mats[mat_name] * basic_mat.CurrentMinPrice) + '골드 \n'
                    total_price_mats += mats[mat_name] * basic_mat.CurrentMinPrice
                msg += one_line

        msg += '<추가 재료>\n'
        for mat_name, required_count in bonus_mats.items():
            for short_name in shorten_names:
                if short_name in mat_name:
                        search_keyword = short_name

            if exclude_materials[search_keyword].get() == 1:
                one_line = '(' + mat_name + ' : 귀속 재료로 처리합니다)\n'
            else:
                bonus_mat = self.search_engine.honingMat_Info[mat_name]
                one_line = mat_name + ' X ' + str(mats_bonus[mat_name]) + ' = ' + '{:.2f}'.format(
                    mats_bonus[mat_name] * bonus_mat.CurrentMinPrice) + '골드 \n'
                total_price_bonus_mats += mats_bonus[mat_name] * bonus_mat.CurrentMinPrice
            msg += one_line

        final_line1 = '\n재련 금액(기본) : ' + '{:.2f}'.format(total_price_mats) + '골드'
        final_line2 = '\n재련 금액(풀숨) : ' + '{:.2f}'.format(total_price_mats + total_price_bonus_mats) + '골드'
        msg += final_line1
        msg += final_line2

        self.loop.run_until_complete(self.send_message(msg))
