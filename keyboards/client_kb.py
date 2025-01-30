from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#Для навигации
b1 = KeyboardButton('/Главная')
b2 = KeyboardButton('/Разработчик')
b3 = KeyboardButton('/Информация')
b4 = KeyboardButton('/Партнеры')


#для партнеров
b11 = KeyboardButton('/NeroKooL_VAPES')
b12 = KeyboardButton('/Магазин_test')


#для меню партнеров
b11_m = KeyboardButton('/Меню_nerokool')
b12_m = KeyboardButton('/Меню_test')

#начальная навигация
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).row(b2, b3).add(b4)

#Главная
kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_main.add(b1)

#Добавлять партнеров кнопки
kb_partners = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_partners.add(b11).add(b12).add(b1)

#меню кнопки
kb_b11_m = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_b11_m.add(b11_m).add(b1)
kb_b12_m = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_b12_m.add(b12_m).add(b1)