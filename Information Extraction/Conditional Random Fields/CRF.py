import pycrfsuite

f_train = open("../training/train_data.txt")
f_test = open("../testing/test_data.txt")

#Create train files and prepare for model
X_train = []
y_train = []

for i in f_train.readlines():
	pieces = i.strip().split()
	sample = []
	sample.append(pieces[0])
	sample.append(pieces[1])
	y_train.append(pieces[2])
	sample.append("1" if pieces[0].islower() else "0")
	X_train.append(sample)


#Create test files and prepare for model
X_test = []
y_test = []

for i in f_test.readlines():
	pieces = i.strip().split()
	sample = []
	sample.append(pieces[0])
	sample.append(pieces[1])
	y_test.append(pieces[2])
	sample.append("1" if pieces[0].islower() else "0")
	X_test.append(sample)

#Create model
trainer = pycrfsuite.Trainer(verbose=False)

print len(y_test), len(y_train)

for xseq, yseq in zip(X_train, y_train):
    trainer.append([xseq], [yseq])

trainer.set_params({
    'c1': 1.0,
    'c2': 1e-3,
    'max_iterations': 50,
    'feature.possible_transitions': True
})

trainer.train('source')
tagger = pycrfsuite.Tagger()
tagger.open('source')

predict = []
for test in X_test:
    predict.extend(tagger.tag([test]))

tp = 0
tn = 0
fp = 0
fn = 0
for i in range(len(y_test)):
	if y_test[i]==predict[i]:
		if y_test[i] == "irrelevant":
			tn += 1
		else:
			tp += 1
	if y_test[i]!=predict[i]:
		if y_test[i] == "irrelevant":
			fp += 1
		else:
			fn += 1

print tp, tn, fp, fn
print "True positives - ",tp
print "True Negatives - ",tn
print "False positives - ",fp
print "False Negatives - ",fn

precision = float(tp)/(tp+fp)
recall = float(tp)/(tp+fn)
f = 2*precision*recall / (precision + recall)
print "Precision - ",precision
print "Recall - ",recall
print "F1-Measure - ",f
