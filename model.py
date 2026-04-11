import pandas as pd
data=pd.read_csv("fake reviews dataset.csv")
print(data.head())

X = data['text_']
Y = data['label']
print(X.head())
print(Y.head())

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
X_vectorizer=vectorizer.fit_transform(X)
print("Text successfully converted into numbers!")
print("Shape:", X_vectorizer.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_vectorizer,Y,test_size=0.2,random_state=42)
print("Training data shape:",X_train.shape)
print("Testing data shape:",X_test.shape)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,Y_train)
print("Model trained successfully!")

from sklearn.metrics import accuracy_score
Y_pred=model.predict(X_test)
accuracy=accuracy_score(Y_test,Y_pred)
print("Model Accuracy:",accuracy)
new_review=["This product is amazing and worth every penny"]
new_review_vectorizer=vectorizer.transform(new_review)
prediction=model.predict(new_review_vectorizer)
if prediction[0]==1:
    print("This review is FAKE")
else:
    print("This review is REAL")

import hashlib
import datetime
class Block:
    def __init__(self, index, review, prediction, previous_hash):
        self.index=index
        self.timestamp=str(datetime.datetime.now())
        self.review=review
        self.prediction=prediction
        self.previous_hash=previous_hash
        self.hash=self.calculate_hash()
    def calculate_hash(self):
        block_string=str(self.index)+self.timestamp+self.review+str(self.prediction)+self.previous_hash
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "None", "0")
    def get_latest_block(self):
        return self.chain[-1]
    def add_block(self, review, prediction):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), review, prediction, previous_block.hash)
        self.chain.append(new_block)
    def print_chain(self):
        for block in self.chain:
            print("\nIndex:", block.index)
            print("Timestamp:", block.timestamp)
            print("Review:", block.review)
            print("Prediction:", block.prediction)
            print("Hash:", block.hash)
            print("Previous Hash:", block.previous_hash)

fake_review_chain = Blockchain()
if prediction[0] == 1:
    result = "FAKE"
else:
    result = "REAL"
fake_review_chain.add_block(new_review[0], result)
fake_review_chain.print_chain()