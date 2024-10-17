from random import *
import json
import requests
import telebot
films = []

API_TOKEN = '7002491636:AAG04JvzXm0cx2YSgwXrnYyocAG0vaXXSBo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start']) #декоратор хз что это - связываем команду старт с ботом
def start_message(message):
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта Барбара")
    bot.send_message(message.chat.id,"Фильмотека была загружена по умолчанию!")

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,"Вот список фильмов")
        bot.send_message(message.chat.id, ", ".join(films))
    except:
        bot.send_message(message.chat.id, "Фильмов нема")

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    bot.send_message(message.chat.id,"Наша фильмотека была успешно сохранена в файле films.json")

bot.polling()
