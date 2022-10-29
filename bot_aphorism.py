import telebot
from telebot import types
TOKEN = ('5619198797:AAG_AtruwPRqf2OrkcNFigoh8xqfyybQOF4')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item = types.InlineKeyboardButton('Ад и рай', callback_data='Ад и рай')
    item2 = types.InlineKeyboardButton('Вечность', callback_data='Вечность')
    item3 = types.InlineKeyboardButton('Жизнь', callback_data='Жизнь')
    item4 = types.InlineKeyboardButton('История', callback_data='История')
    item5 = types.InlineKeyboardButton('Любовь', callback_data='Любовь')
    item6 = types.InlineKeyboardButton('Надежда', callback_data='Надежда')
    item7 = types.InlineKeyboardButton('Опыт', callback_data='Опыт')
    item8 = types.InlineKeyboardButton('Память', callback_data='Память')
    item9 = types.InlineKeyboardButton('Смысл жизни', callback_data='Смысл жизни')
    markup.add(item, item2, item3, item4, item5, item6, item7, item8, item9)


    bot.send_message(message.chat.id, 'Привет! Выбери из списка и нажми на кнопку, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'Ад и рай':
            bot.send_message(call.message.chat.id, 'Мало попасть в рай😇, надо еще там устроиться😩. Жаль, что в рай надо ехать на катафалке😅.')
        elif call.data == 'Вечность':
            bot.send_message(call.message.chat.id, 'Вечность тянется очень долго, особенно под конец😄. Ничто так не торопит, как вечность😜.')
        elif call.data == 'Жизнь':
                bot.send_message(call.message.chat.id, 'Жизнь занимает у людей слишком много времени. Если хочешь, чтобы жизнь тебе улыбнулась, сначала сам улыбнись жизни🥳.')
        elif call.data == 'История':
            bot.send_message(call.message.chat.id, 'История учит, используя запрещенные педагогические приемы. Уроки истории заключаются в том, что люди ничего не извлекают из уроков истории🙄.')
        elif call.data == 'Любовь':
            bot.send_message(call.message.chat.id, 'Может любовь и вправду болезнь, но увы не заразная❤. В ревматизм и в настоящую любовь не верят до первого приступа😀.')
        elif call.data == 'Надежда':
            bot.send_message(call.message.chat.id, 'Мы надеемся приблизительно, зато боимся точно😅. Надеяться надо до последней минуты, но в последнюю минуту можно и перестать🙃.')
        elif call.data == 'Опыт':
            bot.send_message(call.message.chat.id, 'Опыт позволяет нам ошибаться гораздо увереннее😎. Опыт научил меня не доверять даже опыту😑.')
        elif call.data == 'Память':
            bot.send_message(call.message.chat.id, 'Вспоминая, он забывался😄. Лучший способ запомнить что-нибудь - постараться это забыть.')
        elif call.data == 'Смысл жизни':
            bot.send_message(call.message.chat.id, 'Есть ли смысл в жизни🤔, смотря когда😀. Жизнь все время отвлекает наше внимание и мы даже не успеваем заметить, от чего именно.')

bot.polling()
