import os
import logging
from aiogram import Bot, Dispatcher, executor, types
import controller

logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def whoami(message):
    """When use that method we will know who made a request(shows in logs)"""
    user_name = str(message.from_user.full_name)
    user_login = str(message.from_user.username)
    user_id = str(message.from_user.id)
    user_info = \
        "User: " + user_name + " login: " + user_login + " id: " + user_id + " Request text: " + str(message.text)
    logging.info(user_info)


@dp.message_handler(commands=['start'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.start()
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_usd'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top('usd')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_eur'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top('eur')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_gbp'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top('gbp')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_pln'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top('pln')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_usd'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all('usd')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_eur'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all('eur')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_gbp'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all('gbp')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_pln'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all('pln')
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
