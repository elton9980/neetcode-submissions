from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            dic[key].append(str)

        return list(dic.values())
     


         





















        











