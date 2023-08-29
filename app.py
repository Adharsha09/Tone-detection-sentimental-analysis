from flask import *
from keras.models import load_model
import pickle
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

loaded_model = load_model("sentimental_analysis_model")

with open("tokenizer.pickle", 'rb') as handle:
    tokenizer = pickle.load(handle)

def review(Review):
    reviews = []
    review = re.sub('[^a-zA-Z]', ' ',Review) # Cleaning the data
    review = review.lower()  # Converting into lower case
    review = nltk.word_tokenize(review) #Tokenization
    lemm = WordNetLemmatizer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not') # Removing 'Not' from stop words
    review = [lemm.lemmatize(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review) # Joining each word
    reviews.append(review)
    Review = tokenizer.texts_to_sequences(reviews)
    Review = pad_sequences(Review, maxlen = 88)
    Output = loaded_model.predict(Review)
    if Output > 0.5:
        sentiment_str ="Positive"
    else:
        sentiment_str ="Negative"
    
    return sentiment_str,Output

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')
@app.route('/login',methods = ['POST','GET'])

def result():
    if request.method == 'POST':
        text = request.form['text']
        response,s = review(text)
        return render_template('result.html',final_result=response,message = text, score = s[0])
    return None
if __name__ == "__main__": 
    app.run(debug=True,host = '0.0.0.0',port=5000,use_reloader=False)