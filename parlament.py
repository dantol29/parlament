import telebot
from telebot import types

bot = telebot.TeleBot('5827972760:AAEKsxFXWT_vgGHaN7hNAlq4jJK3rcvStsA')
admin_chat_id = 843373640


def menu(message):
    global status
    status = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Anonīma sūdzība")
    item2 = types.KeyboardButton("Noteikumi")
    item3 = types.KeyboardButton("Idejas")
    markup.add(item1, item2, item3)
    bot.send_message(
        message.chat.id, "Izvēlieties vienu no manām komandām🤖", reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['start'])
def start_reply(message):
    global status
    status = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Anonīma sūdzība✉️")
    item2 = types.KeyboardButton("Idejas💡")
    item3 = types.KeyboardButton("Noteikumi📋")
    markup.add(item1, item2, item3)
    bot.send_message(
        message.chat.id, "Laipni lūdzam <b>Olaines 2. vidusskolas</b> bota🤖\nIzvēlies vienu no pogām", reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types="text")
def message_reply(message):
    global status
    if message.text == "Anonīma sūdzība":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Atpakaļ")
        markup.add(item1)
        bot.send_message(message.chat.id, "Uzrakstiet savu sūdzību✉️",
                         reply_markup=markup, parse_mode='html')
        status = 1
    elif message.text == "Atpakaļ":
        menu(message)
    elif message.text == "Idejas":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Atpakaļ")
        markup.add(item1)
        bot.send_message(message.chat.id, "Uzrakstiet savu ideju💡",
                         reply_markup=markup, parse_mode='html')
        status = 1
    elif status == 1:
        if len(message.text) > 7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Atpakaļ")
            markup.add(item1)
            bot.send_message(
                message.chat.id, "Paldies! Jūsu ziņa ir nosūtita!😀", reply_markup=markup)
            status = 0
            bot.forward_message(
                chat_id=admin_chat_id, from_chat_id=message.chat.id, message_id=message.message_id)
        else:
            bot.send_message(
                message.chat.id, "Man tas nepatīk!")
            menu(message)
    elif message.text == "Instrukcija":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Atpakaļ")
        markup.add(item1)
        bot.send_message(
            message.chat.id, "1. Nelieto lamuvārdus\n2. Neapvainojo skolēnus/skolotājus", reply_markup=markup)
        status = 0
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Atpakaļ")
        markup.add(item1)
        bot.send_message(
            message.chat.id, "Es nesaprotu..", reply_markup=markup)
        status = 0


status = 0
bot.polling(none_stop=True)
