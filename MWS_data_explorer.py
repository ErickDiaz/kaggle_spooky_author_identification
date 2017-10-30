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

mwsCorpusDF = pandas.DataFrame(columns=['fileName','text'])

for file in files:
	if (file.endswith('txt')):
		print('|----------- ' + file)
		with open((mwsCorpusPath+file), 'r') as f:
				text=f.read()
		mwsCorpusDF = mwsCorpusDF.append(pandas.DataFrame([[file, text]], columns=['fileName','text']))

testtext = mwsCorpusDF.iloc[0]['text']
searchtxt = mwsData.iloc[0]['text']

if searchtxt not in testtext: 
    print('Not found')		


for index, row in mwsData.iterrows():
	#print(row['text'])
	if row['text'] in testtext:
		print('FOUND!!!!')