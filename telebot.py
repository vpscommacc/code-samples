import telebot
import looking_for_vacancies
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
    """
    Приветствующее сообщение на команду /start

    :param message: переменная
    :type message: telebot.object
    :return: случайное приветствие
    """
    bot.send_message(message.chat.id, words.helos())


@bot.message_handler(commands=['help'])
def start_message(message):
    """
    Вывод умений бота
    :param message: переменная
    :type message: telebot.object
    :return: список умений бота
    """
    bot.send_message(message.chat.id, words.dos)


@bot.message_handler(commands=['goods'])
def start_message(message):
    """
    Похвальное сообщение на команду goods
    :param message: переменная
    :type message: telebot.object
    :return: случайная похвала
    """
    bot.send_message(message.chat.id, words.oods())


@bot.message_handler(commands=['vacancy'])
def start_message(message):
    """
    Вывод вакансий сметчиков
    :param message: переменная
    :type message: telebot.object
    :return: список вакансий сметчиков в Москве с высокими зарплатами
    """
    bot.send_message(message.chat.id, looking_for_vacancies.answers)


@bot.message_handler(content_types=['text'])
def send_text(message):
    """
    Ответ на то или иное сообщение от пользователя
    :param message: сообщение от пользовательтеля
    :type message: telebot.object
    :return: ответ на введёное сообщение
    """
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
    """
    Вывод стикера
    :param message: переменная
    :type message: telebot.object
    :return: стикер
    """
    print(message)


bot.polling()
