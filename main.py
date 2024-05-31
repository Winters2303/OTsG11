import random
import telebot
from telebot import types

print('Bot has started.')

bot = telebot.TeleBot("ВАШ API КЛЮЧ")
# Чтобы получить API КЛЮЧ, нужно написать t.me/@botfather
updates = bot.get_updates()

# Load sentences for horoscope
with open("first.txt", "r", encoding="utf-8") as f1:
    first = f1.readlines()

with open("second.txt", "r", encoding="utf-8") as f2:
    second = f2.readlines()

with open("second_add.txt", "r", encoding="utf-8") as f2_add:
    second_add = f2_add.readlines()

with open("third.txt", "r", encoding="utf-8") as f3:
    third = f3.readlines()


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.from_user.id,
                     f"Привет, {message.from_user.first_name}! \nСейчас я расскажу тебе гороскоп на сегодня.")

    # Prepare buttons
    keyboard = types.InlineKeyboardMarkup()

    # Prepare text and handlers for each zodiac sign
    signs = [
        ('♈ Овен ♈', 'oven'),
        ('♉ Телец ♉', 'telec'),
        ('♊ Близнецы ♊', 'bliznecy'),
        ('♋ Рак ♋', 'rak'),
        ('♌ Лев ♌', 'lev'),
        ('♍ Дева ♍', 'deva'),
        ('♎ Весы ♎', 'vesy'),
        ('♏ Скорпион ♏', 'scorpion'),
        ('♐ Стрелец ♐', 'strelec'),
        ('♑ Козерог ♑', 'kozerog'),
        ('♒ Водолей ♒', 'vodoley'),
        ('♓ Рыбы ♓', 'ryby')
    ]

    for text, callback_data in signs:
        keyboard.add(types.InlineKeyboardButton(text=text, callback_data=callback_data))

    bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

# Method to handle received messages
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if updates:
        bot.send_message(message.from_user.id,
                         f"Привет, {message.from_user.first_name}! \nСейчас я расскажу тебе гороскоп на сегодня.")

        # Prepare buttons
        keyboard = types.InlineKeyboardMarkup()

        # Prepare text and handlers for each zodiac sign
        signs = [
            ('♈ Овен ♈', 'oven'),
            ('♉ Телец ♉', 'telec'),
            ('♊ Близнецы ♊', 'bliznecy'),
            ('♋ Рак ♋', 'rak'),
            ('♌ Лев ♌', 'lev'),
            ('♍ Дева ♍', 'deva'),
            ('♎ Весы ♎', 'vesy'),
            ('♏ Скорпион ♏', 'scorpion'),
            ('♐ Стрелец ♐', 'strelec'),
            ('♑ Козерог ♑', 'kozerog'),
            ('♒ Водолей ♒', 'vodoley'),
            ('♓ Рыбы ♓', 'ryby')
        ]

        for text, callback_data in signs:
            keyboard.add(types.InlineKeyboardButton(text=text, callback_data=callback_data))

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)



# Handler for button clicks
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # If a zodiac button is pressed, show the horoscope
    if call.data in ['oven', 'telec', 'bliznecy', 'rak', 'lev', 'deva', 'vesy', 'scorpion', 'strelec', 'kozerog',
                     'vodoley', 'ryby']:
        # Form the horoscope
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
            second_add) + ' ' + random.choice(third)
        msg = msg.replace("\n", "")

        # Send the horoscope message in Telegram
        bot.send_message(call.message.chat.id, msg)


# Start polling the bot
bot.polling(none_stop=True, interval=0)
