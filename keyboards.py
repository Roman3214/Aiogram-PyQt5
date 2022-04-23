from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_boundary_conditions_department = InlineKeyboardButton('Отделение пограничных состояний', callback_data='button1')
inline_btn_childrens_department = InlineKeyboardButton('Детское отделение', callback_data='button2')
inline_btn_narcology = InlineKeyboardButton('Отделение наркологии', callback_data='button3')

    
inline_kb_full = InlineKeyboardMarkup( resize_keyboard=True).add(inline_btn_boundary_conditions_department)
inline_kb_full.add(inline_btn_childrens_department, inline_btn_narcology)