def find_max_min(numbers):
	max_num = 0
	min_num = numbers[0]

	for num in numbers:
		if num > max_num:
			max_num = num
		elif num < min_num:
			min_num = num
	return [min_num, max_num]
