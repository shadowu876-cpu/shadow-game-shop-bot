import os

# API Tokens & Keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Business Info & IDs
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", "0")
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")
YOUR_GAME_SHOP_PHONE = os.getenv("YOUR_GAME_SHOP_PHONE", "09xxxxxxxxx") # အခု Error တက်နေတဲ့နေရာ

# Payment Links
Kpay_QR_link = os.getenv("Kpay_QR_link", "https://example.com/qr.png")
Wave_QR_link = os.getenv("Wave_QR_link", "https://example.com/qr.png")

