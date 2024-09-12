#Библиотеки
#import sqlite3
from telebot import types
import telebot
from telebot.types import WebAppInfo
bot = telebot.TeleBot('7155829029:AAHUBiFDEmAWw-x3oRKXmWny3VK9SIUdVFA') #Присвоение токена бота

#Начальные кнопки
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('💅 Услуги и прайс', web_app=WebAppInfo(url='https://exesens.github.io/kiseleva-make-up_price/'))
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('📆 Записаться', web_app=WebAppInfo(url='https://exesens.github.io/kiseleva_make_up_calendar/'))
    btn3 = types.InlineKeyboardButton('📝 Моя запись', callback_data='calendar')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('📷 Instagram', url='https://www.instagram.com/kiselevamake?igsh=Z2tjbmR3NW1sZnp0&utm_source=qr')
    btn5 = types.InlineKeyboardButton('💙 VK', url='https://vk.com/kiselevamuah')
    markup.row(btn4, btn5)
    btn6 = types.InlineKeyboardButton('📣 TG канал', url='https://t.me/kiselevamake')
    btn7 = types.InlineKeyboardButton('💬 Написать мне', url='https://t.me/tanya_kir30')
    markup.row(btn6, btn7)
    bot.send_message(message.chat.id, f'Привет <b>{message.from_user.first_name} {message.from_user.last_name}</b>! 😊\nВоспользуйся кнопками ниже👇', parse_mode='html', reply_markup=markup)
    if message.text=='/start':
        bot.delete_message(message.chat.id, message.message_id)

#Реакции нажатия кнопок (
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'price':
        bot.send_photo(callback.message.chat.id,'https://imageup.ru/img169/4912502/1.jpg')#Фото прайса 1
    elif callback.data == 'contacts':
        bot.send_message(callback.message.chat.id,'Мой тел: +79159998556')

#Команды меню
@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, '❗️ Данный бот предназначен для ознакомления с перечнем услуг и их стоимостью, а также для осуществления записи на данные услуги. Услуги оказывает визажист @tanya_kir30, г. Ярославль.')
    if message.text=='/info':
        bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['help'])
def mein(message):
    bot.send_message(message.chat.id, '❓ Появились вопросы касательно прайса или записи, нашли ошибку или вовсе что-то пошло не так? Напишите мне в ЛС  @tanya_kir30 и я помогу разобраться и решить проблему.')
    if message.text=='/help':
        bot.delete_message(message.chat.id, message.message_id)

#Блокировка переписки
@bot.message_handler()
def text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет <b>{message.from_user.first_name} {message.from_user.last_name}</b> 👋',parse_mode='html')
        bot.delete_message(message.chat.id, message.message_id)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До новых встреч! 👋')
        bot.delete_message(message.chat.id, message.message_id)
    else:
        bot.send_message(message.chat.id,'Прости, но я умею отвечать только на нажатие кнопок 😔\n\nНажми внизу кнопку "Меню" и выбери нужный пункт👇')
        bot.delete_message(message.chat.id, message.message_id)

#Бесконечная работа бота
bot.polling(non_stop=True)
