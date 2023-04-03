from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

account_sid = 'AC32f6bcd8852a5135fb1df7a67c97d80a'
auth_token = '787e57aabf74d21ffaea675a17ec3517'
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    if incoming_msg == 'hello':
        resp.message('Hello! How can we help you?')
        message = client.messages.create(
            from_='whatsapp:+15855222049',
            body='Please select an option:',
            to='whatsapp:' + request.values.get('From')
        )
        message.media('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.adslzone.net%2Fcomo-se-hace%2Fphotoshop%2Fquitar-fondo-imagen%2F&psig=AOvVaw3s7ao-cqepa2NNGIeV54rw&ust=1680568732812000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCNCylMS8jP4CFQAAAAAdAAAAABAE')
        message.buttons([
            {
                'type': 'phone_number',
                'title': 'Chat with us',
                'payload': '+1234567890'
            },
            {
                'type': 'url',
                'title': 'About us',
                'payload': 'https://www.upwork.com/ab/proposals/job/~018415b05723381669/apply/'
            }
        ])
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
