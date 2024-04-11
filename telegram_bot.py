import os
from dotenv import load_dotenv
import telebot
from horoscopes import get_daily_horoscope

# Load environment variables from .env file
load_dotenv()

# Access the variables
BOT_TOKEN = os.getenv("API_TOKEN")
username = os.getenv("USERNAME")

# Added an instance of the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Review the purpose of the decorators
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """
    This function will handle welcoming the user
    
    Args:
        message: This will be the text that will trigger the function
    """
    # This messsage loads when the bot is started
    bot.reply_to(message, "Wassup, how are you doing?")

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    """
    This function will handle the sign of the horoscopes

    Args:
        message: This will be the text that will trigger the function
    """
    # The text is a string literal used to send a message from the bot to the user
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    # sends a message from the bot to the chat
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    # review the syntax of the register_next_step_handler
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    """
    This function will handle the sign of the horoscopes

    Args:
        message: This will be the text wthat will be handled
    """
    sign = message.text
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    # review the syntax of the send_message function
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    # Review the syntax of register_next_step_handler
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())

def fetch_horoscope(message, sign):
    """
    This function will handle the fetching of the horoscope information

    Args:
        message: This will be the text that will trigger the function
        sign: This will be used to fetch the specific horoscope
    """
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")

# Understand the syntax of the message_handler decorator
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # This function echoes the user's texts
    bot.reply_to(message, message.text)

# starts the bot and continuously polls for new messages from users.
bot.infinity_polling()