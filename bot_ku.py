import telebot
import mysql.connector

import token_bot

from datetime import datetime
TOKEN=token_bot.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class MyBot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start','help'])
    def start(message):
        photo = open('foto/download (1).png','rb')
        myBot.send_photo(message.from_user.id,photo)
        teks = token_bot.SAPA  + "\n-- admin & developer @muhammadRvld - SMK Taruna Bhakti -- "+"\n" \
            "hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message,teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa "
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if (jmldata > 0):
            # print(data)
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data nihil')

        myBot.reply_to(message, str(kumpuldata))


print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)