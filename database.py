import sqlite3
from parser import get_list_of_sushi_info

connection = sqlite3.connect('app.db')
cursor = connection.cursor()


def create_table(name, columns):
    cursor.execute(f'CREATE TABLE {name} ({columns})')
    connection.commit()


def create_user_with_name_and_tg_id(name, tg_id):
    cursor.execute(f'INSERT INTO users (name, id) VALUES("{name}", "{tg_id}")')
    connection.commit()


def add_user_phone(phone, tg_id):
    cursor.execute(f'UPDATE users SET phone={phone} WHERE id={tg_id}')
    connection.commit()


def add_parsed_data_to_database(sushi_data: list, table_name):
    cursor.executemany(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?)', sushi_data)
    connection.commit()


# should be commented, otherwise duplicate tables will be created
# create_table('sets', 'name VARCHAR(256), weight CHAR(10), price CHAR(10), image VARCHAR(120)')
# create_table('sushi', 'name VARCHAR(256), weight CHAR(10), price CHAR(10), image VARCHAR(120)')
# create_table('rolls', 'name VARCHAR(256), weight CHAR(10), price CHAR(10), image VARCHAR(120)')

# parse data from site
# sushi = get_list_of_sushi_info('https://ninjasushi.com.ua/category/sushi/')
# rolls = get_list_of_sushi_info('https://ninjasushi.com.ua/category/rolls/')
# sets = get_list_of_sushi_info('https://ninjasushi.com.ua/category/sets/')

# add data from site to tables in database
# add_parsed_data_to_database(sushi, 'sushi')
# add_parsed_data_to_database(rolls, 'rolls')
# add_parsed_data_to_database(sets, 'sets')


# just checks if table exists
# print(cursor.execute('SELECT * FROM sushi').fetchall())
# print(cursor.execute('SELECT * FROM rolls').fetchall())



