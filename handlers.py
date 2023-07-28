from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("kk")


@router.message()
async def message_handler(msg: Message):
    # analog of "await bot.send_message(msg.chat.id, "text")
    await msg.answer(msg.from_user.full_name)


