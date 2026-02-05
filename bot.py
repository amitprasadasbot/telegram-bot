from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "8335052092:AAHB55RMP3Y-QdUiRfYIR_hht6PTXn5SpzI"
ADMIN_ID = 1709255409


# ✅ Check if user already exists
def user_exists(user_id):
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                if str(user_id) in user:
                    return True
    except:
        pass
    return False


# ✅ Save user with telegram ID
def save_user(user_id, number):

    if user_exists(user_id):
        return

    with open("users.txt", "a") as file:
        file.write(f"{user_id}:{number}\n")


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_exists(user_id):
        await update.message.reply_text(
            "✅ You are already registered!\nSelect your voucher."
        )

        keyboard = [
            ["Voucher ₹500"],
            ["Voucher ₹1000"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "Choose a voucher:",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text(
            "Hello 👋\n\nPlease enter your mobile number:"
        )


# HANDLE MESSAGES
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id

    if text.isdigit() and len(text) == 10:

        if user_exists(user_id):
            await update.message.reply_text(
                "✅ Number already registered."
            )
            return

        save_user(user_id, text)

        keyboard = [
            ["Voucher ₹500"],
            ["Voucher ₹1000"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "✅ Mobile number saved!",
            reply_markup=reply_markup
        )

    elif text == "Voucher ₹500":
        await update.message.reply_text("🔥 Preparing cart under ₹500...")

    elif text == "Voucher ₹1000":
        await update.message.reply_text("🔥 Preparing cart under ₹1000...")

    else:
        await update.message.reply_text(
            "❌ Enter a valid 10-digit mobile number."
        )


# ⭐ ADMIN — USER COUNT
async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    try:
        with open("users.txt", "r") as file:
            count = len(file.readlines())
    except:
        count = 0

    await update.message.reply_text(f"📊 Total Users: {count}")


def main():

    app = ApplicationBuilder().token(TOKEN).job_queue(None).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("users", users))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("BOT RUNNING 🚀")

    app.run_polling()


if __name__ == "__main__":
    main()
ADMIN_ID =1709255409


# ✅ Check if user already exists
def user_exists(user_id):
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                if str(user_id) in user:
                    return True
    except:
        pass
    return False


# ✅ Save user with telegram ID
def save_user(user_id, number):

    if user_exists(user_id):
        return

    with open("users.txt", "a") as file:
        file.write(f"{user_id}:{number}\n")


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_exists(user_id):
        await update.message.reply_text(
            "✅ You are already registered!\nSelect your voucher."
        )

        keyboard = [
            ["Voucher ₹500"],
            ["Voucher ₹1000"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "Choose a voucher:",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text(
            "Hello 👋\n\nPlease enter your mobile number:"
        )


# HANDLE MESSAGES
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id

    if text.isdigit() and len(text) == 10:

        if user_exists(user_id):
            await update.message.reply_text(
                "✅ Number already registered."
            )
            return

        save_user(user_id, text)

        keyboard = [
            ["Voucher ₹500"],
            ["Voucher ₹1000"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "✅ Mobile number saved!",
            reply_markup=reply_markup
        )

    elif text == "Voucher ₹500":
        await update.message.reply_text("🔥 Preparing cart under ₹500...")

    elif text == "Voucher ₹1000":
        await update.message.reply_text("🔥 Preparing cart under ₹1000...")

    else:
        await update.message.reply_text(
            "❌ Enter a valid 10-digit mobile number."
        )


# ⭐ ADMIN — USER COUNT
async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    try:
        with open("users.txt", "r") as file:
            count = len(file.readlines())
    except:
        count = 0

    await update.message.reply_text(f"📊 Total Users: {count}")


def main():

    app = ApplicationBuilder().token(TOKEN).job_queue(None).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("users", users))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("BOT RUNNING 🚀")

    app.run_polling()


if __name__ == "__main__":
    main()
ADMIN_ID = 1709255409

# ✅ Check if user already exists
def user_exists(user_id):
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            for user in users:
                if str(user_id) in user:
                    return True
    except:
        pass
    return False


# ✅ Save user
def save_user(user_id, number):

    if user_exists(user_id):
        return

    with open("users.txt", "a") as file:
        file.write(f"{user_id}:{number}\n")


# ✅ START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if user_exists(user_id):

        keyboard = [
            ["Voucher ₹500"],
            ["Voucher ₹1000"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "✅ You are already registered!\nSelect your voucher:",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text(
            "Hello 👋\n\nPlease enter your mobile number:"
        )


# ✅ HANDLE USER MESSAGES
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id

    if text.isdigit() and len(text) == 10:

        if user_exists(user_id):
            await update.message.reply_text(
                "✅ Number already registered."
            )
            return

        save_user(user_id, text)

        keyboard = [
            ["Voucher ₹500"],
            ["Voucher ₹1000"]
        ]

        reply_markup = ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )

        await update.message.reply_text(
            "✅ Mobile number saved!",
            reply_markup=reply_markup
        )

    elif text == "Voucher ₹500":
        await update.message.reply_text("🔥 Preparing cart under ₹500...")

    elif text == "Voucher ₹1000":
        await update.message.reply_text("🔥 Preparing cart under ₹1000...")

    else:
        await update.message.reply_text(
            "❌ Enter a valid 10-digit mobile number."
        )


# ✅ ADMIN — USER COUNT
async def users(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    try:
        with open("users.txt", "r") as file:
            count = len(file.readlines())
    except:
        count = 0

    await update.message.reply_text(f"📊 Total Users: {count}")


# ✅ ADMIN — BROADCAST
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    if not context.args:
        await update.message.reply_text(
            "Use:\n/broadcast Your message"
        )
        return

    message = " ".join(context.args)

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
    except:
        users = []

    sent = 0

    for user in users:

        user_id = user.split(":")[0]

        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=message
            )
            sent += 1
        except:
            pass

    await update.message.reply_text(
        f"✅ Broadcast sent to {sent} users."
    )


# ✅ MAIN FUNCTION
def main():

    app = ApplicationBuilder().token(TOKEN).job_queue(None).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("users", users))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("BOT RUNNING 🚀")

    app.run_polling()


if __name__ == "__main__":
    main()
