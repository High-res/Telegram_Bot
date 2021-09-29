from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from src.challengeDependency.challengeMarkup import challenge


def get_data_mark() :
    with open('src/db/menu.json', encoding='utf-8') as fh :
        data = json.load(fh)
    return data

btnMain = KeyboardButton(get_data_mark()['glavnaya']['main_text'])
btnGoToMain = KeyboardButton(get_data_mark()['glavnaya']['after_text'])
btnBackTo = KeyboardButton(get_data_mark()['glavnaya']['back_to'])

btnSertificates = KeyboardButton(get_data_mark()['sertificates']['main_text'])
btnDocumentation = KeyboardButton(get_data_mark()['documentation']['main_text'])
btnAboutCompany = KeyboardButton(get_data_mark()['about_company']['main_text'])
btnSendLocation = KeyboardButton(get_data_mark()['send_location']['main_text'], request_location=True)
btnAvans = KeyboardButton(get_data_mark()['zayavlenie_na_avans']['main_text'])
btnZhalobaPredlozhenie = KeyboardButton(get_data_mark()['zhaloba_predlozhenie']['main_text'])

# -- SECOND LEVEL MENU --
btnDogovorRealizacii = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['dogovor_realizatcii']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['dogovor_realizatcii']['main_text'])
btnDogovorKupliProdazhi = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['dogovor_kupli_prodazhi']['main_text'])
btnDogovorDestrib = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['destrib_dogovor']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['destrib_dogovor']['main_text'])
btnDogovorKonsignacii = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['dogovor_konsignacii']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['dogovor_konsignacii']['main_text'])
btnGetRekvezit = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['poluchit_rekvizity']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['poluchit_rekvizity']['main_text'])
btnZayavlenieAvans = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['zayavlenie_avans']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['zayavlenie_avans']['main_text'])
btnGetPrice = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['price']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['price']['main_text'])
btnSpecificationMello = InlineKeyboardButton(get_data_mark()['documentation']['inside_menu']['specification_mello']['main_text'], callback_data=get_data_mark()['documentation']['inside_menu']['specification_mello']['main_text'])
btnSamoeGlavnoeDlyaComp = KeyboardButton(get_data_mark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['main_text'])
btnDlyaNovenkih = KeyboardButton(get_data_mark()['about_company']['inside_menu']['dlya_novenkih']['main_text'])

# Сертификаты inside
btnKazimpDistributor = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['kazimp_distributor']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['kazimp_distributor']['main_text'])
btnSgrLoson = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_loson']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_loson']['main_text'])
btnSgrMelloPodg = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_mello_podg']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_mello_podg']['main_text'])
btnSgrMolochLosyon = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_moloch_losyon']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_moloch_losyon']['main_text'])
btnSgrMyloKusk = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_mylo_kusk']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_mylo_kusk']['main_text'])
btnSgrPenkaDlyaRukTela = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_penka_dlya_ruk_tela']['main_text'])
btnSgrPoroshok = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_poroshok']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_poroshok']['main_text'])
btnSgrVkladyshi = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_vkladyshi']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_vkladyshi']['main_text'])
btnSgrZhidkoeSrDlyaBelya = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sgr_zhidkoe_sr_dlya_belya']['main_text'])
btnSertImportDo2023 = InlineKeyboardButton(get_data_mark()['sertificates']['inside_menu']['sert_import_do_2023']['main_text'], callback_data=get_data_mark()['sertificates']['inside_menu']['sert_import_do_2023']['main_text'])

btnMissionCompany = KeyboardButton(get_data_mark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['misson_company']['main_text'])
btnVisionCompany = KeyboardButton(get_data_mark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['vision_company']['main_text'])
btnCennostiCompany = KeyboardButton(get_data_mark()['about_company']['inside_menu']['samoe_glavnoe_dlya_companii']['inside_menu']['cennosti_company']['main_text'])
btnGoToTest = KeyboardButton(get_data_mark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['main_text'])
url_button = InlineKeyboardButton(text="Пройти тест", url=get_data_mark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['proiti_test']['link'])
btnStazhirovka = KeyboardButton(get_data_mark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['plan_stazhirovki']['main_text'])
btnThisHelpYou = KeyboardButton(get_data_mark()['about_company']['inside_menu']['dlya_novenkih']['inside_menu']['eto_pomozhet']['main_text'])
def menues() :
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


    # -- THIRD LEVEL MENU

    btnBackAboutThird = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGoToTest).add(btnStazhirovka).add(btnThisHelpYou).add(btnBackTo).add(btnGoToMain)

    go_to_url = InlineKeyboardMarkup().add(url_button)

    return mainMenu, btnDogovor, btnToSertificates, secondLvlMenu, btnBackAbout, btnBackAboutThird, go_to_url

def btn_challenge_yes() :
    btnChallengeYes = InlineKeyboardButton(challenge()['yes'], callback_data=challenge()['yes'])
    return btnChallengeYes

def btn_challenge_no() :
    btnChallengeNo = InlineKeyboardButton(challenge()['no'], callback_data=challenge()['no'])
    return btnChallengeNo
# Challenges
def button_challenge() :
    btnInlines = InlineKeyboardMarkup().add(btn_challenge_yes(), btn_challenge_no())
    return btnInlines
