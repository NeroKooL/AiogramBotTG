from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_b12_m, kb_main
from partners import db_test


async def partner_test(message : types.message):
        await bot.send_message(message.from_user.id, 'Здесь может быть твой магазин. Заполнение по принципу:\n 1.Описание к магазу\n 2.Ссылка на чат\магаз\сайт.\nЕсть возможность добавлять список товара в "меню" с возможностью его редактирования (по желанию).', reply_markup=kb_b12_m)
        await message.delete()

async def menu_nerokool(message : types.Message):
     await db_test.sql_read(message)
     await bot.send_message(message.from_user.id, 'Конец списка товаров.', reply_markup=kb_main)
     await message.delete()


def register_handlers_test(dp : Dispatcher):
    dp.register_message_handler(partner_test, commands=['магазин_test'])
    dp.register_message_handler(menu_nerokool, commands=['меню_test'])