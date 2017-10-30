import pandas
import os
import sys

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

for file in files:
	if (file.endswith('txt')):
		print('|----------- ' + file)
		with open((mwsCorpusPath+file), 'r') as f:
				mwsCorpus+=f.read()
		
##TODO: use NLTK
for index, row in mwsData.iterrows():
	text = row['text']
	if text not in mwsCorpus:
		print('------------ Not found -----------')
		print(text)
		print('----------------------------------')