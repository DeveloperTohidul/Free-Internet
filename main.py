from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# আপনার টেলিগ্রাম বটের টোকেন
TOKEN = "8034878152:AAH-pXJEhuDM0JGWf-WfUSR9B4rTpX8Bb8k"

# /start কমান্ড: Reply Keyboard মেনু প্রদর্শন
async def start(update: Update, context):
    # মেনুতে বাটনগুলো (বাম দিকে)
    keyboard = [
        ["Help"],               # প্রথম লাইন
        ["About"],              # দ্বিতীয় লাইন
        ["Exit"],               # তৃতীয় লাইন
        ["New Feature"],        # চতুর্থ লাইন
        ["Hamster Image"]       # "Hamster Image" বাটন
    ]

    # Reply Keyboard তৈরি করা
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# মেসেজের রেসপন্স ফাংশন
async def handle_message(update: Update, context):
    user_message = update.message.text

    # "Hamster Image" ক্লিক করলে ইউটিউব লিঙ্ক খুলবে
    if user_message == "Hamster Image":
        await update.message.reply_text("Opening Hamster Video: [YouTube](https://www.youtube.com)", parse_mode='Markdown')
    elif user_message == "Help":
        await update.message.reply_text("This bot allows you to view cute hamster images and interact with the bot!")
    elif user_message == "About":
        await update.message.reply_text("This bot was created to share cute hamster images and bring joy! 😊")
    elif user_message == "Exit":
        await update.message.reply_text("Goodbye! Have a great day! 👋")
    elif user_message == "New Feature":
        await update.message.reply_text("This is a new feature!")
    else:
        await update.message.reply_text("Please choose a valid option from the menu.")

# মূল স্ক্রিপ্ট
if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    # কমান্ড হ্যান্ডলার
    application.add_handler(CommandHandler("start", start))

    # মেসেজ হ্যান্ডলার
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # বটটি চালু করা
    print("Bot is running...")
    application.run_polling()
