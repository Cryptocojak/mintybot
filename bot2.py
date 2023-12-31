import tweepy
import time
import logging
from web3 import Web3
from env import consumer_key, consumer_secret, access_token, access_token_secret, if_key
import os

# consumer_key = os.environ['CONSUMER_KEY']
# consumer_secret = os.environ['CONSUMER_SECRET']
# access_token = os.environ['ACCESS_TOKEN']
# access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
# if_key = os.environ['INFURA_KEY']

running = True
query_interval = 7500
CONTRACT_ADDRESS = '0xEEd41d06AE195CA8f5CaCACE4cd691EE75F0683f' #cigawrettes contract
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{if_key}'))

latest_block = w3.eth.get_block('latest')
nft_contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=[{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}])
next_mint = (nft_contract.functions.totalSupply().call())
current_mint = next_mint - 1

#function to get current number of mints
def get_current_number_of_mints(contract):
    global current_mint
    global next_mint

    try:
        next_mint = contract.functions.totalSupply().call()
        current_mint = next_mint - 1
        return current_mint
    except Exception as e:
        logging.exception(f"Error getting total supply: {e}")
        return None   

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

def send_tweet(tweet):
    response = client.create_tweet(text=f"{tweet}")
    logging.info(f"\n\n\n tweet sent \n\n https://twitter.com/user/status/{response.data['id']}\n")
    pass

def main():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    global current_mint

    last_tweeted = current_mint

    while running:
        new_mint = get_current_number_of_mints(nft_contract)
        logging.info(f"🚬 🚬 🚬 🚬 🚬 🚬 {new_mint} ")
        if new_mint is not None and new_mint != last_tweeted:
            logging.info(f"new mint, {new_mint}, last tweeted, {last_tweeted}")
            time.sleep(60)  # Wait for one minute to check for additional mints
            final_mint = get_current_number_of_mints(nft_contract)
            mints_count = final_mint - last_tweeted
            tweet = f"{mints_count} new cigawrette pack(s) detected! \n\n https://blur.io/asset/0xeed41d06ae195ca8f5cacace4cd691ee75f0683f/{final_mint}."
            send_tweet(tweet)
            last_tweeted = final_mint
        time.sleep(query_interval / 1000) 

if __name__ == '__main__':
    main()
