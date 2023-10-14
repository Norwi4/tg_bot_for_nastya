import telebot
from telebot import types
import logging
import asyncio
from aiogram.types import ChatActions

bot = telebot.TeleBot('5864236311:AAEwGXU0uyvxuiei2FSDiijtb8b2B9PTZpI')

#love = ['я тебя люблю', 'люблю тебя', 'люблю']

name = ''
surname = ''
age = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я буду подменять Женю, пока он занят работой и не будет на связи. Если тебе станет скучно, ты всегда можешь поболтать со мной!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def love(message):
    love = ['я тебя люблю', 'люблю тебя', 'люблю', 'я тебя люблю❤️', 'люблю тебя❤️', 'люблю❤️']
    come = ['когда ты приедешь?', 'скоро ты приедешь?', 'когда тебя ждать в гости?', 'когда тебя ждать?', 'ты скоро приедешь?', 'приезжай в гости', 'приезжай ко мне']
    logging.info(message.text)
    print(message.text)
    string = message.text.lower()
    if string in love:
        bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        bot.send_message(message.from_user.id, "и я тебя люблю, малышка❤️")
        #bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name

    elif string in come:
        bot.send_chat_action(message.chat.id, ChatActions.TYPING)
        bot.send_message(message.from_user.id, "я скоро приеду, дорогая \nно пока не знаю когда")
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")
        bot.send_message()

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

'''@bot.message_handler(content_types=['text'])
def st(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')'''





bot.polling(none_stop=True, interval=0)
