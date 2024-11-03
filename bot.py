#coding:utf-8

import telebot
import pytube
from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable

def download_videos_from_youtube(url):
      try:
         yt = YouTube(url)
      except VideoUnavailable:
           response = f'Video {url} is unavaialable, skipping.'

           video = f'err'
           return [ response,video]
      else:
         response = f'Downloading video: {url}'
         video = yt.streams.first().download()
         return [response , video]


api = open("API.txt",'r').read()

bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start','help'])
def send_welcome_message(message):
    bot.reply_to(message,'the bot is alive created by @Dragontechz')



@bot.message_handler(content_types=['text'])
def download_video_from_youtube(message):
    url = message.text
    try:
         yt = YouTube(url)
    except VideoUnavailable:
           response = f'Video {url} is unavaialable, skipping.'

           video = f'err'
           bot.send_video(message.chat_id,video)

    else:
         response = f'Downloading video: {url}'
         video = yt.streams.first().download()
         
         bot.send_video(message.chat_id,video)


bot.infinity_polling()