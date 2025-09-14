import asyncio
from aiogram import Bot, Dispatcher, Router, types


class TelegramSender():
    token = '8119601846:AAFeBAASe9atzTj8FzVbuLq4i-MjpRPlGN0'
    chat_ids = [5335355986]
    # chat_ids = [6019859597]

    def __init__(self):
        self.bot = Bot(token=self.token)

    async def send_messages(self, message: str):
        for chat_id in self.chat_ids:
            await self.bot.send_message(
                chat_id=chat_id,
                text=message,
            )