import telebot
import requests
import random

TOKEN = '8720508967:AAFjAmj4LID6utgZRy-RiYDzMPl2wY5IiWI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men rasm chiza oladigan botman.\n\nSavol yozing yoki 'rasm: ...' deb buyruq bering.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    if text.lower().startswith("rasm:"):
        prompt = text[5:].strip()
        bot.send_message(message.chat.id, "🎨 Rasm chizilyapti...")
        seed = random.randint(1, 99999)
        image_url = f"https://image.pollinations.ai/prompt/{prompt}?seed={seed}&width=1024&height=1024&nologo=true"
        try:
            bot.send_photo(message.chat.id, image_url, caption=f"✅ Rasm tayyor: {prompt}")
        except:
            bot.reply_to(message, "❌ Xatolik bo'ldi.")
    else:
        try:
            url = f"https://text.pollinations.ai/{text}?model=openai"
            r = requests.get(url, timeout=30)
            bot.reply_to(message, r.text)
        except:
            bot.reply_to(message, "⚠️ Ulanib bo'lmadi.")

bot.infinity_polling()

