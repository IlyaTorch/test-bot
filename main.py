from aiogram import Dispatcher, types, Bot, executor
from tortoise import run_async
import logging

from gemini import GeminiAPIClient
from middleware import DbCheckMiddleware
# from schemas import initialize, Response
from constants import BOT_TOKEN
from utils import get_proxy

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(DbCheckMiddleware())


async def send_question(text, params):
    proxy = await get_proxy()
    client = GeminiAPIClient(token=params['token'], model="gemini-pro", proxy=proxy)
    response = await client.send_request(text=text)
    return response


@dp.message_handler(content_types=['text'])
async def prepare_question(message: types.Message, params: str):

    response_data = await send_question(text=message.text, params=params)

    # await Response.create(
    #     user=params['user'],
    #     response_data=response_data,
    #     gemini_token=params['token'],
    # )
    return response_data


if __name__ == '__main__':
    # run_async(initialize())
    executor.start_polling(dp)



