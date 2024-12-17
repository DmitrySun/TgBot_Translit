import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

loggs = './logs'
os.makedirs(loggs, exist_ok=True)
logging.basicConfig(filename=os.path.join(loggs, "bot_log.log"), level=logging.INFO)

translit_dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
    'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}

def translit(text):
    return ''.join(translit_dict.get(el, el) for el in text)

@dp.message(Command(commands=['start']))
async def start(message: Message):
    logging.info(f'{message.from_user.full_name}: {message.from_user.id} запустил бота')
    await message.answer(f'Привет, {message.from_user.full_name}! Я принимаю ФИО на кириллице и возвращаю на латинице!')

@dp.message()
async def any_message(message: Message):
    try:
        initial_text = message.text
        translit_text = translit(initial_text)
        logging.info(f"User {message.from_user.id}: {initial_text} --> {translit_text}")
        await message.answer(translit_text)
    except:
        logging.error(f"Error! User {message.from_user.id} used illegal characters")
        await message.answer("Недопустимые знаки!!!")

if __name__ == '__main__':
    dp.run_polling(bot)