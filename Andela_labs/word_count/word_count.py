# -*- coding: utf-8 -*-

def words(string):
	word_list = string.split()
	word_count = {}
	
	for word1 in word_list:
		count = 0
		for word2 in word_list:
			if word1 == word2:
				count += 1
		try:
			word_count[int(i)] = count
		except:
			word_count[i] = count
	return word_count
