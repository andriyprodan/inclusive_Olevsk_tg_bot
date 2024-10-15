import telebot
from telebot import types

import settings

# Your bot token from BotFather
TOKEN = settings.TOKEN

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Data for categories and corresponding Google Drive links
DATA = {
    "Освіта": {
        "Олевський ліцей № 1": "https://drive.google.com/folder_bank1",
        "Олевський ліцей № 2": "https://drive.google.com/folder_bank2",
        "Олевський ліцей № 3": "https://drive.google.com/folder_bank2",
        "ЦДЮТ": "https://drive.google.com/folder_bank2",
        "Мистецька школа “Олевська музична школа”": "https://drive.google.com/folder_bank2",
        'КУ "Олевський міжшкільний ресурсний центр" Олевської міської ради': "https://drive.google.com/folder_bank2",
        "ДНЗ «Олевський професійний ліцей»": "https://drive.google.com/folder_bank2",
    },
    "Медицина": {
        'КНП "Олевський Центр ПМД" Олевської міської ради': "https://drive.google.com/folder_apteka1",
        'Комунальна установа "Олевська центральна районна лікарня"': "https://drive.google.com/folder_apteka1",
        'Медичний центр “IVA”': "https://drive.google.com/folder_apteka1",
        'Медичний центр “Наш лікар”': "https://drive.google.com/folder_apteka1",
    },
    "Розваги": {
        "Міський Будинок культури": "https://drive.google.com/folder_hospital1",
        "Олевська публічна біблотека": "https://drive.google.com/folder_hospital2",
        "Кафе та ресторани міста": "https://drive.google.com/folder_hospital2",
    },
    "Послуги": {
        "Центр надання адміністративних послуг": "https://drive.google.com/folder_hospital1",
        "Олевський РЕМ": "https://drive.google.com/folder_hospital2",
        "ПриватБанк": "https://drive.google.com/folder_hospital2",
        "ОщадБанк": "https://drive.google.com/folder_hospital2",
        "Відділ обслуговування громадян № 4 (пенсійний фонд)": "https://drive.google.com/folder_hospital2",
        "Олевське управління Коростенської філії Житомирського ОЦЗ": "https://drive.google.com/folder_hospital2",
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
