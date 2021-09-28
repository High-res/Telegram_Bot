from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters.builtin import Command
from datetime import datetime, date, time
import time
from main import dp, bot
from src.actions.getUser import addUser
from src.actions.addLocation import addLocation
from src.actions.getChallenge import getChallengeAction, addChallengeAction
from src.actions.getAvans import getAvans
from src.actions.addToDocx import addToDocx
from src.actions.getZhaloba import getZhaloba
from src.challengeDependency.challengeMarkup import challenge, hoursToMinutes, HourMinute
from src.markups.markups import getDataMark, Menues
from src.mainFunctions.tgUsers import tgUsers
from src.mainFunctions.currentDate import RegDate
from src.mainFunctions.AllWorkersTgID import AllWorkersTgID



def CloackDate() :
    cloak_date = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    return cloak_date

def getDate() :
    today = date.today()
    year = today.strftime('%Y-%m-%d')
    day = today.strftime('%Y-%m')
    return year, day
class Mydialog(StatesGroup):
    otvet = State()
    zhaloba = State()


@dp.message_handler(Command("start"))
async def start_command(message: types.Message): 
    userName = message.from_user.first_name
    userID = message.from_user.id
    if userID in tgUsers() :
        print('Такой пользователь существует')
    else :
        addUser(userName, userID, RegDate())
    tgUsers().clear()
    await bot.send_message(message.from_user.id, getDataMark()['glavnaya']['main_text'], reply_markup=Menues()[0])

@dp.message_handler()
async def documentation_handler(message: types.Message) :
    if message.text == getDataMark()['documentation']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['documentation']['after_text'], reply_markup=Menues()[1] )
    elif message.text == getDataMark()['about_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['after_text'], reply_markup=Menues()[3])
    # Самое главное для компании💯
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['after_text'], reply_markup=Menues()[4])
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['misson_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['misson_company']['after_text'], reply_markup=Menues()[4])
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['after_text'], reply_markup=Menues()[4])
        await bot.send_photo(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['links'])
    elif message.text == getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text'], reply_markup=Menues()[4])
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text_1'], reply_markup=Menues()[4])
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text_2'], reply_markup=Menues()[4])
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['after_text_3'], reply_markup=Menues()[4])
    # Назад до О компании
    elif message.text == getDataMark()['glavnaya']['back_to'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['after_text'], reply_markup=Menues()[3])
    # Для новеньких
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['after_text'], reply_markup=Menues()[5])
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['after_text'], reply_markup=Menues()[6])
        # await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['link'], reply_markup=Menues()[5])
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['main_text'] :
        f = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['link'], 'rb')
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['after_text'], reply_markup=Menues()[5])
        await bot.send_document(message.from_user.id, f)
    elif message.text == getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['main_text'] :
        f = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link'], 'rb')
        a = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_1'], 'rb')
        s = open(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_2'], 'rb')
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['after_text'], reply_markup=Menues()[5])
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_text'], reply_markup=Menues()[5])
        await bot.send_document(message.from_user.id, f)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_1_text'], reply_markup=Menues()[5])
        await bot.send_document(message.from_user.id, a)
        await bot.send_message(message.from_user.id, getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['link_2_text'], reply_markup=Menues()[5])
        await bot.send_document(message.from_user.id, s)
    # Сертификаты
    elif message.text == getDataMark()['sertificates']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['sertificates']['after_text'], reply_markup=Menues()[2])
    # Заявление на аванс
    elif message.text == getDataMark()['zayavlenie_na_avans']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['zayavlenie_na_avans']['after_text'], )
        await Mydialog.otvet.set()
        # Получить автоматически id отправителя и сегодняшнюю дату, что бы он написал сумму сохранить сначала это в json после отправкой письма или в сверстанном макете вывести
    # Жалоба и предложение
    elif message.text == getDataMark()['zhaloba_predlozhenie']['main_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['zhaloba_predlozhenie']['after_text'])
        await Mydialog.zhaloba.set()
    elif message.text == getDataMark()['glavnaya']['after_text'] :
        await bot.send_message(message.from_user.id, getDataMark()['glavnaya']['main_text'], reply_markup=Menues()[0])

# Локация
@dp.message_handler(content_types=['location'])
async def getLocation(message: types.Message) :
    addLocation(message.from_user.first_name, message.from_user.id, message.location.latitude, message.location.longitude, CloackDate(), getDate()[0], getDate()[1])
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

@dp.callback_query_handler(lambda c: c.data == getDataMark()['documentation']['inside_menu']['dogovor_konsignacii']['main_text'])
async def destrib_dogovor(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['documentation']['inside_menu']['dogovor_konsignacii']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['documentation']['inside_menu']['dogovor_konsignacii']['after_text'])
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

# Сертификаты документы
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['kazimp_distributor']['main_text'])
async def KazimpDistributor(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['kazimp_distributor']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['kazimp_distributor']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_loson']['main_text'])
async def sgr_loson(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_loson']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_loson']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_mello_podg']['main_text'])
async def sgr_mello_podg(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_mello_podg']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_mello_podg']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_moloch_losyon']['main_text'])
async def sgr_moloch_losyon(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_moloch_losyon']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_moloch_losyon']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_mylo_kusk']['main_text'])
async def sgr_mylo_kusk(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_mylo_kusk']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_mylo_kusk']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['main_text'])
async def sgr_penka_dlya_ruk_tela(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_poroshok']['main_text'])
async def sgr_poroshok(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_poroshok']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_poroshok']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_vkladyshi']['main_text'])
async def sgr_vkladyshi(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_vkladyshi']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_vkladyshi']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['main_text'])
async def sgr_zhidkoe_sr_dlya_belya(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
@dp.callback_query_handler(lambda c: c.data == getDataMark()['sertificates']['inside_menu']['sert_import_do_2023']['main_text'])
async def sert_import_do_2023(callback_query: types.CallbackQuery) :
    await bot.answer_callback_query(callback_query.id)
    f = open(getDataMark()['sertificates']['inside_menu']['sert_import_do_2023']['links'], 'rb')
    await bot.send_message(callback_query.from_user.id, getDataMark()['sertificates']['inside_menu']['sert_import_do_2023']['after_text'])
    await bot.send_document(callback_query.from_user.id, f)
challengeTgID = []
def getChallengeActionTgId() :
    TgID = getChallengeAction()
    for i in TgID :
        if challenge()['send_time_1'] :
            if hoursToMinutes(HourMinute()) > hoursToMinutes(challenge()['send_time_1']) :
                challengeTgID.append(i['tg_id'])
    return challengeTgID


# Challenge answer here!
@dp.callback_query_handler(lambda c: c.data == challenge()['no'])
async def answerMessageNo(callback_query: types.CallbackQuery) :
    
    if callback_query.from_user.id in getChallengeActionTgId() :
        print('Пользователь проголосовал')
    else :
        addChallengeAction(callback_query.message.text, callback_query.data, callback_query.from_user.id, CloackDate(), HourMinute())
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, challenge()['answerNo'])
   

@dp.callback_query_handler(lambda c: c.data == challenge()['yes'])
async def answerMessageYes(callback_query: types.CallbackQuery) :
    if callback_query.from_user.id in getChallengeActionTgId() :
        print('Пользователь проголосовал')
    else :
        addChallengeAction(callback_query.message.text, callback_query.data, callback_query.from_user.id, CloackDate(), HourMinute())
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, challenge()['answerYes'])

    





@dp.message_handler(state=Mydialog.otvet)
async def answerAvans(message: types.Message, state: FSMContext) :
    if message.from_user.id in AllWorkersTgID() :
        getAvans(message.from_user.id, message.from_user.first_name, message.text, CloackDate())
        await message.reply('Ваше заявление принято, ожидайте!', reply=False)
        await addToDocx()
        await dp.storage.close()
        await dp.storage.wait_closed()
    else :
        await  message.reply('Вы не являетесь сотрудником, свяжитесь с Маржан для выяснения обстоятельств', reply=False)
        await dp.storage.close()
        await dp.storage.wait_closed()

    # Есть баг тут нужно решить!!!!
    

@dp.message_handler(state=Mydialog.zhaloba)
async def zhaloba(message: types.Message, state: FSMContext) :
    getZhaloba(message.from_user.id, message.from_user.first_name, message.text, CloackDate())
    await bot.send_message(message.from_user.id, 'Спасибо за обращение! Мы учтем все ваши жалобы и предложения!')
    await dp.storage.close()
    await dp.storage.wait_closed()

