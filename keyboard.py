from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 Kompaniya haqida"), KeyboardButton(text="📍 Fililallar"))
    rkm.row(KeyboardButton(text="💼 Bo'sh ish o'rinlari"))
    rkm.row(KeyboardButton(text="Menyu"), KeyboardButton(text="🗣 Yangiliklar"))
    rkm.row(KeyboardButton(text="📞 Kontaktlar/Manzil"), KeyboardButton(text="🇺🇿/🇷🇺 Til"))
    return rkm
# -----------------------------------------------------------------------------------


def tillar_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha"))
    rkm.row(KeyboardButton(text="⬅️ Ortga"), )
    return rkm
# ------------------------------------------------------------------------------------


def filial_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Yaqin filiallarni ko'rsatish"))
    rkm.row(KeyboardButton(text="🏢 Bosh ofis"), KeyboardButton(text="Toshkent sh."))
    rkm.row(KeyboardButton(text="⬅️ Ortga"), )
    return rkm


def yaqin_joy_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Yaqin filiallni ko'rsatish", request_location=True))
    rkm.row(KeyboardButton(text="⬅️ Орқага"))
    return rkm


def toshkent_sh_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Samarqand Darvoza"), KeyboardButton(text="📍 Oloy bozori"))
    rkm.row(KeyboardButton(text="📍 Malika"), KeyboardButton(text="📍 Yahyo G'ulomov, 94"))
    rkm.row(KeyboardButton(text="⬅️ Ortga2"), )
    return rkm
# -----------------------------------------------------------------------------------


def bush_ish_joylari():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="TOSHKENT"), KeyboardButton(text="SAMARQAND"))
    rkm.row(KeyboardButton(text="NAMANGAN"), KeyboardButton(text="NAVOIY"))
    rkm.row(KeyboardButton(text="ANDIJON"), KeyboardButton(text="JIZZAX"))
    rkm.row(KeyboardButton(text="NUKUS"), KeyboardButton(text="XORAZM"))
    rkm.row(KeyboardButton(text="SURXONDARYO"), KeyboardButton(text="QASHQADARYO"))
    rkm.row(KeyboardButton(text="Quqon"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm

# ----------------------------------------------------------------------------------------------


def toshkent_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal xodim"), KeyboardButton(text="Call-markaz operatori"))
    rkm.row(KeyboardButton(text="Kuryer"), )
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def universal_xodim():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Yunusobot"), KeyboardButton(text="Mirzo Ulug'bek"))
    rkm.row(KeyboardButton(text="Yashnabot"), KeyboardButton(text="Yakkasaroy"))
    rkm.row(KeyboardButton(text="Uchtepa"), KeyboardButton(text="Sergeli"))
    rkm.row(KeyboardButton(text="Chilonzor"), KeyboardButton(text="Mirobod"))
    rkm.row(KeyboardButton(text="Shayxontohur"), KeyboardButton(text="Omazor"))
    rkm.row(KeyboardButton(text="Bektemir"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def kuryer_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Olmazor"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def call_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Chilonzor"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def yunisobod_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Bahodir"), KeyboardButton(text="📍Oloy Bozori")), KeyboardButton(text="📍Yunusobod")
    rkm.row(KeyboardButton(text="📍Universam"), )
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def mirzo_ulugbek_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Parkent"), KeyboardButton(text="📍Maksim Gorkiy")), KeyboardButton(text="📍Qorasu")
    rkm.row(KeyboardButton(text="📍Ekobozor savdo markazi"), KeyboardButton(text="📍Сельхоз")), KeyboardButton(text="📍 TTZ")
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def yashnabot_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Lisunova 2"), KeyboardButton(text="📍Lisunova"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def yakkasaroy_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Shota Rustaveli"), KeyboardButton(text="📍 Muqimiy")), KeyboardButton(text="📍Next Savdo Markazi")
    rkm.row(KeyboardButton(text="📍Teatralny"), KeyboardButton(text="📍Южный"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def uchtepa_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Beshqayrag'och"), KeyboardButton(text="📍Fozil Tepа")), KeyboardButton(text="📍Lutfiy")
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def sergeli_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Sergeli"), KeyboardButton(text="📍Sergeli Уangi Hayot")), KeyboardButton(text="📍 Sergeli Yarmarka")
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def cilonzor_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Chilonzor"), KeyboardButton(text="📍 Algoritm")), KeyboardButton(text="📍Magic City")
    rkm.row(KeyboardButton(text="📍Katta qani"), KeyboardButton(text="📍Qatortol"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def olmazor_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Orzu"), KeyboardButton(text="📍Qoraqamish 1/3")), KeyboardButton(text="📍Oxunboboev")
    rkm.row(KeyboardButton(text="📍Qoraqamish 2/4"), KeyboardButton(text="📍 Eski shahar"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def bektemir_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍<<Compass>> savdo markazi"), KeyboardButton(text="📍Vodnik")), KeyboardButton(text="📍 Bektemir")
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def mirobot_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Qo'yliq"), KeyboardButton(text="📍Borovskiy"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def sahh_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍ToshMI"), KeyboardButton(text="📍 Sofiya"), KeyboardButton(text="📍Chorsu GUM"))
    rkm.row(KeyboardButton(text="📍 Samarqand darvoza"), KeyboardButton(text="📍Navoiy ko'chasi"), KeyboardButton(text="📍Beltepa"))
    rkm.row(KeyboardButton(text="📍1-shahar klinik shifoxonasi"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️2"))
    return rkm


def bekor_bot():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️3"))
    return rkm