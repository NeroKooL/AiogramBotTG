from aiogram.utils import executor
from create_bot import dp
from partners import db_nerokool, db_test


async def on_startup(_):
    print('Bot Online')
    db_nerokool.sql_start()
    db_test.sql_start()

from handlers import client
client.register_handlers_client(dp)


from partners import client_nerokool, client_test
client_nerokool.register_handlers_nerokool(dp)
client_test.register_handlers_test(dp)

from partners import admin_nerokool, admin_test
admin_nerokool.register_handlers_admin(dp)
admin_test.register_handlers_admin(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)