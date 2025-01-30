from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_b11_m, kb_main
from partners import db_nerokool


async def partner_nerokool(message):
        await bot.send_message(message.from_user.id, f' Магазин: NeroKooL VAPES\nОписание: большой выбор вейпов и залив.\nСсылка на чат: https://t.me/nerokoolchat', reply_markup=kb_b11_m)
        await message.delete()


async def menu_nerokool(message : types.Message):
     await db_nerokool.sql_read(message)
     await bot.send_message(message.from_user.id, 'Конец списка товаров.', reply_markup=kb_main)
     await message.delete()


def register_handlers_nerokool(dp : Dispatcher):
    dp.register_message_handler(partner_nerokool, commands=['NeroKooL_VAPES'])
    dp.register_message_handler(menu_nerokool, commands=['меню_nerokool'])