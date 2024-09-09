from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_buttons():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button1 =  KeyboardButton('Category')
    button2 = KeyboardButton('Basket')
    button3 = KeyboardButton('Contact')
    button4 = KeyboardButton('Setting')
    button5 = KeyboardButton('Feedback')
    keyboard.add(button1, button2, button3, button4,button5)
    return keyboard


def share_contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = KeyboardButton('Share contact', request_contact=True)
    kb.add(button1)




    return kb

def back_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    btn = KeyboardButton('Orqaga')
    kb.add(btn)
    return kb

def feedback_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    btn = KeyboardButton('Back')
    btn2 = KeyboardButton('delete feedback')

    kb.add(btn, btn2)
    return kb


def admin_menu_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    btn = KeyboardButton('Добавить товар')
    btn2 = KeyboardButton('Удалить товар')

    kb.add(btn, btn2)

    return kb



def count_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    for i in range(1, 11):
        kb.add(KeyboardButton(str(i)))

    return kb

def basket_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    btn = KeyboardButton('Korzinaga qoshish')
    btn2 = KeyboardButton('Orqaga')


    btn3 = KeyboardButton('1')
    btn4 = KeyboardButton('2')
    btn5 = KeyboardButton('3')
    btn6 = KeyboardButton('4')
    btn7 = KeyboardButton('5')
    btn8 = KeyboardButton('6')
    btn9 = KeyboardButton('7')
    btn10 = KeyboardButton('8')
    btn11 = KeyboardButton('9')
    btn12 = KeyboardButton('10')     
    kb.add(btn, btn2)

    return kb





