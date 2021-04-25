import json
import pandas as pd
from pandas.io.json import json_normalize
f = open('employee_details.json',)
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
with open("employee_details.json","w") as write_file:
    json.dump(df,write_file)
for d in df:
    if(d['id']==1):
     print("First Id ")  
     print(d['name'],',',d['website'],'website') 

emp_detail_df = pd.DataFrame(df)
print(type(emp_detail_df))
print(emp_detail_df['name'])

         
my_file = 'https://github.com/Radha34/Web-Development-Assignment-/blob/main/fetchJson/employee_details.json'
emp_detail_file = pd.read_json(my_file)
print("Loading json file usign read_json() method")
print(type(emp_detail_file))
emp_details_file.set_index('id', inplace=True)         
print("\n-----Sort data alphabetically according to the username------")
print(emp_detail_file.sort_values(by='name'))


print("\n Printing column wise values \n")
for row_label, row in emp_detail_file.iteritems():
     print(row_label, row, sep='\n', end='\n\n')
print("\n------ Accessing the nested data ------\n")
emp_detail_table = json_normalize(emp_detail_file['address'])     
print(emp_detail_table.head(2))

     
