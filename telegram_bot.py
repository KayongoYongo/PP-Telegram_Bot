import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
from telegram import Update, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Access the variables
api_token = os.getenv("API_TOKEN")
username = os.getenv("USERNAME")


def start(update: Update, context: CallbackContext) -> None:
    """
    Handle the /start command.

    This function is called when the user starts a conversation with the bot by sending the /start command.
    It replies with a greeting message to welcome the user to the Greeting Bot.

    Parameters:
        update (telegram.Update): The update object containing information about the incoming message.
        context (telegram.ext.CallbackContext): The context object containing additional information and functionality for handling the update.

    Returns:
        None
    """
    update.message.reply_text('Hello! Welcome to the Tutorial Bot. Hope it works')


def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(api_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start handler
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()