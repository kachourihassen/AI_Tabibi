from urllib import response


try:
    import json
    import os
    from flask import Flask,request, url_for, redirect, render_template, jsonify, request
 
    import pandas as  pd
    import spacy
    
    import seaborn as sns
    import string

    from tqdm import tqdm
    from textblob import TextBlob
    
    from nltk.corpus import stopwords
    import nltk
    from nltk.stem import WordNetLemmatizer
    from nltk import word_tokenize
    import re
    
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import LogisticRegression
    from sklearn import ensemble
    from sklearn.metrics import accuracy_score
    
    
    from sklearn.preprocessing import FunctionTransformer
    from sklearn.base import BaseEstimator, TransformerMixin
    from sklearn.pipeline import FeatureUnion
    from sklearn.feature_extraction import DictVectorizer
    import re #fournit des opérations de correspondance d'expressions régulière
    import swifter
    import numpy as np
    import pickle
    
    tqdm.pandas()
except Exception as e:
    print("Error : {} ".format(e))

    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')


dataset = 'C:/Users/Kachouri/Desktop/AI/Patient/Data/New Data folder/Data.xlsx' 
df=pd.read_excel(dataset)

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

df['Description'] = df['Description'].apply(lambda x:remove_emoji(x))
df['Speciality'] = df['Speciality'].apply(lambda x:remove_emoji(x))


#from cleantext import clean
def clean_text(text):
    
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text=  re.sub('\d* replies', '',text)
    text = re.sub('\d* likes', '', text)
    text = re.sub('\d* reply', '', text)
    text = re.sub('\d* like', '', text)
    text = text.replace("Report / Delete", "")
    text = text.replace("delete", "")
    return text

df['Description'] = df['Description'].apply(lambda x:clean_text(x))
df['Speciality'] = df['Speciality'].apply(lambda x:clean_text(x))

X = df['Description']
y =df['Speciality']

encoder = LabelEncoder()
y = encoder.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
v = dict(zip(list(y), df['Speciality'].to_list()))

text_clf = Pipeline([
     ('vect', CountVectorizer(analyzer="word", stop_words="english")),
     ('tfidf', TfidfTransformer(use_idf=True)),
     ('clr', MultinomialNB(alpha=.01)),
 ])

text_clf.fit(x_train.to_list(), list(y_train))


text_clf = Pipeline([
     ('vect', CountVectorizer(analyzer="word", stop_words="english")),
     ('tfidf', TfidfTransformer(use_idf=True)),
     ('clr', LogisticRegression())])


text_clf.fit(x_train,y_train)
y_pred_train = text_clf.predict(x_train)
y_pred_test = text_clf.predict(x_test)
#print("\nTraining Accuracy score:",accuracy_score(y_train, y_pred_train))
#print("Testing Accuracy score:",accuracy_score(y_test, y_pred_test))

X_TEST = x_test.to_list()
Y_TEST = list(y_test)

predicted = text_clf.predict(X_TEST)

c = 0

for doc, category in zip(X_TEST, predicted):
    
    if c == 2:break
    
    print("-"*55)
    print(doc)
    print(v[category])
    print("-"*55)

    c = c + 1
    
np.mean(predicted == Y_TEST)

#docs_new = ['Just wondered if anyone had experienced delayed WD after tapering off an anti-depressant, especially mirtazapine? I don"t mean a few days, but feeling great for a few weeks and then suffering WD symptoms. I stopped mirt just over 6 weeks ago after a very slow taper and felt great for the first four weeks. Then a couple of weeks ago, I completely lost my appetite and have dropped lots of weight. No nausea, just having to force every morsel of food down me except for sweets which I can tolerate. I also have severe fatigue and restless legs. I do have stage 3 kidney disease and am awaiting the results of blood tests the doctor got done for me yesterday. All symptoms are indicative of a worstening kidney disease, but they are also WD symptoms. I personally can"t believe WD could start suddenly on week five after stopping a drug, but just wondered if anyone else had experienced it? Thanks']

#predicted = text_clf.predict(docs_new)

#print("Testing Predicted:", v[predicted[0]])
 
app = Flask(__name__)

with open('model.pkl','wb') as f:
    pickle.dump(text_clf,f)
    
# load
with open('model.pkl', 'rb') as f:
    clf2 = pickle.load(f)


#print("Testing Pickle:", v[predicted[0]])

response = ''

@app.route('/ai',methods=['GET','POST'])
def predict_ai():
    global response
    if(request.method == 'POST'):
        request_data = request.data
 
        
        request_data = json.loads(request_data.decode('utf-8')) 
        data = request_data['data']
         
        
        
        docs_new = [data]
        predicted = clf2.predict(docs_new)
        return v[predicted[0]]
    
    return jsonify({'data': str(v[predicted[0]])})
    


if __name__ == '__main__':
    app.run(host='192.168.0.6')
    #app.run(debug=True)
