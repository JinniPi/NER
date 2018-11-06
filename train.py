import json
from Generating_Features import Generating_Features
from sklearn.model_selection import train_test_split
import pycrfsuite

a = Generating_Features()

data = a.get_data_doc("data.json")
print(type(data))

print('dang doc')

X = [a.extract_features(doc) for doc in data]
print(X)
y = [a.get_labels(doc) for doc in data]
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



trainer = pycrfsuite.Trainer(verbose=True)

print(".............")

# Submit training data to the trainer
for xseq, yseq in zip(X_train, y_train):
	trainer.append(xseq, yseq)

# Set the parameters of the model
trainer.set_params({
	# coefficient for L1 penalty
	'c1': 0.1,

	# coefficient for L2 penalty
	'c2': 0.01,  

	# maximum number of iterations
	'max_iterations': 200,

	# whether to include transitions that
	# are possible, but not observed
	'feature.possible_transitions': True
})

# Provide a file name as a parameter to the train function, such that
# the model will be saved to the file when training is finished
trainer.train('crf.model')


`