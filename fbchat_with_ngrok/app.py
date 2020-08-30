from flask import Flask, request
import json
from bot import Bot
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()

with file("tokens.json", "r") as f:
    json_data = json.load(f)



ACCESS_TOKEN = json_data['ACCESS_TOKEN']
VERIFY_TOKEN = json_data['VERIFY_TOKEN']


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return str(challenge)
        return '400'


    else:

        data = json.loads(request.data)
        bot = Bot(ACCESS_TOKEN)

        user_id = data['entry'][0]['messaging'][0]['sender']['id']

        try:
            text_input = str.lower(data['entry'][0]['messaging'][0]['message']['text'])
            print ("Message from user ID {} - {}".format(user_id, text_input))
            if "szia" in text_input and user_id == '<insert_the_user_id>':
                bot.send_text_message(int(user_id), 'szia, user1')
            else:
                bot.send_text_message(int(user_id), 'szia, user2')

        
        except:
            pass


        return '200'

if __name__ == '__main__':
    app.run(debug=True)