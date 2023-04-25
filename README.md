# Emoji Translator
This is a simple web application that allows users to input English text and receive the corresponding emoji. The application uses a Naive Bayes classifier trained on a dataset of English words and their corresponding emojis.

## Usage
To use the application, simply enter some English text into the input field on the home page and click the "Translate" button. The corresponding emoji will be displayed on the translation page.

## Installation
To run the application locally, you will need to have Python 3.x and the following dependencies installed:

1. pandas
2. scikit-learn
3. Flask

## You can install these dependencies using pip:

<pre>
pip install pandas scikit-learn Flask
</pre>
Once you have installed the dependencies, you can start the application by running the app.py file:

<pre>
python app.py
</pre>

The application will start running on http://localhost:5000.

## Dataset
The dataset used to train the classifier is a publicly available open-source dataset of English words and their corresponding emojis. The dataset can be found at the following URL:

<pre>
https://raw.githubusercontent.com/NeelShah18/emot/master/emot/emo_unicode.csv
</pre>

## Contributing
If you would like to contribute to the project, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Credits
This project was created by Abdur Rahman Mansoor.
