import json
import pandas as pd
from pandas.io.json import json_normalize
f = open('sample4.json',)
df = json.load(f)
print("Loading json file using json.load() method")
print(type(df))

data ={"id": 11,
     "name": "John Green",
     "username": "JStanton",
     "email": "John.Green@karina.biz",
     "address": {
       "street": "Avenue Turnpike",
       "suite": "Suite 259",
       "city": "Lebsackbury",
       "zipcode": "31428-2261",
       "geo": {
         "lat": "-38.3386",
         "lng": "57.4532"
       }
     },
     "phone": "024-648-3855",
     "website": "greenpubs.net"
   }
df.append(data)
#adding data to the json file
with open("sample4.json","w") as write_file:
    json.dump(df,write_file)
for d in df:
    if(d['id']==1):
     print("First Id ")  
     print(d['name'],',',d['website'],'website') 

df1 = pd.DataFrame(df)
print(type(df1))
print(df1['name'])

         
my_file = 'C:\\Users\\Radha\\sample4.json'
df2 = pd.read_json(my_file)
print("Loading json file usign read_json() method")
print(type(df2))
df2.set_index('id', inplace=True)         
print("\n-----Sort data alphabetically according to the username------")
print(df2.sort_values(by='name'))


print("\n Printing column wise values \n")
for row_label, row in df2.iteritems():
     print(row_label, row, sep='\n', end='\n\n')
print("\n------ Accessing the nested data ------\n")
df3 = json_normalize(df2['address'])     
print(df3.head(2))

     
