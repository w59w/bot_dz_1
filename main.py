import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
from pathlib import Path
import random


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Hi, dear {message.from_user.first_name}!"
                         f"\nThis is what i can do:"
                         f"\n/start"
                         f"\n/MyInfo"
                         f"\n/random")


@dp.message(Command("MyInfo"))
async def my_nfo_handler(message: types.Message):
    await message.answer(f"Your id is {message.from_user.id}"
                         f"\nYour name is {message.from_user.first_name}"
                         f"\nYour username is {message.from_user.username}")


@dp.message(Command("random"))
async def picture_pic_handler(message: types.Message):
    file_name = random.choice(list((Path(__file__).parent / "Images").iterdir()))
    file_path = Path(__file__).parent / "Images" / file_name
    logging.info(file_path)
    file = types.FSInputFile(file_path)
    await message.answer_photo(file)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
