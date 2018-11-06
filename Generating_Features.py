import json
#Class sinh ra dac trung cua tu
class Generating_Features:
	def word2features(self,doc,i):
		word = doc[i][0]
		postag = doc[i][1]

		#Dinh nghia dac trung
		features = [
			'bias',
			'word.lower=' + word.lower(),
			'word[-3:]=' + word[-3:],
			'word[-2:]=' + word[-2:],
			'word.isupper=%s' % word.isupper(),
			'word.istitle=%s' % word.istitle(),
			'word.isdigit=%s' % word.isdigit(),
			'postag=' + postag

		]

		# Tu dang truoc
		if i > 0 :
			word1 = doc[i-1][0]
			postag1 = doc[i-1][1]
			features.extend([
				'-1:word.lower=' + word1.lower(),
				'-1:word.istitle=%s' % word1.istitle(),
				'-1:word.isupper=%s' % word1.isupper(),
				'-1:word.isdigit=%s' % word1.isdigit(),
				'-1:postag=' + postag1
			])
		else:
			features.append('BOS')

		#tu dang sau
		if i < len(doc) - 1:
			word1 = doc[i+1][0]
			postag1 = doc[i+1][1]
			features.extend([
				'+1:word.lower=' + word1.lower(),
				'+1:word.istitle=%s' % word1.istitle(),
				'+1:word.isupper=%s' % word1.isupper(),
				'+1:word.isdigit=%s' % word1.isdigit(),
				'+1:postag=' + postag1
			])
		else:
			 features.append('EOS')
		
		return features
	

	#ham tra ve dac trung cua documents
	def extract_features(self,doc):
		list_result = []
		for i in range(len(doc)):
			result = self.word2features(doc,i)
			list_result.append(result)		
		return list_result


	def readJson(self,file_input):
		with open(file_input) as jsondata:
			datas = json.load(jsondata)
		return datas

	def get_data_doc(self,file_input):
		list_doc = []
		datas = self.readJson(file_input)
		for data in datas:
			list_word = []
			doc = data['content']
			for sentence in doc:
				for word in sentence:
				  list_word.append((word[0],word[1],word[2]))
			list_doc.append(list_word)


		# print(list_doc[0][0]		
		
		return list_doc




		

	def get_labels(self,doc):
		list_labels = []
		for word in doc :
			list_labels.append(word[2])
		return list_labels
if __name__ == '__main__':
	a = Generating_Features()
	a.get_data_doc("data.json")









		
	


		
	

