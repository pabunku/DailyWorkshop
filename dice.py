import random

di = [1,2,3,4,5,6]
count1 = 10
count2 = 100
count3 = 1000
count4 = 10000

groups = [[], [], [], [], []]
value = []
counts = [[],[],[],[],[],]



def add_group(count, index):
	for i in range(count):
		roll = random.choice(di)
		groups[index].append(roll)
	return groups
	
def get_list(group_list):
	for x in group_list:
		value.append(x)
		
	one = 0; two = 0; three = 0; four = 0; five = 0; six = 0;
	
	for i in range(len(value)):
		for y in range(len(value[i])):
			if value[i][y] == 1:
				one += 1
			elif value[i][y] == 2:
				two += 1
			elif value[i][y] == 3:
				three += 1
			elif value[i][y] == 4:
				four += 1
			elif value[i][y] == 5:
				five += 1 
			elif value[i][y] == 6:
				six += 1 
				
		counts[i] = [one, two, three, four, five, six]
	return counts
	

	
def get_percentages(counts_list):
	for x in range(len(counts_list)):
		
		for y in range(len(counts_list[x])):
			counts_list[x][y] = '{0:.2%}'.format(float(counts_list[x][y])/ len(groups[x]))
		
		a = "%i" %(10**(x + 1))
		counts_list[x].insert(0,a)
		
	return counts_list
	
def print_chart(counts_list):
	title = ['# of Rows', '1s', '2s', '3s', '4s', '5s', '6s']
	get_percentages(counts_list)
	col_width = len("# of rolls") + 2
	for x in range(len(title)):
		print title[x].ljust(col_width),
	print ""
		
	for row in range(len(counts_list)):
		for num in range(len(counts_list[row])):
			print counts_list[row][num].ljust(col_width),
		print ""
		
add_group(count1, 0)
add_group(count2, 1)
add_group(count3, 2)
add_group(count4, 3)
add_group(100000, 4)

get_list(groups)
print_chart(counts)



