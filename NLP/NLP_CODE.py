##############################################################

'''PYTHON FOR NLP'''
#NLP->Natural language Processing.
#web scrapping:-scrapping the text from reviews and convert it into tabuler form.
#Data acqisition->Text Extraction & cleanup->Pre-Processing->Feature Engineering->Model Bulding->
#NLP Techinques
#Feature engineering->process of extracting feature from row data.
######################################
##################Text mining####################
sentence="We are Learning TextMining from sanjivani AI"
#### if we want to know position of learning
sentence.index("Learning")
###It will show learning is at position 7.
#This is going to show character position from 0 including.



######################################
###If we want to know position of TextMining word.
sentence.split().index("Learning")
sentence.split().index("TextMining")
#It will split the words in list and count the position
###if you want to see the list select sentence.split()and the index of the word 
#it will show at 2,3

######################################
#Suppose we want to print any word in reverse order
sentence.split()[2][::-1]
####[start:end end:-1(start)]will start from -1,-2,-3,-4.....
###learning will be printed as gninrael


######################################
#Suppose want to print first and last word of the sentence
words=sentence.split()#tokenization
first_word=words[0]
first_word
last_word=words[-1]
last_word
###now we want to concate the first and last word
concat_word=first_word+" "+last_word
concat_word

######################################
#We want to print even words from sentences
[words[i] for i in range(len(words))  if i%2==0]
##words having odd length will not be printed



######################################
sentence#now we want to display only AI
sentence[-2:]
###it will start from -2,-1 i.e.AIfor
sentence[-3:]
###it will start from -3,-2,-1 i.e. AI

####################
#Suppose we want to display entire sentence in reverse order
sentence[::-1]
###'IA inavijnas morf gniniMtxeT gninraeL era eW'

####################
#Suppose we want to select each word and print in reverse order

words
print(" ".join(word[::-1] for word in words))
##eW era gninraeL gniniMtxeT morf inavijnas IA

print(words)
#################################################
#################################################

##tokenisation
#CHOPPING THE SENTENCE INTO WORDS

import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)

#parts of speech (pos)tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)

#it is mentioning parts of speech
#[('I', 'PRP'),=PRP=pronoun
 #('am', 'VBP'),
 #('reading', 'VBG'),
 #('NLP', 'NNP'),
 #('Fundamentals', 'NNS')]
#stop words from NLTK librarnlty


import nltk
nltk.download('stopwords')
#stopwords module from the nltk.corpus. 
#This module contains lists of stopwords for different languages.
from nltk.corpus import stopwords
stop_words=stopwords.words('English')
print(stop_words)


##13/06/2024
#####################################################
#LET US FILTER THE SENETENCE USING STOP_WORDS
sentence_words="hi hello how are hope you ding well "
sentence_no_stops=" ".join([words for words in sentence_words if words%2==0])
print(sentence_no_stops)


##suppose we want to replace words in string

sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","MALASIYA").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)



##############################################
##suppose we want to do auto correction in the sentence
from autocorrect import Speller
#declare the function Sepller definded for Engilish
spell=Speller(lang='en')
spell("Engilish")
spell("goodi")
#spell=Speller(lang=' ')
#######################################
#Suppose we want to correct sentence

import nltk
nltk.download('punkt')
from nltk import word_tokenize
sentence3="Ntural lanagage processinn deals withh thr aart of extract  "
##let us first tokenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join ([spell(word) for word in sentence3])
print(corrected_sentence)
########################################

##Stemming 
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")
#############################################
##Lematizer
##lematizer looks into dictionary words
import nltk
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")



################################################
###chunking (Shallow parsing ) identifying named entities
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4=" We are learning NLP in python by Sanjivani"
##first we will tokanize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]


 
############################
##sentence tokenization

from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning nlp.Delivered by sanjivaniAI.Do you know where it is located.It is in Kopergaon")
sent
#####################################
#He went to bank and checked acc it was almost 0
#looking this he went to river bank and was crying
from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
##OUTPUT->>>Synset('savings_bank.n.02')
################################################
senetnce2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
##OUTPUT=>>>Synset('trust.v.01')
##########################################
#########14/june/2024

'''
Removing special characters
special char. ,as you know ,
are non-alphnanumeric characters.
these char. are most oftenn found in comments,
references,currency numners etc.
These char add no value  to text understanding 
and induce noise into algo.
for that regex package is used
'''
###REGEX
import re
chat1="Hello, I am having an issue with my order #412889912"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat1)
matches
#output+=> ['412889912']
########################################
########################################

chat2="I have a problem with my order number 412889912"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches
#output+=> ['412889912']
############################################
#############################################
chat3="My order 412889912 is having an issue ,I was charged"
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat3)
matches
#output+=> ['412889912']

################################################
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)    
#################################################
#################################################

###18/june/2024
import re
chat1="Hello, I am having an issue with my order #412889912  ashdjas #78324629"
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1) 
###output==>>>'412889912'



##########################################
chat1='you ask lot of question ## 1235678912,abc@xyz.com'
chat2='here it is : (123) -567-8912,abcd@xyz.com'
chat3='yes,phone: 1235678912 email:abcde@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
##all output::'abc@xyz.com'##extract email id
####it wll show email id
##################################################
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)
##all output=>>>> ('1235678912', '')
#### (\......\) for parentheisis we use (123)
##only for 3 digit number -\d{3}
##for 4 digit number -\d{4}

#############################################

##\n all char in next line
###
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''


get_pattern_match(r'age (\d+)',text)
##output==>>>'52'
#text after age display
get_pattern_match(r'Born(.*)\n',text).strip()
##output==>>'Elon Reeve Musk'
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
##output==>>'June 28, 1971'
get_pattern_match(r'\(age.*\n(.*)',text)
## output==>'Pretoria, Transvaal, South Africa'    
####################################################


###19/june/2024
####################################################
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''


def extract_personal_information(text):
    age=get_pattern_match(r'age (\d+)',text)
    full_name=get_pattern_match(r'Born(.*)\n',text).strip()
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match(r'\(age.*\n(.*)',text)
    ##exrtracting multiple variables
    ##interview question
    return
        {
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)

##multiple variable extraction
#display multiple variable from para in dict form
#output==>>{'age': 52,
 #'name': 'Elon Reeve Musk',
 #'birth_date': 'June 28, 1971',
 #'birth_place': 'Pretoria, Transvaal, South Africa'}

#####################################################
##Dhirubhau Abbani
###########not proper running#################################below
text='''Born	Dhirubhai Ambani
28 December 1932
Chorwad, Junagadh State, British India
(present-day Gujarat, India)
Died	6 July 2002 (aged 69)
Mumbai, Maharashtra, India
Citizenship	British India (1932–1947)
Dominion of India (1947–1950)
India (1950–2002)
Occupation	Businessman
Organization(s)	Reliance Industries
Reliance Capital
Reliance Infrastructure
Reliance Power
Spouse	Kokila Dhirubhai Ambani
​
​(m. 1955)​
Children	4, including Mukesh Ambani and Anil Ambani
Awards	Padma Vibhushan (2016) (posthumously)
'''
get_pattern_match(r'age(\d+)',text)
##output==>>
get_pattern_match(r'Born(.*)\n',text).strip()
##output==>>'Dhirubhai Ambani'
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
####output==>>
get_pattern_match(r'\(age.*\n(.*)',text)
##output==>>'Mumbai, Maharashtra, India'
##############################
import re
def extract_personal_information(text):
    age=get_pattern_match(r'age(\d+)',text)
    full_name=get_pattern_match(r'Born(.*)\n',text).strip()
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match(r'\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)

#####################################################
#####################################################
from PyPDF2 import PdfFileReader
#importing required modules

from PyPDF2 import PdfReader
#creating a pdf reader object
reader=PdfReader('C:/1-python/kopargaon-part-1.pdf') 
#printing number of pages in pdf file
print(len(reader.pages))
##len==>>output==>>307
page=reader.pages[2]
page 
##############
reader2=PdfReader('C:/1-python/matrix_basics.pdf')
print(len(reader2.pages))
##putput==>>20
page=reader2.pages[2]
page
###########################################################
###########################################################
##20/June/2024
import re
sentence5="sharat twitted ,Wittnessing 68th republic day India from Rajpath,\new Dehli ,Mesmorizing performance by India Army!"
re.sub(r'([^\s\w]|_)+',' ',sentence5).split()
#^ excluding
'''
O/P=>>['sharat',
 'twitted',
 'Wittnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 'ew',
 'Dehli',
 'Mesmorizing',
 'performance',
 'by',
 'India',
 'Army']
    '''
    
'''
re.sub(r'([^\s\w]|_)+',' ',some_string)
will replace sequence of non-alphanumeric char
(including punctuation but excluding white space)
with single space.This is commanly use to clean uo to
by removing punctuation and other non-word char making it easy
......
......
'''
######################################
####extracting n grams
#n-grams can be extracted using three techniques
#1.custom funtion
#2.NLTK
#3.TextBlob
####################
#extracting n-grams using custom defined function
# 2 or more extracting
import re
def n_gram_extracter(input_str,n):
    tokens = re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])   
n_gram_extracter("The cute little boy id playing with kitten",2)  
#Split  sentence into 2 words form
'''
O/P==>>

['The', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'id']
['id', 'playing']
['playing', 'with']
['with', 'kitten']
'''
     
n_gram_extracter("The cute little boy id playing with kitten",3)
'''
O/P==>>>
['The', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'id']
['boy', 'id', 'playing']
['id', 'playing', 'with']
['playing', 'with', 'kitten']
'''

####################################################
#1.extract all twitter  handles from following text.Twitter handle
text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = 'https://twitter.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
'''
output::
['elonmusk', 'teslarati', 'dummy_tesla', 'dummy_2_tesla']
'''
######################################################
#2.Extract Concentration Risk types.It will be text that appear 

text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
##Extracting text 
pattern = 'Concentration of Risk:([^\n]*)'
re.findall(pattern,text)
## O/P==>>>> [' Credit Risk', ' Supply Risk']
###################################################################
##companies in europe reports their financial numbers of annual basis
#and you can have a document like this.To extract quartelt and
#period you can use a regex as shown
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'#?: match this and \a or b
matches=re.findall(pattern,text)
matches
##O/P==>>>['2021 Q1', '2021 S1']
###################################################
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern = '\(\d{3}\).\d{3}.-\d{4}|\d{10}'
matches = re.findall(pattern,text)
matches
##O/P==>>>not getting proper result
#################################################
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
##display words after Note1 and Note2
pattern = 'Note \d - ([^\n]*)'
matches = re.findall(pattern, text)
matches
##O/P=>>['Overview', 'Summary of Significant Accounting Policies']

#####################################
#Exrtract financial periods from a company's finanacial reporting
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = 'FY\d{4} Q[1-4]'
matches = re.findall(pattern ,text)
matches
##O/P=>> ['FY2021 Q1', 'FY2020 Q4']

########################################################################
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern  = 'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text, flags=re.IGNORECASE)
##If any lower case is appear then we have to use flags=re.IGNIRECASE
matches
##o/P=>> ['FY2021 Q1', 'fy2020 Q4']
###################################################################
###################################################################
#21/June/2024#############################

from nltk import ngrams
#extracting n using nltk
#n-grams is in built in nltk
list(ngrams("The cute little boy id playing with kitten",2))
##O/P=>>list will be created like above but only 2 char will display together
list(ngrams("The cute little boy id playing with kitten",3))
##only 2 char will display together
##################################################
from textblob import TextBlob 
blob=TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)
'''output::
    [WordList(['The', 'cute']),
     WordList(['cute', 'little']),
     WordList(['little', 'boy']),
     WordList(['boy', 'is']),
     WordList(['is', 'playing']),
     WordList(['playing', 'with']),
     WordList(['with', 'kitten'])]
    '''
blob.ngrams(n=3)
'''output::
    [WordList(['The', 'cute', 'little']),
     WordList(['cute', 'little', 'boy']),
     WordList(['little', 'boy', 'is']),
     WordList(['boy', 'is', 'playing']),
     WordList(['is', 'playing', 'with']),
     WordList(['playing', 'with', 'kitten'])]
    '''
#########################################################################
##Tokenization using Keras,
### IN keras their one more modeule preprocessing in which one more module text
##keras.preprocessing.text 
sentence5
sentence5="sharat twitted ,Wittnessing 68th republic day India from Rajpath,\new Dehli ,Mesmorizing performance by India Army!"
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)
##need to install=>>conda install -c conda-flage keras-preprocessing    to run code

#################################################
##Tokenization using TextBlob
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
''' output::
    WordList(['sharat', 'twitted', 'Wittnessing', '68th', 'republic', 'day', 'India', 'from', 'Rajpath', 'ew', 'Dehli', 'Mesmorizing', 'performance', 'by', 'India', 'Army'])
'''
###########################
###tweet Tokenization 
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
'''output::
    ['sharat',
     'twitted',
     ',',
     'Wittnessing',
     '68th',
     'republic',
     'day',
     'India',
     'from',
     'Rajpath',
     ',',
     'ew',
     'Dehli',
     ',',
     'Mesmorizing',
     'performance',
     'by',
     'India',
     'Army',
     '!']
'''
###########################################################
##Multi-Word_Expression

from nltk.tokenize import MWETokenizer
'''
multi-word tokenizers are essential fro task
where the meaning of the text heavily depends in
the intepretation of phrases as wholes rather than
as sums of individual words .fro instance,
ain sentimate analysis,recongnizing "not good"
as a single negative sentimate unit rather thas as 
"not" And "good" separetely can suignificntly affect the outcone
'''
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
'''output::
    ['sharat',
 'twitted',
 ',Wittnessing',
 '68th',
 'republic_day',
 'India',
 'from',
 'Rajpath,',
 'ew',
 'Dehli',
 ',Mesmorizing',
 'performance',
 'by',
 'India',
 'Army!']
    '''
mwe_tokenizer.tokenize(sentence5.replace('!',' ').split())
'''output::
    ['sharat',
     'twitted',
     ',Wittnessing',
     '68th',
     'republic_day',
     'India',
     'from',
     'Rajpath,',
     'ew',
     'Dehli',
     ',Mesmorizing',
     'performance',
     'by',
     'India',
     'Army']

    '''
################################################################


