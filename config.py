import os

# API Tokens & Keys
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# IDs & Business Info
ADMIN_GROUP_ID = int(os.getenv("ADMIN_GROUP_ID", "0"))
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")

# Payment Links (Error တက်နေတဲ့ နာမည်ကို ဒီမှာ သေချာပြင်ထားပါတယ်)
KPAY_QR_LINK = os.getenv("KPAY_QR_LINK", "https://example.com/qr.png")
WAVEPAY_QR_LINK = os.getenv("WAVEPAY_QR_LINK", "https://example.com/qr.png")

