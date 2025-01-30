from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from partners import db_test
from create_bot import bot
from keyboards import admin_test
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ID = None

class FSMTest(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def make_change(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'QQ, moderator TEST', reply_markup=admin_test)
    await message.delete()

async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMTest.photo.set()
        await message.reply('Загрузить фото товара')

async def cancel_handler(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

async def load_photo(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMTest.next()
        await message.reply('Введи название товара')

async def load_name(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
    await FSMTest.next()
    await message.reply('Введи описание к товару')

async def load_description(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
    await FSMTest.next()
    await message.reply('Укажи цену товара')

async def load_price(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
    await db_test.sql_add_command(state)
    await state.finish()


async def del_callback_run(callback_query: types.CallbackQuery):
    await db_test.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

async def delete_item(message : types.Message):
    if message.from_user.id == ID:
        read = await db_test.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup()\
                .add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))




def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_change, commands=['modtest'], is_chat_admin=True)
    dp.register_message_handler(cm_start, commands=['load_test'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands=['отмена'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMTest.photo)
    dp.register_message_handler(load_name, state=FSMTest.name)
    dp.register_message_handler(load_description, state=FSMTest.description)
    dp.register_message_handler(load_price, state=FSMTest.price)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('dele '))
    dp.register_message_handler(delete_item, commands=['delete_test'])