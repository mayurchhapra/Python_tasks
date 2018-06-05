def buy_nug_calc(num,min=0,twinty=0,nine=0,six=0):
	if min==20:
		twinty = twinty+1
	if min==9:
		nine = nine+1
	if min==6:
		six = six+1
	if num==0:
		print("="*49)
		print('|\tSix = '+str(six)+' Nine = '+str(nine)+" Twinty = "+str(twinty)+"\t\t|")
		# print("="*50)
		return True
	elif num<0:
		return False
	else:
		return buy_nug_calc(num-20,20,twinty,nine,six) or buy_nug_calc(num-9,9,twinty,nine,six) or buy_nug_calc(num-6,6,twinty,nine,six)

while(True):

	nug_value = int(input("\nInsert Nuggets: "))
	
	if buy_nug_calc(nug_value) == True:
		result = "|\t   -- Pattern Possible --\t\t|"
	else:
		result =  "="*49+ "\n|\t   -- Pattern Not Possible --\t\t|"
	print(result)
	print("="*49)