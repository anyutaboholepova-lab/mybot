from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "8613130786:AAHI__R0zfx4dI1kAOKnyU8sHCX3GQ31VjU"
OWNER_ID = 694009198

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "Привiт, подiлись зi мною частинкою свого життя🥹"
    )

    await bot.send_message(
        OWNER_ID,
        f"Новый пользователь: @{message.from_user.username or 'no_username'}"
    )


@dp.message()
async def all_messages(message: Message):

    await message.answer(
        "Я отримав твою iсторiю👀"
    )

    text = f"""
Новое сообщение

От: @{message.from_user.username or 'no_username'}
ID: {message.from_user.id}

Текст:
{message.text}
"""

    await bot.send_message(OWNER_ID, text)


async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())