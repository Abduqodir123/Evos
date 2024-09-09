import telebot
import buttons

import database

bot = telebot.TeleBot("6873868784:AAFfI4Pn-FSKUOhF3823B_tT3shkkOpbURU")

@bot.message_handler(commands=['start'])
def start_message(message):
    user = database.check_user(message.from_user.id)

    if user:
        bot.send_message(message.from_user.id, 'Hush Kelibsiz!', reply_markup=buttons.main_menu_buttons())

    else:
        bot.send_message(message.from_user.id, 'Send phone number by button',reply_markup=buttons.share_contact_button())
        bot.register_next_step_handler(message, get_contact)




@bot.message_handler(commands=['admin'])
def admin_menu(message):

    if message.from_user.id == 777322005:

        bot.send_message(message.from_user.id, 'Вы вошли в админ панель', reply_markup=buttons.admin_menu_buttons())
        bot.register_next_step_handler(message, get_action_from_admin)        

def get_contact(message):
    if message.contact:
        phone_number = message.contact.phone_number
        first_name = message.contact.first_name

        database.register_user(first_name, phone_number, message.from_user.id)

        bot.send_message(message.from_user.id, 'You registered successefuly', reply_markup=buttons.main_menu_buttons())

    else:
        bot.send_message(message.from_user.id, 'Send phone number by button',reply_markup=buttons.share_contact_button())
        bot.register_next_step_handler(message, get_contact)


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Fikiringizni qoldiring':
        bot.send_message(message.from_user.id, 'Fikiringizni kutamiz...', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, get_feedback)
    
    elif message.text == 'Mening buyurtmalarim':
        bot.send_message(message.from_user.id, 'Bir soniya kuting...')

        data = database.select_user_orders(message.from_user.id)

        text = ''

        for i in data:
            text = f'Sizning buyurtmangiz:\n\nTelefon raqamingiz: {i[2]}\nTovar: {i[3]}\nManzil {i[4]}\nUmumiy summa: {i[5]}\n\n'

        bot.send_message(message.from_user.id, text)

    else:
        bot.send_message(message.from_user.id, 'Sizda hozircha zakaz yoq')

def get_feedback(message):
    if message.text == 'Back':
        bot.send_message(message.from_user.id, 'You back to menu', reply_markup=buttons.main_menu_buttons())

    elif message.text == 'delete feedback':
        database.delete_feedback(message.from_uer.id)
        bot.send_message(message.from_user.oid, 'feedback deleted', reply_markup=buttons.main_menu_buttons())

    else:
        telegram_id = message.from_user.id
        user_feetback = message.text
        

    database.add_feetback(telegram_id, user_feetback)

    bot.send_message(telegram_id, 'Fikiringiz uchun rahmat!', reply_markup=buttons.main_menu_buttons())
    bot.send_message(5685977359, 'Yangi commentariya:\n' +message.text)





# def main():
#     db = Database()

#     while True:
#         print("\nBuyurtma qo'shish (q), buyurtma o'chirish (o), mijozlar ro'yxati (r), mijoz buyurtmalari (b), yoki chiqish (exit)")
#         amal = input("Tanlang: ")

#         if amal == 'q':
#             mijoz_id = input("Mijoz ID ni kiriting: ")
#             buyurtma = input("Buyurtmani kiriting: ")
#             db.buyurtma_qoshish(mijoz_id, buyurtma)
#             print("Buyurtma qo'shildi!")

#         elif amal == 'o':
#             mijoz_id = input("Mijoz ID ni kiriting: ")
#             buyurtma = input("O'chiriladigan buyurtmani kiriting: ")
#             db.buyurtma_ochirish(mijoz_id, buyurtma)
#             print("Buyurtma o'chirildi!")

#         elif amal == 'r':
#             print("Mijozlar ro'yxati:")
#             print(db.mijozlar_royxati())

#         elif amal == 'b':
#             mijoz_id = input("Mijoz ID ni kiriting: ")
#             buyurtmalar = db.mijoz_buyurtmalari(mijoz_id)
#             if buyurtmalar:
#                 print(f"{mijoz_id} mijozning buyurtmalari:")
#                 for buyurtma in buyurtmalar:
#                     print("- " + buyurtma)
#             else:
#                 print(f"{mijoz_id} mijoz hali buyurtma qilmagan")

#         elif amal == 'exit':
#             print("Dastur tugadi.")
#             break

#         else:
#             print("Noto'g'ri amal, qaytadan urinib ko'ring.")

# if __name__ == "__main__":
#     main()

def get_action_from_admin(message, get_product_to_delete):
    if message.text == 'Добавить товар':
        bot.send_message(message.from_user.id, 'Отправьте название продукта...')
        bot.register_next_step_handler(message, get_product_name)

    elif message.text == 'Tovarni ochirish':
        bot.send_message(message.from_user.id, 'Tovarni ochirish uchun nomini jonating!..')
        bot.register_next_step_handler(message.from_user.id, get_product_to_delete)



def get_product_name(message):
    product_name = message.text

    bot.send_message(message.from_user.id, f'Отправьте описание товара: {product_name}')
    bot.register_next_step_handler(message, get_product_desc, product_name)


def get_product_desc(message, product_to_delete, product_name):
    product_desc = message.text

    database.database_product(product_to_delete)

    bot.send_message(message.from_user.id, 'Siz tovarni ochirdingiz', reply_markup=buttons.admin_menu_buttons())

    bot.send_message(message.from_user.id, f'Отправьте фотографию {product_name}')
    bot.register_next_step_handler(message, get_product_photo, product_name, product_desc)


def get_product_photo(message, product_name, product_desc):
    if message.photo:
        product_photo = message.photo[-1].file_id

        bot.send_message(message.from_user.id, f'Отправьте цену {product_name}')
        bot.register_next_step_handler(message, get_product_price, product_name, product_desc, product_photo)

    else:
        bot.send_message(message.from_user.id, 'Rasm jonating...')
        bot.register_next_step_handler(message, get_product_photo, product_name, product_desc)


def get_product_price(message, product_name, product_desc, product_photo):
    product_price = float(message.text)



    database.add_product(product_name, product_desc, product_photo, product_price)
    bot.send_message(message.from_user.id, 'Siz tovarni qoshdingiz', reply_markup=buttons.admin_menu_buttons())
    bot.register_next_step_handler(message, get_action_from_admin)


def add_product(message, product_name):
    bot.send_message(message.from_user.id, 'Tovar nomi: Airpods max', reply_markup=buttons.admin_menu_buttons())
    bot.register_next_step_handler(message, )


import sqlite3

def delete_product_by_name(product_name):
    try:
        
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        
        
        cursor.execute("DELETE FROM products WHERE name = ?", (product_name,))
        
        
        conn.commit()
        
        
        if cursor.rowcount == 0:
            print("Bunday ismli produkt topilmadi.")
        else:
            print(f"Produkt '{product_name}' omadli ochirildi.")
    
    except sqlite3.Error as e:
        print(f"Malumotlar bazasi ish boyicha xato chiqdi: {e}")
    
    finally:
        
        if conn:
            conn.close()

delete_product_by_name('product_name_example')


def delete_product_by_name(message, product_name):
    delete_product_by_name = message.text

    database.database_product(delete_product_by_name)
    bot.send_message(message.from_user.id, 'Siz productni ochirdingiz')


     


bot.polling()





