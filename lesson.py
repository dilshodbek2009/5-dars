from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import main_menu, filial_buttons, bush_ish_joylari, tillar_bot, toshkent_bot, universal_xodim, \
    yaqin_joy_bot, toshkent_sh_bot, kuryer_buttons, call_buttons, bekor_bot, bektemir_bot, sergeli_bot, yashnabot_bot, \
    yakkasaroy_bot, yunisobod_bot, mirzo_ulugbek_bot, olmazor_bot, uchtepa_bot, cilonzor_bot, mirobot_bot, sahh_bot

BOT_TOKEN = "6820838705:AAGIJNepg2qk6Uk1IQyW4YB3K5uK2y-PQ_Q"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

evos = "https://avatars.mds.yandex.net/i?id=538ea3bb8d491ed7f2a87dc787e6c58d7c0ee3c8-9725170-images-thumbs&n=13"
evos_photo = "https://tashkent.hh.uz/employer-logo/4136381.jpeg"
evos_photo_oilasi = "https://images.app.goo.gl/pGiQ3p69YQfMb7eb6"
menu = "https://avatars.mds.yandex.net/i?id=f3684734ef812966ce9737bc27865d21be2bd2ae-9211743-images-thumbs&n=13"
evos_kontakt = "https://avatars.mds.yandex.net/i?id=c43936919f5a8f66eaddac141eb92f7072b9cb8a-11379499-images-thumbs&n=13"
photo = "https://avatars.mds.yandex.net/i?id=549031115e9e36734ee67610acae1c91d00b1b9d-12445014-images-thumbs&n=13"


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos, reply_markup=main_menu())


# -----------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="📍 Fililallar"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo,
                               reply_markup=filial_buttons(),
                               caption="""EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.

Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!""")


@dp.message_handler(Text(equals="☕️ Yaqin filiallarni ko'rsatish"))
async def start_bot(message: types.Message):
    await message.answer(text="Энг яқин филиални топиш учун жойлашувингизни юборинг", reply_markup=yaqin_joy_bot())


@dp.message_handler(Text(equals="Toshkent sh."))
async def start_bot(message: types.Message):
    await message.answer(text="Toshkent sh.", reply_markup=toshkent_sh_bot())


@dp.message_handler(Text(equals="🏢 Bosh ofis"))
async def start_bot(message: types.Message):
    with open("photo_2024-05-06_14-18-09.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""Manzil:  Furqat ko'chasi 175, 1-kirish, 4-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998712031212""")
        latitude = 41.324241
        longitude = 69.242080
        await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Samarqand Darvoza"))
async def start_bot(message: types.Message):
    with open("photo_2024-05-06_14-25-16.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""Filial: "Samarqand Darvoza"

Manzil: Qoratosh, 5A""")
        latitude = 41.324241
        longitude = 69.242080
        await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Oloy bozori"))
async def start_bot(message: types.Message):
    with open("photo_2024-05-06_14-28-14.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""Filial: Oloy bozori

Manzil: Amir Temur prospekti, 42

Kontakt: +998 71 203 12 12""")
        latitude = 41.324241
        longitude = 69.242080
        await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Malika"))
async def start_bot(message: types.Message):
    with open("photo_2024-05-06_14-29-55.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""Filial: Malika

Manzil: Bog'iravon, 29

Kontakt: +998 71 203 12 12""")
        latitude = 41.324241
        longitude = 69.242080
        await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Yahyo G'ulomov, 94"))
async def start_bot(message: types.Message):
    with open("photo_2024-05-06_14-31-47.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   caption="""Filial: Yahyo G'ulomov ko'chasi, 94

Manzil: Yahyo G'ulomov ko'chasi, 94

Kontak: +998 71 203 12 12""")
        latitude = 41.324241
        longitude = 69.242080
        await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="⬅️ Ortga2"))
async def start_bot(message: types.Message):
    await message.answer(text="Toshkent sh.", reply_markup=filial_buttons())


@dp.message_handler(Text(equals="⬅️ Орқага"))
async def start_bot(message: types.Message):
    await message.answer(text="Toshkent sh.", reply_markup=filial_buttons())


# -------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="🏢 Kompaniya haqida"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo_oilasi,
                               caption="""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


# ---------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="💼 Bo'sh ish o'rinlari"))
async def start_bot(message: types.Message):
    await message.answer(text="evos jamoasuga qushiling", reply_markup=bush_ish_joylari())


@dp.message_handler(Text(equals="Ortga ↩️"))
async def start_bot(message: types.Message):
    await message.answer(text="evos jamoasuga qushiling", reply_markup=main_menu())


@dp.message_handler(Text(equals="❌ Bekor qilish ❌"))
async def start_bot(message: types.Message):
    await message.answer(text="evos jamoasuga qushiling", reply_markup=main_menu())


@dp.message_handler(Text(equals="TOSHKENT"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=toshkent_bot())


@dp.message_handler(Text(equals="Universal xodim"))
async def photo_bot(message: types.Message):
    with open("photo_2024-05-06_13-34-25.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   reply_markup=universal_xodim(),
                                   caption="🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak       🕑 Erkin jadval (iloji bo'lsa)     ✔️ Yoqimli tashqi ko'rinish      💰 Ish haqi 17228.96 dan (soliqlargacha) bir soatiga", )


@dp.message_handler(Text(equals="Ortga ↩️2"))
async def start_bot(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang", reply_markup=bush_ish_joylari())


@dp.message_handler(Text(equals="Kuryer"))
async def photo_bot(message: types.Message):
    with open("photo_2024-05-06_15-01-17.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   reply_markup=kuryer_buttons(),
                                   caption="""📌 Yosh 20 dan 35 gacha

🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 Erkin jadval (iloji bo'lsa)

👨‍💼/👩‍💼 Chiroyli ko'rinish

🚘 Shaxsiy transport bo'lishligi shart

📍Oylik maosh joylashuv va regonga qarab""")


@dp.message_handler(Text(equals="Call-markaz operatori"))
async def photo_bot(message: types.Message):
    with open("photo_2024-05-06_15-25-22.jpg", "rb") as photo:
        await message.answer_photo(photo=photo,
                                   reply_markup=call_buttons(),
                                   caption="""📌 Yosh 18 dan 35 gacha

🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 To'liq bandlik

👨‍💼/👩‍💼 Chiroyli ko'rinish

🧑‍💻/👩‍💻 Kompyuter yoki noutbuk bo'lishi kerak
Biz taqdim etamiz:
- Rasmiy ish
- Kompaniya tomonidan taqdim etiladigan ovqatlanish
- Birinchi ish kuningizdan hisoblanadigan  ish xaqi
- Soatlik ish haqi""")


@dp.message_handler(Text(equals="Ortga ↩️3"))
async def start_bot(message: types.Message):
    await message.answer(text="orga", reply_markup=universal_xodim())


@dp.message_handler(Text(equals="Yunusobot"))
async def start_bot(message: types.Message):
    await message.answer(text="yunusobod", reply_markup=yunisobod_bot())


@dp.message_handler(Text(equals="Mirzo Ulug'bek"))
async def start_bot(message: types.Message):
    await message.answer(text="Mirzo Ulug'bek", reply_markup=mirzo_ulugbek_bot())


@dp.message_handler(Text(equals="Yashnabot"))
async def start_bot(message: types.Message):
    await message.answer(text="Yashnabot", reply_markup=yashnabot_bot())


@dp.message_handler(Text(equals="Yashnabot"))
async def start_bot(message: types.Message):
    await message.answer(text="Yashnabot", reply_markup=yashnabot_bot())


@dp.message_handler(Text(equals="Yakkasaroy"))
async def start_bot(message: types.Message):
    await message.answer(text="Yakkasaroy", reply_markup=yakkasaroy_bot())


@dp.message_handler(Text(equals="Uchtepa"))
async def start_bot(message: types.Message):
    await message.answer(text="Uchtepa", reply_markup=uchtepa_bot())


@dp.message_handler(Text(equals="Sergeli"))
async def start_bot(message: types.Message):
    await message.answer(text="Sergeli", reply_markup=sergeli_bot())


@dp.message_handler(Text(equals="Chilonzor"))
async def start_bot(message: types.Message):
    await message.answer(text="Chilonzor", reply_markup=cilonzor_bot())


@dp.message_handler(Text(equals="Mirobod"))
async def start_bot(message: types.Message):
    await message.answer(text="Mirobod", reply_markup=mirobot_bot())


@dp.message_handler(Text(equals="Shayxontohur"))
async def start_bot(message: types.Message):
    await message.answer(text="Shayxontohur", reply_markup=sahh_bot())


@dp.message_handler(Text(equals="Omazor"))
async def start_bot(message: types.Message):
    await message.answer(text="Omazor", reply_markup=sahh_bot())


@dp.message_handler(Text(equals="Bektemir"))
async def start_bot(message: types.Message):
    await message.answer(text="Bektemir", reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Bahodir"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Bahodir""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Oloy Bozori"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""oloy bozor""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Yunusobod"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""yunusobod""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Universam"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""universam""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Parkent"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""parkent""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Maksim Gorkiy"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""maksim gorki""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Qorasu"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""qorasu""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Ekobozor savdo markazi"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Ekobozor savdo markazi""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Сельхоз"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Сельхоз""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 TTZ"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""TTZ bozor""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Lisunova 2"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Lisunova 2""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Lisunova"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Lisunova""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Shota Rustaveli"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Shota Rustaveli""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Next Savdo Markazi"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Next Savdo Markazi""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Teatralny"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Teatralny""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Южный"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""📍Южный""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Beshqayrag'och"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Beshqayrag'och""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Fozil Tepа"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Fozil Tepа""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Lutfiy"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Lutfiy""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Sergeli"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Sergeli""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Sergeli Уangi Hayot"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Sergeli Уangi Hayot""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Chilonzor"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption=""" Chilonzor""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Algoritm"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Algoritm""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Magic City"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Magic City""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Katta qani"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Katta qani""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Qatortol"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Qatortol""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Orzu"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption=""" Orzu""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Qoraqamish 1/3"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Qoraqamish 1/3""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Oxunboboev"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Oxunboboev""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Qoraqamish 2/4"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""📍Qoraqamish 2/4""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Eski shahar"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""📍 Eski shahar""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍<<Compass>> savdo markazi"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Compass savdo markazi""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Vodnik"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Vodnik""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Bektemir"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""📍 Bektemir""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Qo'yliq"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption=""" Qo'yliq""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Borovskiy"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Borovskiy""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍ToshMI"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Sofiya"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="📍 Sofiya")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Chorsu GUM"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="""Chorsu GUM""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍 Samarqand darvoza"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption=""" Samarqand darvoza""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Navoiy ko'chasi"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="Navoiy ko'chasi")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍Beltepa"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="Beltepa")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


@dp.message_handler(Text(equals="📍1-shahar klinik shifoxonasi"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=photo,
                               caption="1-shahar klinik shifoxonasi")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude, reply_markup=bektemir_bot())


# ----------------------------------------------------------------------------------


async def stat_bot(message: types.Message):
    await message.answer_photo(photo=menu,
                               caption="<a href='https://evos.uz/'>Evos saytiga o'tish</a>",
                               parse_mode="HTML")
    await message.answer(
        text="<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a> | <a href='https://t.me/evosdeliverybot'>Telegram</a> | <a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>",
        parse_mode="HTML")


# -------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="📞 Kontaktlar/Manzil"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_kontakt,
                               caption="""Manzil: Furqat ko'chasi 175, kirish 1, 2-qavat. 
                        Mo'ljal: MAKRO THE TOWER
                        Kontakt: +998 71 203 12 12""")
    latitude = 41.324241
    longitude = 69.242080
    await message.answer_location(latitude=latitude, longitude=longitude)


# --------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="🇺🇿/🇷🇺 Til"))
async def start_bot(message: types.Message):
    await message.answer(text="tilni o'zgartirish", reply_markup=tillar_bot())


@dp.message_handler(Text(equals="⬅️ Ortga"))
async def start_bot(message: types.Message):
    await message.answer(text="evos jamoasuga qushiling", reply_markup=main_menu())


# -------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="🗣 Yangiliklar"))
async def start_bot(message: types.Message):
    await message.answer(text="""Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")


if __name__ == '__main__':
    executor.start_polling(dp)
