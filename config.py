import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ADMIN_GROUP_ID = os.getenv("ADMIN_GROUP_ID", "0")
BOT_NAME = os.getenv("BOT_NAME", "Shadow Game Shop")

# အခုတက်နေတဲ့ Error အတွက် ဖြည့်စွက်ချက်
Kpay_QR_link = os.getenv("Kpay_QR_link", "https://example.com/default-qr")

