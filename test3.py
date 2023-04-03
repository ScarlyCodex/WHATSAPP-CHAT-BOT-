from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming request data
    data = request.json
    # Process the data and generate a response
    response = {
        'success': True,
        'data': data
    }
    # Return the response as a JSON object
    return response, 200