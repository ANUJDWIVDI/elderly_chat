from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

# Define simple responses for the AI companion
responses = {
    "hello": "Hello there! How can I help you today?",
    "goodbye": "Goodbye! Have a nice day.",
    "how are you": "I'm doing well, thank you for asking.",
    "what can you do": "I can help you with various tasks, such as providing information, answering questions, and scheduling reminders.",
    "name": "My name is AI Companion.",
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        old_age_home = request.form['old_age_home']

        # Validate login credentials and redirect to portal
        return redirect('/portal')

    return render_template('index.html')

@app.route('/portal', methods=['GET'])
def portal():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Check if the user input matches any of the predefined responses
        response = responses.get(user_input.lower())

        # If no matching response is found, provide a generic response
        if response is None:
            response = "I'm still learning and may not have an answer for that yet."

        return jsonify({'response': response})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
