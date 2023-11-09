from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Replace <password> with your actual MongoDB Atlas password
uri = "mongodb+srv://chethankeshavmurthy:okchethan123@cluster0.jvsptl5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the 'Cluster0' database
db = client['Cluster0']

# Access the 'menstrual_data' collection
menstrual_data = db['menstrual_data']

@app.route('/visualize')
def visualize():
    # Get the data from MongoDB
    data = menstrual_data.find()

    # Get the dark mode preference from the query string (if set)
    dark_mode = request.args.get('dark_mode', default='light')

    return render_template('visualize.html', data=data, dark_mode=dark_mode)

if __name__ == '__main__':
    app.run(debug=True)
