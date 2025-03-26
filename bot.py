from aiogram import Bot, Dispatcher, types, Router, filters, F
import asyncio
import tg_echo_eroshina.config as config
# Токен вашего бота
API_TOKEN = "7704827569:AAEw684JLtkcY_e1-CMKwuLEywYGp_4mhJQ"

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
start_router = Router()

# Обработчик команды /start
@start_router.message(filters.CommandStart())
@start_router.message(filters.CommandHelp())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я echo bot. Напиши мне что-нибудь, и я повторю.")

# Обработчик текстовых сообщений
@start_router.message(F.text)
async def echo(message: types.Message):
    await message.answer("Вы сказали: " + message.text)

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())