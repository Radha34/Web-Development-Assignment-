import xml.etree.ElementTree as ET
import pandas as pd

xml_data = open('employeexml.xml', 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML

data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)

df = pd.DataFrame(data).T  # Write in DF and transpose it
df.columns = cols  # Update column names
print(df)

details = ['Arun', 'Bang', 'Engineer', 'Computer','65,000','306','15']
  
# Using 'details' as the column name
# and equating it to the list
df['Details'] = details

print(df.shape)

emp_df = df.transpose()

updated_emp_df = emp_df.set_axis(['First_Name', 'Last_Name', 'Title','Division','Salary','Building','Room'], axis='columns')
updated_emp_df = updated_emp_df.set_axis(['Emp_1','Emp_2','Emp_3','Emp_4','Emp_5','Emp_6','Emp_7','Emp_8','Emp_9'],axis='index')
print("\n Formatted columns and rows names :\n ")
print(updated_emp_df)
print("\n Sorting the data acoording to highest employee salary \n")
print(updated_emp_df.sort_values(by='Salary', ascending=False))

print("\n Getting details of an employee by his name \n")

filter_ = updated_emp_df['First_Name'] == "Arun"
print(updated_emp_df[filter_])
         
#convert the dataframe to xml file
def to_xml(df, filename=None, mode='w'):
    def row_to_xml(row):
        xml = ['<employee>']
        for i, col_name in enumerate(row.index):
            xml.append('  <field name="{0}">{1}</field>'.format(col_name, row.iloc[i]))
        xml.append('</employee>')
        return '\n'.join(xml)
    res = '\n'.join(df3.apply(row_to_xml, axis=1))

    if filename is None:
        return res
    with open(filename, mode) as f:
        f.write(res)

pd.DataFrame.to_xml = to_xml
df.to_xml('updated_emp_record.xml')
print("\n Creating a new xml file with updated employee record -'updated_emp_record.xml' ")
