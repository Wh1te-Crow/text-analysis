import math
alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"
alphabet_with_space = " "+alphabet
Dictionary_of_Bigrams_first={}
Dictionary_of_Bigrams_second={}
Dictionary_of_Bigrams_with_spaces_first={}
Dictionary_of_Bigrams_with_spaces_second={}
def create_Dictionary_of_Bigrams(Dictionary_of_Bigrams):
        for i in alphabet:
                for j in alphabet:
                        Dictionary_of_Bigrams[i+j]=0
        return(Dictionary_of_Bigrams)

def create_Dictionary_of_Bigrams_with_spaces(Dictionary_of_Bigrams_with_spaces):
	for i in alphabet_with_space:
		for j in alphabet_with_space:
			Dictionary_of_Bigrams_with_spaces[i+j]=0

def print_Dictionary_of_Bigrams_with_spaces(Dictionary_of_Bigrams_with_spaces):
	Table={}
	Table[0]=list(" "+alphabet_with_space)
	for i in range(1,33):
		Table[i]=list(alphabet_with_space[i-1])

	for i in range(len(alphabet_with_space)):
		for j in range(len(alphabet_with_space)):

				Table[i+1]=Table[i+1]+[(Dictionary_of_Bigrams_with_spaces[alphabet_with_space[i]+alphabet_with_space[j]])]
	for i in range(0,33):
		Temp=""
		for j in range(len(Table[i])):
			Temp+=str(Table[i][j])+(5-len(str(Table[i][j])))*" "
		Table[i]=Temp[0:len(Temp)]

	Temp=""

	for i in range(len(Table)):
		Temp+=str(Table[i])+"\n"
	Table = Temp
	print(Table)	


def print_Dictionary_of_Bigrams(Dictionary_of_Bigrams):
	Table = {}
	Table[0] = list(" "+alphabet)
	
	for i in range(1,32):
		Table[i]=list(alphabet[i-1])
	
	for i in range(len(alphabet)):
		for j in range(len(alphabet)):
				Table[i+1]=Table[i+1]+[(Dictionary_of_Bigrams[alphabet[i]+alphabet[j]])]
	
	for i in range(0,32):
		Temp=""
		for j in range(len(Table[i])):
			Temp+=str(Table[i][j])+(5-len(str(Table[i][j])))*" "
		Table[i]=Temp[0:len(Temp)]

	Temp=""

	for i in range(len(Table)):
		Temp+=str(Table[i])+"\n"
	Table = Temp
	print(Table)

def cleaning(string):
	string = string.lower()
	string = string.replace('ё','е')
	string = string.replace('ъ','ь')

	
	for i in string:
		if not(i in alphabet_with_space):
			string = string.replace(i, ' ')
	Flag = True
	while Flag:
		if "  " in string:
			string = string.replace('  ',' ')
		else:
			Flag = False
	return string



'''
file = open('book.txt', encoding='utf-8')
clear_text = cleaning(file.read())


clear_file = open('clear_book.txt', 'w')
clear_file.write(clear_text)
file.close()
clear_file.close()


#print('clean text saved...')
'''
#Bigrams search
print('Bigrams')

file = open('clear_book.txt')
text = file.read()

create_Dictionary_of_Bigrams_with_spaces(Dictionary_of_Bigrams_with_spaces_first)
for i in range(len(text)-1):
	Dictionary_of_Bigrams_with_spaces_first[text[i:i+2]]+=1
print('first way of search with spaces:\n')
print_Dictionary_of_Bigrams_with_spaces(Dictionary_of_Bigrams_with_spaces_first)

create_Dictionary_of_Bigrams_with_spaces(Dictionary_of_Bigrams_with_spaces_second)
for i in range(0,len(text)-1,2):
	Dictionary_of_Bigrams_with_spaces_second[text[i:i+2]]+=1
print('second way of search with spaces:\n')
print_Dictionary_of_Bigrams_with_spaces(Dictionary_of_Bigrams_with_spaces_second)

file.close()

create_Dictionary_of_Bigrams(Dictionary_of_Bigrams_first)
create_Dictionary_of_Bigrams(Dictionary_of_Bigrams_second)
file = open('clear_book.txt')
Our_string = file.read()
Text = Our_string.replace(' ','')

for i in range(len(Text)-1):
	Dictionary_of_Bigrams_first[Text[i:i+2]]+=1

for i in range(0,len(Text)-1,2):
	Dictionary_of_Bigrams_second[Text[i:i+2]]+=1
print('first way of search without spaces:\n')
print_Dictionary_of_Bigrams(Dictionary_of_Bigrams_first)

print('second way of search without spaces:\n')
print_Dictionary_of_Bigrams(Dictionary_of_Bigrams_second)

entropy_dict = {}

#letter frequency

print('letter frequency')

#dict initialization
dictionary_alphabet = {}

for i in alphabet_with_space:
	dictionary_alphabet[i]=0

for i in alphabet_with_space:
	for j in Our_string:
		if j == i:
			dictionary_alphabet[j]+=1
temp_arr=list(alphabet_with_space)
temp_Arr = []
for i in temp_arr:
	temp_Arr+=[dictionary_alphabet[i]]
Flag = True
while Flag:
 	Flag = False
 	for i in range(len(temp_Arr)-1):
 		if temp_Arr[i]<temp_Arr[i+1]:
 			temp_Arr[i],temp_Arr[i+1]=temp_Arr[i+1],temp_Arr[i]
 			temp_arr[i],temp_arr[i+1]=temp_arr[i+1],temp_arr[i]
 			Flag = True
for i in temp_arr:
	Temp_string = "---"+i+"---: "+str(dictionary_alphabet[i])
	print(Temp_string)


#quantity search
entropy_dict = {}
quantity=0
entropy=0
for i in alphabet_with_space:
	quantity+=dictionary_alphabet[i]

for i in alphabet_with_space:
	entropy -= (dictionary_alphabet[i]/(quantity*1.0))*math.log2(dictionary_alphabet[i]/(quantity*1.0))
entropy_dict['entropy with spaces']= entropy

quantity = quantity - dictionary_alphabet[' ']
entropy = 0
for i in alphabet:
	entropy -= (dictionary_alphabet[i]/(quantity*1.0))*math.log2(dictionary_alphabet[i]/(quantity*1.0))
entropy_dict['entropy without spaces']= entropy
entropy=0
quantity=0
for i in Dictionary_of_Bigrams_first.keys():
	quantity+=Dictionary_of_Bigrams_first[i]

for i in Dictionary_of_Bigrams_first.keys():
	if Dictionary_of_Bigrams_first[i]!=0:
		entropy -=(Dictionary_of_Bigrams_first[i]/quantity)*math.log2(Dictionary_of_Bigrams_first[i]/quantity)
entropy_dict['entropy_of_Bigrams_first']=0.5*entropy

entropy=0
quantity=0
for i in Dictionary_of_Bigrams_second.keys():
	quantity+=Dictionary_of_Bigrams_second[i]
for i in Dictionary_of_Bigrams_second.keys():
	if Dictionary_of_Bigrams_second[i]!=0:
		entropy -=(Dictionary_of_Bigrams_second[i]/quantity)*math.log2(Dictionary_of_Bigrams_second[i]/quantity)
entropy_dict['entropy_of_Bigrams_second']=0.5*entropy

entropy=0
quantity=0
for i in Dictionary_of_Bigrams_with_spaces_first.keys():
	quantity+=Dictionary_of_Bigrams_with_spaces_first[i]
for i in Dictionary_of_Bigrams_with_spaces_first.keys():
	if Dictionary_of_Bigrams_with_spaces_first[i]!=0:
		entropy -=(Dictionary_of_Bigrams_with_spaces_first[i]/quantity)*math.log2(Dictionary_of_Bigrams_with_spaces_first[i]/quantity)
entropy_dict['entropy_of_Bigrams_with_spaces_first']=0.5*entropy

entropy=0
quantity=0
for i in Dictionary_of_Bigrams_with_spaces_second.keys():
	quantity+=Dictionary_of_Bigrams_with_spaces_second[i]
for i in Dictionary_of_Bigrams_with_spaces_second.keys():
	if Dictionary_of_Bigrams_with_spaces_second[i]!=0:
		entropy -=(Dictionary_of_Bigrams_with_spaces_second[i]/quantity)*math.log2(Dictionary_of_Bigrams_with_spaces_second[i]/quantity)
entropy_dict['entropy_of_Bigrams_with_spaces_second']=0.5*entropy

for i in entropy_dict.keys():
	print(i+":   "+str(entropy_dict[i]))
print('R:  '+str(1-(1.068+1.761)/10))
file.close()
