import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN 
#from handler import main+


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)







if __name__ == '__main__':

    from handler import dp,  check_send_message_txt#, send_input_photo#send_to_admin
    #lists_function = [send_input_photo, check_send_message_txt ]
    executor.start_polling(dp, on_startup = check_send_message_txt)
   
    '''for i in range(1):
        my_thread = Thread(target=main(), args=(i,))
        my_thread_two = Thread(target=start_tegram(), args=(i,))
        my_thread.start() and         my_thread_two.start()
       '''
      
      
    #main()
    #from handler import dp#, main#, send_to_admin#,  send_input_file #send_to_admin
    #executor.start_polling(dp, on_startup=)
    #main()
    #for i in range(1):
    #    my_thread = Thread(target=main(), args=(i,))
        #my_thread.start()
    #    executor.start_polling(dp)
    #    
    #main()
      #, on_startup=send_to_admin)#, on_startup=send_input_file)#send_to_admin, send_input_text)
    
    