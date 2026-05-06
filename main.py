import telebot
import requests
import os

# Telegram bot tokeningiz
TOKEN = '8720508967:AAFjAmj4LID6utgZRy-RiYDzMPl2wY5IiWI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def answer_everything(message):
    try:
        # Pollinations AI tizimi (Wikipedia va hamma ma'lumotni biladi)
        url = f"https://text.pollinations.ai/{message.text}?model=openai"
        r = requests.get(url, timeout=20)
        
        if r.status_code == 200:
            bot.reply_to(message, r.text)
        else:
            bot.reply_to(message, "AI biroz charchadi, qayta yozing.")
    except:
        bot.reply_to(message, "Ulanishda xato bo'ldi.")

print("Bot serverda ishga tushdi!")
bot.infinity_polling()
