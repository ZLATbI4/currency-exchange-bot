import os
import logging
import aioschedule as aioschedule
import asyncio
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


async def scheduler():
    logging.info("Rates will be updated every hour")
    aioschedule.every().hour.do(controller.write_fresh_data, 'usd')
    aioschedule.every().hour.do(controller.write_fresh_data, 'eur')
    aioschedule.every().hour.do(controller.write_fresh_data, 'gbp')
    aioschedule.every().hour.do(controller.write_fresh_data, 'pln')
    while True:
        aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup_tasks(x):
    controller.write_fresh_data('usd')
    controller.write_fresh_data('eur')
    controller.write_fresh_data('gbp')
    controller.write_fresh_data('pln')
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = on_startup_tasks)

