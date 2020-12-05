### Parse the XML and then put everything into JSON format
filesIn= '~/sec/allUrls/'
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import os, random, datetime, sys,re 
import xmltodict, json
import matplotlib
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
sys.getrecursionlimit()
sys.setrecursionlimit(100000)

indi={}
for file in os.listdir(filesIn):
    if 'txt' in file.split('.'):
        with open (filesIn+file, 'r') as f :
            combineText=[]
            for i in f.readlines():
                combineText.append(i)
            indi[file]=combineText


for k, v in indi.items():
    textToParse= ' '.join([i for i in v])
    soup = BeautifulSoup(textToParse, "lxml")
    for k, v in enumerate(str(soup.findChild()).split()):
            if v =='<xml>': 
                idx1=k
            elif  v == '</xml>': 
                idx2 = k

                print(idx1, idx2)

                r= ''.join(str(soup.findChild()).split()[idx1:idx2+1])
                import xml.etree.ElementTree as ET
                import lxml.etree as ET

                soup4 = BeautifulSoup(r, "lxml")

                xml_dict = json.loads(json.dumps(xmltodict.parse((soup4.prettify()))))
                
                for k, v in xml_dict.items():
                    for k, v in v['body'].items():
                        for k, v in v['ownershipdocument'].items():
                            if isinstance(v,dict):
                                if 'issuertradingsymbol' in v.keys():
                                    print(v['issuertradingsymbol'])
