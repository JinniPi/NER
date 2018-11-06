import pycrfsuite
import json
from Generating_Features import Generating_Features
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import classification_report

a = Generating_Features()

data = a.get_data_doc("data.json")
print(type(data))

print('dang doc')

X = [a.extract_features(doc) for doc in data]
# print(X)
y = [a.get_labels(doc) for doc in data]
# print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("----log x_test-------")
print(X_test)
print(y_test)

tagger = pycrfsuite.Tagger()
tagger.open('crf.model')
y_pred = [tagger.tag(xseq) for xseq in X_test]

# Let's take a look at a random sample in the testing set
i = 12
for x, y in zip(y_pred[i], [x[1].split("=")[1] for x in X_test[i]]):
    print("%s (%s)" % (y, x))

print("-------- dang danh gia--------")


# Create a mapping of labels to indices
labels = {"O": 0, "I-ART": 1,"I-DAT": 2,"I-LOC": 3,"I-MON": 4,"I-ORG": 5,"I-PCT": 6,"I-TIM": 7,"I-TTL": 8,"I-PER": 9}

# Convert the sequences of tags into a 1-dimensional array
predictions = np.array([labels[tag] for row in y_pred for tag in row])
# print("-----------predictions--------------")
# print(predictions)
truths = np.array([labels[tag] for row in y_test for tag in row])
# print("-------truths--------")
# print(truths)

# Print out the classification report
print(classification_report(
    truths, predictions,
    target_names=["O","I-ART","I-DAT","I-LOC","I-MON","I-ORG","I-PCT","I-TIM","I-TTL","I-PER"]))