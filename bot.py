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
        "Олевський ліцей № 1": "https://drive.google.com/drive/folders/TODO",
        "Олевський ліцей № 2": "https://drive.google.com/drive/folders/TODO",
        "Олевський ліцей № 3": "https://drive.google.com/drive/folders/TODO",
        "ЦДЮТ": "https://drive.google.com/drive/folders/TODO",
        "Мистецька школа “Олевська музична школа”": "https://drive.google.com/drive/folders/19eb63hU827yzmbPbKEs8vCSMK0dbey5K",
        'КУ "Олевський міжшкільний ресурсний центр" Олевської міської ради': "https://drive.google.com/drive/folders/TODO",
        "ДНЗ «Олевський професійний ліцей»": "https://drive.google.com/drive/folders/TODO",
    },
    "Медицина": {
        'КНП "Олевський Центр ПМД" Олевської міської ради': "https://drive.google.com/drive/folders/11Wy9jUvHF7Qgx7HRd1EcAeK0GGvu0AUg",
        'Комунальна установа "Олевська центральна районна лікарня"': "https://drive.google.com/drive/folders/TODO",
        'Медичний центр “IVA”': "https://drive.google.com/drive/folders/TODO",
        'Медичний центр “Наш лікар”': "https://drive.google.com/drive/folders/TODO",
    },
    "Розваги": {
        "Міський Будинок культури": "https://drive.google.com/drive/folders/TODO",
        "Олевська публічна біблотека": "https://drive.google.com/drive/folders/TODO",
        "Кафе та ресторани міста": "https://drive.google.com/drive/folders/TODO",
    },
    "Послуги": {
        "Центр надання адміністративних послуг": "https://drive.google.com/drive/folders/TODO",
        "Олевський РЕМ": "https://drive.google.com/drive/folders/TODO",
        "ПриватБанк": "https://drive.google.com/drive/folders/TODO",
        "ОщадБанк": "https://drive.google.com/drive/folders/1-C_PuvZ-_fV_TSQ4CSyRYOLffqyp5L8I",
        "Відділ обслуговування громадян № 4 (пенсійний фонд)": "https://drive.google.com/drive/folders/1-C_PuvZ-_fV_TSQ4CSyRYOLffqyp5L8I",
        "Олевське управління Коростенської філії Житомирського ОЦЗ": "https://drive.google.com/drive/folders/TODO",
    },
}


CATEGORY_NAMES = list(DATA.keys())


# Start command handler
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    # Додаємо кнопки категорій
    for category in CATEGORY_NAMES:
        markup.add(types.KeyboardButton(category))

    # Відправляємо повідомлення
    bot.send_message(message.chat.id, "Виберіть категорію:", reply_markup=markup)


# Handling button presses (categories)
@bot.message_handler(
    func=lambda message: message.text in CATEGORY_NAMES
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
    print('blah')
    bot.polling(none_stop=True)
