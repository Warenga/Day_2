def find_max_min(numbers):
	max_num = 0
	min_num = numbers[0]

	for num in numbers:
		if num > max_num:
			max_num = num
		elif num < min_num:
			min_num = num
	if min_num == max_num:
		return [len(numbers)]
	else:
		return [min_num, max_num]
