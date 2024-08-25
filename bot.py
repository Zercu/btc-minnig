from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TELEGRAM_TOKEN, ADMIN_USERNAME, ADMIN_PASSWORD
from admin import check_admin, add_new_user, grant_admin
from mining import Miner
from wallet import withdraw_to_wallet
from database import create_tables, add_mining_record, get_mining_records

# Initialize miner instance with pool URL and wallet address
miner = Miner(pool_url='stratum+tcp://pool.url:port', wallet_address='your_wallet_address')

# Initialize the database tables
create_tables()

# Command: /start
def start(update, context):
    update.message.reply_text('Welcome to the Bitcoin Mining Bot!')

# Command: /start_mining
def start_mining(update, context):
    user = update.message.from_user.username
    if check_admin(user, ADMIN_PASSWORD):
        mined_amount = miner.start_mining()
        add_mining_record(user, mined_amount)
        update.message.reply_text(f'Mined {mined_amount:.5f} BTC. Total Balance: {miner.get_balance():.5f} BTC.')
    else:
        update.message.reply_text('Access denied.')

# Command: /stop_mining
def stop_mining(update, context):
    user = update.message.from_user.username
    if check_admin(user, ADMIN_PASSWORD):
        result = miner.stop_mining()
        update.message.reply_text(result)
    else:
        update.message.reply_text('Access denied.')

# Command: /status
def status(update, context):
    status = miner.get_status()
    update.message.reply_text(status)

# Command: /withdraw <wallet_address>
def withdraw(update, context):
    user = update.message.from_user.username
    if check_admin(user, ADMIN_PASSWORD):
        address = context.args[0]
        amount = miner.get_balance()
        result = withdraw_to_wallet(address, amount)
        if result.get('status') == 'success':
            update.message.reply_text(f'Withdrawal of {amount:.5f} BTC to {address} completed.')
            miner.balance = 0  # Reset balance after withdrawal
        else:
            update.message.reply_text('Withdrawal failed.')
    else:
        update.message.reply_text('Access denied.')

# Command: /history
def history(update, context):
    user = update.message.from_user.username
    records = get_mining_records(user)
    if records:
        history_text = "\n".join([f"Amount: {record[2]:.5f} BTC at {record[3]}" for record in records])
        update.message.reply_text(f"Mining History:\n{history_text}")
    else:
        update.message.reply_text("No mining records found.")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('start_mining', start_mining))
    dp.add_handler(CommandHandler('stop_mining', stop_mining))
    dp.add_handler(CommandHandler('status', status))
    dp.add_handler(CommandHandler('withdraw', withdraw, pass_args=True))
    dp.add_handler(CommandHandler('history', history))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
