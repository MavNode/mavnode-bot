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
