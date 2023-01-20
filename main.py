import openai
import telebot
from config import OPENAI_API_KEY, TOKEN_API

openai.api_key = (OPENAI_API_KEY)
bot = telebot.TeleBot(TOKEN_API)

@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id,text="Welcome to the smart search engine for a programmer. Ask any question in a message. The bot understands any language well, but we recommend making requests in English.")

@bot.message_handler(func = lambda message: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling(none_stop=True)