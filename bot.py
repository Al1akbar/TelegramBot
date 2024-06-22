import telebot
from PIL import Image

bot = telebot.TeleBot("token") ## @bot

@bot.message_handler(content_types=['photo'])
def file_handler(msg):
    try:
        print(msg)
        raw = msg.photo[-1].file_id
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        temp_file = 'temp.jpg'
        with open(temp_file, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(msg.chat.id, text='Rasm qabul qilindi. Kuting...')
        try:
            with Image.open(temp_file) as i:
                new_image = i.resize((354, 472))
                new_image_path = 'resized_image.png'
                new_image.save(new_image_path)
            with open(new_image_path, 'rb') as img_file:
                bot.send_photo(msg.chat.id, photo=img_file)
        except Exception as e:
            bot.send_message(msg.chat.id, text='Rasmni qayta ishlashda xatolik yuz berdi.')
            print(f'Error: {e}')
    except Exception as e:
        bot.send_message(msg.chat.id, text='Rasmni yuklashda xatolik yuz berdi.')
        print(f'Error: {e}')

@bot.message_handler(content_types=['text'])
def text_handler(msg):
    print(msg)

bot.polling(none_stop=True)
