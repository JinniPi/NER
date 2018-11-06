import os

import re
import json
FJoin = os.path.join
class Prepare_Data:

	def read_file(self,file_name):
		list_line = []
		for line in open(file_name):
			list_line.append(line)
		#print(list_line)
		return list_line

	def get_list_sentence(self,list_line):
		list_sentence = []
		sentence = []
		for line in list_line:
			if line != '\n' :
				sentence.append(line)
			if line == '\n' :
				if(sentence != []):
					list_sentence.append(sentence)
				sentence = []
		#print(list_sentence)
		# print(len(list_sentence))
		# print(list_sentence[0])
		return list_sentence

	#Tra ve cac cau lay cot 1 , 2 .5
	def get_data_word(self,word):
		list_row = word.split('\t')
		result = (list_row[0],list_row[1],list_row[4].replace('\n','')) 
		# print(list_row)
		# print(result)
		return result
	#Tra ve du lieu cua mot cau
	def get_data_sentence(self,sentence):
		result = []
		for word in sentence:
			word_result = self.get_data_word(word)
			result.append(word_result)
		return result
	#Tra ve du lieu cho mot document
	def get_data_document(self,document):
		result = []
		for sentence in document:
			result_sentence = self.get_data_sentence(sentence)
			result.append(result_sentence)
		return result

	#lay danh sach file trong thu muc, lay danh sach thu muc con
	def GetFiles(self,path):
		file_list = []
		file_result = []
		for dir, subdirs, files in os.walk(path):
			file_list.extend([FJoin(dir, f) for f in files])
		for file in file_list:
			match = re.search(r'en.tags', file)
			if match:
				# print(file)
				file_result.append(file)
		return file_result

	#ghi data ra file json
	def get_all_data(self,path):
		list_result = []
		list_file = self.GetFiles(os.path.expanduser(path))
		for file in list_file:
			list_line = self.read_file(file)
			list_sentence = self.get_list_sentence(list_line)
			file_result = self.get_data_document(list_sentence)
			list_result.append(file_result)
		print(len(list_result))
		print(list_result)
		return list_result
	def  write_data_json(self,path,file_output):
		key = ('document','content')
		count = 1
		Datas = self.get_all_data(path)
		self.f = open(file_output, "w")
		self.f.write('[')
		for data in Datas:
			if count == len(Datas):
				dic = dict.fromkeys(key)
				dic['document'] = count
				dic['content'] = data
				line = json.dumps(dic,ensure_ascii=False) + "\n"
			else:
				count = count + 1
				dic = dict.fromkeys(key)
				dic['document'] = count
				dic['content'] = data
				line = json.dumps(dic,ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return file_output
	

		
if __name__ == "__main__":
	a = Prepare_Data()
	# list_line = a.read_file("en.tags")
	# list_sentence = a.get_list_sentence(list_line)
	# sentence = list_sentence[0]
	# print(sentence)
	# print(type(sentence))

	# result = a.get_data_document(list_sentence)
	# print(len(result))
	# print(result)
	a.write_data_json("/home/trang/Downloads/gmb-1.0.0/data","data.json")
