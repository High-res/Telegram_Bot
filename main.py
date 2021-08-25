import asyncio
import time
from aiogram.dispatcher.filters.builtin import Command
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aioschedule
import time
from datetime import datetime
from datetime import date
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from markups import getDataMark
import markups as nav
import config
import actions


print('Worked main file')
loop = asyncio.get_event_loop()
bot = Bot(config.MAIN_BOT_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())

tg_id = []
msg_date = []
msg_date_now = []


def getWorkerTgID() :
    allWorkers = actions.getWorkerss()
    for w in range(0, len(allWorkers)) :
        if allWorkers[w]['tg_id'] != 0 :
            tg_id.append(allWorkers[w]['tg_id'])
    return tg_id
def currentDate() : 
    current_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M')

    return current_datetime

def getText():
    get_text = actions.getText()

    return get_text

def getMsgDate() :
    for i in range(len(getText())) :
        msg_date.append(getText()[i])
    
    return msg_date



def getMsgDateNow() :
    for i in range(len(getText())) :
        msg_date_now.append(getText()[i]['msg_date'])
    
    return msg_date_now
def CloackDate() :
    cloak_date = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    return cloak_date


def RegDate() :
    register_date = datetime.now().strftime('%Y-%m-%d')
    return register_date
def getDate() :
    today = date.today()
    year = today.strftime('%Y-%m-%d')
    return year
# Дата регистрации пользователя register_date
# print(cloak_date)
tg_id = []
def tgUsers() :
    tgUsers = actions.getUser()
    for i in range(len(tgUsers)) :
        tg_id.append(tgUsers[i]['tg_id'])
    return tg_id
    
allWorkersID = []

def AllWorkersTgID() :
    getAllWorkers = actions.getWorkerss()
    for j in range(len(getAllWorkers)) :
        if getAllWorkers[j]['tg_id'] != 0 :
            allWorkersID.append(getAllWorkers[j]['tg_id'])
    
    return allWorkersID
@dp.message_handler(Command("start"))
async def start_command(message: types.Message): 
    userName = message.from_user.first_name
    userID = message.from_user.id
    if userID in tgUsers() :
        print('Такой пользователь существует')
    else :
        actions.addUser(userName, userID, RegDate())
    tgUsers().clear()
    await bot.send_message(message.from_user.id, getDataMark()['glavnaya']['main_text'], reply_markup=nav.mainMenu)
    
class Mydialog(StatesGroup):
    otvet = State()
    zhaloba = State()

@dp.message_handler()
async def documentation_handler(message: types.Message) :
    if message.text == getDataMark()['documentation']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['documentation']['after_text'], reply_markup=nav.btnDogovor )
    elif message.text == getDataMark()['about_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['after_text'], reply_markup=nav.secondLvlMenu)
    # Самое главное для компании💯
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['after_text'], reply_markup=nav.btnBackAbout)
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['misson_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['misson_company']['after_text'], reply_markup=nav.btnBackAbout)
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['after_text'], reply_markup=nav.btnBackAbout)
        await bot.send_photo(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['links'])
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text'], reply_markup=nav.btnBackAbout)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text_1'], reply_markup=nav.btnBackAbout)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text_2'], reply_markup=nav.btnBackAbout)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text_3'], reply_markup=nav.btnBackAbout)
    # Назад до О компании
    elif message.text == getDataMark()['glavnaya']['back_to'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['after_text'], reply_markup=nav.secondLvlMenu)
    # 
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['after_text'], reply_markup=nav.btnDlyaNovenkihThird)
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['after_text'], reply_markup=nav.go_to_url)
        # await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['link'], reply_markup=nav.btnDlyaNovenkihThird)
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['main_text'] :
        f = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['link'], 'rb')
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['after_text'], reply_markup=nav.btnDlyaNovenkihThird)
        await bot.send_document(message.from_user.id, f)
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['main_text'] :
        f = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link'], 'rb')
        a = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_1'], 'rb')
        s = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_2'], 'rb')
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['after_text'], reply_markup=nav.btnDlyaNovenkihThird)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_text'], reply_markup=nav.btnDlyaNovenkihThird)
        await bot.send_document(message.from_user.id, f)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_1_text'], reply_markup=nav.btnDlyaNovenkihThird)
        await bot.send_document(message.from_user.id, a)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_2_text'], reply_markup=nav.btnDlyaNovenkihThird)
        await bot.send_document(message.from_user.id, s)
    elif message.text == getDataMark()['zayavlenie_na_avans']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['zayavlenie_na_avans']['after_text'], )
        await Mydialog.otvet.set()
        # Получить автоматически id отправителя и сегодняшнюю дату, что бы он написал сумму сохранить сначала это в json после отправкой письма или в сверстанном макете вывести
    elif message.text == getDataMark()['zhaloba_predlozhenie']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['zhaloba_predlozhenie']['after_text'])
        await Mydialog.zhaloba.set()
    elif message.text == getDataMark()['glavnaya']['after_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['glavnaya']['main_text'], reply_markup=nav.mainMenu)


@dp.message_handler(content_types=['location'])
async def getLocation(message: types.Message) :
    actions.addLocation(message.from_user.first_name, message.from_user.id, message.location.latitude, message.location.longitude, CloackDate(), getDate())
    print(message)
    await bot.send_message(message.from_user.id, f'https://2gis.kz/almaty?m={message.location.longitude}%2C{message.location.latitude}%2F19.35  \nВы находитесь здесь!')
    
    # print(f'https://www.google.com/maps/@{message.location.latitude},{message.location.longitude},19.73z  {message.from_user.first_name}')

@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['dogovor_realizatcii']['main_text'])
async def dogovor_realizatcii(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['dogovor_realizatcii']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['dogovor_realizatcii']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)

@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['main_text'])
async def dogovor_kupli_prodazhi(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)

@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['destrib_dogovor']['main_text'])
async def destrib_dogovor(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['destrib_dogovor']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['destrib_dogovor']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)


@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['poluchit_rekvizity']['main_text'])
async def poluchit_rekvizity(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['poluchit_rekvizity']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['poluchit_rekvizity']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)


@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['zayavlenie_avans']['main_text'])
async def zayavlenie_avans(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['zayavlenie_avans']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['zayavlenie_avans']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)


    
@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['price']['main_text'])
async def price(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['price']['links'], 'rb')
    j = open(getDataMark()['documentation']['inside_menu']['price']['links_1'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['price']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
    await bot.send_document(callback_query.from_user.id, j)

    
@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['specification_mello']['main_text'])
async def specification_mello(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['specification_mello']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, 'Спецификация мелло')
    await bot.send_document(callback_query.from_user.id, f)

@dp.message_handler(content_types=['document'])
async def getDocument(message : types.Message) :
    file = bot.get_file(message.document.file_id)
    print(file)

@dp.message_handler(state=Mydialog.otvet)
async def answerAvans(message: types.Message, state: FSMContext) :
    if message.from_user.id in AllWorkersTgID() :
        actions.getAvans(message.from_user.id, message.from_user.first_name, message.text, CloackDate())
        await message.reply('Ваше заявление принято, ожидайте!', reply=False)
        await actions.addToDocx()
        await dp.storage.close()
        await dp.storage.wait_closed()
    else :
        await  message.reply('Вы не являетесь сотрудником, свяжитесь с Маржан для выяснения обстоятельств', reply=False)
        await dp.storage.close()
        await dp.storage.wait_closed()

    # Есть баг тут нужно решить!!!!
    

@dp.message_handler(state=Mydialog.zhaloba)
async def zhaloba(message: types.Message, state: FSMContext) :
    actions.getZhaloba(message.from_user.id, message.from_user.first_name, message.text, CloackDate())
    await bot.send_message(message.from_user.id, 'Спасибо за обращение! Мы учтем все ваши жалобы и предложения!')
    await dp.storage.close()
    await dp.storage.wait_closed()


# Auto send message
async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)

async def sendToWorkers() :
    print('Заработало с main файла')
    for j in range(len(getMsgDate())) :
        if currentDate() in getMsgDate()[j]['msg_date'] :
            text = getMsgDate()[j]['msg_text']
            for i in getWorkerTgID() :
                print(i)
                await send_message(channel_id=i, text = text)
                getWorkerTgID().clear()

# Birthday send message
user = []
bday_user = []
all_tg_id = []

def bDay() :
    today = date.today()
    bday = today.strftime('%m-%d')
    return bday

def takeWorkers() :
    workers = actions.getWorkerss()
    for i in workers :
        user.append(i)
    return user
    

def get_birthday_name() :
    for row in takeWorkers() :
        # print(row)
        if bDay() == row['b_day'] :
            # print(row)
            bday_user = row
            bday_user_name = bday_user['name']
            bday_user_tg_id = bday_user['tg_id']
    takeWorkers().clear()
    return bday_user_name, bday_user_tg_id, bday_user



def get_workers_id() :
    if get_birthday_name()[2] != [] :
        for ro in takeWorkers() :
            if bday_user != ro :
                if ro['tg_id'] != 0 :
                    all_tg_id.append(ro['tg_id'])
        takeWorkers().clear()
    return all_tg_id
    

async def send_birthday() :
    if get_birthday_name()[0] != [] :
        await bot.send_message(chat_id = get_workers_id(), text = f'Сегодня день рождение у {get_birthday_name()[0]}')
    else :
        print('Not today!')


if __name__ == "__main__" :
    # executor.start_polling(dp, loop=loop, on_startup = onStartup)
    executor.start_polling(dp, loop=loop)
        