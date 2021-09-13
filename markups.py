from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
import actions
import markup


def getDataMark() :
    with open('db/menu.json', encoding='utf-8') as fh :
        data = json.load(fh)
    return data

btnMain = KeyboardButton(getDataMark()['glavnaya']['main_text'])
btnGoToMain = KeyboardButton(getDataMark()['glavnaya']['after_text'])
btnBackTo = KeyboardButton(getDataMark()['glavnaya']['back_to'])

btnSertificates = KeyboardButton(getDataMark()['sertificates']['main_text'])
btnDocumentation = KeyboardButton(getDataMark()['documentation']['main_text'])
btnAboutCompany = KeyboardButton(getDataMark()['about_company']['main_text'])
btnSendLocation = KeyboardButton(getDataMark()['send_location']['main_text'], request_location=True)
btnAvans = KeyboardButton(getDataMark()['zayavlenie_na_avans']['main_text'])
btnZhalobaPredlozhenie = KeyboardButton(getDataMark()['zhaloba_predlozhenie']['main_text'])

# -- SECOND LEVEL MENU --
btnDogovorRealizacii = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['dogovor_realizatcii']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['dogovor_realizatcii']['main_text'])
btnDogovorKupliProdazhi = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['main_text'])
btnDogovorDestrib = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['destrib_dogovor']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['destrib_dogovor']['main_text'])
btnDogovorKonsignacii = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['dogovor_konsignacii']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['dogovor_konsignacii']['main_text'])
btnGetRekvezit = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['poluchit_rekvizity']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['poluchit_rekvizity']['main_text'])
btnZayavlenieAvans = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['zayavlenie_avans']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['zayavlenie_avans']['main_text'])
btnGetPrice = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['price']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['price']['main_text'])
btnSpecificationMello = InlineKeyboardButton(getDataMark()['documentation']['inside_menu']['specification_mello']['main_text'], callback_data=getDataMark()['documentation']['inside_menu']['specification_mello']['main_text'])
btnSamoeGlavnoeDlyaComp = KeyboardButton(getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['main_text'])
btnDlyaNovenkih = KeyboardButton(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['main_text'])

# Сертификаты inside
btnKazimpDistributor = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['kazimp_distributor']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['kazimp_distributor']['main_text'])
btnSgrLoson = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_loson']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_loson']['main_text'])
btnSgrMelloPodg = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_mello_podg']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_mello_podg']['main_text'])
btnSgrMolochLosyon = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_moloch_losyon']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_moloch_losyon']['main_text'])
btnSgrMyloKusk = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_mylo_kusk']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_mylo_kusk']['main_text'])
btnSgrPenkaDlyaRukTela = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['main_text'])
btnSgrPoroshok = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_poroshok']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_poroshok']['main_text'])
btnSgrVkladyshi = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_vkladyshi']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_vkladyshi']['main_text'])
btnSgrZhidkoeSrDlyaBelya = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['main_text'])
btnSertImportDo2023 = InlineKeyboardButton(getDataMark()['sertificates']['inside_menu']['sert_import_do_2023']['main_text'], callback_data=getDataMark()['sertificates']['inside_menu']['sert_import_do_2023']['main_text'])

btnMissionCompany = KeyboardButton(getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['misson_company']['main_text'])
btnVisionCompany = KeyboardButton(getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['main_text'])
btnCennostiCompany = KeyboardButton(getDataMark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['main_text'])
btnGoToTest = KeyboardButton(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['main_text'])
url_button = InlineKeyboardButton(text="Пройти тест", url=getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['link'])
btnStazhirovka = KeyboardButton(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['main_text'])
btnThisHelpYou = KeyboardButton(getDataMark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['main_text'])

# Главное меню
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(btnDocumentation, btnAboutCompany).add(btnSertificates).add(btnSendLocation).add(btnAvans).add(btnZhalobaPredlozhenie)
# Документация 🗃
btnDogovor = InlineKeyboardMarkup().add(btnDogovorRealizacii, btnDogovorKupliProdazhi).add(btnDogovorDestrib, btnDogovorKonsignacii).add(btnGetRekvezit, btnZayavlenieAvans).add(btnGetPrice, btnSpecificationMello)
# Сертификаты
btnToSertificates = InlineKeyboardMarkup().add(btnKazimpDistributor, btnSgrLoson).add(btnSgrMelloPodg, btnSgrMolochLosyon).add(btnSgrMyloKusk, btnSgrPenkaDlyaRukTela).add(btnSgrPoroshok, btnSgrVkladyshi).add(btnSgrZhidkoeSrDlyaBelya, btnSertImportDo2023)
# О компании !
secondLvlMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSamoeGlavnoeDlyaComp).add(btnDlyaNovenkih).add(btnGoToMain)
# Самое главное для компании💯
btnBackAbout = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMissionCompany).add(btnVisionCompany).add(btnCennostiCompany).add(btnBackTo).add(btnGoToMain)


btnBackDogovor = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDogovor, btnGoToMain)

# -- THIRD LEVEL MENU

btnBackAboutThird = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSamoeGlavnoeDlyaComp, btnDlyaNovenkih).add(btnMissionCompany, btnVisionCompany, btnCennostiCompany).add(btnGoToMain)

btnDlyaNovenkihThird = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGoToTest).add(btnStazhirovka).add(btnThisHelpYou).add(btnBackTo).add(btnGoToMain)
go_to_url = InlineKeyboardMarkup().add(url_button)

print(markup.challenge())
def btnChallengeYes() :
    btnChallengeYes = InlineKeyboardButton(markup.challenge()['yes'], callback_data=markup.challenge()['yes'])
    return btnChallengeYes

def btnChallengeNo() :
    btnChallengeNo = InlineKeyboardButton(markup.challenge()['no'], callback_data=markup.challenge()['no'])
    return btnChallengeNo
# Challenges
def buttonChallenge() :
    btnInlines = InlineKeyboardMarkup().add(btnChallengeYes(), btnChallengeNo())
    return btnInlines
