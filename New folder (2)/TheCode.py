import pandas as pd
f1= open ('Beyond the Wall of Sleep.txt',encoding="utf8")
q1= f1.read()
q2= f2.read()a
q1= q1.split()
q2= q2.split()
import string
t= str.maketrans('','',string.punctuation)
q1= [w.translate(t)for w in q1]
q2= [w.translate(t)for w in q2]
q1= [word.lower()for word in q1]
q2= [word.lower()for word in q2]
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words= stopwords.words('english')
q1= [w for w in q1 if not w in stop_words]
q2= [w for w in q2 if not w in stop_words]
intr= set(q1)& set(q2)
print(len(intr))
print(intr)
