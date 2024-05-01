from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

# Function to handle the "/del" command
async def del_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://swagger.shidoscan.com/cosmos/staking/v1beta1/validators/YOUR_OPERATOR_VALOPER_ADDRESS/delegations'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total_delegators = len(data.get('delegation_responses', []))
        await update.message.reply_text(f'Hey, your delegator count is {total_delegators} !')
    else:
        await update.message.reply_text('Failed to fetch data. Please try again later.')

# Function to handle the "/all" command
async def all_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://swagger.shidoscan.com/cosmos/staking/v1beta1/validators/YOUR_OPERATOR_VALOPER_ADDRESS/delegations'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total_shido = sum(int(delegation['balance']['amount']) for delegation in data.get('delegation_responses', []))
        # Divide by 10^18 to convert to SHIDO from the smallest unit
        total_shido_converted = total_shido / 1e18
        await update.message.reply_text(f'Hey, you have a total of {total_shido_converted:,.6f} SHIDO delegated to you!')
    else:
        await update.message.reply_text('Failed to fetch data. Please try again later.')

# Function to handle the "/top10" command
async def top10_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://swagger.shidoscan.com/cosmos/staking/v1beta1/validators/YOUR_OPERATOR_VALOPER_ADDRESS/delegations'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract delegations and convert amounts to integers for sorting
        delegations = [
            (delegation['delegation']['delegator_address'], int(delegation['balance']['amount']))
            for delegation in data.get('delegation_responses', [])
        ]
        # Sort delegations by the amount, descending
        sorted_delegations = sorted(delegations, key=lambda x: x[1], reverse=True)
        # Take the top 10
        top10_delegations = sorted_delegations[:10]
        # Format the message
        message = "Top 10 Delegators:\n"
        for idx, (address, amount) in enumerate(top10_delegations, start=1):
            message += f"{idx}. {address}: {amount / 1e18:,.6f} SHIDO\n"
        await update.message.reply_text(message)
    else:
        await update.message.reply_text('Failed to fetch data. Please try again later.')

# Function to handle the "/info" command
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    validator_address = 'YOUR_SIGNER_VALCONS_ADDRESS'
    url = f'https://swagger.shidoscan.com/cosmos/slashing/v1beta1/signing_infos/{validator_address}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = data.get('val_signing_info', {})
        
        # Extracting the required details
        jailed_until = info.get('jailed_until', 'N/A')
        missed_blocks_counter = info.get('missed_blocks_counter', 'N/A')
        
        # Formatting the jailed status
        if jailed_until == '1970-01-01T00:00:00Z':
            jailed_status = 'Not Jailed'
        else:
            jailed_status = f'Jailed Until: {jailed_until}'
        
        # Creating the response message
        message = (f"Jailed Status: {jailed_status}\n"
                   f"Missed Blocks: {missed_blocks_counter}")
        await update.message.reply_text(message)
    else:
        await update.message.reply_text('Failed to fetch data. Please try again later.')

# Main function to set up the bot
def main() -> None:
    application = Application.builder().token('YOUR_BOT_TOKEN').build()

    # Add command handlers
    del_handler = CommandHandler('del', del_command)
    application.add_handler(del_handler)

    all_handler = CommandHandler('all', all_command)
    application.add_handler(all_handler)

    top10_handler = CommandHandler('top10', top10_command)
    application.add_handler(top10_handler)

    info_handler = CommandHandler('info', info_command)
    application.add_handler(info_handler)

    # Run the bot until you press Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()
