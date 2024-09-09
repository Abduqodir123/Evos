import psycopg2

db_name = 'GadgetLand'
user = 'postgres'
host = 'localhost'
port = 5432
password = '1234'

connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
cursor = connect.cursor()


def check_user(telegram_id):
    db_name = 'GadgetLand'
    user = 'postgres'
    host = 'localhost'                                                                                                                                                                                                                                                                                     
    port = 5432
    password = '1234'

    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(f"SELECT  telegram_id FROM users WHERE telegram_id = {telegram_id};")

    user = cursor.fetchone()

    if user:
        return True
    else:
        return False
    


def  register_user(usersname, phone_number, telegram_id):
    db_name = 'GadgetLand'
    user = 'postgres'
    host = 'localhost'                                                                                                                                                                                                                                                                                     
    port = 5432
    password = '1234'

    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(f" INSERT INTO users (user_name, phone_number, telegram_id)VALUES ('{usersname}', '{phone_number}', {telegram_id});")

    connect.commit()
    connect.close()

def add_feedback(telegram_id, user_feedback):
    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(" INSERT INTO feedback (telegram_id, user_feedback) VALUES (%s, %s);", (telegram_id, user_feedback))

    connect.commit()
    connect.close()


def delete_feedback(telegram_id ):
    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(" DELETE FROM feedback WHERE telegram_id = %s;", (telegram_id,))


def eng_yuqori_baho_film(film_baholar):
    if not film_baholar:
        return None
    return max(film_baholar, key=lambda x: x['baho'])

def eng_yuqori_naqd_pul_beruvchi(mijozlar):
    if not mijozlar:
        return None
    return max(mijozlar, key=lambda x: x['naqd_pul'])


film_baholar = [{'nomi': 'Film1', 'baho': 8.5}, {'nomi': 'Film2', 'baho': 9.0}, {'nomi': 'Film3', 'baho': 7.8}]
eng_yuqori_baho_film_nomi = eng_yuqori_baho_film(film_baholar)['nomi']
print("Eng yuqori baho beruvchi film:", eng_yuqori_baho_film_nomi)

mijozlar = [{'ismi': 'Isfandiyor', 'naqd_pul': 500}, {'ismi': 'Zafar', 'naqd_pul': 800}, {'ismi': 'Abduqodir', 'naqd_pul': 600}]
eng_yuqori_naqd_pul_beruvchi_ismi = eng_yuqori_naqd_pul_beruvchi(mijozlar)['ismi']
print("Eng yuqori naqd pul beruvchi mijoz:", eng_yuqori_naqd_pul_beruvchi_ismi)


def select_user_orders(telegram_id ):
    connect = psycopg2.connect(database=db_name, user=user, host=host, password=password, port=port)
    cursor = connect.cursor()

    cursor.execute(" DELETE FROM feedback WHERE telegram_id = %s;", (telegram_id,))

    data = cursor.fetchall()

    return data


class Database:
    def __init__(self):
        self.mijozlar = {}

    def buyurtma_qoshish(self, mijoz_id, buyurtma):
        if mijoz_id in self.mijozlar:
            self.mijozlar[mijoz_id].append(buyurtma)
        else:
            self.mijozlar[mijoz_id] = [buyurtma]

    def buyurtma_ochirish(self, mijoz_id, buyurtma):
        if mijoz_id in self.mijozlar and buyurtma in self.mijozlar[mijoz_id]:
            self.mijozlar[mijoz_id].remove(buyurtma)
            if not self.mijozlar[mijoz_id]:  
                del self.mijozlar[mijoz_id]  

    def mijoz_buyurtmalari(self, mijoz_id):
        return self.mijozlar.get(mijoz_id, [])

    def mijozlar_royxati(self):
        return list(self.mijozlar.keys())

    def mijozlar_soni(self):
        return len(self.mijozlar)
    
def add_product(product_name, product_desc, product_photo, product_price):
    connect = psycopg2.connect(database=db_name, user=user, port=port, host=host, password=password)
    cursor = connect.cursor()


    cursor.execute("INSERT INTO Product (product_name, description, photo, product_price) VALUES (%s, %s, %s, %s);",
                        (product_name, product_desc, product_photo, product_price))
        





    connect.commit()
    connect.close()

def delete_product_by_name(product_name):
    connect = psycopg2.connect(database=db_name, user=user, port=port, host=host, password=password)
    cursor = connect.cursor()

    cursor.execute("DELETE FROM products WHERE product_name=%s;", (product_name,))

    connect.commit()
    connect.close()


