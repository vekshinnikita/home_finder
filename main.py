

import asyncio
from avito import AvitoFinder
from cian import CianFinder
from telegram import TelegramSender


async def main():
    telegram_sender = TelegramSender()
    cian_finder = CianFinder()
    avito_finder = AvitoFinder()
    

    while True:
        notifications = []

        notifications.extend(cian_finder.find())
        notifications.extend(avito_finder.find())

        if notifications:
            message = '\n'.join(notifications)
            await telegram_sender.send_messages(message)
            print('Send message')
        else:
            print('Nothing found')

        await asyncio.sleep(60)



if __name__=='__main__':
    asyncio.run(main())