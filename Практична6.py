import telebot
from telebot import types

TOKEN = '7681786484:AAGrPeSTyatKnncBtB52yMA4iv1BPUM9k48'
bot = telebot.TeleBot(config.TOKEN)

courses = {
    1: {'name': 'Курс Python', 'price': 1000},
    2: {'name': 'Курс Web-розробки', 'price': 1200}
}

@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = """
    Привіт! Я бот для продажу курсів.
    Ось доступні курси:
    1. Курс Python - 1000 грн
    2. Курс Web-розробки - 1200 грн
    
    Вибери курс, який хочеш купити, написавши номер (1 або 2).
    """
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(func=lambda message: message.text.isdigit())
def choose_course(message):
    course_id = int(message.text)
    if course_id in courses:
        course = courses[course_id]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button = types.KeyboardButton(f"Оплатити {course['name']} за {course['price']} грн")
        markup.add(button)
        bot.send_message(message.chat.id, f"Ви вибрали курс: {course['name']}. Натисніть кнопку для оплати.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Будь ласка, виберіть номер курсу: 1 або 2.")

@bot.message_handler(func=lambda message: "Оплатити" in message.text)
def payment(message):
    try:
        course_info = message.text.split(" за ")
        course_name = course_info[0].replace("Оплатити ", "")  
        course_price_str = course_info[1].replace(" грн", "")  
        course_price = int(course_price_str)

        bot.send_message(message.chat.id, f"Ви вибрали курс {course_name}. Вартість: {course_price} грн. Оплата вважається успішною!")
        bot.send_message(message.chat.id, f"Дякуємо за покупку! Ви успішно зареєстровані на курс: {course_name}.")
        bot.send_message(message.chat.id, "Якщо вам потрібно більше курсів, просто напишіть /start.")
    
    except Exception as e:
        print(f"Error in payment handler: {e}")
        bot.send_message(message.chat.id, "Щось пішло не так з обробкою вашої оплати. Спробуйте ще раз.")

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Bot polling error: {e}")
