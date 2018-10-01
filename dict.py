alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя"
alphabet_with_space = " "+alphabet
Dictionary={}
def create_dict():
	#'mws' monograms with spaces
	#'bwsf'bigrams with spaces The first way to choose
	#'bf'  bigrams without spaces The first way to choose
	#'bwss'bigrams with spaces The second way to choose
	#'bs'  bigrams with spaces The second way to choose
	Dictionary['mws']=Dictionary['m']=Dictionary['bwsf']=Dictionary['bf']=Dictionary['bwss']=Dictionary['bs']={}

	for i in alphabet_with_space:
		for j in alphabet_with_space:
			Dictionary['bwsf'][i+j]=0


	for i in alphabet:
		for j in alphabet:
			Dictionary['bf'][i+j]=0

	Dictionary['bwss'],Dictionary['bs']=Dictionary['bwsf'],Dictionary['bf']

	for i in alphabet_with_space:
		Dictionary['mws'][i]=0

def print_dict():
	def print_table_ws(key):

		Table = {}
		Table[0] = list(" "+alphabet)
	
		for i in range(1,32):
			Table[i]=list(alphabet[i-1])

		for i in range(len(alphabet)):
			for j in range(len(alphabet)):
				Table[i+1]=Table[i+1]+[(Dictionary[key][alphabet[i]+alphabet[j]])]

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

	def print_table(key):

		Table = {}
		Table[0] = list(" "+alphabet)
	
		for i in range(1,32):
			Table[i]=list(alphabet[i-1])
	
		for i in range(len(alphabet)):
			for j in range(len(alphabet)):
					Table[i+1]=Table[i+1]+[(Dictionary[key][alphabet[i]+alphabet[j]])]
	
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

	def print_number_of_letters():

		temp_arr=list(alphabet_with_space)
		temp_Arr = []
		for i in temp_arr:
			temp_Arr+=[Dictionary['mws'][i]]
		Flag = True
		while Flag:
 			Flag = False
 			for i in range(len(temp_Arr)-1):
 				if temp_Arr[i]<temp_Arr[i+1]:
 					temp_Arr[i],temp_Arr[i+1]=temp_Arr[i+1],temp_Arr[i]
 					temp_arr[i],temp_arr[i+1]=temp_arr[i+1],temp_arr[i]
 					Flag = True
		for i in temp_arr:
			Temp_string = "["+i+"]: "+str(Dictionary['mws'][i])
			print(Temp_string)

	print('<---digrams first way without spaces--->')
	print_table('bf')
	print('<---digrams first way with spaces--->')
	print_table_ws('bwsf')
	print('<---digrams second way without spaces--->')
	print_table('bs')
	print('<---digrams second way with spaces--->')
	print_table_ws('bwss')
	print('<---number of letters--->')
	print_number_of_letters()

create_dict()
print_dict()


