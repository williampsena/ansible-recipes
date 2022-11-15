from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def main():
    coin = random.choice(["heads", "tails"])
    return 'You got {0}!'.format(coin)
