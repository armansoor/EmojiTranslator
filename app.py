import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, render_template, request

# Load the dataset of English words and their corresponding emojis
data_url = "https://raw.githubusercontent.com/NeelShah18/emot/master/emot/emo_unicode.csv"
data = pd.read_csv(data_url)

# Preprocess the data by removing NaN values and splitting into X and y
data.dropna(inplace=True)
X = data["Text"].values.astype("U")
y = data["Emoji"].values.astype("U")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Convert the text data to numerical features using TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train a Naive Bayes classifier on the training data
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Define a Flask app for the web interface
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return render_template("home.html")

# Define a route for the translation page
@app.route("/translate", methods=["POST"])
def translate():
    # Get the user input from the web form
    text = request.form["text"]
    
    # Convert the input to a numerical feature using TF-IDF vectorization
    X_input = vectorizer.transform([text])
    
    # Use the trained classifier to predict the corresponding emoji
    y_pred = clf.predict(X_input)
    
    # Render the translation page with the predicted emoji
    return render_template("translate.html", text=text, emoji=y_pred[0])

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
