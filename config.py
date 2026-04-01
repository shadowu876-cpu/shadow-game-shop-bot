import os

# API Tokens & Keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# IDs & Business Info
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", "0")
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")

# Phone Numbers (Error တက်နေတဲ့ နာမည်တွေကို ဒီမှာ အကုန်ထည့်ပေးထားပါတယ်)
YOUR_GAME_SHOP_PHONE = os.getenv("YOUR_GAME_SHOP_PHONE", "09680072956")
WAVE_GAME_SHOP_PHONE = os.getenv("WAVE_GAME_SHOP_PHONE", "09680072956")
YGYI_GAME_SHOP_PHONE = os.getenv("YGYI_GAME_SHOP_PHONE", "09680072956") # ဒီစာကြောင်းကို အခု Error အတွက် ထည့်ထားပါတယ်

# Payment Links
Kpay_QR_link = os.getenv("Kpay_QR_link", "https://i.ibb.co/XXXXX/kbzpay-qr.png")
Wave_QR_link = os.getenv("Wave_QR_link", "https://i.ibb.co/XXXXX/kbzpay-qr.png")

