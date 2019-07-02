import telebot

bot = telebot.TeleBot("752580762:AAG4dwXG4BpjPJ14fMlUnDo2NvtfpAiRv_E")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "я ебал твою тёлку":
        bot.send_message(message.chat.id, "у!")
    elif message.text == "как работа?":
        bot.send_message(message.chat.id, "пиарщики заебали")
    if message.text == "как дел?":
        bot.send_message(message.chat.id, "жиза говно")
    elif message.text == "смотри какая тачка":
        bot.send_message(message.chat.id, "ору")
    if message.text == "че делаешь":
        bot.send_message(message.chat.id, "лежу")
    if message.text == "что самое вкусное на свете?":
        bot.send_message(message.chat.id, "чипсики")
    elif message.text == "вот бы":
        bot.send_message(message.chat.id, "жирной хавки")
    if message.text == "что такое vc?":
        bot.send_message(message.chat.id, "TJournal знаешь?")
    elif message.text == "говно" or message.text == "уныло" or message.text == "жиза отстой":
        bot.send.message(message.chat.id, "ну ты шо")
    if message.text == "бля пиздец":
        bot.send_message(message.chat.id, "ёбаный рот этого казино")
    elif message.text == "кто самый крутой рэпер?":
        bot.send_message(message.chat.id, "оксимирон")

bot.polling(none_stop=True, interval=0)