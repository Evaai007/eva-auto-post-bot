import asyncio
from telegram import Bot
from datetime import datetime

BOT_TOKEN = "8895915658:AAHBREiio1McrX0w_61AqQ7CHUJEs0JrxiM"
GROUP_IDS = [-1003722190023, -1002225866960]
INTERVAL = 300

bot = Bot(token=BOT_TOKEN)

posts = [
    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎✨ EVA AI MARKET - SPECIAL OFFER ✨💎
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

☁️ AWS CLOUD PREMIUM
🔹 128V • 256V • 512V

🤖 CLAUDE AI ELITE
🔹 Claude Pro • Claude Max

👑 GPT PREMIUM PLUS
🔹 GPT Plus • GPT Pro

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Amazon Bedrock Claude AI Opus
✅ GPT Plus + Claude Access
✅ Gemini Ultra Support

🌍 International | ⚡ Instant Delivery

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📢 OFFICIAL CHANNELS
👉 Main: https://t.me/AWSXCLOUDEBUYSELL
👉 Premium: https://t.me/+zP2HsqN-cGAyYzk1

📞 Admin: @eva007_8

🛒 AUTO SHOP BOT: @eva_ai_market_bot
🌐 WEB STORE: https://payhip.com/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ PREMIUM SERVICE GUARANTEED ⭐
✔️ Real Seller - Trusted & Verified
✔️ Instant Delivery - Get Access Immediately
✔️ 24/7 Support - Always Available
✔️ Worldwide Service - No Restrictions
✔️ Money Back Guarantee

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""",

    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 LIMITED TIME OFFER 🚀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 SPECIAL DISCOUNTS TODAY!

☁️ AWS Cloud - Premium Access
🤖 Claude AI - Full Features
👑 GPT Plus - Unlimited Usage

⏰ Offer Valid: 24 Hours Only!

📞 Contact: @eva007_8
🛒 Shop Now: @eva_ai_market_bot

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""",

    """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ JOIN OUR COMMUNITY ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💎 EVA AI MARKET

📢 Official Channel: https://t.me/AWSXCLOUDEBUYSELL
👥 Community Group: https://t.me/evacloudmarket

✅ 1000+ Happy Customers
✅ Real Reviews & Ratings
✅ 24/7 Active Support

👉 Join Now & Get Started!

📞 Admin: @eva007_8

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
]

post_index = 0

async def auto_post():
    global post_index
    
    while True:
        try:
            for group_id in GROUP_IDS:
                await bot.send_message(
                    chat_id=group_id,
                    text=posts[post_index]
                )
                print(f"✅ Post sent to {group_id} at {datetime.now()}")
            
            post_index = (post_index + 1) % len(posts)
            await asyncio.sleep(INTERVAL)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            await asyncio.sleep(60)

async def main():
    print("🚀 Auto Post Bot Started!")
    print(f"📢 Groups: {GROUP_IDS}")
    print(f"⏰ Interval: {INTERVAL} seconds")
    await auto_post()

if __name__ == '__main__':
    asyncio.run(main())
