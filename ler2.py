import telebot
import os
import random

bot = telebot.TeleBot("752580762:AAG4dwXG4BpjPJ14fMlUnDo2NvtfpAiRv_E")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == "send nudes" or message.text.lower() == "сенд нудес":
        directory = 'C:/Users/Beeblebrox/lera/Ler1/nudes'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.chat.id, 'upload_photo')
        bot.send_photo(message.chat.id, img)
        img.close()
    elif message.text.lower() == "соси" or message.text.lower() == "иди на хуй" or message.text.lower() == "отъебись" or message.text.lower() == "иди на хуй!":
        bot.send_sticker(message.chat.id, 'CAADAgADqAQAAoJRKAPilBkMUTh-fgI')
    if message.text.lower() == "я ебал твою тёлку" or message.text.lower() == "я ебал твою телку":
        bot.send_message(message.chat.id, "у!")
    if message.text.lower() == "как дел?":
        bot.send_message(message.chat.id, "жиза говно")
    elif message.text.lower() == "смотри какая тачка":
        bot.send_message(message.chat.id, "ору")
    if message.text.lower() == "чё делаешь" or message.text.lower() == "че делаешь":
        bot.send_message(message.chat.id, "лежу") or bot.send_message(message.chat.id, "лежу-пержу")
    if message.text.lower() == "что самое вкусное на свете?":
        bot.send_message(message.chat.id, "чипсики")
    elif message.text.lower() == "чего бы ты хотела?":
        bot.send_message(message.chat.id, "денег и жирной хавки")
    if message.text.lower() == "что такое vc?" or message.text.lower() == "что такое vc.ru?" or message.text.lower() == "что такое виси?":
        bot.send_message(message.chat.id, "TJournal знаешь?")
    elif message.text.lower() == "говно" or message.text.lower() == "уныло" or message.text.lower() == "жиза отстой":
        bot.send.message(message.chat.id, "ну ты шо")
    if message.text.lower() == "бля пиздец":
        bot.send_message(message.chat.id, "ёбаный рот этого казино")
    elif message.text.lower() == "кто самый крутой рэпер?":
        bot.send_message(message.chat.id, "оксимирон")
    if message.text.lower() == "охуенно" or message.text.lower() == "охуенно!":
        bot.send_message(message.chat.id, "бля, да я знаю!")
    elif message.text.lower() == "ору" or message.text.lower() == "ору!" or message.text.lower() == "лол":
        bot.send_message(message.chat.id, "хули ты ржёшь?")
    if message.text.lower() == "чё делаешь?" or message.text.lower() == "че делаешь?":
        bot.send_message(message.chat.id, "лежу-пержу")
    elif message.text.lower() == "какое самое красивое место в мире?" or message.text.lower() == "где лучше всего жить?" or message.text.lower() == "куда бы ты хотела отправиться?":
        bot.send_message(message.chat.id, "На этот вопрос я могу однозначно ответить — Татарстан")
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "ДЕБИЛЫ БЛЯДЬ")
    elif message.text.lower() == "пизда":
        bot.send_message(message.chat.id, "пизда у тебя в штанах")
    if message.text.lower() == "нет":
        bot.send_message(message.chat.id, "пидора ответ")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "секс отстой")
    if message.text.lower() == "собаня" or message.text.lower() == "собака" or message.text.lower() == "соба" or message.text.lower() == "пёс" or message.text.lower() == "песа":
        bot.send_message(message.chat.id, "дыа")

bot.polling(none_stop=True, interval=0)