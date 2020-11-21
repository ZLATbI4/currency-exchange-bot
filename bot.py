import os
import logging
from aiogram import Bot, Dispatcher, executor, types
import controller

logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['top'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    user_name = str(message.from_user.full_name)
    user_login = str(message.from_user.username)
    user_id = str(message.from_user.id)
    user_info = "User: " + user_name + " login: " + user_login + " id: " + user_id \
                + " Request text: " + str(message.text)
    logger = logging.info(user_info)
    resp = controller.last_report_top()
    logger = logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    user_name = str(message.from_user.full_name)
    user_login = str(message.from_user.username)
    user_id = str(message.from_user.id)
    user_info = "User: " + user_name + " login: " + user_login + " id: " + user_id \
                + " Request text: " + str(message.text)
    logger = logging.info(user_info)
    resp = controller.last_report_all()
    logger = logging.info(resp)
    await bot.send_message(message.chat.id, resp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
