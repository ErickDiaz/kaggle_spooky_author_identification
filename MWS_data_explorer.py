import pandas
import os
import sys
import nltk
from nltk.tokenize import sent_tokenize

def validatePathName(pathName):
	if(pathName.endswith('/')):
		return pathName
	else:
		return pathName + '/'
#Create env
#conda create -n pandas_env python=3 pandas

labels = pandas.read_csv('train.csv')
text = pandas.read_csv('text.csv', doublequote = True, encoding = 'latin-1')

kaggleData = text.join(labels)

mwsData = kaggleData[kaggleData['author'] == 'MWS']

devmwsCorpusPath = '/Users/erickdiaz/Documents/kaggle_spooky_author_identification/edgar_philip_love_poe/corpus/shelley'

mwsCorpusPath= validatePathName(devmwsCorpusPath if ( len(sys.argv) < 2 ) else sys.argv[1])

## Get current Shelly corpus
files = os.listdir(mwsCorpusPath)

mwsCorpus = ''
raw_corpus = ''

for file in files:
	if (file.endswith('txt')):
		print('|----------- ' + file)
		openFile = open((mwsCorpusPath+file), 'r')
		raw_corpus += openFile.read()

mwsCorpus = sent_tokenize(raw_corpus.replace('\n', ' '))
#text = nltk.Text(newData)

for index, row in mwsData.iterrows():
	kaggle_sentence = row['text']
	found = False
	for sentence in mwsCorpus:
		result = nltk.edit_distance(sentence, kaggle_sentence)
		if(result < 45):
			print('kaggle sentence ----->' + kaggle_sentence +'<-------')
			print('corpus: ------->' + sentence +'<-------')
			found = True
			mwsCorpus.remove(sentence)
			break
	if (not found):
		print('#####################################################')
		print('#################### NOT FOUND ######################')
		print('kaggle sentence ----->' + kaggle_sentence +'<-------')
		print('#####################################################')



