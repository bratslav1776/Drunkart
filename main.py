import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет')
    elif message.text == 'Кто ты?':
        bot.send_message(message.from_user.id, 'Я бот')
    elif message.text == 'Как тебя зовут?':
        bot.send_message(message.from_user.id, 'Меня зовут Drunkart03')
    elif message.text == 'Что ты умеешь?':
        bot.send_message(message.from_user.id, '"Я умею отвечать на несколько простых вопросов - кто я, как меня зовут и что я умею делать')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши что-то другое.')
        
bot.polling(none_stop=True, interval=0)    
