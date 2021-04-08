import telebot
import parse
import words

bot = telebot.TeleBot('1496906755:AAGWQlB_BhGJCne7kRLc4FmVjNfquUUE1vw')

dialogue = {
    "как тебя зовут?": "БостестоБот",
    "ты точно сам отвечаешь?": "Нет, я просто скидываю сообщения, которые в меня заложили",
    "а когда он это сделает?": "Когда-нибудь...в общем режим хатико включен",
    "спасибо тебе": "На что запрограмиировали, то и делаю",
    "пока": "Покеда пап"
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, words.helos())


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, words.dos)


@bot.message_handler(commands=['goods'])
def start_message(message):
    bot.send_message(message.chat.id, words.oods())


@bot.message_handler(commands=['vacancy'])
def start_message(message):
    bot.send_message(message.chat.id, parse.answers)


@bot.message_handler(content_types=['text'])
def send_text(message):
    mess = message.text.lower()

    if mess == "привет":
        bot.send_message(message.chat.id, words.helos())
    elif mess == 'как дела?':
        bot.send_message(message.chat.id, words.ows())
    elif mess == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif mess in dialogue:
        bot.send_message(message.chat.id, dialogue[mess])
    else:
        bot.send_message(message.chat.id, 'Я не знаю что ответить')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
