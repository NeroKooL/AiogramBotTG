from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client, kb_main, kb_partners

async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, f'Добрый день, {message.from_user.first_name} {message.from_user.last_name}.☺️\nОсновные команды и информация: /info\nВся навигация по кнопкам, которые появляются снизу!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Чтобы бот смог ответить в ЛС, зайди к боту @MyTastyVape_bot и нажми Start!')
    

async def command_dev(message : types.message):
    await bot.send_message(message.from_user.id, 'Разработчик бота: @NeroKooL.\nЧтобы узнать что-то - писать в ЛС.', reply_markup=kb_main)
    await message.delete()


async def command_info(message : types.message):
    await bot.send_message(message.from_user.id, 'Доступные команды бота:\n/dev - разработчик бота.\n/main - переход к начальной странице.\n/info - основная информация.\
\nКанал создан для простого поиска вейпов/залив из подключенных магазинов к боту.', reply_markup=kb_main)
    await message.delete()


async def command_partner(message : types.message):
    await bot.send_message(message.from_user.id, 'Наши партнеры', reply_markup=kb_partners)
    await message.delete()



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'главная', 'main'])
    dp.register_message_handler(command_dev, commands=['разработчик', 'dev'])
    dp.register_message_handler(command_info, commands=['информация', 'info'])
    dp.register_message_handler(command_partner, commands=['партнеры', 'partners'])