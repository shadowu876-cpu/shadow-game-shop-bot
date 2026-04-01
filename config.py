import os

# API Keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# IDs & Settings (ဒါတွေမပါရင် Button error တက်တတ်ပါတယ်)
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", "-1003495884295")
PRICE_MARKUP_PERCENTAGE = float(os.getenv("PRICE_MARKUP_PERCENTAGE", "10.0"))
MIN_TOPUP = int(os.getenv("MIN_TOPUP", "1000"))

# Business Info
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")
YOUR_GAME_SHOP_PHONE = os.getenv("YOUR_GAME_SHOP_PHONE", "09680072956")

