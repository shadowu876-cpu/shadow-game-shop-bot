import logging
import os
import threading
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from dotenv import load_dotenv

# config.py ထဲက အချက်အလက်တွေကို ယူသုံးမယ်
from config import (
    TELEGRAM_BOT_TOKEN, BOT_NAME, ADMIN_GROUP_ID, SUPABASE_URL, SUPABASE_KEY, 
    APIFY_API_TOKEN, YGYI_GAME_SHOP_PHONE, YGYI_GAME_SHOP_PASS, PRICE_MARKUP_PERCENTAGE
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# --- Keep-alive Web Server (Flask) ---
# Render မှာ ၂၄ နာရီနိုးနေဖို့အတွက် ဖြစ်ပါတယ်
app = Flask('')

@app.route('/')
def home():
    return "I'm alive and running Shadow Game Shop Bot!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- Bot Commands & Handlers ---

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    # User ရဲ့ နာမည်နဲ့ Welcome message
    user_name = message.from_user.full_name
    welcome_text = (
        f"မင်္ဂလာပါ {user_name}၊\n"
        f"သင့်ကို ကျွန်တော်တို့ {BOT_NAME} ဆိုင်ခွဲမှ ကြိုဆိုပါတယ်ဗျာ။\n"
        "အောက်ပါ button များမှ ဝန်ဆောင်မှုကို ရယူပါ။"
    )
    
    # Main Menu Buttons
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("My info 👤", callback_data="my_info"),
        types.InlineKeyboardButton("ငွေဖြည့်မည် 💰", callback_data="deposit"),
        types.InlineKeyboardButton("ငွေဖြည့်မှတ်တမ်း 📜", callback_data="deposit_history"),
        types.InlineKeyboardButton("ဂိမ်းအော်ဒါမှတ်တမ်း 🎮", callback_data="order_history"),
        types.InlineKeyboardButton("MLBB diamond ဝယ်မည် 💎", callback_data="buy_mlbb"),
        types.InlineKeyboardButton("PUBG UC ဝယ်မည် 🔫", callback_data="buy_pubg"),
        types.InlineKeyboardButton("Support ☎️", callback_data="support"),
        types.InlineKeyboardButton("Reseller 🤝", callback_data="reseller"),
        types.InlineKeyboardButton("Privacy Policy 🛡️", callback_data="privacy")
    ]
    keyboard.add(*buttons)
    
    await message.answer(welcome_text, reply_markup=keyboard)

# My Info Handler
@dp.callback_query_handler(lambda c: c.data == 'my_info')
async def process_my_info(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    name = callback_query.from_user.full_name
    # ဤနေရာတွင် Supabase မှ data ဆွဲရန် logic ထည့်ရမည် (လောလောဆယ် placeholder ပြထားသည်)
    info_text = (
        f"🆔 ID: {user_id}\n"
        f"👤 Name: {name}\n"
        f"💵 လက်ကျန်ငွေ: 0 MMK\n"
        f"🛒 သုံးစွဲခဲ့သမျှ: 0 MMK"
    )
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("သိပါပြီ ✅", callback_data="delete_msg"))
    
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=info_text,
        reply_markup=keyboard
    )

# Message ဖျက်ရန် (သိပါပြီ button အတွက်)
@dp.callback_query_handler(lambda c: c.data == 'delete_msg')
async def delete_current_msg(callback_query: types.CallbackQuery):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    # Start message ပြန်ပို့ပေးနိုင်သည်
    await cmd_start(callback_query.message)

# Admin က ဈေးနှုန်း Update လုပ်ရန် ခိုင်းသည့်စာကို စစ်ဆေးခြင်း
@dp.message_handler(lambda message: "Bot ရေ ဈေးသွားစစ်ပြီး ၅% တင်ရောင်းပါ" in message.text)
async def admin_sync_prices(message: types.Message):
    # Admin စစ်ဆေးခြင်း logic (config ထဲက ID နဲ့တိုက်စစ်ပါ)
    await message.reply("ဈေးနှုန်းများ စတင်စစ်ဆေးနေပါသည်။ ခေတ္တစောင့်ဆိုင်းပေးပါ။ (Apify Bot စတင်နေပါပြီ)")
    # ဤနေရာတွင် Apify Actor ကိုလှမ်းခေါ်ရပါမည်

if __name__ == '__main__':
    # Flask ကို Background မှာ run မယ်
    t = threading.Thread(target=run_flask)
    t.start()
    
    # Bot ကို စတင်မယ်
    logging.info("Bot is starting...")
    executor.start_polling(dp, skip_updates=True)

