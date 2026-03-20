class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        map = {}
        result = []

        for i in nums:
            map[i] = map.get(i, 0) + 1

        sortedMap = sorted(map.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(sortedMap[i][0])

        return result
