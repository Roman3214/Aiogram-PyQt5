import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN 

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)







if __name__ == '__main__':

    from handler import dp,  check_send_message_txt#, send_input_photo#send_to_admin
    #lists_function = [send_input_photo, check_send_message_txt ]
    executor.start_polling(dp, on_startup = check_send_message_txt)
   
  
