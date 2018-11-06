
# def read_file(file_name):
#     list_line = []
#     for line in open(file_name):
#         list_line.append(line)
#     #print(list_line)
#     return list_line
# def get_list_sentence(list_line):
#   list_sentence = []
#   sentence = []
#   for line in list_line:
#       if line != '\n' :
#           sentence.append(line)
#       if line == '\n' :
#           if(sentence != []):
#               list_sentence.append(sentence)
#           sentence = []
#   #print(list_sentence)
#   print(len(list_sentence))
#   print(list_sentence[0])
#   return list_sentence
			
		
# list_line = read_file("en.tags")
# list_sentence = get_list_sentence(list_line)
# import os
# import re
# FJoin = os.path.join
# def GetFiles(path):
# 	file_list = []
# 	file_result = []
# 	for dir, subdirs, files in os.walk(path):
# 		file_list.extend([FJoin(dir, f) for f in files])
# 	for file in file_list:
# 		match = re.search(r'en.tags', file)
# 		if match:
# 			print(file)
# 			file_result.append(file)
# 	return file_result
# def split_sentence(sentence):
# 	result = sentence.split('\t','')
# 	return result
# if __name__ == "__main__":

# 	file = GetFiles(os.path.expanduser("/home/trang/Downloads/gmb-1.0.0/data"))
 
	   
	# for dir in dirs:
	#     print dir
import json
def readJson(file_input):
	list_result = []
	with open(file_input) as jsondata:
		datas = json.load(jsondata)
	print(type(datas))
	pass

readJson("data.json")
