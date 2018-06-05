
# For Convert String to Value


def print_path(lift_state,floor):
	# print("Root Called");
	# lift_state_floor = floor
	if lift_state < floor:
		assigned_root = 1
		floor = floor + 1
	else:
		assigned_root = -1
		floor = floor - 1

	# print("Root Called ROOT "+str(lift_state)+" --- "+str(floor))
	
	for i in range(lift_state,floor,assigned_root):
		print("Floor = "+ str(i))
	# lift_state = lift_state_floor
	print("Lift is on "+str(i)+"th Floor\n")
	
	return i #As a Lift_State


def root(lift_state, floor):
	final_path = []
	unique = set()

	# For Remove Duplicate
	for value in floor:
		if value not in unique:
			final_path.append(value)
			unique.add(value)
	temp=0
	for i in range(len(final_path)):
		for j in range(len(final_path)):
			# For Maintain Sequence
			if(lift_state < floor[i]):
				#Asc
				if(final_path[i] < final_path[j]):
					temp = final_path[i]
					final_path[i] = final_path[j]
					final_path[j] = temp

			else:
				#Desc
				if(final_path[i] > final_path[j]):
					temp = final_path[i]
					final_path[i] = final_path[j]
					final_path[j] = temp

	print(final_path)

	# For Print path
	for i in range(len(final_path)):
		lift_state = print_path(lift_state,final_path[i])
		
	return lift_state

# root(lift_state,floor)

lift_state = 0
while(True):
	
	assigned_root=0
	floor_input_from_user = input("Enter Floor: ")

	def converter(value):
		list_value = list(value.split(','))
		for i in range(len(list_value)):
			list_value[i] = int(list_value[i])
		return list_value

	print(converter(floor_input_from_user))
	floor = converter(floor_input_from_user)

	lift_state = root(lift_state,floor)
