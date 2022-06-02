import wikipedia
import settings
import telebot

bot = telebot.TeleBot(settings.bot_token)


@bot.message_handler(commands=['help'])
def help(message):
    msg = 'Для выполнения запроса введите : /poisk "ключивое слово для поиска"'
    bot.send_message(message.chat.id, msg, parse_mode='html')


@bot.message_handler(commands=['poisk'])
def poisk(message):
    query = message.text.split()
    if len(query) > 1:
        arg = ''.join(query[1:])
    st = wikipedia.search(query, results=10, suggestion=True)
    result = wikipedia.summary(query, sentences=10, chars=0, auto_suggest=True)

    bot.send_message(message.chat.id, st, parse_mode='html')
    bot.send_message(message.chat.id, result, parse_mode='html')


print('Бот запущен')
bot.polling(non_stop=True)
