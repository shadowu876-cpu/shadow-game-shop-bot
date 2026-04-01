import os

# API Tokens & Keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# IDs & Business Info (Render က နာမည်တွေနဲ့ ကိုက်အောင် ပြင်ထားပါတယ်)
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", "0")
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")

# Payment Links (Render ထဲက နာမည်အတိုင်း ပြင်ပေးထားပါတယ်)
Kpay_QR_link = os.getenv("Kpay_QR_link", "https://example.com/qr.png")

