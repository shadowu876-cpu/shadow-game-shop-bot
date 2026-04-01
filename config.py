import os

# API Tokens & Keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN") # အခုတက်နေတဲ့ Error အတွက်
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# IDs & Business Info
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", "-1003495884295")
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")

# Phone & Password Info
YOUR_GAME_SHOP_PHONE = os.getenv("YOUR_GAME_SHOP_PHONE", "09680072956")
WAVE_GAME_SHOP_PHONE = os.getenv("WAVE_GAME_SHOP_PHONE", "09680072956")
YGYI_GAME_SHOP_PHONE = os.getenv("YGYI_GAME_SHOP_PHONE", "09680072956")
YGYI_GAME_SHOP_PASS = os.getenv("YGYI_GAME_SHOP_PASS", "123456")

# Pricing & Links
Kpay_QR_link = os.getenv("Kpay_QR_link", "https://i.ibb.co/XXXXX/kbzpay-qr.png")
Wave_QR_link = os.getenv("Wave_QR_link", "https://i.ibb.co/XXXXX/kbzpay-qr.png")
PRICE_MARKUP_PERCENTAGE = float(os.getenv("PRICE_MARKUP_PERCENTAGE", "10.0"))
MIN_TOPUP = int(os.getenv("MIN_TOPUP", "1000"))

