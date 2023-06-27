import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()


def create_table():
    cursor.execute('CREATE TABLE users (id INTEGER, name VARCHAR(120), phone CHARACTER(20))')


def create_user_with_name_and_tg_id(name, tg_id):
    cursor.execute(f'INSERT INTO users (name, id) VALUES("{name}", "{tg_id}")')
    connection.commit()


def add_user_phone(phone, tg_id):
    cursor.execute(f'UPDATE users SET phone={phone} WHERE id={tg_id}')
    connection.commit()
