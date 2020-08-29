from flask import Flask, request

PAGE_ACCESS_TOKEN = '<INSERT_YOUR_ACCESS_TOKEN_HERE>'
VERIFY_TOKEN = 'secret'


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
        print(request.data)
        return '200'

if __name__ == '__main__':
    app.run(debug=True)