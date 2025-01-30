from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/main')

#кнопки админа для магаза nerokool
load_nerokool = KeyboardButton('/load_nerokool')
del_nerokool = KeyboardButton('/delete_nerokool')

admin_nerokool = ReplyKeyboardMarkup(resize_keyboard=True)
admin_nerokool.row(load_nerokool, del_nerokool).add(b1)


load_test = KeyboardButton('/load_test')
del_test = KeyboardButton('/delete_test')

admin_test = ReplyKeyboardMarkup(resize_keyboard=True)
admin_test.row(load_test, del_test).add(b1)