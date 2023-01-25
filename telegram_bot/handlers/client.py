from aiogram  import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome to Dominos Pizza!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Speaking with Bot here:\nhttps://t.me/Dominos_PizzaSUPERBOT")

#@dp.message_handler(commands=['Work_schedule'])
async def pizza_schedule_command(message: types.Message):
    await bot.send_message(message.from_user.id, '24/7')

#@dp.message_handler(commands=['Address'])
async def pizza_adress_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Shevchenko Avenue, 100')
    
@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message) 
    

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_schedule_command, commands=['Work_schedule'])
    dp.register_message_handler(pizza_adress_command, commands=['Address'])
    dp.register_message_handler(pizza_menu_command, commands=['Menu'])