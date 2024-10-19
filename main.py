

import asyncio
from cian import CianFinder
from telegram import TelegramSender


async def main():
    telegram_sender = TelegramSender()
    cian_finder = CianFinder()
    

    while True:
        notifications = cian_finder.find()

        if notifications:
            message = '\n'.join(notifications)
            await telegram_sender.send_messages(message)
            print('Send message')
        else:
            print('Nothing found')

        await asyncio.sleep(60)



if __name__=='__main__':
    asyncio.run(main())