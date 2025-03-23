from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200625534"})  # Replace with your actual student number

@app.route('/learnixai')
def learnixai():
    return jsonify({"message": "Welcome to LearnixAI!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    request_data = request.get_json(silent=True, force=True)

    response_text = "Hello! This is a response from your webhook."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
