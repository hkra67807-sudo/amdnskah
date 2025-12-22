import telebot
import google.generativeai as genai
from fpdf import FPDF
import os
from flask import Flask
from threading import Thread

# سيرفر بسيط لضمان تشغيل البوت على Render مجاناً
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Online!"

# جلب المفاتيح من إعدادات Render
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    topic = message.text
    bot.reply_to(message, f"⏳ جاري تحضير بحث عن: {topic}...")
    try:
        response = model.generate_content(f"اكتب بحث مفصل باللغة العربية عن {topic}")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        clean_text = response.text.encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 10, txt=clean_text)
        path = f"{topic}.pdf"
        pdf.output(path)
        with open(path, 'rb') as f:
            bot.send_document(message.chat.id, f, caption="تفضل هذا بحثك مجاناً!")
        os.remove(path)
    except:
        bot.reply_to(message, "حدث خطأ، حاول مرة أخرى.")

if __name__ == "__main__":
    Thread(target=lambda: bot.polling(none_stop=True)).start()
    app.run(host='0.0.0.0', port=10000)
  
