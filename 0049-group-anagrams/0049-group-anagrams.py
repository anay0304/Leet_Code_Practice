class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        map = {}

        for i in strs:
            key = tuple(sorted(i))

            if key not in map:
                map[key] = []

            map[key].append(i)

        return map.values()