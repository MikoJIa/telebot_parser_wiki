import telebot
import wikipedia

# зададим параметр языка
wikipedia.set_lang('ru')


Token = '6644044267:AAEHmE0hurBxHR_cA4ysMOiE-tFU_lMJSzQ'

# подключаемся к нашему токену

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def welcom(message):
    bot.send_message(message.chat.id, "Hello, I am bot Niko. I can answer some answers!!!")


@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, "I am limited in answers")


@bot.message_handler(content_types=['text'])  # сдесь мы будем получать текст от пользователя
def talk(message):
    if message.text == 'Привет':  # это то что мы получаем от пользователя
        bot.send_message(message.chat.id, "Здравствуйте!! Как ваши дела?")  #  тут то что мы отправим от нашего бота
    # теперь пишем что мы будем отправлять
    elif message.text in ['Отлично', 'Хорошо', 'Прекрасно', 'Лучше всех']:
        bot.send_message(message.chat.id, "Я за вас очень рад!!!")
    else:
        low_r = message.text  # текст от пользователя с ключевым словом для поиска
        low_r = low_r.replace(' ', '_')    #  в нашем тексте нужно заменить все пробелы на нижнее подчёркивание
        page = wikipedia.page(low_r)  # тут мы передаём значение которое наш бот будет искать
        bot.send_message(message.chat.id, page.summary)  # передади нашу страничку через википедию


bot.polling(none_stop=True)  # это для того чтобы зациклился проект
