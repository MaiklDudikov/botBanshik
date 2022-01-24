import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Баня 🍻")
    item2 = types.KeyboardButton("😊 Как дела ?")
    item3 = types.KeyboardButton("Привет 😎")
    item4 = types.KeyboardButton("🎲 Рандомное число")
    item5 = types.KeyboardButton("💵 Кубышка")
 
    markup.add(item1, item2, item3, item4, item5)
 
    bot.send_message(message.chat.id, "Привет, {0.first_name} !\nЯ - <b>{1.first_name}</b>, созданный чтобы быть полезным для Вас !)".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела ?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, сам как, братишка ? 😉', reply_markup=markup)
        elif message.text == 'Привет 😎':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Работаю", callback_data='work')
            item2 = types.InlineKeyboardButton("На раслабоне", callback_data='not work')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Чем занимаешься, брат ? 😁', reply_markup=markup)
        elif message.text == 'Баня 🍻':

            markup = types.InlineKeyboardMarkup(row_width=2) # ширина ряда
            item1 = types.InlineKeyboardButton("Да 👍", callback_data='yes')
            item2 = types.InlineKeyboardButton("Нет 🙅‍♂️", callback_data='no')
            item3 = types.InlineKeyboardButton("Пока не знаю 🤷‍♂️", callback_data='if')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Ёоу, в баню пойдешь сегодня ? 💆🍻🍱', reply_markup=markup)
        elif message.text == '💵 Кубышка':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("50 💶", callback_data='50')
            item2 = types.InlineKeyboardButton("100 💷", callback_data='100')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Сколько сдал сегодня в кубышку ? 💰', reply_markup=markup)

        else:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Пока", callback_data='bye')
            item2 = types.InlineKeyboardButton("Или ещё пообщаемся ?", callback_data='not bye')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Я не знаю что тебе ответить, братишка 😢', reply_markup=markup)
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько, продолжай в том же духе 😊')
            if call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢 ну поиграй с друзьями в "Рандомное число" от 0 до 100')
            if call.data == 'work':
                bot.send_message(call.message.chat.id, 'Красавчик 😊 кто-то должен работать 😉')
            if call.data == 'not work':
                bot.send_message(call.message.chat.id, 'Можно пивко сейчас хуярить 😎')
            if call.data == '50':
                bot.send_message(call.message.chat.id, 'Всё по стандарту 😉')
            if call.data == '100':
                bot.send_message(call.message.chat.id, 'Да ты алигарх 😎')
            if call.data == 'bye':
                bot.send_message(call.message.chat.id, 'До встречи 👋')
                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😉",
                    reply_markup=None)
            if call.data == 'not bye':
                bot.send_message(call.message.chat.id, 'Какая тебя тема интересует ? 😏')
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Красавчик, орешки 🌰 не забудь !)')
            if call.data == 'if':
                bot.send_message(call.message.chat.id, 'Как надумаешь, пиши ✍')
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'Тогда на связи, хорошего дня тебе, братишка !')
                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😉",
                    reply_markup=None)

            # remove inline buttons (удалить встроенные кнопки и сообщение)
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😉",
                # reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                text="Спасибо за ответ !")

    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)