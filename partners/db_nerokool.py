import sqlite3 as sq
from create_bot import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#инлайн кнопка на продавца
inline = InlineKeyboardMarkup(row_width=1)
inlineb1 = InlineKeyboardButton(text='Написать продавцу', url='https://t.me/nerokool')
inline.add(inlineb1)

def sql_start():
    global base, cur
    base = sq.connect('./data/nerokool.db')
    cur = base.cursor()
    if base:
        print('DATA BASE nerokool connected!')
    base.execute('CREATE TABLE IF NOT EXISTS nerokool(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO nerokool VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM nerokool').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]} BYN', reply_markup=inline)


async def sql_read2():
    return cur.execute('SELECT * FROM nerokool').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM nerokool WHERE name == ?', (data,))
    base.commit()