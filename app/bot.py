import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import controller
import db

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

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
    resp = controller.last_report_top(db.USD)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_eur'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top(db.EURO)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_gbp'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top(db.GBP)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['top_pln'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_top(db.PLN)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_usd'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all(db.USD)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_eur'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all(db.EURO)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_gbp'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all(db.GBP)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


@dp.message_handler(commands=['all_pln'])
async def report_message(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')
    whoami(message)
    resp = controller.last_report_all(db.PLN)
    logging.info(resp)
    await bot.send_message(message.chat.id, resp)


async def scheduler():
    logging.info("Rates will be updated every hour")
    while True:
        controller.write_fresh_data()
        await asyncio.sleep(360)


async def on_startup_tasks(x):
    logging.info("Perform startup tasks")
    asyncio.create_task(scheduler())
    logging.info("Startup tasks performed")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = on_startup_tasks)

