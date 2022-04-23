import asyncio
import aiogram
from numpy import unicode_
from main import bot, dp
from aiogram.types import Message, InputMedia
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions, MediaGroup, InputMediaDocument, InputFile
from config import admin_id
import sqlite3

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove


from keyboards import inline_kb_full
from test_db import users_id_Pogr, users_id_Detsk, users_id_Narkolog, ALL
import os
import time

'''
#for i in len(users_id_db):
async def send_input_file(dp):
  #await bot.send_file(chat_id= users_id_db[const])    
    const = 0
    while const < len(users_id_db):
        chat_id = int(users_id_db[const])
        photo = open("F:\\фотки\\2880x1800_799985_[www.ArtFile.ru].jpg", 'rb')
        caption = "it's just photo, don't worry"
        await bot.send_photo(chat_id, photo, caption)    
        const += 1

async def send_input_photo(dp):
  #await bot.send_file(chat_id= users_id_db[const])    
    #const = 0
    #while const < len(users_id_db):
    chat_id = admin_id
    photo = open("F:\\фотки\\bg-03.jpg", 'rb')
    caption = "it's just photo, don't worry"
    await bot.send_photo(chat_id, photo, caption)    
     #   const += 1'''
'''

'''

@dp.message_handler(commands=['start'])
async def Keyboard_Button(message: Message):
    global button
    button = await bot.send_message(message.chat.id, "Выберите отделение в котором вы работаете.", reply_markup=inline_kb_full)



@dp.message_handler()
async def other_command(message: Message):
    next_id = message.message_id
    print(next_id)
    # хуета полная
    
async def send_object(id):
    try:
        connn = sqlite3.connect('users.db')
        cursors = connn.cursor()
        text = cursors.execute('SELECT text_message FROM datainfo ORDER BY ROWID ASC LIMIT 1')#SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
        text_end = [q for q in text]
        connn.commit()
        photo = cursors.execute('SELECT photo_message FROM datainfo ORDER BY ROWID ASC LIMIT 1')
        photo_end = [q for q in photo]
        connn.commit()
        video = cursors.execute('SELECT video_message FROM datainfo ORDER BY ROWID ASC LIMIT 1')
        video_end = [q for q in video]
        connn.commit()
        docum = cursors.execute('SELECT documentation_message FROM datainfo ORDER BY ROWID ASC LIMIT 1')
        docum_end = [q for q in docum]
        connn.commit()
        checkid = cursors.execute('SELECT * FROM datainfo ')
        checkid_end = [q for q in checkid]
        connn.commit()
        #connn.close()
    except sqlite3.Error as error:
        print('Error', error)
    finally:
        if(connn):
            connn.close()

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        if checkid_end != []:
            for send_object in text_end[0]:
                if send_object != None:
                    await bot.send_message(int(id), str(send_object))
                    sql_update_query = """DELETE FROM datainfo WHERE text_message = ?"""
                    cursor.execute(sql_update_query, (send_object, ))
                    conn.commit()       
                    print("Соединение с SQLite закрыто1")        
                elif text_end[0] == None:
                    break

            for send_object in photo_end[0]:
                if send_object != None:
                    await bot.send_photo(id, open(send_object, 'rb'))
                    sql_update_query = """DELETE FROM datainfo WHERE photo_message = ?"""
                    cursor.execute(sql_update_query, (send_object, ))
                    conn.commit()
                    print("Соединение с SQLite закрыто2")  
                if photo_end[0] == None:
                    break    

            for send_object in video_end[0]:
                if send_object != None:
                    await bot.send_video(id, open(send_object, 'rb'))
                    sql_update_query = """DELETE FROM datainfo WHERE video_message = ?"""
                    cursor.execute(sql_update_query, (send_object, ))
                    conn.commit()
                    print("Соединение с SQLite закрыто3")       
                if video_end[0] == None:
                    break

            for send_object in docum_end[0]:
                if send_object != None:
                    await bot.send_document(id, open(send_object, 'rb'))
                    sql_update_query = """DELETE FROM datainfo WHERE documentation_message = ?"""
                    cursor.execute(sql_update_query, (send_object, ))
                    conn.commit()
                if docum_end[0] == None:
                    break
        else:
            print('Отпрвавка завершена')
                
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")  
      

async def check_send_message_txt(dp):
    #chat_id = admin_id
    #print(id_message())
    #id_message()
    try:
        connn = sqlite3.connect('users.db')
        cursors = connn.cursor()
        request = cursors.execute('SELECT branch_name FROM who_to_send_a_message_to')#SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
        branch_name = [q for q in request]

        #print(e[0][1])
        connn.commit()
        checkid = cursors.execute('SELECT * FROM datainfo ')
        checkid_end = [q for q in checkid]
        connn.commit()
        #connn.close()
    except sqlite3.Error as error:
        print('Error', error)
    finally:
        if(connn):
            connn.close()
    if checkid_end != []:
        while True:
        
            time.sleep(1)
            
            if  branch_name[0][0] == 'Send_All':
                for id in set(ALL):
                    await send_object(id)

            elif  branch_name[0][0] == 'Send_Pogr_Children':
                for id in users_id_Pogr + users_id_Detsk:
                    await send_object(id)

            elif  branch_name[0][0] == 'Send_Pogr_Narko':
                for id in users_id_Pogr + users_id_Narkolog:
                    await send_object(id)     

            elif  branch_name[0][0] == 'Send_Children_Narko':
                for id in users_id_Detsk + users_id_Narkolog:
                    await send_object(id)  

            elif  branch_name[0][0] == 'Send_Pogr':
                for id in users_id_Pogr:
                    await send_object(id)  

            elif  branch_name[0][0] == 'Send_Children':
                for id in users_id_Detsk:
                    await send_object(id)  

            elif  branch_name[0][0] == 'Send_Narko':
                for id in users_id_Narkolog:
                    await send_object(id)  
            break
                #print(media)
                #await bot.send_media_group(id, media)   
'''
                try:
                    connn = sqlite3.connect('users.db')
                    cursors = connn.cursor()
                    text = cursors.execute('SELECT * FROM datainfo ORDER BY ROWID ASC LIMIT 1')#SELECT * FROM SAMPLE_TABLE ORDER BY ROWID ASC LIMIT 1
                    e = [q for q in text]
                    #print(e[0][1])
                    connn.commit()
                    #connn.close()
                except sqlite3.Error as error:
                    print('Error', error)
                finally:
                    if(connn):
                        connn.close()
                try:        
                    count = 0
                    for send_object in e[0]:
                        if send_object != None:
                            
                            try:
                                conn = sqlite3.connect('users.db')
                                cursor = conn.cursor()
                                if count == 0:
                                    print('0')
                                    '''
'''
                                    with open('tee.txt', 'w', encoding= 'utf-8') as read_file:
                                        tex = read_file.write(send_object)
                                    with open('tee.txt', 'r', encoding= 'utf-8') as read_file:
                                        textii = read_file.read()'''
                                        
'''
                                    await asyncio.sleep(3)
                                    await bot.send_message(int(id), str(send_object))
                                    #time.sleep(1)
                                    await asyncio.sleep(3)
                                    sql_update_query = """DELETE FROM datainfo WHERE text_message = ?"""
                                    cursor.execute(sql_update_query, (send_object, ))
                                    conn.commit()
                                elif count == 1:
                                    print('1')
                                    await asyncio.sleep(3)
                                    await bot.send_photo(id, open(send_object, 'rb'))
                                    await asyncio.sleep(3)
                                    sql_update_query = """DELETE FROM datainfo WHERE photo_message = ?"""
                                    cursor.execute(sql_update_query, (send_object, ))
                                    conn.commit()
                                elif count == 2:
                                    print('2')
                                    await asyncio.sleep(3)
                                    await bot.send_video(id, open(send_object, 'rb'))
                                    await asyncio.sleep(3)
                                    sql_update_query = """DELETE FROM datainfo WHERE video_message = ?"""
                                    cursor.execute(sql_update_query, (send_object, ))
                                    conn.commit()
                                elif count == 3:
                                    print('3')
                                    await asyncio.sleep(3)
                                    await bot.send_document(id, open(send_object, 'rb'))
                                    await asyncio.sleep(3)
                                    sql_update_query = """DELETE FROM datainfo WHERE documentation_message = ?"""
                                    cursor.execute(sql_update_query, (send_object, ))
                                    conn.commit()
                                
                                    
                            except sqlite3.Error as error:
                                print("Ошибка при работе с SQLite", error)
                            finally:
                                if conn:
                                    conn.close()
                                    print("Соединение с SQLite закрыто")
                        count +=1
                        if count == 4:
                            count = 0
                except IndexError as error:
                    print('the list is empty ')
                    break'''
                #await bot.send_photo(i, poh)
                #time.sleep(1)
                #os.remove(list_photot()[count1])
                #count1 +=1
'''
            q = 0
            for r in range(5):
                if q < len(list_photot()):
                    with open(list_photot()[q], 'rb') as send:
                        poh = send.read()
                q +=1
            count1 = 0
'''
            #for lp in list_photot():
            #if list_photot() == []:    
            #    os.remove('textALL.txt')


'''
        elif os.path.isfile('textP.txt') == True:
            with open('textP.txt', 'r', encoding= 'utf-8') as read_file:
                tex = read_file.read()
            for i in users_id_Pogr:
                await bot.send_message(chat_id=i, text= tex)
            os.remove('textP.txt')
            
        elif os.path.isfile('textD.txt') == True:
            with open('textD.txt', 'r', encoding= 'utf-8') as read_file:
                tex = read_file.read()
            for i in users_id_Detsk:
                await bot.send_message(chat_id=i, text= tex)
            os.remove('textD.txt')
            
        elif os.path.isfile('textN.txt') == True:
            with open('textN.txt', 'r', encoding= 'utf-8') as read_file:
                tex = read_file.read()
            for i in users_id_Narkolog:
                await bot.send_message(chat_id=i, text= tex)
            os.remove('textN.txt')
        elif e[0][0] == None:
            break
'''
        

        
            
        

async def send_input_photo(dp):
    chat_id = admin_id
    list_format_photo = ['.raw', '.jpeg', '.jpg', '.tiff', '.psd', '.bmp', '.png', '.gif']
    
    dir = os.listdir()
    
    list_path_photo = []
    
    q = 0 
    for i in list_format_photo:
        for photo in dir:
            #photo = str(photo).lower()
            if str(photo).lower().find(i) != -1:
                list_path_photo.append(photo)
                print(list_path_photo)
                with open(list_path_photo[q], 'rb') as send:
                    await bot.send_photo(chat_id, send)
                #print(list_path[q])
                q +=1 
                break
    pass
        #await bot.send_photo(chat_id, e)
                #list_path.append(photo)
                
                #print(photo) 
    
    #photo = open("H:\\фотки\\bg-03.jpg", 'rb')
    #caption = "it's just photo, don't worry"
    #await bot.send_photo(chat_id, list_path)#, caption)


async def send_documents(dp):
    pass  
    #await bot.send_document() 
     

'''
async def send_to_admin(dp):
    const = 0
    while const < len(users_id_db):
        try:
            await bot.send_message(chat_id=int(users_id_db[const]), text='thanks for using my bot :)') #579244655,text="Please off sound") 
        except aiogram.utils.exceptions.BotBlocked:
            print(f'User nuber {const} deleted the bot ')
    #except NameError:
    #    print(f'User nuber {const} deleted the bot ')
        const += 1
        # def send-message need to try: except: Error

'''

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_boundary_conditions_department(callback_query: CallbackQuery):
  
    name = f'{callback_query.from_user.first_name}'
    first_name = f'{callback_query.from_user.last_name}'
    user_id = f'{callback_query.from_user.id}' 
    if first_name == 'None':
        text = f' Добро пожаловать "{name}" ! Новые уведомления будут отправлены в ближайшее время!)'
    else: 
        text = f' Добро пожаловать "{name} {first_name}" ! Новые уведомления будут отправлены в ближайшее время!)'
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
       #cursor.execute("SELECT `user_id` FROM `users_telegram` WHERE `user_id` = ?", (f'{int(user_id)}',))
        
        cursor.execute('INSERT OR IGNORE INTO "Pogr_sost_telegram" ("user_id", "user_name" , "user_surname") VALUES (?,?,?)', (f'{int(user_id)}',f'{str(name)}', f'{str(first_name)}', ))
        
        conn.commit()
      
    except sqlite3.Error as error:
        print('Error', error)
 
    finally:
        if(conn):
           conn.close()
    
    await bot.send_message(callback_query.from_user.id, text)
    await button.delete()

    
@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_childrens_department(callback_query: CallbackQuery):
  
    name = f'{callback_query.from_user.first_name}'
    first_name = f'{callback_query.from_user.last_name}'
    user_id = f'{callback_query.from_user.id}' 
    if first_name == 'None':
        text = f' Добро пожаловать "{name}" ! Новые уведомления будут отправлены в ближайшее время!)'
    else: 
        text = f' Добро пожаловать "{name} {first_name}" ! Новые уведомления будут отправлены в ближайшее время!)'
    

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
       #cursor.execute("SELECT `user_id` FROM `users_telegram` WHERE `user_id` = ?", (f'{int(user_id)}',))
        
        cursor.execute('INSERT OR IGNORE INTO "childrens_department" ("user_id", "user_name" , "user_surname") VALUES (?,?,?)', (f'{int(user_id)}',f'{str(name)}', f'{str(first_name)}', ))
        
        conn.commit()
      
    except sqlite3.Error as error:
        print('Error', error)
 
    finally:
        if(conn):
           conn.close()
    
    await bot.send_message(callback_query.from_user.id, text)
    await button.delete()

@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_narcology(callback_query: CallbackQuery):
    delete = callback_query.id
    print(delete)
    name = f'{callback_query.from_user.first_name}'
    first_name = f'{callback_query.from_user.last_name}'
    user_id = f'{callback_query.from_user.id}' 
    if first_name == 'None':
        text = f' Добро пожаловать "{name}" ! Новые уведомления будут отправлены в ближайшее время!)'
    else: 
        text = f' Добро пожаловать "{name} {first_name}" ! Новые уведомления будут отправлены в ближайшее время!)'
    

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
       #cursor.execute("SELECT `user_id` FROM `users_telegram` WHERE `user_id` = ?", (f'{int(user_id)}',))
        
        cursor.execute('INSERT OR IGNORE INTO "narcology" ("user_id", "user_name" , "user_surname") VALUES (?,?,?)', (f'{int(user_id)}',f'{str(name)}', f'{str(first_name)}', ))
        
        conn.commit()
      
    except sqlite3.Error as error:
        print('Error', error)
 
    finally:
        if(conn):
           conn.close()
    
    await bot.send_message(callback_query.from_user.id, text)
    await button.delete()
"""
@dp.message_handler(lambda c:True, content_types=['text'])#этот блок выполнится если юзер отправит боту сообщение
def info_message(message: Message):
    bot.edit_message_reply_markup(message.chat.id, message_id = message.message_id-1, reply_markup = '')# удаляем кнопки у последнего сообщения

"""
@dp.message_handler(commands=['help'])
async def send_help(message: Message):
    await message.reply("Чем я могу помочь?")

'''
@dp.message_handler()
async def echo (message: Message):
    text = f' "{message.from_user.first_name}" Привет ты написал мне: {message.text}, this is you username :"{message.from_user.username}"'
    print(message, text)
    #await bot.send_message(chat_id=message.from_user.id, text=text)
    await message.answer(text=text)
'''
'''   
 {"message_id": 665, "from":
    {"id": 584914872, 
        "is_bot": false,
        "first_name": "чех", 
        "username": "cheh102", 
        "language_code": "ru"}, 
    "chat": {"id": 584914872, 
        "first_name": "чех", 
        "username": "cheh102", 
        "type": "private"}, 
    "date": 1644235891, 
    "text": "Привет"} 
     "чех" Привет ты написал мне: Привет
'''