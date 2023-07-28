# async work
import asyncio
# logging for debug
import logging

#
from aiogram import Bot, Dispatcher
# message markup settings, HTML and markdown
from aiogram.enums.parse_mode import ParseMode
# data stores for user states
from aiogram.fsm.storage.memory import MemoryStorage

# bot settings
import config
# funcs of bot
from handlers import router


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # data witch no in bd will remove with reload
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    # remove all updates, bot will work with only new messages
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())