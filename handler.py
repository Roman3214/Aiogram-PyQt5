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

@dp.message_handler(commands=['start'])
async def Keyboard_Button(message: Message):
    global button
    button = await bot.send_message(message.chat.id, "Выберите отделение в котором вы работаете.", reply_markup=inline_kb_full)



@dp.message_handler()
async def other_command(message: Message):
    next_id = message.message_id
    print(next_id)
  
    
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
                elif text_end[0] == None:
                    break

            for send_object in photo_end[0]:
                if send_object != None:
                    await bot.send_photo(id, open(send_object, 'rb'))
                    sql_update_query = """DELETE FROM datainfo WHERE photo_message = ?"""
                    cursor.execute(sql_update_query, (send_object, ))
                    conn.commit
                if photo_end[0] == None:
                    break    

            for send_object in video_end[0]:
                if send_object != None:
                    await bot.send_video(id, open(send_object, 'rb'))
                    sql_update_query = """DELETE FROM datainfo WHERE video_message = ?"""
                    cursor.execute(sql_update_query, (send_object, ))
                    conn.commit()    
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
@dp.message_handler(commands=['help'])
async def send_help(message: Message):
    await message.reply("Чем я могу помочь?")
