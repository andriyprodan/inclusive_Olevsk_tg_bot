import telebot
from telebot import types

import settings

# Your bot token from BotFather
TOKEN = settings.TOKEN

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Data for categories and corresponding Google Drive links
DATA = {
    "Банки": {
        "Банк 1": "https://drive.google.com/folder_bank1",
        "Банк 2": "https://drive.google.com/folder_bank2",
    },
    "Аптеки": {
        "Аптека 1": "https://drive.google.com/folder_apteka1",
        "Аптека 2": "https://drive.google.com/folder_apteka2",
    },
    "Лікарні": {
        "Лікарня 1": "https://drive.google.com/folder_hospital1",
        "Лікарня 2": "https://drive.google.com/folder_hospital2",
    },
}


# Start command handler
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    # Додаємо кнопки категорій
    markup.add(types.KeyboardButton("Банки"))
    markup.add(types.KeyboardButton("Аптеки"))
    markup.add(types.KeyboardButton("Лікарні"))

    # Відправляємо повідомлення
    bot.send_message(message.chat.id, "Виберіть категорію:", reply_markup=markup)


# Handling button presses (categories)
@bot.message_handler(
    func=lambda message: message.text in ["Банки", "Аптеки", "Лікарні"]
)
def category_selected(message):
    category = message.text
    addresses = DATA[category]

    # Create a new keyboard with the addresses as inline buttons
    markup = types.InlineKeyboardMarkup()
    for name, url in addresses.items():
        markup.add(types.InlineKeyboardButton(name, url=url))

    bot.send_message(
        message.chat.id, f"Адреси для категорії {category}:", reply_markup=markup
    )


# Help command handler
@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(message.chat.id, "Напишіть /start для початку.")


# Run the bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
