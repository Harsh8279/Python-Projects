import string

f  = open("Contacts.vcf","r")

content = f.read()


c_lst = content.split('\n')

cnt = 0
contact=[]
for i in c_lst:
	if 'FN' in i or 'TEL;'in i:
		if 'FN' in i:
			n=i.split(':')[-1]
			
			contact.append(n)
		if 'TEL;' in i and 'FN' not in i:
			no = i.split(':')[-1]
			
			contact.append(no)


l_lst = list(string.ascii_letters)


i =0 
d_lst = list(string.digits)
dict_contact=dict()

no=[]
key=""
value=[]
for i in contact:
	
	flag = 0
	value=[]
	for j in range(len(i)):
		if(i[j]) in l_lst:
			continue

		elif (i[j]) in d_lst and (i[j]) not in l_lst:
			flag=1

	if(flag!=1):
		key = i
	else:
		value.append(i)	
		
	dict_contact[key] = str(value)
	

import csv

with open('Contacts.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in dict_contact.items():
       writer.writerow([key, value])



