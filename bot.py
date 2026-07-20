import os
import asyncio
from telegram import Bot
from datetime import datetime

BOT_TOKEN = os.environ["BOT_TOKEN"]

GROUP_IDS = [
    -1003722190023,
    -1002225866960
]

INTERVAL = 300

bot = Bot(token=BOT_TOKEN)

posts = [
"""💎 EVA AI MARKET

☁️ AWS 128V • 256V • 512V

✅ Amazon Bedrock Claude AI Opus
✅ GPT Plus + Claude Access
✅ Gemini Ultra Support

📞 Admin: @eva007_8
📢 Channel: https://t.me/AWSXCLOUDEBUYSELL
🛒 Shop Bot: @eva_ai_market_bot
""",

"""🚀 SPECIAL OFFER

☁️ AWS CLOUD
🤖 Claude AI
👑 GPT Plus

⚡ Instant Delivery
🌍 Worldwide

📞 @eva007_8
""",

"""💎 EVA AI MARKET

✔ Trusted Seller
✔ Fast Delivery
✔ 24/7 Support

📢 https://t.me/AWSXCLOUDEBUYSELL
"""
]

post_index = 0

async def auto_post():
    global post_index

    while True:
        try:
            for group in GROUP_IDS:
                await bot.send_message(
                    chat_id=group,
                    text=posts[post_index]
                )

            print(f"Posted at {datetime.now()}")

            post_index = (post_index + 1) % len(posts)

            await asyncio.sleep(INTERVAL)

        except Exception as e:
            print(e)
            await asyncio.sleep(60)

async def main():
    print("Bot Started")
    await auto_post()

if __name__ == "__main__":
    asyncio.run(main())
