from flask import Flask, abort, jsonify, request
from flask_cors import CORS
import nltk.data

app = Flask(__name__)
CORS(app)

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

@app.route("/api", methods = ['POST'])
def hello():
    data = request.get_json(silent=True)
    
    # To Do: 
    # Call the real ML Model here
    # check_disclosure(data['text'])    
    example_disclosure_sentences = ["I will meet you at 7pm.", 
                                    "I got the flu.",
                                    "It's only the second day of the month and I am completely out of money."]
    sentences = sent_detector.tokenize(data['text'].strip())

    disclosure_sentences = ""
    result = "non-disclosure"

    for sentence in sentences:
        if sentence in example_disclosure_sentences:
            disclosure_sentences += "<<"+sentence+">>"
            result = "disclosure"
        else:
            disclosure_sentences += sentence
        disclosure_sentences += " "

    return jsonify(results = [result, disclosure_sentences])

# def check_disclosure(data):
#     # To Do:
#     # 1. Sentence tokenize    
#     # 2. Check every sentences with model
#     # 3. Get disclosure sentence(s)
#     # 4. Send back the disclosure sentence

if __name__ == '__main__':
    app.run(port = 9000, debug = True) 
