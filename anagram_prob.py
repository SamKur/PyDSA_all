#input  -> 
st = ["eat", "tea", "tan", "ate", "nat", "bat"]
#output -> [["bat"], ["nat","tan"], ["ate","eat","tea"]] #any order

from collections import defaultdict
class Solution:
    def groupAnagrams(self, st):
        anagram_map = defaultdict(list) #sorted word will be key
        result = []
        for s in st:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        # return anagram_map

        # result = [v for k,v in anagram_map]  --> error
        for value in anagram_map.values():
            result.append(value)
        return result


s =Solution()
print(s.groupAnagrams(st))