class Solution:
    def groupThePeople(self, group_sizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for person,size in enumerate(group_sizes):
            groups[size].append(person)
        ans = []
        for size,group in groups.items():
            ans+= [group[i:i+size] for i in range(0,len(group),size)]
        return ans