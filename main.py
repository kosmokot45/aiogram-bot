import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

async def main():
    ...

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())