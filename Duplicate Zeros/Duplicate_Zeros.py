def duplicate_zeros(list):
	x = len(list)
	new_list = []
	for i in range(x):
		new_list.append(list[i])
		if list[i] == 0:
			new_list.append(0)
	return new_list

spisok = [0, 0, 1, 2, 100, 0, 5, 0]
print(duplicate_zeros(spisok))
