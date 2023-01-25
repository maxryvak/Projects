from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Work_schedule')
b2 = KeyboardButton('/Address')
b3 = KeyboardButton('/Menu')
# b4 = KeyboardButton('/Give phone number', request_contact=(True))
# b5 = KeyboardButton('/Where I am?', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)  #.row(b4, b5)