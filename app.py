# client_id="c88ef2cefd2f4356865fbc59040812f3"
# #Client Secret
# client_secret="qwpNcbhCOyrmOq9ofFEezjGIl2mqonHZ"

import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Client ID and Client Secret should be imported from environment variables for security
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


def get_access_token(client_id, client_secret):
    data = {'grant_type': 'client_credentials'}
    response = requests.post(
        'https://us.battle.net/oauth/token',
        data=data,
        auth=(client_id, client_secret)
    )
    return response.json()['access_token']


def get_card_data(access_token, class_name, min_mana, rarity):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        'class': class_name,
        'manaCost': min_mana,
        'rarity': rarity,
        'pageSize': 10,
        'locale' : "en_US"
    }
    response = requests.get(
        'https://us.api.blizzard.com/hearthstone/cards',
        headers=headers,
        params=params
    )
    return response.json()['cards']


@app.route('/')
def home():
    access_token = get_access_token(client_id, client_secret)
    cards = get_card_data(access_token, 'druid', 7, 'legendary')
    # sort cards by ID
    cards.sort(key=lambda card: card['id'])
    print(cards)
    return render_template('index.html', cards=cards)



