# MavNode Bot Tutorial

---

## Introduction

Welcome to the MavNode Bot Tutorial! This tutorial will guide you through the process of creating a Telegram bot that queries validator information on the Shido Network, which is built on the Cosmos SDK. The goal is to provide you with a hands-on guide to develop a bot that can interact with blockchain data, useful for users who want up-to-date information directly through Telegram.

The bot we are going to build is designed to be simple yet functional, providing key data points about validators in the Shido Network ecosystem. Whether you are a participant in the network or just interested in blockchain technology, this bot will serve as a great tool for accessing decentralized data.

## Prerequisites

Before we get started, make sure you have the following:
- A basic understanding of Python programming.
- A server or local machine with Python installed.
- A Telegram account to interact with the BotFather and test your bot.

## Step 1: Creating Your Telegram Bot

The first step in creating a Telegram bot is to register the bot with Telegram and obtain an API token. This token will allow your script to interact authentically with the Telegram API.

### Register Your Bot with BotFather

1. **Start a chat with BotFather**: BotFather is the official Telegram bot that handles the creation and management of bots. Open Telegram, search for "@BotFather", and start a conversation.

2. **Create a new bot**: Type `/newbot` and send it to BotFather. You will be prompted to give your bot a name and then a username. The username must end in 'bot' (e.g., `MavNodeBot`).

3. **Get your token**: After successfully creating your bot, BotFather will provide you with an API token. This token is essential for making API calls to Telegram. Keep it secure and do not share it.

*Note: Treat your token like a password. Anyone with access to it can control your bot.*

After obtaining your token, you're ready to start setting up your bot's environment and programming it to interact with the Shido Network. In the next section, we'll cover setting up your project and installing necessary dependencies.

---

## Step 2: Setting Up Your Project Environment

This section will guide you through setting up your project environment, cloning the repository, and installing all necessary libraries to run your Telegram bot.

### Install Git and Clone the Repository

Before you can start working with the bot, you need to install Git on your machine to clone the repository. This allows you to manage the project's files and keep track of any changes.

1. **Install Git**:
   - Open your terminal.
   - Install Git by running the command:
     ```
     sudo apt-get install git
     ```

2. **Clone the repository**:
   - Once Git is installed, you can clone the repository to your local machine or server.
   - Use the following command to clone the repository:
     ```
     git clone https://github.com/MavNode/validatorbot/tree/main
     ```
   - Navigate to the project directory:
     ```
     cd validatorbot
     ```

### Install Required Libraries

Now that you have the project files, the next step is to install the necessary Python libraries to ensure the bot runs smoothly.

1. **Install Python Libraries**:
   - Ensure Python and pip (Python’s package installer) are installed on your machine.
   - Install the required libraries using pip and the `requirements.txt` file included in the repository:
     ```
     pip install -r requirements.txt
     ```

This completes the setup of your project environment. You now have all the necessary files and libraries installed to begin configuring and running your bot.

---

## Step 3: Customizing the Bot Code

This part of the tutorial will walk you through customizing the `vbot.py` file. You will need to replace certain placeholders with your actual data to make the bot functional for your specific use case.

### Setting Up Your Validator Addresses

To fetch validator-specific data, the bot must know which validator addresses to query. The code provided has placeholders marked as `YOUR_OPERATOR_VALOPER_ADDRESS` and `YOUR_SIGNER_VALCONS_ADDRESS`. Here's how to update them:

1. **Find `YOUR_OPERATOR_VALOPER_ADDRESS`**:
   - This placeholder is used in the commands `/del`, `/all`, and `/top10`.
   - Replace `YOUR_OPERATOR_VALOPER_ADDRESS` with your validator's operator address. You can find this address in your validator setup or in the blockchain explorer for Shido Network.

```python
async def all_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://swagger.shidoscan.com/cosmos/staking/v1beta1/validators/YOUR_OPERATOR_VALOPER_ADDRESS/delegations'
```

2. **Find `YOUR_SIGNER_VALCONS_ADDRESS`**:
   - This placeholder is found in the `/info` command.
   - Replace `YOUR_SIGNER_VALCONS_ADDRESS` with your validator's signer (consensus) address. This address is used for identifying your validator in the network's consensus and slashing data.

```python
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    validator_address = 'YOUR_SIGNER_VALCONS_ADDRESS'
    url = f'https://swagger.shidoscan.com/cosmos/slashing/v1beta1/signing_infos/{validator_address}'
```

### Insert Your Telegram Bot Token

To connect your script with the Telegram API, you need to insert your unique bot token provided by BotFather during the creation of your bot.

1. **Locate the `YOUR_BOT_TOKEN` placeholder**:
   - This placeholder is found in the `main()` function of your `vbot.py` script.

2. **Replace the placeholder**:
   - Replace `YOUR_BOT_TOKEN` with the actual token you received from BotFather.

### Example of Modified Main Function

Here’s what part of your `main()` function should look like after making the necessary replacements:

```python
def main() -> None:
    application = Application.builder().token('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11').build()
```

---

## Step 4: Running Your Telegram Bot

Before you run your bot, make sure you've completed the following checklist:
- [ ] Environment and dependencies are correctly set up.
- [ ] Bot token and validator addresses have been correctly inserted into `vbot.py`.
- [ ] You have checked for syntax errors or configuration mistakes.

Once you're all set, you can start your bot by running the following command in your terminal:

```bash
python3 vbot.py
```

