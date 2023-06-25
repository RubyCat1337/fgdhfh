import telebot


def bot_send(bot_token, chat_id,message):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id,message)