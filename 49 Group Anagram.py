class Solution():
	def groupAnagrams(strs):
		hash_table = {}
		for string in strs:
			ss = ''.join(sorted(string))
		if ss in hash_table:
			hash_table[ss].append(string)
		else:
			hash_table[ss] = string
		return hash_table.values()

my_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution.groupAnagrams(my_list)