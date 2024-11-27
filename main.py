from telebot import TeleBot

bot = TeleBot("7755084538:AAGZ3U28C0EyqSobD4vAZjvC-6541fFIgcE")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Ответь правильно на вопросы и ты получишь секретный код")
    bot.send_message(message.chat.id, "Напиши 'Я готов', чтобы начать.")


@bot.message_handler(content_types=["text"])
def first_task(message):
    user_response = message.text.lower()
    if user_response == "я готов":
        bot.send_message(message.chat.id, "Отлично, первая часть кода: 60")
        bot.send_message(message.chat.id, "Следующий вопрос: Из какого цветка было сделано снотворное для Джульетты?")
    elif user_response == "лютик":
        bot.send_message(message.chat.id, "Правильно, следующая чать кода: 303027")
        bot.send_message(message.chat.id, "Следующий вопрос: Любимый завтрак твоей девушки?")
    elif user_response == "блины":
        bot.send_message(message.chat.id, "Правильно, следующая часть кода: 25")
        bot.send_message(message.chat.id, "Следующий вопрос: В какой стране была твоя девушка впервые заграницей?")
    elif user_response == "болгария":
        bot.send_message(message.chat.id, "Отлично! Последняя часть кода: 052928")
    else:
        bot.send_message(message.chat.id, "Неправильно!")


bot.infinity_polling()











