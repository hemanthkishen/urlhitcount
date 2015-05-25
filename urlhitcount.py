import time
import datetime
from time import strftime
from datetime import datetime
from operator import itemgetter
from itertools import groupby
import bisect
from collections import defaultdict
from collections import OrderedDict

Input_File=open("input.txt","r") #Read from file

data = list() #Create a list

for line in Input_File:
    line=line.strip()
    k=line.split('|') #Seperate the timestamp
    k[0]=datetime.utcfromtimestamp(int(k[0])).strftime('%m/%d/%Y GMT')
    data.append(k) #Append data after timestamp
    
data1= sorted(data) #Sort data in ascending order

Hit=dict()

for date, items in groupby(data1, lambda data1: data1[0]):
    print(date) #Prints the date MM/DD/YYYY GMT
    Hit={}
    
    for s,p in items:
        
        p=str(p)
        Hit[p]=Hit.get(p,0)+1

    d_sorted_by_value = OrderedDict(sorted(Hit.items(), key=lambda x: x[1],reverse=True))

    for l,k in d_sorted_by_value.items():
        print l,k #Prints the URL and hits
    print "\n"
