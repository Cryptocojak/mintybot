# 🚬 Cigawrette Twitter Bot

A Twitter bot that detects new minted "cigawrettes" NFTs (https://www.cigawrettepacks.shop/) and tweets about it. This bot uses the `tweepy` library for Twitter API access and `web3` to interact with the Ethereum blockchain.

## 📋 Requirements
- Python 3.x
- tweepy
- web3
- An Infura account

## 🚀 Quickstart

1. Clone the repo:
```bash
git clone https://github.com/Cryptocojak/mintybot.git
```

2. Install required Python packages:
```bash
pip install tweepy web3
```

3. Set up your `.env` file with the following variables:
- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_TOKEN`
- `ACCESS_TOKEN_SECRET`
- `INFURA_KEY`

4. Run the bot:
```bash
python bot2.py
```

## 🔍 What does it do?

The bot keeps running in the background and periodically queries the Ethereum blockchain to get the total supply of minted cigawrettes. If there are any new mints, it tweets about them.

### Key Variables
- `running`: Controls whether the bot keeps running.
- `query_interval`: Time between each query to the blockchain (in milliseconds).
- `CONTRACT_ADDRESS`: Ethereum address of the cigawrettes NFT smart contract.

### Key Functions

#### `get_current_number_of_mints(contract)`
Fetches the current number of minted cigawrettes from the Ethereum blockchain.

#### `send_tweet(tweet)`
Uses Tweepy to send a tweet.

## ⏭️ Future Work
- Implement error-handling for Twitter API rate limits.
- Tweet additional information like the current price or owners.
- Brand detection (President's Club Membership)

## 🤝 Contributing
Feel free to submit pull requests or issues to improve the bot!
