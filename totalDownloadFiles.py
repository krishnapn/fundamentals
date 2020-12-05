## How many files to download per quarter
import os, sys, re
from collections import Counter
import numpy as np
import pandas as pda
import seaborn as sns
import matplotlib.pyplot as plt

filesIn= '/Users/krishnaneupane/Documents/personal/academic/disst/gitFiles/sec/allUrls/00000_all_urls/'
fType= ['13F-HR', '13F-HR/A', '13F-NT', '13F-NT/A', '13FCONP','4','5', '3']

perForm={}
for file in os.listdir(filesIn):
    if 'txt' in file.split('.'):
        df = pd.read_csv(filesIn+file, sep='\t', encoding='latin-1')
        i='Description:           Master Index of EDGAR Dissemination Feed by Form Type'
        df= df[i].str.split()
        df=df[5:]
       
        counter=dict(Counter(df.apply(lambda x : x[0])))
    perForm[file[0:6]]=counter
    
## Put everything in Dataframe
df= pd.DataFrame([(key, k, v) for key,val in perForm.items() for k, v in val.items() if k in fType])

## Print the Count 
for j in fType:
    
    i=df[df[1]==j]

    # plt.xticks(rotation=70)
    i['yr']=i[0].apply(lambda x: x.split('_')[0])
    i = i[i['yr'] !='urlCsv']

    i['yr']=i['yr'].apply(lambda x :int(x) )
    post_2007= np.sum(i[i['yr'] >=2007][2])
    total= np.sum(i[i['yr'] >=1994][2])
    print(j, 'Post 2007: ',post_2007 ,'Total: ', total)
